from face_lib import face_lib
import cv2


FL = face_lib()


no_of_faces, faces_coors = FL.faces_locations(face_img, max_no_faces = 10) #default number of max_no_faces is 2
FL.set_detection_params(scoreThreshold=0.82, iouThreshold=0.24) # default paramters are scoreThreshold=0.7, iouThreshold=0.3

img = cv2.imread(path_to_image)
faces = FL.get_faces(img) #return list of RGB faces image

img_to_verfiy = cv2.imread(path_to_image_to_verify) #image that contain face you want verify
gt_img = cv2.imread(path_to_image_to_compare) #image of the face to compare with

face_exist, no_faces_detected = FL.recognition_pipeline(img_to_verfiy, gt_image)