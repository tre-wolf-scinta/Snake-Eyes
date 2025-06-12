#gui/main_window.py
import sys
from PyQt6.QtWidgets import (
  QApplication,  QMainWindow,
  QPushButton,
  QWidget,  QVBoxLayout,
  QGridLayout,
  QVBoxLayout,
  QDockWidget,
  QListWidget,
  QLabel,
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from .shortcuts import setup_nav_shortcuts

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

# Create sidebar using QDockWidget so users can move sidebar as needed for visual accessibility
    self.sidebar = QDockWidget("Tools")
# Use QListWidget to hold list of tools user can choose from in sidebar
    self.tools_list = QListWidget()
    self.sidebar.setWidget(self.tools_list)
# Adds sidebar to main window and stick it to left side of screen
    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)

# Creating container to hold widgets in main area
    main_container = QWidget()
# Using VBoxLayout to stack label heading on top of buttons 
    main_layout = QVBoxLayout()
# Create QLabel to put on top of main content area
    self.dice_bag_header = QLabel("Dice Bag")
# Make label focusable 
    self.dice_bag_header.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
# Add header label to main layout
    main_layout.addWidget(self.dice_bag_header)

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
# Add grid of buttons under the label heading in the main vertical layout
    main_layout.addLayout(button_layout)
# Set main layout to main container widget
    main_container.setLayout(main_layout)

# Add main container to the central widget of MainWindow
    self.setCentralWidget(main_container)

# Set navigation shortcuts for main window
    setup_nav_shortcuts(
      parent_window = self,
      sidebar_widget = self.tools_list,
      main_content_widget = self.dice_bag_header
    )
