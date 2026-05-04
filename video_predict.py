from ultralytics import YOLO


def predict_wildlife():
    model = YOLO(r"C:\Other\ImageTraining\runs\african_wildlife_26s\weights\best.pt")
    results = model.predict(
        source=r"C:\Other\ImageTraining\assets\video.mp4",
        save=True,
        stream=True,
        device=0,
        half=True,
        imgsz=640,
        conf=0.25,
        vid_stride=1,
        project=r"C:\Other\ImageTraining\predict_runs",
        name="video_predict_gpu_26s"
    )
    for _ in results:
        pass


def predict_chicken():
    model = YOLO(r"C:\Other\ImageTraining\runs\chicken\weights\best.pt")
    results = model.predict(
        source=r"C:\Other\ImageTraining\assets\video_chicken1.mp4",
        save=True,
        stream=True,
        device=0,
        half=True,
        imgsz=640,
        conf=0.25,
        vid_stride=1,
        project=r"C:\Other\ImageTraining\predict_runs",
        name="video_chicken"
    )
    for _ in results:
        pass


if __name__ == "__main__":
    # predict_wildlife()
    predict_chicken()
