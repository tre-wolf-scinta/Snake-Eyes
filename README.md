# Snake-Eyes
*Accessible dice rolling application designed specifically for visually impaired users.*


## Table of Contents
- [Overview](#overview)  
- [Features](#features)  
- [Accessibility](#accessibility)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Supported Dice Types](#supported-dice-types)  
- [Development](#development)  
- [Testing](#testing)  
- [Contributing](#contributing)  
- [Roadmap](#roadmap)  
- [License](#license)  
- [Contact](#contact)  

---

## Overview
SnakeEyes Dice Roller is a lightweight, Windows desktop application written in Python, designed to facilitate quick and easy dice rolling for tabletop gamers and other users who rely on screen readers, particularly NVDA. The app prioritizes accessibility and usability to ensure visually impaired users can independently perform dice rolls with confidence and accuracy.

---

## Features
- **Accessible UI:** Fully compatible with NVDA screen reader.
- **Multiple Dice Types:** Support for d4, d6, d8, d10, d12, and d20 
- **Custom Rolls:** Allows rolling multiple dice and modifiers.
- **Keyboard Navigation:** Complete keyboard-driven interface, no mouse needed.
- **Audio Feedback:** Clear verbal feedback of roll results.
- **History Log:** Keeps a session history of recent rolls for reference.
- **Lightweight:** Minimal resource usage and fast startup time.
- **Portable:** No complex installation required; runs as standalone Python app.

---

## Accessibility
Accessibility is central to SnakeEyes' design:
- Fully tested with NVDA on Windows 11.
- UI elements are labeled properly for screen readers.
- Keyboard focus indicators and logical tab order.
- Audio cues and speech output confirm actions and results.
- Designed with feedback from visually impaired users.

For detailed accessibility notes, see [`docs/accessibility.md`](docs/accessibility.md).

---

## Installation

### Prerequisites
- Python 3.9 or higher (64-bit recommended)
- Windows 10 or 11
- NVDA screen reader (optional but recommended)

### Steps
1. Clone the repository:
2. Navigate to the project directory:
3. Install dependencies:
pip install -r requirements.txt
4. Run the app:
python main.py
 
Usage
- Launch the app via python main.py 
- Use arrow keys and tab to navigate menus.
- Select dice type and number of dice to roll.
- Press Enter or Space to roll.
- Listen for the NVDA readout of the roll result.
- Use the history feature to review past rolls.
- Exit using standard keyboard commands (e.g., Alt+F4).
 
Configuration
Configuration options can be adjusted in config.ini (future version). Currently, the app supports:

- Default dice type
- Speech verbosity level
- History size
- Example configuration file coming soon.
 
Supported Dice Types
Dice Type
Description
d4
Four-sided die
d6
Standard six-sided
d8
Eight-sided
d10
Ten-sided
d12
Twelve-sided
d20
Twenty-sided
 
 
Development
Project Structure
Getting Started

- Fork the repo and clone your fork.

- Create a feature branch (git checkout -b feature/your-feature).

- Implement your changes with focus on accessibility and clean code.

- Write tests and update documentation as needed.

- Submit a pull request with a detailed description.
 
Testing

- Unit tests located in tests/ using unittest framework.

- Run tests with:
- python -m unittest discover tests

- Accessibility tests performed with NVDA.

- Manual UI testing recommended for each new feature.
 
Contributing
- Contributions are welcome! Please read CONTRIBUTING.md before submitting issues or pull requests.

- Follow coding standards and accessibility guidelines.

- Write descriptive commit messages.

- Respect branching and PR workflow.
 
Roadmap
Planned features:

- Configurable voice options

- Advanced roll formulas

- Export roll history to file

- Localization support

- Packaging as standalone executable (.exe)
See docs/roadmap.md for details and timelines.
 
License
This project is licensed under the MIT License.
 
Contact
For questions, issues, or feedback, please contact:
Tre Scinta  | tre.scinta90@gmail.com
GitHub: https://github.com/tre-wolf-scinta
 
Thank you for using SnakeEyes — making dice rolling accessible for everyone.
