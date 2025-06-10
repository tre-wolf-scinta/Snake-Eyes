import sys
from PyQt6.QtWidgets import (
  QApplication,  QMainWindow,
  QPushButton,
  QWidget,  QVBoxLayout,
  QGridLayout,
  QDockWidget,
  QListWidget,
)
from PyQt6.QtCore import Qt

# MainWindow class definition
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("SnakeEyes - Accessible Dice Roller")
    self.resize(800, 600)

    # Creating menu bar
    menu_bar = self.menuBar()

    # Add menus to menu bar with hot key bindings
    file_menu = menu_bar.addMenu("&File")
    edit_menu = menu_bar.addMenu("&Edit")
    help_menu = menu_bar.addMenu("&Help")

    # Placeholder for menu actions

    # Create sidebar using QDockWidget so users can move sidebar as needed for visual accessibility

    self.sidebar = QDockWidget("Tools")

    # Use QListWidget to hold list of tools user can choose from in sidebar
    self.tools_list = QListWidget()
    self.sidebar.setWidget(self.tools_list)

    # Adds sidebar to main window and stick it to left side of screen
    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)

# Creating container to hold widgets in main area
    main_container = QWidget()

# Using grid layout for displaying buttons
    button_layout = QGridLayout()
# Add button labels to an array
    dice_labels = ["D4", "D6", "D8", "D10", "D12", "D20"] 

# Add buttons with labels to grid
    positions = [(row, col) for row in range(2) for col in range(3)]

    for position, text in zip(positions, dice_labels):
      button = QPushButton(text)
      button.setMinimumSize(100, 50) 
      #button.setAccessibleName("Roll a " + text)
      button_layout.addWidget(button, position[0], position[1])
# Add grid of buttons to the main container
    main_container.setLayout(button_layout)

# Add main container to the central widget of MainWindow
    self.setCentralWidget(main_container)
