from face_lib import face_lib
import cv2


FL = face_lib()



img = cv2.imread("./starry_night222.png")
faces = FL.get_faces(img) #return list of RGB faces image

img_to_verfiy = cv2.imread("./starry_night222.png") #image that contain face you want verify
gt_image = cv2.imread("./starry_night.png") #image of the face to compare with

face_exist, no_faces_detected = FL.recognition_pipeline(img_to_verfiy, gt_image)
print(face_exist)