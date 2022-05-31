
# =============================================================================
# 
# import cv2
# cap=cv2.VideoCapture(r"C:\Users\Abdur rahim nishad\Downloads\index (1).mp4")
# #print(cap)
# 
# while True:
#     ret,frame=cap.read()
#     frame=cv2.resize(frame,(500,400))
#     cv2.imshow("frame",frame)
#     k=cv2.waitKey(25)
#     if k==ord("q") & 0xFf:
#         break
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================


#gray color video


import cv2
cap2=cv2.VideoCapture(r"C:\Users\Abdur rahim nishad\Downloads\index (1).mp4")


while True:
    ret,frame=cap2.read()
    frame=cv2.resize(frame,(500,400))
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k=cv2.waitKey(25)
    if k==ord("a") & 0xFf:
        break
cap2.release()

cv2.destroyAllWindows()


#Now capture video from webcam and save into memory

# =============================================================================
# import cv2
# #cap3=cv2.VideoCapture(0)
# #if warning comes i have to do
# cap3=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# 
# #formate: DIVX, XVID, MJPG, X264,WMV1,WMV2
# #if i save it
# 
# fourcc=cv2.VideoWriter_fourcc(*  "XVID")
# #it contain 4 patameter like name,dodec,fps,resolution
# output=cv2.VideoWriter(r'C:\Users\Abdur rahim nishad\.spyder-py3\output',fourcc,20.0,(100,700),0)
# 
# while cap3.isOpened():
#     ret,frame=cap3.read()
#     if ret==True:
#          #frame=cv2.resize(frame,(1500,700))
#          gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         #i can use flip than i have to use 0 in output variable
#          gray=cv2.flip(gray,0)
#          #cv2.imshow("frame",frame)
#          cv2.imshow("gray",gray)
#          output.write(gray)
#          if cv2.waitKey(100) & 0xFF==ord("a"):
#          #k=cv2.waitKey(25)
#          #if k==ord("a") & 0xFf:
#              break
#      
# cap3.release()
# output.release()
# cv2.destroyAllWindows()
# =============================================================================











