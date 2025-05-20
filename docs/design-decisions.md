# Design Decisions for Dice Roller Application

This document outlines the key design decisions made during the development of the Dice Roller application and the reasoning behind them.

## 1. Choice of GUI Framework: PyQt6
**Decision:** Use PyQt6 for the Graphical User Interface.

**Reasoning:**

  - **Accessibility:** Qt (and by extension PyQt6) has strong built-in support for accessibility features, which is a core requirement for this project (screen reader compatibility). Standard Qt widgets are generally accessible by default.

  - **Cross-Platform Potential:** While the immediate target is Windows, PyQt6 is a cross-platform toolkit, offering flexibility if the application were to be ported to macOS or Linux in the future.

  - **Mature and Feature-Rich:** PyQt6 is a comprehensive library with a wide range of widgets and tools for building desktop applications.

  - **Python Bindings:** Provides idiomatic Python bindings to the powerful Qt framework.

## 2. Choice of Text-to-Speech (TTS) Engine: pyttsx3
**Decision:** Use the pyttsx3 library for Text-to-Speech functionality.

**Reasoning:**

  - **Cross-Platform:** pyttsx3 works offline and supports multiple TTS engines available on different operating systems (SAPI5 on Windows, NSSpeechSynthesizer on macOS, espeak on Linux). This aligns with potential future cross-platform compatibility.

  - **Simplicity:** It offers a relatively straightforward API for basic TTS tasks like saying text and adjusting properties like rate or voice (though advanced voice selection wasn't a primary focus here).

  - ** Fewer External Dependencies:** It aims to work without requiring external services, which is suitable for a lightweight desktop app. (Note: On Windows, it might rely on pypiwin32 for SAPI5 interaction).

  - **Sufficient for Requirements:** For simply announcing the dice roll result, pyttsx3 is adequate.

## 3. Sound Effect Playback: winsound Module
**Decision:** Use the built-in Python winsound module for playing the dice roll sound effect.

**Reasoning:**

  - **Windows Specific & Lightweight:** winsound is part of the standard library, meaning no extra installation is needed for this core functionality on the target OS.

  - **Simplicity for WAV:** It's very simple to use for playing .wav files, which is sufficient for a basic sound effect.

  - **Asynchronous Playback:** winsound.SND_ASYNC allows the sound to play without blocking the GUI, ensuring the application remains responsive.

  - **No External Libraries Needed:** Avoids adding another dependency just for a simple sound effect on the primary target platform.

## 4. Accessibility as a Core Tenet
**Decision:** Prioritize accessibility features throughout the design.

**Reasoning:**

  - **Best Practices:** Implementing accessibility for all users is a best practice of all modern application development.

**Implementation Details:**

  - Using standard, accessible PyQt6 widgets.

  - Setting accessible names and tooltips for interactive elements (QComboBox, QPushButton, QLabel for results).

  - Ensuring keyboard navigability (inherent in Qt).

  - Providing TTS output as the primary means of conveying the dice roll result for visually impaired users.

  - Using QLabel.setBuddy() to associate descriptive labels with their respective controls.

## 5. User Experience (UX) Considerations
**Decision:** Simple, clear interface with immediate feedback.

**Reasoning:**

  - **Ease of Use:** The application should be intuitive, with a clear path to selecting dice type and rolling.

  - **Feedback:**

    - **Visual:** The result is displayed in a QLabel.

    - **Auditory:** A dice roll sound provides immediate non-verbal feedback that an action occurred.

    - **Auditory (TTS):** The result is spoken, reinforcing the outcome and catering to accessibility.

    - **Error/Info Messages:** Non-critical issues (like a missing sound file or TTS initialization failure) are communicated via QMessageBox dialogs without halting the application's core functionality where possible.

## 6. Dice Types
**Decision:** Include a predefined list of common polyhedral dice (D4, D6, D8, D10, D12, D20, D100).

**Reasoning:** These are standard dice types used in many tabletop role-playing games and other games, covering a wide range of common use cases. The QComboBox provides an easy way for users to select from this list.

## 7. Modularity and Structure
**Decision:** Encapsulate the application logic within a single class (DiceRollerApp).

**Reasoning:** For an application of this relatively small scope, a single class is sufficient to manage the UI, event handling, and core logic. This keeps the structure simple and easy to understand. If the application were to grow significantly, refactoring into multiple modules/classes would be considered.

## 8. External Assets Management
**Decision:** Require the dice_roll.wav sound file to be in the same directory as the script.

**Reasoning:**

  - **Simplicity:** This is the easiest approach for a small, standalone application, avoiding complex path management or packaging for a single asset.

  - **User Notification:** The application checks for the file at startup and informs the user if it's missing, guiding them to provide it.