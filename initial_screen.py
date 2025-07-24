from PyQt6.QtWidgets import (
  QWidget, QVBoxLayout, QLabel,
  QComboBox, QPushButton, QLineEdit,
  QGraphicsOpacityEffect
)
from PyQt6.QtCore import Qt, QPropertyAnimation

from constants import MAX_PLAYER_COUNT

class InitialScreen(QWidget):
  player_name = ''
  selected_index = 0
  bot_options = list(str(x) for x in range(MAX_PLAYER_COUNT))

  def __init__(self, on_start_callback):
    super().__init__()
    self.on_start_callback = on_start_callback
    self.setup_ui()
    
  def setup_ui(self):
    # Containers
    layout = QVBoxLayout(self)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # Elements
    self.screen_title = QLabel("BLACKJACK")
    self.screen_title.setStyleSheet('font-weight: bold; font-size: 32px; padding-bottom: 24px')
    # 
    self.name_label = QLabel("Enter your name:")
    self.name_label.setStyleSheet('font-size: 14px; font-weight: bold')
    # 
    self.name_input = QLineEdit()
    self.name_input.setFixedWidth(312)
    self.name_input.textChanged.connect(self.on_name_input_change)
    
    self.name_input.setStyleSheet('''
      padding: 8px;
      color: #fafafa;
      font-size: 16px;
      border-radius: 8px; 
      background-color: #052e16; 
      border: 2px solid #16a34a;
    ''')
    # 
    self.name_input_error = QLabel("Please enter a name!")
    self.name_input_error.setStyleSheet('font-size: 14px; color: #fca5a5')
    self.name_input_error.hide()
    # 
    self.bot_count_label = QLabel("No. of bot players:")
    self.bot_count_label.setStyleSheet('font-size: 14px; font-weight: bold; padding-top: 4px')
    # 
    self.bot_count_input = QComboBox()
    self.bot_count_input.setFixedWidth(312)
    self.bot_count_input.setCurrentIndex(0)
    self.bot_count_input.addItems(self.bot_options)
    self.bot_count_input.activated.connect(self.on_bot_count_select)
    self.bot_count_input.setStyleSheet('''
      QComboBox {
        padding: 8px;
        color: #fafafa;
        font-size: 16px;
        border-radius: 8px;
        margin-bottom: 24px;
        border: 2px solid #16a34a;
        background-color: #052e16; 
      }
      QComboBox QAbstractItemView {
        background-color: auto;
      } 
    ''')
    # 
    self.action_button = QPushButton("Start Game")
    self.action_button.clicked.connect(self.on_start_game_click)
    self.action_button.setStyleSheet('''
      QPushButton { 
        color: #fafafa;
        border-radius: 8px;
        background-color: #16a34a;
        text-transform: uppercase;
        font-size: 16px; padding: 12px 24px;
      }
      QPushButton:hover {
        background-color: #15803d;
      }
      QPushButton:pressed {
        background-color: #166534;
      }
    ''')
    # Composing
    layout.addWidget(self.screen_title, alignment=Qt.AlignmentFlag.AlignHCenter)
    layout.addWidget(self.name_label)
    layout.addWidget(self.name_input)
    layout.addWidget(self.name_input_error)
    layout.addWidget(self.bot_count_label)
    layout.addWidget(self.bot_count_input)
    layout.addWidget(self.action_button, alignment=Qt.AlignmentFlag.AlignCenter)
    
  def on_bot_count_select(self, index):
    self.selected_index = index
    
  def on_name_input_change(self, text):
    self.player_name = text.strip()
    if self.name_input_error.isVisible:
      self.name_input_error.hide()
    
  def on_start_game_click(self):
    if len(self.player_name) == 0:
      self.name_input_error.show()
      return
    self.fade_initial_screen()
    
  def start_game(self):
    # Remove widget
    self.setParent(None)
    self.deleteLater()
    if callable(self.on_start_callback):
      self.on_start_callback(
        name=self.player_name, 
        bot_count = self.bot_options[self.selected_index]
      )
      
  def fade_initial_screen(self):
    opacity = QGraphicsOpacityEffect(self)
    self.setGraphicsEffect(opacity)
    self.element_animation = QPropertyAnimation(opacity, b'opacity')
    self.element_animation.setDuration(300)
    self.element_animation.setStartValue(1)
    self.element_animation.setEndValue(0)
    self.element_animation.start()
    self.element_animation.finished.connect(self.start_game)