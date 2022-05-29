import cv2


# =============================================================================
# print(cv2.__version__)
# img=cv2.imread(r"C:\Users\Abdur rahim nishad\OneDrive\Desktop\New folder - Copy\Screenshot_1.png",1)
# img=cv2.resize(img,(1000,600))
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# 
# #gray
# print(cv2.__version__)
# img2=cv2.imread(r"C:\Users\Abdur rahim nishad\OneDrive\Desktop\New folder - Copy\Screenshot_1.png",0)
# img2=cv2.resize(img2,(1000,600))
# cv2.imshow("Gray image",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# #color increased
# 
# print(cv2.__version__)
# img3=cv2.imread(r"C:\Users\Abdur rahim nishad\OneDrive\Desktop\New folder - Copy\Screenshot_1.png",-1)
# img3=cv2.resize(img3,(1000,600))
# cv2.imshow("Gray image",img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================


path=input("enter the path")
img3=cv2.imread(path,0)
cv2.imshow("converted",img3)
k=cv2.waitKey()
if k==ord("s"):
    cv2.imwrite(r"C:\Users\Abdur rahim nishad\OneDrive\Desktop\sda\output.png",img3)
else:
    cv2.destroyAllWindows()



img4=cv2.imread(r"C:\Users\Abdur rahim nishad\OneDrive\Desktop\New folder - Copy\Screenshot_1.png",-1)
img4=cv2.resize(img3,(1000,600))
img4=cv2.flip(img4,1)
cv2.imshow("Gray image",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()







