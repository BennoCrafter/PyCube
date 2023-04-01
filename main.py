from random import randint


class World:
    def __init__(self):
        # todo add world_settings.json
        # settings
        self.world = (15, 6)
        self.player = [3, 4]
        self.blocks = [(1, 4), (3, 6), (3, 8), (4, 5)]

        self.direction_vectors = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
        # WELCOME
        print("Welcome to PyLab!")
        print()
        print("Use [w][a][s][d] to move.")
        print("And for exit the program use [x].")
        print("The finish is to touch the [o]")
        print("I wish you much fun!")

    def paint(self):
        player_tuple = tuple(self.player)
        for y_runner in range(1, self.world[1] + 1):
            for x_runner in range(1, self.world[0] + 1):
                current = (x_runner, y_runner)
                if current == player_tuple:
                    print("x", end='')
                elif current in self.blocks:
                    print("o", end="")
                else:
                    print("-", end='')
            print()

    def valid_pos(self):
        return 1 <= self.player[0] <= self.world[0] and 1 <= self.player[1] <= self.world[1]

    def place(self, direc):
        # Get the direction vector for the given input direction
        direction_vector = self.direction_vectors.get(direc)
        if direction_vector:
            # Compute the new block position by adding the direction vector to the player position
            new_block_pos = tuple(sum(x) for x in zip(self.player, direction_vector))

            if new_block_pos not in self.blocks:
                self.blocks.append(new_block_pos)
            else:
                print("There's already a block!")

    def remove(self, direc):
        direction_vector = self.direction_vectors.get(direc)
        if direction_vector:
            # Compute the new block position by adding the direction vector to the player position
            new_block_pos = tuple(sum(x) for x in zip(self.player, direction_vector))

            if new_block_pos in self.blocks:
                self.blocks.remove(new_block_pos)
            else:
                print("There's no block!")

    def move(self, direc):
        movement_vector = world.direction_vectors.get(direc)
        if movement_vector is not None:
            new_position = [self.player[0] + movement_vector[0],
                            self.player[1] + movement_vector[1]]
            if tuple(new_position) not in self.blocks:
                self.player = new_position
            else:
                print("There's and obstacle!")


if __name__ == "__main__":
    world = World()
    while True:
        if world.valid_pos():
            world.paint()
            print()
        move = input('Next Step:')
        # INPUTS
        world.move(move)
        if move == "o":
            world.place(input("Direction:"))
        elif move == "x":
            world.remove(input("Direction:"))
        elif move == 'x':
            exit()
