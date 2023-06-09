from PyQt5.QtWidgets import QWidget, QStyle, QSlider, QSizePolicy, QFileDialog, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QStyle
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl, QTime
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from Functions import ScreenSize
from CustomPyQt import ClickableVideoWidget, ClickableSlider

screenwidth, screenheight = ScreenSize()

class Window(QWidget):
    def __init__(self, TextsForData, parent=None):
        super().__init__(parent)
        self.TextsForData = TextsForData
        self.setWindowTitle("PyQt5 Media Player")
        self.setWindowIcon(QIcon('player.png'))
        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)
        self.init_ui()
        self.show()

    def slider_released_at(self, position):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.setPosition(position)
        else:
            self.mediaPlayer.setPosition(position)
            # Do not start playback if the player was paused


    def update_play_button(self, state):
        play_icon = QIcon("resources/play.png")
        if state == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playBtn.setIcon(play_icon)
    
    def hideEvent(self, event):
        self.mediaPlayer.stop()
        event.accept()

    def init_ui(self):
        
        open_icon = QIcon("resources/OpenMediaButton.png")
        sound_icon = QIcon("resources/Sound.png")
        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # create video widget object
        videowidget = ClickableVideoWidget()
        videowidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # create open button
        openBtn = QPushButton('Open Video')
        openBtn.setIcon(open_icon)
        openBtn.clicked.connect(self.open_file)
        # create volume slider
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setFixedWidth(100)
        self.volumeSlider.valueChanged.connect(self.set_volume)
        # create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.clicked.connect(self.play_video)
        self.playBtn.setShortcut("ctrl+Space")
        # create volume label
        self.volumeLabel = QLabel("🔊")
        # create slider
        self.slider = ClickableSlider(Qt.Horizontal, self.mediaPlayer)
        self.slider.setRange(0,0)

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # create labels to show the current time and total duration
        self.currentTimeLabel = QLabel()
        self.currentTimeLabel.setText("0:00")
        self.totalTimeLabel = QLabel()
        self.totalTimeLabel.setText("0:00")
        timeLabelPalette = self.currentTimeLabel.palette()
        timeLabelPalette.setColor(QPalette.WindowText, Qt.black)
        self.currentTimeLabel.setPalette(timeLabelPalette)
        self.totalTimeLabel.setPalette(timeLabelPalette)
        self.slashlabel=QLabel()
        self.slashlabel.setText("/")
        slashlabelPalette=self.slashlabel.palette()
        slashlabelPalette.setColor(QPalette.WindowText, Qt.black)
        self.slashlabel.setPalette(slashlabelPalette)
        # create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)
        hboxLayout.setSpacing(5)
        # set widgets to the hbox layout
        hboxLayout.addWidget(openBtn, alignment=Qt.AlignBottom)
        hboxLayout.addWidget(self.playBtn, alignment=Qt.AlignBottom)
        hboxLayout.addWidget(self.slider, alignment=Qt.AlignBottom)
        hboxLayout.addWidget(self.currentTimeLabel, alignment=Qt.AlignBottom)
        hboxLayout.addWidget(self.slashlabel, alignment=Qt.AlignBottom)
        hboxLayout.addWidget(self.totalTimeLabel, alignment=Qt.AlignBottom)
        hboxLayout.addWidget(self.volumeLabel, alignment=Qt.AlignBottom)
        hboxLayout.addWidget(self.volumeSlider, alignment=Qt.AlignBottom)
        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.setContentsMargins(5, 0, 5, 0)
        vboxLayout.setSpacing(12)
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)
        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)
        # media player signals
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.mediaStatusChanged.connect(self.media_status_changed)
        self.slider.sliderReleasedAt.connect(self.slider_released_at)
        self.slider.sliderValueChanged.connect(self.set_position)
        self.mediaPlayer.stateChanged.connect(self.update_play_button)
        videowidget.clicked.connect(self.play_video)
        videowidget.setFocusPolicy(Qt.StrongFocus)
        self.openProject()
    def skip_forward(self):
        position = self.mediaPlayer.position()
        new_position = position + 5000  # 5 seconds in milliseconds
        self.mediaPlayer.setPosition(new_position)

    def skip_backward(self):
        position = self.mediaPlayer.position()
        new_position = position - 5000  # 5 seconds in milliseconds
        self.mediaPlayer.setPosition(new_position)

    def set_volume(self, volume):
        self.mediaPlayer.setVolume(volume)
    def open_file(self):
        try:
            filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
            if filename != '':
                self.TextsForData.set_vP(filename)
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
                self.playBtn.setEnabled(True)
                self.mediaPlayer.pause()
                self.mediaPlayer.setPosition(0)  # Set the position to the first frame
        except:
            print("directshad")
    def openProject(self):
        if self.TextsForData.get_vP() != "None":
            filename = self.TextsForData.get_vP()
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    def media_status_changed(self, status):
        if status == QMediaPlayer.LoadedMedia:
            self.mediaPlayer.pause()
            self.mediaPlayer.setPosition(0)
    def position_changed(self, position):
        self.slider.setValue(position)
    # update the current time label
        currentTime = QTime(0, 0).addMSecs(position)
        self.currentTimeLabel.setText(currentTime.toString("mm:ss"))
    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
        # update the total time label
        totalTime = QTime(0, 0).addMSecs(duration)
        self.totalTimeLabel.setText(totalTime.toString("mm:ss"))

    def set_position(self, position):
        self.mediaPlayer.positionChanged.disconnect(self.position_changed)
        self.mediaPlayer.setPosition(position)
        self.mediaPlayer.positionChanged.connect(self.position_changed)


    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())