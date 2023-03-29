import cv2
import urllib.request
import numpy as np
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

url='<IP_OF_THE_ESP32_CAM>/cam-lo.jpg'
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)

count=0

gauth = GoogleAuth()
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)
folder ="NAME_OF_THE_GOOGLE_DRIVE_FOLDER"

while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp, -1)
    
    cv2.imshow("live transmission", frame)

    key=cv2.waitKey(5)
    
    if key==ord('k'):
        t='test.jpg'
        cv2.imwrite(t, frame)
        print("image saved as: " + t)
        f= drive.CreateFile({'parents':[{'id': folder}],'title': t})
        f.SetContentFile(t)
        f.Upload()
        print("image uploaded to Google Drive as: " + t)
        break

cv2.destroyAllWindows()