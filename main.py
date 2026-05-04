from ultralytics import YOLO


def train_wildlife():
    model = YOLO("yolo26n.pt")
    model.train(
        data=r"c:\Other\ImageTraining\datasets\african-wildlife\african-wildlife.yaml",
        epochs=100,
        imgsz=640,
        patience=15,
        batch=8,
        project=r"C:\Other\ImageTraining\runs",
        name="african_wildlife_26s",
        workers=0,
        device=0
    )


def train_chicken():
    model = YOLO("yolo26n.pt")
    model.train(
        data=r"c:\Other\ImageTraining\datasets\chicken\data.yaml",
        epochs=100,
        imgsz=640,
        patience=15,
        batch=8,
        project=r"C:\Other\ImageTraining\runs",
        name="chicken",
        workers=0,
        device=0
    )


if __name__ == "__main__":
    # train_wildlife()
    train_chicken()
