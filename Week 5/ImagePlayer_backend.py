from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from ImagePlayer import Ui_ImagePlayer
from opencv_filters import filters, apply_filter, filters_func
from Navigator import Page2
from datetime import datetime
import cv2
import sys

class ImagePlayer_Backend:
    def __init__(self):
        app = QApplication(sys.argv)
        self.ImagePlayer = QMainWindow()
        self.ui = Ui_ImagePlayer()
        self.ui.setupUi(self.ImagePlayer)
        self.ImagePlayer.show()

        self.ui.btnBrowse.pressed.connect(self.browseFile)
        self.ui.btnRefresh.pressed.connect(self.clearImage)

        self.camera_index = self.ui.availableCameras.currentData() if self.ui.availableCameras.currentData() is not None else 0
        self.grayScale_value = self.ui.verticalSlider.value()
        self.filter_name = ""
        self.ui.availableCameras.addItems(self.get_available_cameras())
        self.ui.availableCameras.currentIndexChanged.connect(lambda: self.updateCameraData(self.ui.availableCameras.currentText()))
        self.ui.availableFilters.currentIndexChanged.connect(lambda: self.updateFilterData(self.ui.availableFilters.currentText()))
        self.ui.btnBrowse_2.pressed.connect(self.capture)
        self.ui.verticalSlider.valueChanged.connect(self.updateGrayScaleValue)
        self.ui.verticalSlider.valueChanged.connect(self.updateFrame)
        #self.ui.availableFilters.currentIndexChanged.connect(self.updateFrame)

        self.ui.availableFilters.addItems(filters)

        self.timer = QTimer(self.ImagePlayer)
        self.timer.timeout.connect(self.updateFrame)
        

        sys.exit(app.exec_())

    def updateCameraData(self, data):
        self.camera_index = int(data)
    
    def updateFilterData(self, data):
        self.filter_name = data
    def updateGrayScaleValue(self, value):
        self.grayScale_value = value
    

    def get_available_cameras(self):
        available_cameras = []
        camera_index = 0

        while True:
            cap = cv2.VideoCapture(camera_index)
            if not cap.isOpened():
                break

            available_cameras.append(str(camera_index))
            cap.release()
            camera_index += 1

        return available_cameras

    def capture(self, num_frames=1):  
        cap = cv2.VideoCapture(self.camera_index)

        now = datetime.now()
        current_time = now.strftime("%H-%M-%S")

        for i in range(num_frames):
            ret, frame = cap.read()
            
            if ret:
                image_filename = f"captured_image_{current_time}_{i}.jpg"
                cv2.imwrite(image_filename, frame)
                cv2.imshow('frame', frame)
                cv2.waitKey(1000)

        cap.release()
        cv2.destroyAllWindows()

    def browseFile(self):
        file_dialog = QFileDialog()
        self.image_path, _ = file_dialog.getOpenFileName(None, "Open Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

        if not self.image_path:
            print("File not loaded")
            sys.exit()

        self.image = cv2.imread(self.image_path)

        if self.image is None or self.image.shape[0] == 0 or self.image.shape[1] == 0:
            print("Invalid image.")
            sys.exit()

        q_image = QImage(self.image.data, self.image.shape[1], self.image.shape[0], self.image.strides[0], QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_image)

        self.ui.label.setPixmap(pixmap)
        self.ui.label.setScaledContents(True)
        self.timer.start(int(1000 / 40))
    
    def updateFrame(self):
        frame = self.image

        if frame is None or frame.shape[0] == 0 or frame.shape[1] == 0:
            print("Error loading image.")
            return

        if self.grayScale_value == 127:
            q_image = QImage(frame.data, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_BGR888)
        else:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.convertScaleAbs(gray_frame, alpha=self.grayScale_value / 255.0)
            q_image = QImage(gray_frame.data, gray_frame.shape[1], gray_frame.shape[0], gray_frame.strides[0], QImage.Format_Grayscale8)
        
        if self.filter_name is not "" and self.grayScale_value is not 127:
            filtered_frame = apply_filter(self.filter_name, gray_frame)
            q_image = QImage(filtered_frame.data, filtered_frame.shape[1], filtered_frame.shape[0], filtered_frame.strides[0], QImage.Format_Grayscale8)
        elif self.filter_name is not "" and self.grayScale_value is 127:
            filtered_frame = apply_filter(self.filter_name, frame)
            q_image = QImage(filtered_frame.data, filtered_frame.shape[1], filtered_frame.shape[0], filtered_frame.strides[0], QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_image)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setScaledContents(True)

    def clearImage(self):
        self.ui.label.clear()
        self.timer.stop()

if __name__ == "__main__":
    backend = ImagePlayer_Backend()
    sys.exit(app.exec_())
