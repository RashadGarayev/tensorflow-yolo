import numpy as np
import time
import tensorflow as tf
import cv2
from darkflow.net.build import TFNet

config = tf.ConfigProto(log_device_placement=True)
#config.gpu_option.allow_growth=True
with tf.Session(config=config) as sess:
    options = {
        'model' : 'cfg/yolo.cfg',
        'load' : 'cfg/yolo.weights',
        'threshold' : 0.2,
        'gpu' : 1
    }
    tfnet=TFNet(options)
colors=[tuple(255*np.random.rand(3)) for _ in range(10)]
capture=cv2.VideoCapture('B.mp4')
#capture.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

while True:
    stime=time.time()
    ret,frame=capture.read()
    if ret:
        results=tfnet.return_predict(frame)
        for color,result in zip(colors,results):
            tl=(result['topleft']['x'],result['topleft']['y'])
            br=(result['bottomright']['x'],result['bottomright']['y'])
            label=result['label']
            confidence=result['confidence']
            text='{}: {:0f}%'.format(label,confidence*100)
            frame=cv2.rectangle(frame,tl,br,color,5)
            frame=cv2.putText(frame,text,tl,cv2.FONT_ITALIC,1,(0,0,0),2)
        cv2.imshow('frame',frame)
        #print('FPS {:.1f}'.format(1/(time.time()-stime)))
		
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()