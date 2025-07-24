from os import path
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation
from PyQt6.QtWidgets import QWidget, QLabel, QGraphicsBlurEffect, QGraphicsOpacityEffect

class GameBackground(QWidget):
  def __init__(self, parent, blur_amount=0):
    super().__init__(parent)
    self.parent = parent
    self.blur_amount = blur_amount
    self.pixmap = QPixmap(path.join('assets', 'game_background.png'))
    self.set_background()
    
  def set_background(self):
    self.setGeometry(0, 0, self.parent.width(), self.parent.height())
    self.background_label = QLabel(self)
    self.background_label.setGeometry(0, 0, self.parent.width(), self.parent.height())
    self.background_label.setPixmap(
      self.pixmap.scaled(
        self.parent.size(), 
        Qt.AspectRatioMode.KeepAspectRatio, 
        Qt.TransformationMode.SmoothTransformation
      )
    )
    self.background_label.setScaledContents(True)
    # Blur effect
    blur_effect = QGraphicsBlurEffect(self.parent)
    blur_effect.setBlurRadius(self.blur_amount)
    self.background_label.setGraphicsEffect(blur_effect)
    # Opacity
    self.opacity_effect = QGraphicsOpacityEffect(self)
    self.setGraphicsEffect(self.opacity_effect)


  def animate_update_blur(self):
    self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
    self.opacity_animation.setDuration(1000)
    self.opacity_animation.setStartValue(1.0)
    self.opacity_animation.setEndValue(0.0)
    self.opacity_animation.start()