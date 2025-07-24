from PyQt6.QtWidgets import QMainWindow

from initial_screen import InitialScreen
from game_background import GameBackground

class MainWindow(QMainWindow):
  initial_screen_data = {
    'bot_count': 0,
    'player_name': ''
  }
  
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)
    self.setWindowTitle('BLACKJACK')
    self.setMinimumSize(1050, 650)
    self.game_background = GameBackground(self, blur_amount=15)
    self.initial_screen = InitialScreen(self.on_start_game_click)
    self.setCentralWidget(self.initial_screen)

  def on_start_game_click(self, name, bot_count):
    self.initial_screen_data['player_name'] = name
    self.initial_screen_data['bot_count'] = bot_count
    self.game_background.animate_update_blur()
    pass;
    