"""The HitWicket chess-like game."""

import itertools

from typing import Literal

from exceptions import InvalidGameInputFormat

Grid = list[list[str]]
Players = Literal['A', 'B']
Movements = Literal['L', 'R', 'F', 'B']


class Game:
    GRID_SIZE = 5

    def __init__(self) -> None:
        """The game class handles the game instance."""
        # TODO: Change to input.
        # -----------------------------------
        # Test Cases
        # -----------------------------------
        # Player 1 -> P3, P2, P5, P4, P1
        # Player 2 -> P2, P1, P3, P5, P4

        self.__p1_characters = ['P2', 'P1', 'P3',
                                'P5', 'P4']  # self.get_characters(player=1)
        self.__p2_characters = ['P3', 'P2', 'P5',
                                'P4', 'P1']  # self.get_characters(player=2)

        self.__grid = self.create_grid()

        self.place_characters(
            player='A', characters=self.__p1_characters
        )
        self.place_characters(
            player='B', characters=self.__p2_characters
        )

        self.__player_turn: Players = 'A'

        self.display()
        self.turn()

    def get_characters(self, player: Players) -> list[str]:
        """Get the player characters from input as list."""
        print(f'Player {player} Input :')

        return list(
            map(
                lambda x: x.strip(),
                input().strip().split(',')
            )
        )

    def create_grid(self) -> Grid:
        """Generate NxN grid. N is defined as `Game.GRID_SIZE`."""

        return [['x'] * Game.GRID_SIZE for _ in range(Game.GRID_SIZE)]

    def place_characters(self, player: Players, characters: list[str]) -> Grid:
        """Place the characters in the grid.
        player can be 1 or 2. Refer `Players` type hint.
        """

        for r, c in itertools.product(
            range(Game.GRID_SIZE), range(Game.GRID_SIZE)
        ):
            if r == Game.GRID_SIZE - 1 and player == 'A':
                self.__grid[r][c] = f'A-{characters[c]}'
            elif r == 0 and player == 'B':
                self.__grid[r][c] = f'B-{characters[c]}'
        return self.__grid

    def move(self, character: str, direction: Movements) -> Grid:
        """Move the character in a specific direction.
        Refer `Movements` type for possible values.
        """
        return self.__grid

    def display(self) -> None:
        """Display grid."""
        for r in self.__grid:
            for c_val in r:
                print(c_val, end='\t')
            print()

    def turn(self) -> Grid:
        print(f"Player {self.__player_turn}'s Move:")
        movement = input().strip()

        if movement.find(':') == -1:
            raise InvalidGameInputFormat(
                "Invalid movement format <character_name>:<move> (e.g:- P1:L, P2:R, P3:F, P3:B)"
            )

        character, direction = movement.split(':')

        if direction not in {'L', 'R', 'F', 'B'}:
            raise InvalidGameInputFormat(
                "Invalid movement format <character_name>:<move> (e.g:- P1:L, P2:R, P3:F, P3:B)"
            )

        # Move the character & display the grid.
        self.move(character, direction)
        self.display()

        # Update the chance.
        self.__player_turn = 'B' if self.__player_turn == 'A' else 'A'

        return self.__grid


if __name__ == '__main__':
    g = Game()
