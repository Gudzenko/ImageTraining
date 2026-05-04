from pathlib import Path
from icrawler.builtin import BingImageCrawler
from PIL import Image


OUTPUT_DIR = Path("datasets/chicken_raw_test")
TEMP_DIR = OUTPUT_DIR / "_tmp"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)

QUERIES = [
    "adult chicken standing",
    "adult chicken sitting",
    "adult white chicken",
    "adult black chicken",
    "adult brown chicken",
    "adult chicken front view",
    "adult chicken back view",
    "adult chicken side view",
    "adult chicken behind wire fence",
    "adult chicken in cage",
    "adult free range chicken",
    "adult chicken farm",
    "adult chickens flock",
    "adult chickens outdoor",
    "adult chickens indoor farm",
    "adult hen walking",
    "adult rooster standing",
    "adult laying hen farm",
    "poultry farm chicken adult",
    "adult chicken close up",
]

MAX_IMAGES_PER_QUERY = 200


def get_next_index(output_dir: Path) -> int:
    existing = sorted(output_dir.glob("*.*"))
    nums = []
    for f in existing:
        if f.stem.isdigit():
            nums.append(int(f.stem))
    return (max(nums) + 1) if nums else 1


def clear_temp_dir(temp_dir: Path) -> None:
    for f in temp_dir.glob("*"):
        if f.is_file():
            f.unlink()


def is_valid_image(path: Path) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False


def normalize_and_move_images(temp_dir: Path, output_dir: Path, start_index: int) -> int:
    current_index = start_index

    for src in sorted(temp_dir.glob("*")):
        if not src.is_file():
            continue

        if not is_valid_image(src):
            src.unlink(missing_ok=True)
            continue

        try:
            with Image.open(src) as img:
                img = img.convert("RGB")
                dst = output_dir / f"{current_index:05d}.jpg"
                img.save(dst, format="JPEG", quality=95)
                current_index += 1
        except Exception:
            pass
        finally:
            src.unlink(missing_ok=True)

    return current_index


def download_query(query: str, max_num: int) -> None:
    clear_temp_dir(TEMP_DIR)

    crawler = BingImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={"root_dir": str(TEMP_DIR)},
    )

    print(f"Downloading: {query}")
    crawler.crawl(
        keyword=query,
        max_num=max_num,
        overwrite=False,
    )

    next_index = get_next_index(OUTPUT_DIR)
    new_next_index = normalize_and_move_images(TEMP_DIR, OUTPUT_DIR, next_index)
    print(f"Saved {new_next_index - next_index} images")


def main() -> None:
    for query in QUERIES:
        download_query(query, MAX_IMAGES_PER_QUERY)

    print("\nDone.")
    print(f"All images saved to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
