import torch
from PIL import Image, ImageDraw
from facenet_pytorch import MTCNN


def detect_face(image: Image, resize: int, face_size: int) -> tuple[Image, int]:
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Running on device: {device}")
    mtcnn = MTCNN(
        image_size=resize,
        min_face_size=face_size,
        factor=0.6,
        keep_all=True,
        post_process=True,
        device=device
    )
    boxes, _ = mtcnn.detect(image)
    if boxes is not None:
        for box in boxes:
            draw = ImageDraw.Draw(image)
            draw.rectangle(box.tolist(), outline='red', width=3)
    return image, len(boxes)