import cv2

path="F:\Image Processing\lena.jpg"
img=cv2.imread(path)
imaGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imaGray,(99,99),0)
cv2.imshow("EINSTEIN",imaGray)
cv2.imshow('output',img)
cv2.imshow("Rahat",imgBlur)
cv2.waitKey(0)