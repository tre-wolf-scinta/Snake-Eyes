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
from PyQt6.QtGui import QFocusEvent

from .shortcuts import setup_nav_shortcuts
from core.dice_logic import Dice
from core.announcer import announce

# Custom label class definition
class FocusableLabel(QLabel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.default_style = "font-size: 24px; font-weight: bold; color: black;"
    self.focused_style = "font-size: 24px; font-weight: bold; color: black; background-color: #a8d8ff;"
    self.setStyleSheet(self.default_style)
    self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

  def focusInEvent(self, event: QFocusEvent):
    self.setStyleSheet(self.focused_style)
    super().focusInEvent(event)

  def focusOutEvent(self, event: QFocusEvent):
    self.setStyleSheet(self.default_style)
    super().focusOutEvent(event)

# MainWindow class definition
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("SnakeEyes - Accessible Dice Roller")
    self.resize(800, 600)
    self._setup_ui()
    self._connect_signals()

  def _setup_ui(self):
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
# Use custom FocusableLabel to put on top of main content area
    self.dice_bag_header = FocusableLabel("Dice Bag")
# Add header label to main layout
    main_layout.addWidget(self.dice_bag_header)

# Using grid layout for displaying buttons
    button_layout = QGridLayout()
    self.dice_buttons = {}
    dice_types = [20, 12, 10, 8, 6, 4]
    positions = [(row, col) for row in range(3) for col in range(2)]
    for position, sides in zip(positions, dice_types):
      button_text = f"D{sides}"
      button = QPushButton(button_text)
      button.setMinimumSize(100, 50)
      button_layout.addWidget(button, position[0], position[1])
      self.dice_buttons[sides] = button

# Add grid of buttons under the label heading in the main vertical layout
    main_layout.addLayout(button_layout)
# Set main layout to main container widget
    main_container.setLayout(main_layout)

# Add main container to the central widget of MainWindow
    self.setCentralWidget(main_container)

  def _connect_signals(self):    
    setup_nav_shortcuts(
      parent_window = self,
      sidebar_widget = self.tools_list,
      main_content_widget = self.dice_bag_header
    )
    for sides, button in self.dice_buttons.items():
      die = Dice(sides=sides)
      button.click.connect(self._create_roll_handler(die))

  def _create_roll_handler(self, dice_to_roll: Dice):
    def handler():
      result = dice_to_roll.roll()
      announce(f"You rolled a {dice_to_roll} and got a {result}")
    return handler