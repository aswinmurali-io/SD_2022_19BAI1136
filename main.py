"""The HitWicket chess-like game."""

import itertools

from typing import Literal

Grid = list[list[str]]
Players = Literal[1, 2]


class InvalidGameInputFormat(Exception):
    pass


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

        self.__p1_characters = ['B-P2', 'B-P1', 'B-P3',
                                'B-P5', 'B-P4']  # self.get_characters(player=1)
        self.__p2_characters = ['A-P3', 'A-P2', 'A-P5',
                                'A-P4', 'A-P1']  # self.get_characters(player=2)

        self.__grid = self.create_grid()

        self.place_characters(
            player=1, characters=self.__p1_characters
        )
        self.place_characters(
            player=2, characters=self.__p2_characters
        )

        self.__player_turn: Players = 1

        print(self.__grid)

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
            if r == Game.GRID_SIZE - 1 and player == 1:
                self.__grid[r][c] = f'A-{characters[c]}'
            elif r == 0 and player == 2:
                self.__grid[r][c] = f'B-{characters[c]}'
        return self.__grid

    def turn(self, ) -> Grid:
        print(f"Player {self.__player_turn}'s Move:")

        return self.__grid


if __name__ == '__main__':
    g = Game()
