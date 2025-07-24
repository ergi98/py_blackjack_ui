from PyQt6.QtWidgets import QApplication

from main_window import MainWindow

stylesheet = """
  QMainWindow {
      background-image: url("D:/_Qt/img/cat.jpg"); 
      background-repeat: no-repeat; 
      background-position: center;
  }
"""

def main():
  # Create the app instance
  # Only one per app is allowed
  app = QApplication([])
  # Create app window and show
  window = MainWindow()
  window.show()
  # Start the event loop
  app.exec()
  # 
  pass


if __name__ == '__main__':
  main()