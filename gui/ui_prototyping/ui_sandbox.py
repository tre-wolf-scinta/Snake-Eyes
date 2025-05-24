import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,  QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__() # Call parent constructor
    self.central_widget = QWidget()
    self.setCentralWidget(self.central_widget)
    self.setWindowTitle("Snake-Eyes Sandbox") # Main app title bar text
    self.setGeometry(100, 100, 400, 300) # (x, y, width, height)
    self.init_ui() # Initialize UI elements for main app window

  def init_ui(self):
    # Instantiate a QHBoxLayout object
    self.central_layout=QHBoxLayout()

    # Create push button widgets for each type of dice
    self.d20_button = QPushButton("D20")
    self.d12_button = QPushButton("D12")
    self.d10_button = QPushButton("D10")
    self.d8_button = QPushButton("D8")
    self.d6_button = QPushButton("D6")

    #Add widgets to layout manager object
    self.central_layout.addWidget(self.d20_button)
    self.central_layout.addWidget(self.d12_button)
    self.central_layout.addWidget(self.d10_button)
    self.central_layout.addWidget(self.d8_button)
    self.central_layout.addWidget(self.d6_button)

    # Assign the QHBoxLayout object (central_layout) to manage children widgets for MainWindow's central widget
    self.central_widget.setLayout(self.central_layout)

    self.sidebar = QVBoxLayout()
    self.stacked_widget = QStackedWidget()

def main ():
  # Create instance of QApplication with ability to take command-line arguments
  app = QApplication(sys.argv)

  # Create and show instance of MainWindow
  window = MainWindow()
  window.show()

  # Ensure clean exit
  sys.exit(app.exec())

# if __name__ == '__main__':
main()
