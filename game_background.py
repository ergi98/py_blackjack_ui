from os import path
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation
from PyQt6.QtWidgets import QLabel, QGraphicsBlurEffect, QGraphicsOpacityEffect

class GameBackground(QLabel):
  def __init__(self, parent, blur_amount=0):
    super().__init__(parent)
    self.parent = parent
    self.blur_amount = blur_amount
    self.pixmap = QPixmap(path.join('assets', 'game_background.png'))
    self.set_background()
    
  def set_background(self):
    self.setGeometry(0, 0, self.parent.width(), self.parent.height())
    self.setPixmap(
      self.pixmap.scaled(
        self.parent.size(), 
        Qt.AspectRatioMode.KeepAspectRatio, 
        Qt.TransformationMode.SmoothTransformation
      )
    )
    self.setScaledContents(True)
    # Blur effect
    self.blur_effect = QGraphicsBlurEffect(self.parent)
    self.blur_effect.setBlurRadius(self.blur_amount)
    self.setGraphicsEffect(self.blur_effect)

  def animate_update_blur(self, updated_value = 0):
    self.blur_animation = QPropertyAnimation(self.blur_effect, b"blurRadius")
    self.blur_animation.setDuration(300)
    self.blur_animation.setStartValue(self.blur_amount)
    self.blur_animation.setEndValue(updated_value)
    self.blur_animation.start()