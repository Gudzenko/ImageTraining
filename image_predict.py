from pathlib import Path
from ultralytics import YOLO

# path to the trained model
MODEL_PATH = r"C:\Other\ImageTraining\runs\african_wildlife_26s\weights\best.pt"

# list of input images
IMAGE_PATHS = [
    r"C:\Other\ImageTraining\assets\image1.jpg",
    r"C:\Other\ImageTraining\assets\image2.jpg",
]

# output directory for results
OUTPUT_DIR = Path(r"C:\Other\ImageTraining\output_images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# load model
model = YOLO(MODEL_PATH)

# run prediction for each image
for image_path in IMAGE_PATHS:
    results = model.predict(
        source=image_path,
        conf=0.25,
        save=True,
        device=0,          # GPU
        project=str(OUTPUT_DIR),
        name="predict",
        exist_ok=True
    )

print("Done.")
print(f"Results saved to: {OUTPUT_DIR / 'predict'}")
