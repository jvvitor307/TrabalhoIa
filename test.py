from face_lib import face_lib
import cv2
FL = face_lib()


def verificacao(img_to_verify, gt_image):
    saida = cv2.imread(img_to_verify)
    base = cv2.imread(gt_image)
    face_exist, no_faces_detected = FL.recognition_pipeline(saida, base, threshold = 0.95)
    return face_exist
