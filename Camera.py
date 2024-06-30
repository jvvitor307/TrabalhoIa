import cv2


def capturar_foto():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite("foto.jpg", frame)
    return "foto.jpg"
