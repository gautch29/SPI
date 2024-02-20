import cv2
import random
from multiprocessing import Process,Pipe

Known_distance = 50
Known_width = 25
#ref_image = cv2.imread("Ref_image.jpg")
fonts = cv2.FONT_HERSHEY_COMPLEX
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

rnd = random.Random()

colors = []
for i in range(0, 10):
	colors.append((rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)))

def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image): 
	return (width_in_rf_image * measured_distance) / real_width  

def Distance_finder(Focal_Length, real_face_width, face_width_in_frame): 
	return (real_face_width * Focal_Length)/face_width_in_frame  

#def face_data(image): 
#
#	face_width = 0
#	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
#	faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
#	for (_, _, _, w) in faces:
#		face_width = w 
#
#	return face_width

def faces_data(image): 

	face_width = []

	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
	faces = face_detector.detectMultiScale(gray_image, 1.3, 5) 

	for (x, y, h, w) in faces:
		face_width.append([x, y, h, w])

	return face_width 

Focal_length_found = 806
print(Focal_length_found)

cap = cv2.VideoCapture(0) 

if cap.isOpened(): 
    #Récupère les propriétées de la capture video
    videoWidth  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    videoHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Video width: ", videoWidth)
    print("Video height: ", videoHeight)
    print("Video fps: ", fps)

while True: 

    _, frame = cap.read()
    faces_widths = faces_data(frame)

    i = 0
    for face in faces_widths:
        i = i + 1
        Distance = Distance_finder(Focal_length_found, Known_width, face[3])
		
        print(Distance)
        print((face[0] + face[3]/2)/videoWidth, (face[1] + face[2]/2)/videoHeight) #Coordonnées du centre du visage

#    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

def sendData(child_conn):
    msg = Distance + " " + (face[0] + face[3]/2)/videoWidth + " " + (face[1] + face[2]/2)/videoHeight
    child_conn.send(msg)
    child_conn.close()