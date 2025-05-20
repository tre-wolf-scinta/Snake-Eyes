# Dice Roller Application Roadmap

## Project Overview
A lightweight, accessible Windows desktop application built in Python for rolling various types of dice, with GUI, Text-to-Speech (TTS) output, and sound effects.

### Current Statustp
The application is currently in the design phase. Development expected to begin on or around May 28, 2025

Expected Key Features for v1.0:
- GUI built with PyQt6.
- Dice selection: D4, D6, D8, D10, D12, D20, D100.
- "Roll Dice" button functionality.
- Visual display of the roll result.
- Audible announcement of the roll result via TTS (pyttsx3).
- Dice rolling sound effect (dice_roll.wav).
- Basic accessibility (keyboard navigation, screen reader compatibility for core elements).

## Future Development Plan
### V2: Enhancements & Configuration 

#### History Log:

- Implement a feature to display a log of recent rolls made during the current session.
- Allows users to review past rolls easily within the application.
- User Benefit: Quick reference to previous outcomes without needing to remember or write them down.

#### Configuration File (config.ini):

- Introduce an external configuration file (config.ini) to allow users to customize application behavior.
- Planned Configuration Options:
	1. DefaultDiceType: Set the dice type that is selected by default when the application starts (e.g., D20).
	2. SpeechVerbosityLevel: Control how much detail the TTS announces (e.g., "Rolled 15" vs. "You rolled a 15 on a D20").
	3. HistorySize: Define the maximum number of rolls to keep in the session history log.

- User Benefit: Personalize the application to their preferences and common usage patterns.

#### Configurable Voice Options (TTS):

- Allow users to select from available system TTS voices.
- Potentially offer options to adjust speech rate and volume via the config.ini or a settings UI.
- User Benefit: Improved user experience by choosing a preferred voice and speech style.

### V3: Advanced Functionality 

####Advanced Roll Formulas:

- Implement a parser for more complex roll expressions (e.g., "2d6+3", "4d8-2", "d20 advantage/disadvantage" where it rolls twice and takes higher/lower).
- Update UI to accept formula input instead of just selecting a single dice type.
- User Benefit: Greatly expands the utility for various tabletop games and scenarios requiring complex dice mechanics.

#### Export Roll History to File:

- Add functionality to save the current session's roll history to an external file (e.g., .txt or .csv).
- Option could be in a "File" menu or a dedicated button.
- User Benefit: Allows for persistent record-keeping of rolls, useful for game logging or analysis.

### V4: Polish & Distribution 
#### Localization Support (i18n):

- Adapt the application's UI text to support multiple languages.
- Investigate if TTS output can be localized based on system settings or user choice (depends on pyttsx3 capabilities with installed voices).
- User Benefit: Makes the application accessible to a wider global audience.

#### Packaging as Standalone Executable:

- Use tools like PyInstaller or cx_Freeze to package the Python application into a standalone .exe file for Windows.
- This would eliminate the need for users to install Python or any dependencies separately.
- User Benefit: Simplifies distribution and installation for end-users on Windows.

### Configuration Notes (for future config.ini)
The config.ini file will be structured to allow easy modification of settings. An example structure will be provided when the feature is implemented. Key planned settings include:

1. DefaultDiceType
2. SpeechVerbosityLevel (e.g., 0=minimal, 1=standard, 2=detailed)
3. HistorySize (e.g., 20, 50, 100)

## General Notes

- This roadmap is a living document and may be subject to change based on development progress and user feedback.

- Accessibility will continue to be a consideration for all new features.