# 🐍 Snake Game

A classic **Snake Game** built using **Python Turtle** and **Object-Oriented Programming (OOP)**.

The player controls the snake using the keyboard, eats food to increase the score and grow the snake, and must avoid hitting the walls or its own tail.

---

## 📌 Project Overview

This project is a Python implementation of the classic Snake Game.

The project was developed to practice:

* Python programming
* Object-Oriented Programming (OOP)
* Classes and objects
* Turtle graphics
* Keyboard event handling
* Loops and conditional statements
* Collision detection
* Game logic
* Modular programming

---

## 🎮 Game Features

* 🐍 Snake movement
* ⌨️ Keyboard controls
* 🍎 Random food generation
* 📈 Score tracking
* 🐍 Snake growth after eating food
* 🧱 Wall collision detection
* 💥 Tail/self-collision detection
* 🏆 Game Over message
* 🎯 Object-Oriented design

---

## 🕹️ Controls

| Key            | Action     |
| -------------- | ---------- |
| ⬆️ Up Arrow    | Move Up    |
| ⬇️ Down Arrow  | Move Down  |
| ⬅️ Left Arrow  | Move Left  |
| ➡️ Right Arrow | Move Right |

The snake cannot immediately move in the opposite direction.

For example, if the snake is moving right, pressing the left arrow will not immediately turn it around.

---

## 🛠️ Technologies Used

* **Python**
* **Turtle Graphics**
* **Object-Oriented Programming**
* **PyCharm / VS Code**
* **Git & GitHub**

---

## 📂 Project Structure

```text
Snake-Game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
└── README.md
```

### `main.py`

The main file of the game.

It is responsible for:

* Creating the game screen
* Creating the Snake, Food, and Scoreboard objects
* Setting keyboard controls
* Running the main game loop
* Checking collisions
* Updating the game

---

### `snake.py`

Contains the `Snake` class.

The class is responsible for:

* Creating the snake
* Creating the initial snake segments
* Moving the snake
* Controlling the snake's direction
* Adding new segments when the snake eats food

The snake is made up of multiple Turtle objects stored inside a list.

---

### `food.py`

Contains the `Food` class.

The Food class:

* Creates the food object
* Gives it a circular shape
* Gives it a red color
* Places it at a random position
* Refreshes its position after being eaten

---

### `scoreboard.py`

Contains the `Scoreboard` class.

The Scoreboard class is responsible for:

* Displaying the current score
* Increasing the score
* Updating the score display
* Displaying the `GAME OVER` message

---

# 🧠 How the Game Works

## 1. Creating the Snake

When the game starts, the `Snake` class creates the initial snake.

The snake starts with three segments.

The segments are stored in a list:

```python
self.segments = []
```

Each segment is a Turtle object.

---

## 2. Snake Movement

The snake moves continuously through the `move()` method.

The body segments follow the segment in front of them.

The movement can be visualized as:

```text
Tail → Body → Head
```

More specifically:

```text
Tail follows Body
Body follows Head
Head moves forward
```

The segments are moved from the last segment toward the first segment.

This is important because each segment needs to move to the **previous position of the segment in front of it**.

---

## 3. Keyboard Controls

The game uses Turtle's keyboard event handling.

The arrow keys control the snake:

```text
Up Arrow    → Up
Down Arrow  → Down
Left Arrow  → Left
Right Arrow → Right
```

Turtle headings are:

```text
0°   → Right
90°  → Up
180° → Left
270° → Down
```

---

## 4. Food

The food is created using the `Food` class.

The food appears at a random position on the screen.

Example:

```python
random_x = random.randint(-280, 280)
random_y = random.randint(-280, 280)
```

This allows the food to appear in different locations each time.

---

## 5. Eating Food

The game checks the distance between the snake's head and the food.

When the snake gets close enough to the food:

1. The score increases.
2. The snake grows.
3. The food moves to a new random location.

This creates the main gameplay loop.

```text
Snake finds food
       ↓
Snake eats food
       ↓
Score increases
       ↓
Snake grows
       ↓
Food appears somewhere else
```

