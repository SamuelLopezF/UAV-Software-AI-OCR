import cv2
import pytesseract
import re


vid = cv2.VideoCapture(r"NARUTO.mp4")

frameCount = 0
while(True):

    ret, frame = vid.read()
    if frameCount % 30 == 0:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray_gpu = cv2.UMat(gray)
        gray_gpu = gray_gpu.get()

        blur = cv2.GaussianBlur(gray_gpu, (5,5), 0)
        _, frame_thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        input = frame_thresh
        result = pytesseract.image_to_string(input, config=r"--psm 3")
        filtered = re.sub('[^a-zA-Z!.,\n ]', '', result )
        print(filtered)
        cv2.imshow('frame', input)

    frameCount += 1

    if not ret:
        print("cannot recieve framerouni or end of footage")
        break
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()