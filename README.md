# ImageTraining

A project for training and using YOLO models for object detection. Supports two datasets: African wildlife and chickens.

---

## Project Structure

### Scripts

| File                | Description                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `main.py`           | Runs model training. Contains two methods: `train_wildlife()` for African wildlife and `train_chicken()` for chickens. |
| `video_predict.py`  | Runs predictions on video. Methods: `predict_wildlife()` and `predict_chicken()`.                                      |
| `image_predict.py`  | Runs predictions on images. Saves results to `output_images/`.                                                         |
| `dowloader.py`      | Downloads chicken images from Bing to build a dataset.                                                                 |
| `compress_video.py` | Compresses video using FFmpeg (libx264).                                                                               |
| `video_cutter.py`   | Cuts and merges video segments using FFmpeg.                                                                           |
| `helper.py`         | Checks GPU availability and PyTorch version.                                                                           |

### Folders

| Folder                       | Description                                             |
| ---------------------------- | ------------------------------------------------------- |
| `datasets/african-wildlife/` | African wildlife dataset.                               |
| `datasets/chicken/`          | Chicken dataset.                                        |
| `runs/`                      | Training results (weights, metrics). Excluded from git. |
| `predict_runs/`              | Video prediction results. Excluded from git.            |
| `output_images/`             | Image prediction results. Excluded from git.            |
| `assets/`                    | Source videos and images for testing.                   |

---

## Installation

```bash
pip install -r requirements.txt
```

Requires a CUDA-compatible GPU and [FFmpeg](https://ffmpeg.org/) installed.

---

## Usage

### Training

```bash
python main.py
```

Trains on the chicken dataset by default. To switch to wildlife — uncomment `train_wildlife()` in `main.py`.

### Video Prediction

```bash
python video_predict.py
```

### Image Prediction

```bash
python image_predict.py
```
