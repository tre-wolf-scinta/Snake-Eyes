# Dice Roller Application Setup
This document provides instructions on how to set up and run the Dice Roller desktop application.

## 1. Prerequisites
  - Python: Version 3.6 or newer is recommended. You can download Python from python.org. Make sure to check the option "Add Python to PATH" during installation.

  - pip: Python's package installer. It usually comes with Python installations.

  - Git (Optional): If you want to clone the project repository. You can download Git from git-scm.com.

## 2. Setup Steps

### 1. Get the Project Files
  - Clone the Repository 

git clone https://github.com/tre-wolf-scinta/snake-eyes 

### 2. Create and Activate a Virtual Environment 
*Using a virtual environment is highly recommended to isolate project dependencies.*

  - **Create the virtual environment:**
  - Open your terminal/command prompt in the project directory and run:

python -m venv venv

This creates a folder named venv in your project directory.

  - **Activate the virtual environment:**

	- On Windows (Command Prompt/PowerShell):

venv\Scripts\activate

	- On Windows (Git Bash):

source venv/Scripts/activate

	- On macOS/Linux:

source venv/bin/activate

Your terminal prompt should change to indicate that the virtual environment is active (e.g., (venv) at the beginning of the prompt).

3. Install Dependencies
**Install the required Python packages using the requirements.txt file:**

pip install -r requirements.txt

This command will download and install PyQt6, pyttsx3, and pypiwin32 (on Windows).

4. Add the Dice Roll Sound Effect
  - Obtain a dice rolling sound effect. This should be a .wav file.

  - Rename this file to dice_roll.wav.

  - Place the dice_roll.wav file in the same directory as the main Python script (e.g., dice_roller_app.py).

  - If this file is not present, the application will still run, but an informational message will appear, and no sound effect will play during dice rolls.

## 3. Running the Application
**Once the setup is complete and the virtual environment is activated:**

 Navigate to the project directory in your terminal/command prompt if you aren't already there.

**Run the main Python script:**

python dice_roller_app.py

The Dice Roller application window should now appear.

## 4. Troubleshooting

**pyttsx3 issues on Windows:** If Text-to-Speech is not working, ensure pypiwin32 was installed correctly. Sometimes, a manual pip install pypiwin32 might be needed if the conditional install in requirements.txt had issues.

**"Command not found":** This usually means Python or pip is not correctly installed or not added to your system's PATH environment variable. Revisit the Python installation steps.

**Sound file not playing:** Double-check that the sound file is named exactly dice_roll.wav and is in the same directory as the Python script. Also, ensure it's a valid WAV file.