# Mayhem-Clone


## Overview
Mayhem is a two-player space-themed arcade game developed using Python and Pygame. Each player controls a spaceship, navigating around a central obstacle and battling against each other by shooting bullets. The objective is to avoid crashing into the obstacle and manage to outmaneuver the opponent. 

## Game Features
- **Two player controls:** Each spaceship can rotate left, rotate right, thrust forward, and shoot bullets.
- **Physics mechanics:** Spaceships maintain inertia after moving in a direction and a mild gravity pulls them downward.
- **Obstacle interaction:** A central obstacle affects navigation and strategy.
- **Simple collision detection:** Spaceships disappear upon collision with the obstacle, and bullets are destroyed upon contact with any game element.

## Installation
To run Mayhem, you need Python and Pygame installed on your system. Follow these steps to set up:

1. **Install Python:**
   Ensure that Python is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame:**
   Pygame is required to run this game. Install it via pip with the following command: pip install pygame
   
## How to Play

### Starting the Game:
Run the game script from your terminal or command prompt:

### Game Controls:
- **Player 1 Controls:**
  - **W:** Thrust forward
  - **A:** Rotate left
  - **D:** Rotate right
  - **Space:** Fire

- **Player 2 Controls:**
  - **Up Arrow (↑):** Thrust forward
  - **Left Arrow (←):** Rotate left
  - **Right Arrow (→):** Rotate right
  - **Enter/Return (To be implemented):** Fire

### Objective:
Avoid the obstacle and opponent bullets while trying to shoot down the opponent. Each hit on the opponent or crash into the obstacle can end the game or reduce health, depending on how the collision logic is implemented.



