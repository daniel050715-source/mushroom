from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("best.pt")
    # 測試資料夾裡的照片（之後換新照片只要改這裡的路徑）
    results = model.predict(
        source=r"C:\Users\User\Desktop\mushroom_dataset\images\val",
        save=True,
        conf=0.5
    )