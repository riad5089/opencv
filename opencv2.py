import cv2
cap=cv2.VideoCapture(r"C:\Users\Abdur rahim nishad\Downloads\index (1).mp4")
#print(cap)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,400))
    cv2.imshow("frame",frame)
    k=cv2.waitKey(25)
    if k==ord("q") & 0xFf:
        break
cap.release()
cv2.destroyAllWindows()
    