# 🐍 Snake Game

A classic **Snake Game** built using **Python Turtle** and **Object-Oriented Programming (OOP)**.

The player controls the snake using the keyboard, eats food to increase the score and grow the snake, and tries to achieve the highest possible score while avoiding collisions with the walls and its own tail.

The game automatically **resets after a collision**, while the highest score is preserved for the next round and between program sessions.

---

## 📌 Project Overview

This project is a Python implementation of the classic Snake Game.

It was developed as part of my **Python learning journey** to practice programming concepts by building a complete, interactive game using multiple Python modules and OOP principles.

The project focuses on:

* Python programming
* Object-Oriented Programming (OOP)
* Classes and objects
* Turtle graphics
* Keyboard event handling
* Lists and loops
* File handling
* Collision detection
* Game logic
* Modular programming
* Persistent data storage

---

## 🎮 Game Features

* 🐍 Snake movement
* ⌨️ Keyboard controls
* 🍎 Random food generation
* 📈 Score tracking
* 🐍 Snake growth after eating food
* 🧱 Wall collision detection
* 💥 Tail/self-collision detection
* 🔄 Automatic game reset after collision
* 🏆 High-score tracking
* 💾 Persistent high-score storage using a file
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

For example, if the snake is moving right, pressing the left arrow will not immediately turn the snake around.

---

## 🛠️ Technologies Used

* **Python**
* **Turtle Graphics**
* **Object-Oriented Programming**
* **File Handling**
* **VS Code / PyCharm**
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
├── data.txt
├── .gitignore
└── README.md
```

> **Note:** `data.txt` stores the local high score and is ignored by Git using `.gitignore`.

---

## 📄 File Responsibilities

### `main.py`

The main file of the game.

It is responsible for:

* Creating the game screen
* Creating the Snake, Food, and Scoreboard objects
* Setting keyboard controls
* Running the main game loop
* Detecting food collisions
* Detecting wall collisions
* Detecting tail collisions
* Resetting the game after a collision
* Updating the screen

---

### `snake.py`

Contains the `Snake` class.

The class is responsible for:

* Creating the snake
* Creating the initial snake segments
* Moving the snake
* Controlling the snake's direction
* Extending the snake after eating food
* Resetting the snake after a collision

The snake segments are stored in a list.

---

### `food.py`

Contains the `Food` class.

The Food class is responsible for:

* Creating the food object
* Giving the food a circular shape
* Giving the food a red color
* Placing the food at a random position
* Refreshing its position after being eaten

---

### `scoreboard.py`

Contains the `Scoreboard` class.

The Scoreboard class is responsible for:

* Displaying the current score
* Tracking the high score
* Updating the score display
* Resetting the current score
* Saving a new high score
* Loading the previous high score from a file

---

### `data.txt`

Stores the player's **high score**.

The file allows the high score to remain available even after the program is closed and run again.

For example:

```text
15
```

When the program starts, the value is read from `data.txt` and displayed as the current high score.

> `data.txt` is a local file and is ignored by Git because the value changes during gameplay.

---

### `.gitignore`

The `.gitignore` file prevents local/generated files from being tracked by Git.

For example:

```gitignore
data.txt
__pycache__/
*.pyc
```

This prevents the local high-score data and Python cache files from appearing as changes in the Git repository.

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

The basic movement concept is:

```text
Tail follows Body
Body follows Head
Head moves forward
```

The segments are moved from the last segment toward the first segment.

This allows each segment to take the previous position of the segment in front of it.

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

The direction methods also prevent the snake from immediately reversing direction.

For example:

```text
Moving Right → Cannot immediately move Left
Moving Up    → Cannot immediately move Down
```

---

## 4. Food

The food is created using the `Food` class.

The food appears at a random position on the screen.

The random coordinates are generated within the playable area:

```python
random_x = random.randint(-280, 280)
random_y = random.randint(-280, 280)
```

Every time the snake eats the food, the food is moved to a new random location.

---

## 5. Eating Food

The game checks the distance between the snake's head and the food.

When the snake gets close enough to the food:

1. The food moves to a new position.
2. The snake grows.
3. The score increases.
4. The scoreboard is updated.

The gameplay flow is:

```text
Snake finds food
       ↓
Snake eats food
       ↓
Food moves
       ↓
Snake grows
       ↓
Score increases
       ↓
Continue playing
```

---

## 6. Snake Growth

When the snake eats food, a new segment is added to the end of the snake.

For example:

```text
Start:

🐍 🟩 🟩

After eating:

🐍 🟩 🟩 🟩

After eating again:

