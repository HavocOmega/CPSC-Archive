# board.py for Assignment 4
# Written by: Ryll Santillan
# UCID: 30257967

# Note: Develop algorithm for collision detection
# Ideas so far are to read each line or just keep checking in that general direction for an answer

class Board: 
    def __init__(self):
        self.steps = 0
        self.player_count = 0
        self.escaped = []
        self.dead = []

        self.directions = {
            "U": [-1,0],
            "D": [1, 0],
            "L": [0,-1],
            "R": [0,1]
        }

        self.map = []
        self.players = []
        self.exit = None

        try:
            map_file = open("./map.txt")
            for i in range(12):
                current_line = map_file.readline().split("\n")[0]
                line = []
                for j in range(16):
                    if current_line[j] == "#":
                        line.append("#")
                    else:
                        line.append(" ")
                self.map.append(line)
            map_file.close()
        except IndexError as index_error:
            print("Map Contents are invalid")
        except:
            print("Map does not exist")

        try:
            player_file = open("./players.txt")
            player_count = len(player_file.readlines())
            self.player_count = player_count
            player_file.seek(0,0)
            for i in range(player_count):
                player_cords = player_file.readline().split("\n")[0].split(" ")
                player_cords = [int(i) for i in player_cords]
                self.players.append(player_cords)
            player_file.close()
        except:
            print("Player file do not exist")

        try:
            exit_file = open("./exit.txt")
            self.exit = exit_file.readline().split("\n")[0].split(" ")
            self.exit = [int(i) for i in self.exit]
            exit_file.close()
        except:
            print("Exit file do not exist")

        return
    
    def get_board(self):
        game_board = [i[:] for i in self.map]

        for player in range(len(self.players)):
            game_board[self.players[player][0]][self.players[player][1]] = "P"

        game_board[self.exit[0]][self.exit[1]] = "E"

        return game_board
    
    def isPlacementValid(self, Position: list):
        if (Position[0] < 0 or Position[1] < 0) or (Position[0] > 11 or Position[1] > 15):
            return False
        return True
     
    def update(self, direction):
        player_direction = self.directions[direction]
        direction_index =  0 if (direction == "U" or direction == "D") else 1
        new_coords = [i[:] for i in self.players]
        inactive = []
        game_board = self.get_board()

        self.steps += 1
        
        n = len(new_coords)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if new_coords[j][direction_index] > new_coords[j+1][direction_index]:
                    new_coords[j], new_coords[j+1] = new_coords[j+1], new_coords[j]
                swapped = True
            if (swapped == False):
                break

        if player_direction[direction_index] > 0:
            new_coords.reverse()

        for i in range(len(new_coords)):
            position = new_coords[i]
            desired_position = [position[0] + player_direction[0], position[1] + player_direction[1]]

            if not self.isPlacementValid(desired_position):
                new_coords[i] = new_coords[i]
            else:
                current_occupant = game_board[desired_position[0]][desired_position[1]]
                if current_occupant == "#":
                    self.dead.append(i)
                    inactive.append(i)
                    new_coords[i] = desired_position
                elif current_occupant == "E":
                    self.escaped.append(i)
                    inactive.append(i)
                    new_coords[i] = desired_position
                elif desired_position in new_coords:
                    new_coords[i] = new_coords[i]
                else:
                    new_coords[i] = desired_position

        for i in inactive:
            new_coords.pop(i)

        self.players = new_coords
        return
    
    def get_state(self):
        robot_amount = self.player_count
        escaped_robots = len(self.escaped)
        dead_robots = len(self.dead)

        print(escaped_robots, dead_robots, robot_amount)
        state = 0
        if escaped_robots == robot_amount and dead_robots == 0:
            state = 1
        elif dead_robots == robot_amount and escaped_robots == 0:
            state = 2
        elif dead_robots > 0 and escaped_robots > 0 and (escaped_robots + dead_robots) == robot_amount:
            state = 3
        return state
    
    def save_map(self):
        save_file = open("./save.txt", "w")
        for i in range(len(self.map)):
            current_line = self.map[i]
            line = ""
            for j in range(len(current_line)):
                line = line + current_line[j]
            save_file.write(line + "\n")

        for i in range(len(self.players)):
            save_file.write(str(self.players[i][0]) + " " + str(self.players[i][1]) + " ")
        save_file.write("\n")

        save_file.write(str(self.exit[0]) + " " + str(self.exit[1]) + "\n")

        for i in self.dead:
            save_file.write(str(i) + " ")
        save_file.write("\n")
            
        for i in self.escaped:
            save_file.write(str(i) + " ")
        save_file.write("\n")

        save_file.write(str(self.steps) + " " + str(self.player_count) + "\n")

        save_file.close()
        return
    
    def load_map(self):
        save_file = open("./save.txt")

        loaded_map = []
        for i in range(12):
            current_line = save_file.readline().split("\n")[0]
            line = []
            for j in range(16):
                line.append(current_line[j])
            loaded_map.append(line)

        current_line = save_file.readline().split("\n")[0].split(" ")
        current_line.pop(len(current_line) - 1)

        loaded_players = []
        for i in range(0, len(current_line), 2):
            loaded_players.append([int(current_line[i]), int(current_line[i + 1])])

        loaded_exit = save_file.readline().split("\n")[0].split(" ")
        loaded_exit = [int(i) for i in self.exit]

        current_line = save_file.readline().split("\n")[0].split(" ")
        current_line.pop(len(current_line) - 1)
        loaded_dead = [i for i in current_line]
        current_line = save_file.readline().split("\n")[0].split(" ")
        current_line.pop(len(current_line) - 1)
        loaded_escaped = [i for i in current_line]

        self.map = loaded_map
        self.players = loaded_players
        self.exit = loaded_exit
        self.dead = loaded_dead
        self.escaped = loaded_escaped

        current_line = save_file.readline().split("\n")[0].split(" ")
        self.steps = int(current_line[0])
        self.player_count = int(current_line[1])

        save_file.close()
        return
    
    def get_steps(self):
        return self.steps