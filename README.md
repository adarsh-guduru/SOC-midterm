# SoC Race and Learn – Midterm Report

This repository documents my 4-week journey through various topics in programming and AI, as part of the SoC Race and Learn program. The focus areas include Python, Pygame, Neural Networks, CNNs, Reinforcement Learning, and Q-Learning.

------------------------------------------------------------
Weekly Overview
------------------------------------------------------------

Week 1 – Python, OOP, and Pygame

Python & OOP:
- Python is an interpreted, high-level, dynamically typed programming language.
- Object-Oriented Programming (OOP) involves:
  - Class & Object – blueprint and instance.
  - Encapsulation – keeping attributes private.
  - Inheritance – one class deriving from another.
  - Polymorphism – same interface, different behaviors.

Example:
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()  # Output: Bark

Pygame Basics:
- pygame.init() initializes the library.
- Used to build 2D games.
- Concepts learned:
  - Main game loop (event handling, update, draw).
  - pygame.display, pygame.Rect, blit, and collision detection.
- Built a Snake Game clone.

------------------------------------------------------------

Week 2 – Neural Networks, CNNs, and PyTorch

Neural Networks:
- Composed of layers of artificial neurons.
- Key parts:
  - Input → Hidden Layers → Output
  - Activation functions: ReLU, Tanh, Sigmoid
  - Loss function: measures prediction error
  - Backpropagation: updates weights using gradient descent

CNNs:
- Used for image-related tasks.
- Layers:
  - Convolution Layer – applies filters to images.
  - Pooling Layer – reduces dimensionality.
  - Fully Connected Layer – final classification.

PyTorch:
- A deep learning framework.
- Learned about:
  - Tensors and operations
  - Defining models using torch.nn.Module
  - Optimizers and loss functions
  - Training loops (forward → loss → backward → step)
- Implemented a basic image classifier on CIFAR-10 dataset.

------------------------------------------------------------

Week 3 – Reinforcement Learning (RL)

Fundamentals:
- RL involves an agent learning from interaction with an environment.
- Key elements:
  - State – current environment condition
  - Action – what agent can do
  - Reward – feedback signal
  - Policy – mapping from states to actions
  - Value Function – expected return from a state/action

Learning Paradigm:
- Agent observes → acts → receives reward → updates knowledge.
- Goal is to maximize cumulative reward.
- Explored Markov Decision Process (MDP) formulation.

------------------------------------------------------------

Week 4 – Q-Learning and Deep Q Networks (DQN)

Q-Learning:
- A model-free RL algorithm.
- Learns a Q-table of state-action values.
- Update rule:
  Q(s, a) = Q(s, a) + α [r + γ * max(Q(s’, a’)) - Q(s, a)]
  where:
    α = learning rate
    γ = discount factor
    r = reward
    s’ = next state

Deep Q-Networks (DQN):
- Replaces Q-table with a neural network.
- Used in complex problems like games (e.g., Atari).
- Key techniques:
  - Experience Replay – samples past experiences randomly.
  - Target Networks – stabilize learning.
  - Epsilon-greedy policy – balances exploration vs exploitation.

Observations:
- DQNs are powerful but require careful tuning.
- Great for solving visual-based control problems.

------------------------------------------------------------

Summary:

| Week | Topic                        | Key Concepts Covered                                       |
|------|------------------------------|-------------------------------------------------------------|
| 1    | Python & Pygame              | OOP, Classes, Snake Game, Event Loops                      |
| 2    | Neural Nets & CNNs           | Layers, Activations, Backprop, PyTorch Basics              |
| 3    | Reinforcement Learning       | MDP, Policy, Value, David Silver Lectures                  |
| 4    | Q-Learning & Deep Q Learning | Q-tables, DQN, Experience Replay, Target Net, Exploration |

------------------------------------------------------------

Assignments:

- Week 1 and Week 2 assignments were practical exercises.
- Week 3 involved note-making for concepts.
- Week 4 focused on reading-based understanding of DQNs.

------------------------------------------------------------

This repository serves as a progress log and concept reference from the SoC Race and Learn midterm sprint.