🐍 🟩 🟩 🟩 🟩
```

The longer the snake becomes, the more difficult it is to avoid hitting its own body.

---

# 💥 Collision Detection

Collision detection is an important part of the game.

The game checks for two main types of collisions:

1. Wall collision
2. Tail/self-collision

Unlike the original version of the game, a collision **does not permanently end the program**.

Instead, the game automatically resets and allows the player to start another round.

---

## 1. Wall Collision

The game checks whether the snake's head reaches the boundary of the game screen.

The playable area is approximately:

```text
x: -280 to 280
y: -280 to 280
```

If the snake reaches outside this area:

```text
Collision
   ↓
Reset snake
   ↓
Reset current score
   ↓
Keep high score
   ↓
Start a new round
```

---

## 2. Tail Collision

The game checks whether the snake's head touches any part of its own body.

The collision check uses:

```python
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
        ...
```

`snake.segments[1:]` skips the head and checks only the remaining body segments.

If the head gets too close to one of the body segments, the round is reset.

---

# 🔄 Game Reset System

One of the recent improvements to the project is the **automatic game reset system**.

Previously, a collision would result in a game-over state.

Now, when the snake collides with a wall or its own tail:

```text
Collision detected
       ↓
Check current score
       ↓
Update high score if necessary
       ↓
Reset current score
       ↓
Reset snake
       ↓
Start a new round
```

This allows the player to continue playing without restarting the Python program.

---

# 🏆 High Score System

The game now maintains two values:

```text
Score
High Score
```

For example:

```text
Score: 5  High Score: 12
```

The **Score** represents the player's score in the current round.

The **High Score** represents the highest score achieved across rounds.

---

## High Score Logic

When a collision occurs, the game checks:

```text
Current Score > High Score?
```

If the current score is higher:

```text
Current Score
      ↓
New High Score
      ↓
Save High Score
      ↓
Reset Current Score
```

If the current score is not higher, only the current score is reset.

The high score remains unchanged.

---

# 💾 Persistent High Score

The high score is stored in `data.txt`.

This means the high score is not lost when the program is closed.

The process works like this:

```text
Program starts
      ↓
Read high score from data.txt
      ↓
Display high score
      ↓
Play game
      ↓
Achieve new high score
      ↓
Save new high score to data.txt
      ↓
Close program
      ↓
Run program again
      ↓
Read saved high score
```

For example:

```text
First session:

High Score: 0
     ↓
Player scores 10
     ↓
High Score: 10
```

After closing and running the program again:

```text
Score: 0  High Score: 10
```

The high score remains available.

---

# 📊 Score System

The `Scoreboard` class manages both the current score and the high score.

When food is eaten:

```text
Score increases by 1
```

Example:

```text
Score: 1
Score: 2
Score: 3
Score: 4
...
```

When a collision occurs:

```text
Current score → 0
High score    → preserved
```

The scoreboard is updated after every score change and reset.

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
Reset if Collision Occurs
    ↓
Update Screen
    ↓
Repeat
```

The loop continues running even after a collision.

Instead of ending the program, the snake and current score are reset and a new round begins.

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
Snake reset
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
Current score
High score
Score updates
High-score persistence
Score reset
```

This separation makes the code easier to understand, maintain, and extend.

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
       Movement      Random      Score
       Controls      Position    High Score
       Growth        Refresh     Reset
       Reset                     File Storage
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

No external Python packages are required.

Make sure Python is installed on your computer.

Check your Python version using:

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
* List slicing
* Random numbers
* Event listeners
* Turtle graphics
* Collision detection
* File handling
* Reading and writing files
* Persistent data storage
* Modular programming
* Object-Oriented Programming

---

# 🚀 Future Improvements

Possible improvements for future versions:

* 🎨 Improve game interface
* ⏩ Increase snake speed as the score increases
* 🔊 Add sound effects
* 🎯 Add different types of food
* 🧱 Add obstacles
* 🌟 Add difficulty levels
* ❤️ Add multiple lives
* 🏅 Add more game statistics
* 🕹️ Add pause/resume functionality
* 🖥️ Improve the overall game UI

---

# 🎯 Learning Goal

The main goal of this project was to strengthen my **Python programming and Object-Oriented Programming skills** by building a complete game from scratch.

Through this project, I practiced:

* Designing classes
* Separating program functionality into modules
* Handling user input
* Working with Turtle graphics
* Implementing game loops
* Detecting collisions
* Managing game state
* Working with files
* Persisting data between program sessions

This project is part of my ongoing **Python learning journey** and portfolio development.

---

# 📈 Project Status

**Completed — Part of my Python Learning Journey**

The core Snake Game is complete, including:

* Snake movement
* Keyboard controls
* Food generation
* Snake growth
* Score tracking
* Wall collision
* Tail collision
* Automatic game reset
* High-score tracking
* Persistent high-score storage

Future improvements may be added as I continue learning Python and game development.

---

# 👨‍💻 Author

**Mohammad Mahroof**

Python Developer | Software Developer

---

⭐ If you found this project interesting, feel free to star the repository.
