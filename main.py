"""The HitWicket chess-like game."""

import itertools

from typing import Literal, Tuple, Union

from exceptions import InvalidGameInputFormat

Grid = list[list[str]]
Players = Literal['A', 'B']
Movements = Literal['L', 'R', 'F', 'B']


class Game:
    GRID_SIZE = 5
    NOTHING_BLOCK = '-'

    def __init__(self) -> None:
        """The game class handles the game instance."""
        # TODO: Change to input.
        # -----------------------------------
        # Test Cases
        # -----------------------------------
        # Player 1 -> P3, P2, P5, P4, P1
        # Player 2 -> P2, P1, P3, P5, P4

        # self.get_characters(player=1)
        self.__p1_characters = ['H1', 'P2', 'P5', 'P4', 'P1']
        # self.get_characters(player=2)
        self.__p2_characters = ['P2', 'P1', 'P3', 'H2', 'P4']

        self.__grid = self.create_grid()

        self.place_characters(
            player='A', characters=self.__p1_characters
        )
        self.place_characters(
            player='B', characters=self.__p2_characters
        )

        self.p1_score = 0
        self.p2_score = 0

        self.run()

    def run(self) -> None:
        """Run the game."""
        self.__player_turn: Players = 'A'

        self.display()
        try:
            while True:
                self.turn()
        except KeyboardInterrupt:
            print('Game Interrupted')

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

        return [
            [Game.NOTHING_BLOCK] * Game.GRID_SIZE
            for _ in range(Game.GRID_SIZE)
        ]

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

    def get_player_character_name_from(self, character: str) -> str:
        """Get the full player's character name from local character name."""
        return f'{self.__player_turn}-{character}'

    def velocity(self, character: str) -> Tuple[int, Literal[1, -1]]:
        """Movement for each character as velocity is handled here."""
        local_direction: Literal[1, -1] = \
            1 if self.__player_turn == 'A' else -1
        character_type = character[0]
        units = 0
        if character_type == 'P':
            units = 1
        elif character_type == 'H':
            units = 2
        return local_direction * units, local_direction

    def move(self, character: str, direction: Movements) -> Grid:
        """Move the character in a specific direction.
        Refer `Movements` type for possible values.
        """
        target = self.get_player_character_name_from(character)

        for r in range(len(self.__grid)):
            for c in range(len(self.__grid[r])):
                if self.__grid[r][c] == target:
                    velocity, local_direction = self.velocity(character)
                    if character == 'H2':
                        if direction == 'FL':
                            self.__grid[r - velocity][c + local_direction] = target
                        elif direction == 'FR':
                            self.__grid[r - velocity][c - local_direction] = target
                        elif direction == 'BL':
                            self.__grid[r + velocity][c + local_direction] = target
                        elif direction == 'BR':
                            self.__grid[r + velocity][c - local_direction] = target
                    elif character[0] in {'H', 'P'}:
                        if direction == 'L':
                            p = c
                            while p != c + velocity:
                                self.__grid[r][p] = Game.NOTHING_BLOCK
                                p += local_direction
                            self.__grid[r][c + velocity] = target
                        elif direction == 'R':
                            p = c
                            while p != c - velocity:
                                self.__grid[r][p] = Game.NOTHING_BLOCK
                                p -= local_direction
                            self.__grid[r][c - velocity] = target
                        elif direction == 'F':
                            p = r
                            while p != r - velocity:
                                self.__grid[p][c] = Game.NOTHING_BLOCK
                                p -= local_direction
                            self.__grid[r - velocity][c] = target
                        elif direction == 'B':
                            p = r
                            while p != r + velocity:
                                self.__grid[p][c] = Game.NOTHING_BLOCK
                                p += local_direction
                            self.__grid[r + velocity][c] = target
                    else:
                        raise InvalidGameInputFormat(
                            "Invalid movement. Please use L, R, F, B."
                        )
                    self.__grid[r][c] = Game.NOTHING_BLOCK
                    return self.__grid
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

        if direction not in {'L', 'R', 'F', 'B', 'FL', 'FR', 'BL', 'BR'}:
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
