import cv2
import pytesseract


vid = cv2.VideoCapture("NARUTO.mp4")

frameCount = 0
while(True):
    
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_gpu = cv2.UMat(gray)

    gray_gpu = gray_gpu.get()

    # _, tresh = cv2.threshold(gray_gpu, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # tresh = tresh.get()


    # img_rbg = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    if frameCount %30 == 0:
        print(pytesseract.image_to_string(gray_gpu))

    if not ret:
        print("cannot recieve framerouni")
        break

    # cv2.imshow('frame', gray)

    frameCount += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    


vid.release()
cv2.destroyAllWindows()