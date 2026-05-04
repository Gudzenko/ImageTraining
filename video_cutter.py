import subprocess
import tempfile
from pathlib import Path
from typing import List, Tuple


class VideoCutter:
    def cut_and_merge(
        self,
        input_video: str,
        intervals: List[Tuple[str, str]],
        output_video: str,
    ) -> str:
        input_path = Path(input_video).resolve()
        output_path = Path(output_video).resolve()

        if not input_path.exists():
            raise FileNotFoundError(f"Видео не найдено: {input_path}")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            parts = []

            for index, (start, end) in enumerate(intervals, start=1):
                part_path = tmp_path / f"part_{index:03d}.mp4"
                parts.append(part_path)

                self._run([
                    "ffmpeg",
                    "-y",
                    "-i", str(input_path),
                    "-ss", start,
                    "-to", end,
                    "-c:v", "libx264",
                    "-c:a", "aac",
                    "-preset", "fast",
                    str(part_path),
                ])

            concat_file = tmp_path / "concat.txt"

            with open(concat_file, "w", encoding="utf-8") as f:
                for part in parts:
                    f.write(f"file '{part.as_posix()}'\n")

            self._run([
                "ffmpeg",
                "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", str(concat_file),
                "-c", "copy",
                str(output_path),
            ])

        return str(output_path)

    def compress_video(
            self,
            input_video: str,
            output_video: str,
            crf: int = 24,
            preset: str = "medium",
            audio_bitrate: str = "128k",
    ) -> str:
        input_path = Path(input_video).resolve()
        output_path = Path(output_video).resolve()

        if not input_path.exists():
            raise FileNotFoundError(f"Видео не найдено: {input_path}")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        self._run([
            "ffmpeg",
            "-y",
            "-i", str(input_path),
            "-c:v", "libx264",
            "-preset", preset,
            "-crf", str(crf),
            "-c:a", "aac",
            "-b:a", audio_bitrate,
            str(output_path),
        ])

        return str(output_path)

    @staticmethod
    def _run(cmd: List[str]) -> None:
        subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )


if __name__ == "__main__":
    cutter = VideoCutter()

    merged_path = cutter.cut_and_merge(
        input_video="./predict_runs/video_chicken/video_chicken1.avi",
        intervals=[
            ("00:00:59", "00:01:30"),
            ("00:01:50", "00:01:57"),
            ("00:02:07", "00:02:10"),
            ("00:02:29", "00:02:40"),
            ("00:02:48", "00:03:20"),
            ("00:03:37", "00:03:57"),
            ("00:04:49", "00:04:58"),
            ("00:05:24", "00:05:56"),
        ],
        output_video="./predict_runs/video_chicken/video_chicken1_merge.mp4",
    )

    compressed_path = cutter.compress_video(
        input_video=merged_path,
        output_video="./predict_runs/video_chicken/video_chicken1_compressed.mp4",
        crf=24,
    )

    print("Склеенное видео:", merged_path)
    print("Сжатое видео:", compressed_path)
