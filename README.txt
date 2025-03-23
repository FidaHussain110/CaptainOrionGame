Captain Orion: Lost in the Stars - Technical Documentation
=========================================================

1. Where the Code is Hosted
---------------------------
The source code for "Captain Orion: Lost in the Stars" is hosted on GitHub at the following URL:
[Insert your GitHub repository URL here, e.g., https://github.com/yourusername/CaptainOrionGame].
The repository contains all game files, including this documentation, in a non-zipped format for public access.

2. External Services
--------------------
This project does not rely on any external services, APIs, or databases. It is a standalone Python application that runs locally or on a hosted console (e.g., PythonAnywhere) without requiring internet connectivity beyond initial deployment.

3. Languages and Technologies
-----------------------------
- **Python 3.7**: The primary programming language used for the entire game. All logic, user interaction, and game mechanics are implemented in Python.
- **Standard Libraries**: 
  - `random`: Used for randomizing outcomes (e.g., items found, stealth rolls).
  - `time`: Used to introduce delays (via `time.sleep`) for pacing and dramatic effect.
No additional frameworks, libraries, or dependencies are required beyond a standard Python installation.

4. System Requirements and Supported Applications
------------------------------------------------
- **Minimum Requirements**:
  - Python 3.7 or higher installed on the system.
  - A command-line interface (e.g., Terminal on macOS/Linux, Command Prompt or PowerShell on Windows).
  - At least 50 MB of free disk space for the game files.
- **Supported Operating Systems**:
  - Windows (7, 10, 11)
  - macOS (10.13 and later)
  - Linux (any distribution with Python 3.7+ support, e.g., Ubuntu, Fedora)
- **Supported Applications**:
  - Any Python-compatible IDE (e.g., PyCharm, VS Code) for editing or debugging.
  - PythonAnywhere (web-based console) for hosting and sharing the game online.
- **Notes**: No graphical interface is required; the game runs entirely in a text-based console.

5. Coding/Naming Conventions
----------------------------
- **Function Names**: Use snake_case (e.g., `search_wreckage`, `solve_puzzle`) for readability and consistency with Python conventions.
- **Class Names**: Use CamelCase (e.g., `Player`) as per PEP 8 guidelines.
- **Variable Names**: Descriptive and lowercase with underscores (e.g., `required_parts`, `puzzle_solved`).
- **Comments**: Brief and inline where necessary to explain logic (e.g., `# Bonus for laser`).
- **User Interface**: Print statements include emojis (e.g., 🌌, ✅, ⚔️) to enhance visual feedback and immersion.
- **File Structure**: Each game chapter is in a separate file (`chapter1.py`, `chapter2.py`, etc.) for modularity, with `main.py` as the entry point and `player.py` defining the `Player` class.

6. How to Run/Build/Deploy the Program
--------------------------------------
- **Running Locally**:
  1. Clone the repository: `git clone [your GitHub URL]`.
  2. Navigate to the project directory: `cd CaptainOrionGame`.
  3. Ensure all files (`main.py`, `chapter1.py`, etc.) are in the same directory.
  4. Run the game: `python main.py` (or `python3 main.py` on some systems).
  - The game will start in the terminal, prompting the player for input at each step.
- **Building**: No compilation is required as Python is an interpreted language. Ensure Python 3.7+ is installed.
- **Deploying on PythonAnywhere**:
  1. Create an account at [pythonanywhere.com](https://www.pythonanywhere.com).
  2. Go to the "Files" tab and upload all `.py` files (`main.py`, `chapter1.py`, etc.).
  3. Test by opening `main.py` and clicking "Run" to verify functionality.
  4. Go to the "Consoles" tab, select "Start a new console" > "Custom."
  5. Name the console (e.g., "OrionGame") and enter: `python3.7 /home/yourusername/main.py`.
  6. Share the console URL with others via the "Share with others" option.
- **Troubleshooting**: If errors occur (e.g., "ModuleNotFoundError"), ensure all files are uploaded and paths are correct.

7. Overview of the Architecture
-------------------------------
- **Modular Design**: The game is split into six Python files for clarity and maintainability:
  - `player.py`: Defines the `Player` class to manage the player’s name and inventory.
  - `chapter1.py`: Handles "Crash Landing" (searching wreckage, repairing the ship).
  - `chapter2.py`: Handles "Alien Ruins" (deciphering symbols, solving a puzzle).
  - `chapter3.py`: Handles "Creatures of the Dark" (sneaking, fighting).
  - `chapter4.py`: Handles "Final Piece" (searching old wreckage, decoding a message).
  - `chapter5.py`: Handles "Final Choice" (making the endgame decision).
  - `main.py`: Orchestrates the game flow by importing and calling functions from each chapter.
- **Game Flow**: 
  - The game progresses linearly through five chapters, with player choices affecting outcomes.
  - The `Player` class tracks inventory, which influences later decisions (e.g., using items in combat or the final choice).
  - Randomness (via `random.randint`) and delays (via `time.sleep`) add variety and pacing.
- **Key Features**:
  - Interactive text-based gameplay with user prompts at every major decision point.
  - Inventory system linking chapters (e.g., finding a "Laser" in Chapter 1 aids combat in Chapter 3).
  - Fail states (e.g., losing combat in Chapter 3 ends the game).
- **Dependencies**: Only standard Python libraries (`random`, `time`), ensuring portability.

8. How to Start the Program
---------------------------
- **Local Execution**:
  1. Ensure Python 3.7+ is installed (`python --version` to check).
  2. Download or clone the project files into a single directory.
  3. Open a terminal and navigate to the directory: `cd path/to/CaptainOrionGame`.
  4. Run: `python main.py`.
  5. Follow the on-screen prompts to make choices (e.g., "1" to search the cockpit, "yes" to decode a message).
- **Hosted Execution (PythonAnywhere)**:
  1. Upload all `.py` files to your PythonAnywhere account under `/home/yourusername/`.
  2. Open a console and run: `python3.7 /home/yourusername/main.py`.
  3. Interact with the game via the console interface.
- **Gameplay Tips**:
  - Answer prompts with numbers (e.g., "1") or text (e.g., "yes") as indicated.
  - Inventory items collected early can impact later chapters, so explore thoroughly!
- **Expected Output**: The game starts with a welcome message, progresses through chapters with narrative text and prompts, and ends with a final decision and "Game Complete" message.

Additional Notes for Developers/Admins
--------------------------------------
- **Debugging**: If the game crashes, check for missing files or typos in user input handling. Add `print()` statements to trace execution if needed.
- **Extending the Game**: Add new chapters by creating additional `.py` files and importing them into `main.py`. Extend the `Player` class with attributes like health or skills for more complexity.
- **Error Handling**: Current input validation is basic (e.g., defaults for invalid choices). Enhance with try-except blocks for robustness if desired.
- **Maintenance**: Update item lists or riddle answers in chapter files to refresh content without altering the core structure.

Last Updated: March 23, 2025
