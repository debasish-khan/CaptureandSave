
import cv2

cap = cv2.VideoCapture(0)           #captures video
fourcc = cv2.VideoWriter_fourcc(*'XVID')                    #encodesintovideoformat
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))          #writesvideowith 20fps and frame size 640*480

print(cap.isOpened())
while(cap.isOpened()):                      #ifcameraisopen
    ret, frame = cap.read()                  #readframe
    if ret == True:                          #iftrue
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))                #printwidth
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))               #printheight

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
