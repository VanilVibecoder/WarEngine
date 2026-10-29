# War Engine — Tactical Card Game

**War Engine** is a turn-based tactical card game built with Python for two players.

The project is a custom variation of the classic War card game, featuring different unit types, attack statistics, special combat rules, and an initiative system.

It is being developed as a personal Python project to practice object-oriented programming, software architecture, game logic, and independent problem-solving.

## Features

The current MVP includes:

- Generation and shuffling of a 52-card deck.
- Five unique card types with different attack values.
- Initial distribution of 8 cards to each player.
- Local two-player Hotseat mode.
- Hidden card selection using terminal screen clearing.
- Random selection of the first attacking player.
- Combat resolution based on attack values and special rules.
- Garrison system for collecting captured cards and victory points.
- Neutral discard pile for tied battles.
- Automatic card supply at the beginning of each round.
- Initiative rotation between players.
- Complete game loop with automatic game-over detection.

## Card Types

| Card Type | Quantity | Attack (ATK) |
|---|---:|---:|
| Soldier | 26 | 10 |
| Officer | 14 | 20 |
| Assassin | 6 | 5 |
| King | 4 | 35 |
| Joker | 2 | 50 |
| **Total** | **52** | |

### Special Combat Rule

The **Assassin** automatically defeats the King and Joker, regardless of their attack values.

All other battles are resolved by comparing ATK values.

## How to Play

1. Each player receives 8 random cards.
2. At the beginning of each round, players draw cards from the central deck while cards remain available.
3. The attacking player selects a card first, followed by the defending player.
4. Both cards are revealed and compared.
5. The winner collects both cards in their Garrison.
6. If both cards have equal ATK, they are moved to the neutral discard pile.
7. The round winner becomes the next attacking player. In a tie, the initiative switches.
8. The game ends when the central deck and both players' hands are empty.

### Victory Conditions

In the current MVP, each card in a player's Garrison is worth **1 victory point**.

The player with the most victory points at the end of the game wins.

## Tech Stack

- **Python 3.13+** — core programming language
- **Object-Oriented Programming (OOP)** — game components and state management
- **Python Standard Library** — randomization and console interactions
- **uv** — Python environment and project management
- **Git & GitHub** — version control

## Installation and Usage

### Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

### Run the Game

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/WarEngine.git
cd WarEngine
```

Run the application:

```bash
uv run python main.py
```

The game runs in the terminal. Two players take turns using the same keyboard.

**Recommended environment:** Windows terminal.

*Replace `YOUR_USERNAME` with your GitHub username.*

## Development Status

**Status: Playable MVP**

The core gameplay loop has been implemented, including deck generation, card distribution, combat resolution, Garrison management, initiative rotation, and game-over detection.

### Roadmap

- [x] Card and deck generation
- [x] Two-player gameplay
- [x] Combat resolution
- [x] Garrison and victory points
- [x] Initiative rotation
- [x] Hidden card selection
- [x] Complete game loop
- [ ] Unique ultimate abilities for all five card tiers
- [ ] Card recruitment from the Garrison
- [ ] Advanced victory point system
- [ ] Automated testing with pytest
- [ ] Console interface improvements
- [ ] Code refactoring and project structure improvements

## Learning Objectives

This project focuses on developing practical Python engineering skills:

- Designing classes and managing object interactions.
- Working with lists and mutable game state.
- Implementing algorithms and conditional logic.
- Handling user input and edge cases.
- Debugging and testing Python applications.
- Using Git for version control.
- Building a complete application from initial requirements to a working product.

## Future Vision

The long-term goal is to transform War Engine from a simple card game into a tactical card battler with unique abilities, strategic card recruitment, and more advanced combat mechanics.

The project is developed incrementally, with an emphasis on clean code, practical learning, and independent software development.