from PyQt5.QtCore import QSize, QPropertyAnimation, pyqtProperty, QEasingCurve, Qt, pyqtSignal
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QPushButton, QSlider, QDesktopWidget, QProxyStyle, QStyle, QComboBox, QHeaderView
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5 import QtGui, QtCore

from Functions import ScreenSize

screenwidth, screenheight = ScreenSize()
class CustomDropDownStyle(QProxyStyle):
    def __init__(self, icon_path, *args, **kwargs):
        super(CustomDropDownStyle, self).__init__(*args, **kwargs)
        self.custom_icon = QIcon(icon_path)

    def drawPrimitive(self, element, option, painter, widget=None):
        if element == QStyle.PE_IndicatorArrowDown:
            pixmap = self.custom_icon.pixmap(QSize(16, 16))
            painter.drawPixmap(option.rect.x(), option.rect.y(), pixmap)
        else:
            super().drawPrimitive(element, option, painter, widget)

class CustomQComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super(CustomQComboBox, self).__init__(*args, **kwargs)
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet("""
    QComboBox {
        padding-right: 20px;
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox QAbstractItemView {
        background-color: transparent;
        border: none;
        outline: none;
        border-radius: 0;
        selection-background-color: transparent;
    }
    QComboBox:disabled {
        background-color: #808080;
    }
""")

    def wheelEvent(self, event):
        event.ignore()

class CustomMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)
        self.setStyleSheet("""
    QMenu {
        border: none;
        background-color: #F0F0F0; /* Change this to your desired background color */
        selection-background-color: #A0A0A0; /* Change this to your desired selection color */
    }
""")


    def changeEvent(self, event):
        if event.type() == event.WindowStateChange:
            if not self.isMaximized():
                self.resize(QSize(int(screenwidth/3*2), int(screenheight/3*2)))
                self.center()

        super(CustomMainWindow, self).changeEvent(event)

    def center(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        screen_center = screen_geometry.center()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_center)
        self.move(window_geometry.topLeft())
class CustomTableWidget(QTableWidget):
    
    def mousePressEvent(self, event):
        clicked_index = self.indexAt(event.pos())
        if not clicked_index.isValid():
            self.clearSelection()
            self.setCurrentCell(-1, -1)
            self.itemSelectionChanged.emit()  # Emit the signal manually
        super().mousePressEvent(event)

class CustomButton(QPushButton):
    def __init__(self, parent=None, start_color=QColor(31, 90, 146), end_color=QColor(52, 196, 251), pressed_color=None, disabled_color=QColor(180, 180, 180)):
        super(CustomButton, self).__init__(parent)
        self._background_color = start_color

        self.hover_animation = QPropertyAnimation(self, b'backgroundColor')
        self.hover_animation.setDuration(250)  # 250 ms for the transition
        self.hover_animation.setEasingCurve(QEasingCurve.OutCubic)

        self.setMouseTracking(True)

        if pressed_color is None:
            pressed_color = start_color.darker(150)

        self.normal_start_color = start_color
        self.normal_end_color = end_color
        self.pressed_color = pressed_color
        self.disabled_color = disabled_color

        # Set the initial background color
        self.backgroundColor = start_color

        # Call enterEvent and leaveEvent to set the initial style correctly
        self.enterEvent(None)
        self.leaveEvent(None)

    @pyqtProperty(QColor)
    def backgroundColor(self):
        return self._background_color

    @backgroundColor.setter
    def backgroundColor(self, color):
        self._background_color = color
        self.setStyleSheet(f"QPushButton {{"
                           f"    color: rgb(255, 255, 255);"
                           f"    border-radius: 5px;"
                           f"    background-color: {color.name()};"
                           f"}}"
                           f"QPushButton:hover {{"
                           f"    background-color: {color.lighter(130).name()};"
                           f"}}"
                           f"QPushButton:pressed {{"
                           f"    background-color: {self.pressed_color.name()};"
                           f"}}"
                           f"QPushButton:disabled {{"
                           f"    background-color: {self.disabled_color.name()};"
                           f"}}")

    def enterEvent(self, event):
        if not self.isEnabled():
            return
        self.hover_animation.setStartValue(self.normal_start_color)
        self.hover_animation.setEndValue(self.normal_end_color)
        self.hover_animation.setDirection(QPropertyAnimation.Forward)
        self.hover_animation.start()
        super(CustomButton, self).enterEvent(event)

    def leaveEvent(self, event):
        if not self.isEnabled():
            return
        self.hover_animation.setDirection(QPropertyAnimation.Backward)
        self.hover_animation.start()
        super(CustomButton, self).leaveEvent(event)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.EnabledChange:
            if self.isEnabled():
                self.hover_animation.setStartValue(self.disabled_color)
                self.hover_animation.setEndValue(self.normal_start_color)
            else:
                self.hover_animation.setStartValue(self.normal_start_color)
                self.hover_animation.setEndValue(self.disabled_color)
            self.hover_animation.setDirection(QPropertyAnimation.Forward)
            self.hover_animation.start()
        super(CustomButton, self).changeEvent(event)
        
