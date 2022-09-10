# Grid Game

Submitted by **Aswin Murali, 19BAI1136**.

## Setup

To game uses `python` to execute logic. Type the below command to run the game.

```bash
python main.py
```

## Gameplay

### Basic handling input

```md
Player A Input :
P3, P2, P5, H1, P1
Player B Input :
P2, P1, P3, P5, H2
B-P2    B-P1    B-P3    B-P5    B-H2
-       -       -       -       -
-       -       -       -       -
-       -       -       -       -
A-P3    A-P2    A-P5    A-H1    A-P1
Player A's Move:
H1:F
B-P2    B-P1    B-P3    B-P5    B-H2
-       -       -       -       -
-       -       -       A-H1    -
-       -       -       -       -
A-P3    A-P2    A-P5    -       A-P1
Player B's Move:
P2:F
-       B-P1    B-P3    B-P5    B-H2
B-P2    -       -       -       -
-       -       -       A-H1    -
-       -       -       -       -
A-P3    A-P2    A-P5    -       A-P1
Player A's Move:
H1:F
-       B-P1    B-P3    A-H1    B-H2
B-P2    -       -       -       -
-       -       -       -       -
-       -       -       -       -
A-P3    A-P2    A-P5    -       A-P1
```

### Pawns + Hero1 in action, Hero1 killing Pawn (with mock characters as input for both A and B)

```md
B-P2    B-P1    B-P3    B-P5    B-P4
-       -       -       -       -
-       -       -       -       -
-       -       -       -       -
A-H1    A-P2    A-P5    A-P4    A-P1
Player A's Move:
H1:F
B-P2    B-P1    B-P3    B-P5    B-P4
-       -       -       -       -
A-H1    -       -       -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player B's Move:
P2:F
-       B-P1    B-P3    B-P5    B-P4
B-P2    -       -       -       -
A-H1    -       -       -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player A's Move:
H1:F
A-H1    B-P1    B-P3    B-P5    B-P4
-       -       -       -       -
-       -       -       -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player B's Move:
P5:F
A-H1    B-P1    B-P3    -       B-P4
-       -       -       B-P5    -
-       -       -       -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player A's Move:
H1:L
-       -       A-H1    -       B-P4
-       -       -       B-P5    -
-       -       -       -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player B's Move:
Game Interrupted
```

### Using Hero2 + Hero1 killing Hero2 (with mock characters as input for both A and B)

```md
B-P2    B-P1    B-P3    B-H2    B-P4
-       -       -       -       -
-       -       -       -       -
-       -       -       -       -
A-H1    A-P2    A-P5    A-P4    A-P1
Player A's Move:
H1:F
B-P2    B-P1    B-P3    B-H2    B-P4
-       -       -       -       -
A-H1    -       -       -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player B's Move:
H2:FL
B-P2    B-P1    B-P3    -       B-P4
-       -       -       -       -
A-H1    -       B-H2    -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player A's Move:
H1:L
B-P2    B-P1    B-P3    -       B-P4
-       -       -       -       -
-       -       A-H1    -       -
-       -       -       -       -
-       A-P2    A-P5    A-P4    A-P1
Player B's Move:
Game Interrupted
```
