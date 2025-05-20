# Dice Roller Application Architecture

## Overview
The Dice Roller is a lightweight Windows desktop application built in Python. It provides a graphical user interface (GUI) for users to simulate rolling dice of various types (D4, D6, D8, D10, D12, D20, D100). The application is designed with accessibility in mind, featuring screen reader compatibility and Text-to-Speech (TTS) output for the results. A sound effect accompanies the dice roll.

## Core Technologies
- Programming Language: Python 3.x

## Components
  The application is structured around a single main class DiceRollerApp which inherits from QWidget.

##	# 3.1. User Interface (UI) 
- DiceRollerApp (PyQt6)
- Main Window (DiceRollerApp):
  - The primary container for all UI elements.

### 3.2. Application Logic - DiceRollerApp Methods
- __init__(self):
- Initializes the TTS engine (pyttsx3.init()).

### 3.3. Text-to-Speech (TTS) Module (pyttsx3)
- An instance of the pyttsx3 engine is created during application initialization.

### 3.4. Sound Effect Module (winsound)
- The winsound.PlaySound() function is used directly within the perform_roll() method.

### 3.5. External Assets
- dice_roll.wav: A sound file that must be present in the same directory as the script for the dice rolling sound effect to play.

## 4. Data Flow / User Interaction
- Application Start:
  - main() function initializes QApplication and DiceRollerApp.

## 5. Accessibility Considerations
- PyQt6 Widgets: Standard Qt widgets are used, which generally have good built-in accessibility support.

## 6. Error Handling
- TTS Initialization: A try-except block handles potential errors during pyttsx3.init(). If it fails, a QMessageBox informs the user, and the application continues without voice output.