class CustomHeaderProxyStyle(QProxyStyle):

    def drawControl(self, element, option, painter, widget=None):
        if element == QStyle.CE_HeaderLabel:
            # Fill the entire header region with the desired background color
            if isinstance(widget, QHeaderView):
                header = widget
                total_width = header.length()
                total_height = option.rect.height()
                painter.fillRect(0, 0, total_width, total_height, QtGui.QColor('#F0F0F0'))

            # Draw the section background and text
            painter.save()
            painter.fillRect(option.rect, QtGui.QColor('#F0F0F0'))
            painter.setPen(Qt.black)
            painter.drawText(option.rect, Qt.AlignCenter, option.text)
            painter.restore()
        else:
            super().drawControl(element, option, painter, widget)
class ClickableSlider(QSlider):
    sliderReleasedAt = pyqtSignal(int)  # Add this custom signal
    sliderValueChanged = pyqtSignal(int)  # Add a new custom signal for value changes

    def __init__(self, orientation, player, parent=None):
        super().__init__(orientation, parent)
        self.setTracking(False)  # Disable tracking to prevent updating the value while dragging
        self.player = player  # Store the player reference
        self.videoWasPlaying = False  # Add a flag to store the playback status

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Update the videoWasPlaying flag
            self.videoWasPlaying = self.player.state() == QMediaPlayer.PlayingState

            # Pause the video while user is sliding the slider
            self.player.pause()

            value = self.minimum() + (self.maximum() - self.minimum()) * event.x() / self.width()
            self.setValue(round(value))  # Convert the float value to an integer
            self.sliderValueChanged.emit(round(value))  # Emit the sliderValueChanged signal
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            value = self.minimum() + (self.maximum() - self.minimum()) * event.x() / self.width()
            self.setValue(round(value))
            self.sliderReleasedAt.emit(round(value))  # Emit the custom signal with the value
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            value = self.minimum() + (self.maximum() - self.minimum()) * event.x() / self.width()
            self.sliderReleasedAt.emit(round(value))  # Convert the float value to an integer and emit the custom signal
            self.sliderValueChanged.emit(round(value))  # Emit the sliderValueChanged signal

            # Resume playing the video if it was playing before
            if self.videoWasPlaying:
                self.player.play()

            event.accept()
        else:
            super().mouseReleaseEvent(event)
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        key = event.key()
        if key == Qt.Key_Right:
            self.parent().skip_forward()
        elif key == Qt.Key_Left:
            self.parent().skip_backward()

class ClickableVideoWidget(QVideoWidget):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
            event.accept()
        else:
            super().mousePressEvent(event)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.parent().skip_forward()
        elif event.key() == Qt.Key_Left:
            self.parent().skip_backward()
        elif event.key() == Qt.Key_Down:
            volume = max(0, self.parent().volumeSlider.value() - 5)
            self.parent().volumeSlider.setValue(volume)
        elif event.key() == Qt.Key_Up:
            volume = min(100, self.parent().volumeSlider.value() + 5)
            self.parent().volumeSlider.setValue(volume)
        else:
            super().keyPressEvent(event)