---

## 6. Snake Growth

When the snake eats food, a new segment is added to the snake.

This makes the snake longer as the player continues playing.

For example:

```text
Start:

🐍 🟩 🟩

After eating food:

🐍 🟩 🟩 🟩

After eating again:

🐍 🟩 🟩 🟩 🟩
```

---

# 💥 Collision Detection

Collision detection is one of the most important parts of the game.

There are two main collisions that can end the game.

## 1. Wall Collision

The game checks whether the snake's head reaches the boundary of the game screen.

If the snake goes outside the playable area:

```text
GAME OVER
```

is displayed.

---

## 2. Tail Collision

The game also checks whether the snake's head touches any part of its own body.

The logic checks the distance between the head and each body segment.

Conceptually:

```python
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        # Game Over
```

`snake.segments[1:]` skips the head and checks only the body segments.

If the head gets too close to one of them, the game ends.

---

# 📊 Score System

The `Scoreboard` class keeps track of the player's score.

The score starts at:

```text
Score: 0
```

Every time the snake eats food:

```text
Score: 1
Score: 2
Score: 3
...
```

The scoreboard is updated after every successful food collision.

---

# 🔄 Main Game Loop

The game continuously runs inside a loop.

The basic flow is:

```text
Start Game
    ↓
Move Snake
    ↓
Check Food Collision
    ↓
Check Wall Collision
    ↓
Check Tail Collision
    ↓
Update Screen
    ↓
Repeat
```

The loop continues until the snake collides with a wall or its own tail.

---

# 🧩 Object-Oriented Programming

This project uses OOP to divide the game into separate classes.

### Main Classes

```text
Snake
Food
Scoreboard
```

Each class has its own responsibility.

### Snake Class

Responsible for:

```text
Snake creation
Snake movement
Snake direction
Snake growth
```

### Food Class

Responsible for:

```text
Food creation
Random food positioning
Food refreshing
```

### Scoreboard Class

Responsible for:

```text
Score
Score updates
Game Over message
```

This makes the code easier to understand, maintain, and extend.

---

# 🏗️ Class Relationship

The overall structure can be understood as:

```text
                Snake Game
                    │
        ┌───────────┼───────────┐
        │           │           │
      Snake        Food      Scoreboard
        │           │           │
     Movement    Random      Score
     Controls    Position    Game Over
     Growth
```

---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/MohammadMahroof/Snake-Game.git
```

## 2. Open the Project

Open the project folder in VS Code, PyCharm, or another Python IDE.

## 3. Run the Program

Run:

```bash
python main.py
```

The Snake Game window will open.

---

# 📋 Requirements

The project uses Python's built-in `turtle` module.

No external packages are required.

Make sure Python is installed on your computer.

You can check your Python version using:

```bash
python --version
```

---

# 📚 Python Concepts Practiced

This project helped practice several important Python concepts:

* Variables
* Lists
* Functions
* Classes
* Objects
* Constructors
* Methods
* Inheritance
* Loops
* Conditional statements
* `for` loops
* `while` loops
* Slicing
* Random numbers
* Event listeners
* Turtle graphics
* Collision detection
* Modular programming
* Object-Oriented Programming

---

# 🚀 Future Improvements

Possible improvements for future versions:

* 🏆 High-score system
* 💾 Save high score to a file
* 🔄 Restart game option
* ⏩ Increase snake speed over time
* 🎨 Improve game design
* 🔊 Add sound effects
* ❤️ Add multiple lives
* 🎯 Add different types of food
* 🧱 Add obstacles
* 🌟 Add different difficulty levels

---

# 🎯 Learning Goal

The main goal of this project was to strengthen Python programming and Object-Oriented Programming skills by building a complete game from scratch.

It also helped practice breaking a larger program into smaller, reusable classes and modules.

---

# 👨‍💻 Author

**Mohammad Mahroof**

Python Developer | Software Developer

---

# ⭐ Project Status

**Completed**

This project was created as part of my Python learning journey and portfolio development.

If you found this project useful, feel free to ⭐ star the repository.
