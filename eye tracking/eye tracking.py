import cv2

cap = cv2.VideoCapture(0)


while True:
    ret ,frame = cap.read()
    
    if ret is False :
        break
    
    roi = frame[240:300,320:380]
    rows, cloums,_ = roi.shape
    cv2.rectangle(frame,(320,240),(380,300),(250,150,35),1)
    
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)
    contours,_ =  cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    contours= sorted(contours,key=lambda x : cv2.contourArea(x),reverse =True)
    
    
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,0,255),1)
        cv2.line(roi,(0,y+int(h/2)),(cloums,y+int(h/2)),(0,0,255),1)
        
        break
    
    
    
    
    
    roi = cv2.resize(roi,(240,240))
    cv2.imshow("roi",roi)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()    