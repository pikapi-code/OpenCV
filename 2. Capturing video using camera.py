import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

# We provide the file name, fourcc code, Frames per second, and size.
out = cv2.VideoWriter("videos/output.avi", fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        # Get the frame properties
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # To convevrt the video to gray
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release() 
cv2.destroyAllWindows()