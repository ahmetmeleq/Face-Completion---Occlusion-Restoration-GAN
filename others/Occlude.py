#References:
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# Sentdex - Youtube

import numpy as np
import cv2
import glob
import os
import copy

face_cascade = cv2.CascadeClassifier('C:\\Users\\ahmet\\PycharmProjects\\BmProject\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\ahmet\\PycharmProjects\\BmProject\\haarcascade_eye.xml')
face_cascade2 = cv2.CascadeClassifier('C:\\Users\\ahmet\\PycharmProjects\\BmProject\\haarcascade_profileface.xml')

main_path = "C:/Users/ahmet/Desktop"
path='C:/Users/ahmet/Desktop/data'
path2='C:/Users/ahmet/PycharmProjects/BmProject'


counter = 0
eyes=None
eyes2=None
myctr = 0

for filename in glob.glob(os.path.join(path,'*')):
    img=cv2.imread(filename,1)
    img_label= copy.copy(img)

    mybool = 0

    # We check for faces.
    faces = face_cascade.detectMultiScale(img, minNeighbors=4)
    for (x, y, w, h) in faces:
        # We detect the coordinates of the faces.
        area_of_interest = img[y: y + h, x: x + w]


        eyes = eye_cascade.detectMultiScale(area_of_interest, minNeighbors=3)
        for (ex, ey, ew, eh) in eyes:
            if (1):
                print(ew,eh)
                mybool = 1
                # We make the occlusion here.
                cv2.rectangle(area_of_interest, (ex - 5, ey - 5), (ex + ew + 90, ey + eh + 10), (0, 0, 0), -1)

            # To make only one occlusion, we break at first face and first eye that is found on an image.
            break
        # To make only one occlusion, we break at first face and first eye that is found on an image.
        break


    if(mybool == 1):
        try:
        # For this statement to function well, we assign None values to variables: eyes, eyes2 and (ex, ey, ew, eh) 
         if(isinstance(eyes,np.ndarray)| isinstance(eyes2,np.ndarray)):
             print(eyes, eyes2, counter)
             print(' ')

             cv2.imwrite(os.path.join(path2, 'occluded', os.path.basename(filename)), img)
             cv2.imwrite(os.path.join(path2, 'labels', os.path.basename(filename)), img_label)
             print(os.path.join(path2, 'occluded', os.path.basename(filename)), img)
             print(os.path.join(path2, 'labels', os.path.basename(filename)), img)
             counter = counter + 1




        except AttributeError:
            print("We got an error.",counter)

    # There is an if statement above. this line is for it to function well.
    eyes = None
    eyes2 = None
    (ex, ey, ew, eh) = (None,None,None,None)
