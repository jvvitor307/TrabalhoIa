import os
import cv2
cv2path = os.path.dirname(cv2.__file__)


def find(name, path):
    for root, dirs, files in os.walk(path):
        if (name in files) or (name in dirs):
            return os.path.join(root, name)
    # Caso nao encontre, recursao para diretorios anteriores
    return find(name, os.path.dirname(path))


xml_path = find('haarcascade_frontalface_alt2.xml', cv2path)
print(xml_path)