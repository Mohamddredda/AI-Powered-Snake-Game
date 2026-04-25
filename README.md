# 🐍 AI-Powered Snake Game

## 📌 Overview
This project is a classic Snake game with an intelligent twist, developed using Python and the Pygame library. The main part of the game is the snake navigating the screen; as it eats a fruit, it grows in length, and the game ends if it hits its own body or the wall. Rather than relying on manual directional controls, the game utilizes AI logic to determine the best move for the snake, allowing it to automatically navigate toward the food while avoiding obstacles.
## ✨ Key Features
* **AI Navigation:** The `ai_move()` and `minimax()` functions evaluate the board state to find the safest and shortest route to the target.
* **Interactive Food Placement:** The game listens for mouse events, tracking where the player clicks to use it for food placement.
* **Dynamic Visuals:** The `draw_snake()` function handles graphical rendering of the snake on the screen, including its body, alternating green and dark green colors, and eyes.
* **Obstacles:** The game environment generates rectangular brown obstacles at random positions that the AI must dodge to avoid a game over.
* **Score Tracking:** The score starts from 0 and increases by one every time the snake consumes an Apple. The `message()` function handles rendering text, such as game over messages, current scores, and high scores on the screen.
* **Keyboard Controls:** The keyboard detects specific keys like 'Q' for quitting the game or 'C' to continue after a game over.

## ⚙️ System Architecture & Logic
* **Game Loop:** The `game_loop()` function orchestrates all gameplay operations, including input handling, updating positions, collision detection, and rendering updates. This logic governs how the software manages the game's state and flow.
* **Hardware Integration:** The software portion, consisting of device drivers and the game logic unit, manages functions like displaying Apple and Snake sprites, calculating scores, and detecting wall collisions. The device drivers act as a bridge connecting hardware components, such as the controller and VGA monitor, to the logic control unit.

## 🚀 How to Run
1. Ensure Python and the Pygame library are installed on your system.
2. Place the required background images (`pp.jpg` and `homepage.jpg`) in the same directory as the main script.
3. Run the Python script to launch the application.
4. Click anywhere on the welcome screen to start.
5. Click the mouse anywhere within the game boundaries to place an apple, and watch the AI calculate the path!
