import os
import cv2
arr = os.listdir('.')
count=0
for file in arr :
    if file.endswith(".png") or file.endswith(".jpg"):
        face_ade=cv2.CascadeClassifier("face.xml")
        img= cv2.imread(file,1)
        gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=face_ade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)
        for x,y,w,h in face:

            # x and y are the positions of rectangle that was for the face i just took those co-ordinates and expanded them ***warning doesnt work with every image***
            imgCropped=img[y-100:y+h*2,200:x+w*2]
            count=count+1
            cnt=str(count)
            cv2.imwrite("face"+cnt+" .jpg",imgCropped)
            imc=cv2.imshow("cropped",imgCropped)
            cv2.waitKey(1000)
            cv2.destroyAllWindows() 



