# gui/shortcuts.py
from PyQt6.QtGui import QAction

"""
  sets up navigation shortcuts for the application

  args:
    parent_window: A QMainWindow object to which shortcuts are added
    sidebar_widget: The widget inside the sidebar which should receive focus
    main_content_widget: The widget within the main area to receive focus (e.g., QLabel)
"""
def setup_nav_shortcuts(parent_window, sidebar_widget, main_content_widget):

  def create_focus_slot(target_widget):
    def focus_slot():
      target_widget.setFocus()
    return focus_slot

# Creating nav shortcut to set focus to sidebar
    focus_sidebar_action = QAction("Focus Tools Sidebar", parent_window)
    focus_sidebar_action.setShortcut("Ctrl+1")
    focus_sidebar_action.triggered.connect(create_focus_slot(sidebar_widget))
    parent_window.addAction(focus_sidebar_action)

# Creating nav shortcut to set focus to main content area
    focus_main_action = QAction("Focus main area", parent_window)
    focus_main_action.setShortcut("Ctrl+2")
    focus_main_shortcut.triggered.connect(create_focus_slot(main_content_widget))
    parent_window.addAction(focus_main_action)

