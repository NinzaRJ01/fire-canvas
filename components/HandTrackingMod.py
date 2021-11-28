import cv2,time,sys
import mediapipe as mp
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets  import *

class HandTracker(QObject):
    VideoSignal = pyqtSignal(QImage)
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    def __init__(self,parent=None):
        super(HandTracker, self).__init__(parent)

        self.hands = self.mp_hands.Hands(
                model_complexity=1,
                max_num_hands=1,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5)
        

    @pyqtSlot()
    def startTracking(self):
        cap = cv2.VideoCapture(0)
        hands = self.hands
        mp_hands = self.mp_hands
        mp_drawing = self.mp_drawing
        mp_drawing_styles = self.mp_drawing_styles
        PTime=0# previous time
        CTime=0# current time
        while cap.isOpened():
            success, image = cap.read()
            # image = cv2.resize(image, (1050, 1610))
    
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue
            #Resizes Image
            image = cv2.flip(image, 1)
            image = cv2.resize(image, )

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
              for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS) #,
            # mp_drawing_styles.get_default_hand_landmarks_style(),
            # mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
            self.printCor(results,image)
            CTime=time.time()#current time
            fps=1/(CTime-PTime)#FPS
            PTime=CTime#previous time is replaced by current time
            
            cv2.putText(image,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
            # cv2.imshow('MediaPipe Hands',image)

            
            height, width, _ = image.shape
			
            qt_image = QImage(image.data,
									width, 
									height,
			   						QImage.Format_RGB888)

            pixmap = QPixmap(qt_image)
            qt_image = pixmap.scaled(1000, 600, Qt.KeepAspectRatio)
            qt_image = QImage(qt_image)
            self.VideoSignal.emit(qt_image)
    
            if cv2.waitKey(5) & 0xFF == 27:
                break
        closeCap(cap)
    def closeCap(self,cap):
        cap.release()
    def printCor(self,results, image):
      image_height, image_width, _ = image.shape
      mp_hands = self.mp_hands
      if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            #  print(
            #     f'Index finger tip coordinates: (',
            #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
            #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
            #  )
             if (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height) :
                 if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                    print("PICK ")
    def __exit__(self):
        self.hands.close()

class ImageViewer(QWidget):
	def __init__(self, parent = None):
		super(ImageViewer, self).__init__(parent)
		self.image = QImage()
		self.setAttribute(Qt.WA_OpaquePaintEvent)



	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawImage(0,0, self.image)
		self.image = QImage()

	def initUI(self):
		self.setWindowTitle('Test')

	
	@pyqtSlot(QImage)
	def setImage(self, image):
		if image.isNull():
			print("viewer dropped frame!")

		self.image = image
		# if image.size() != self.size():
		# 	# self.setFixedSize(self.size())
		# 	self.image.scaled(self.size())
		self.update()