# board.py for Assignment 4
# Written by: Ryll Santillan
# UCID: 30257967

# Note: Develop algorithm for collision detection
# Ideas so far are to read each line or just keep checking in that general direction for an answer

directions = {
    "U": [-1,0],
    "D": [1, 0],
    "L": [0,-1],
    "R": [0,1]
}

def isPlacementValid(Position: list):
    if (Position[0] < 0 or Position[1] < 0) or (Position[0] > 11 or Position[1] > 15):
        return False
    return True


class Board: 
    def __init__(self):
        self.steps = 0
        self.escaped = []
        self.dead = []

        self.currentBoard = None

        self.map = []
        self.players = []
        self.exit = None

        try:
            map_file = open("./map.txt")
            for i in range(12):
                current_line = map_file.readline().split("\n")[0]
                line = []
                for j in range(16):
                    line.append(current_line[j])
                self.map.append(line)
            map_file.close()
        except IndexError as index_error:
            print("Map Contents are invalid")
        except:
            print("Map does not exist")

        try:
            player_file = open("./players.txt")
            player_count = len(player_file.readlines())
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
        if self.currentBoard != None:
            return self.currentBoard
        
        self.currentBoard = self.map
        for player in range(len(self.players)):
            self.currentBoard[self.players[player][0]][self.players[player][1]] = "P"

        self.currentBoard[self.exit[0]][self.exit[1]] = "E"

        return self.currentBoard
     
    def update(self, direction):
        new_coords = [None]*len(self.players)
        queued_bots = {}
        player_direction = directions[direction]

        for player in self.players:
            bot_index = self.players.index(player)
            if bot_index in self.dead or bot_index in self.escaped: continue
            desired_pos = [player[0] + player_direction[0], player[1] + player_direction[1]]
            current_occupant = self.currentBoard[desired_pos[0]][desired_pos[1]]

            if current_occupant == "#":
                self.dead.append(bot_index)
                self.currentBoard[player[0]][player[1]] = " "
            elif current_occupant == "E":
                self.escaped.append(bot_index)
                self.currentBoard[player[0]][player[1]] = " "
            elif not isPlacementValid(desired_pos):
                new_coords[bot_index] = None
            elif current_occupant == "P":
                queued_bots[bot_index] = desired_pos
            else:
                new_coords[bot_index] = desired_pos

        while len(queued_bots) > 0:
            print(queued_bots)
            for key in list(queued_bots.keys()):
                print(key)
                v = queued_bots[key]
                occupant_index = self.players.index(v)
                print(v," ",occupant_index)


                if new_coords[occupant_index] is not None:
                    new_coords[key] = v
                    del queued_bots[key]

        print(new_coords)
        for pos in new_coords:
            if pos != None:
                bot_index = new_coords.index(pos)
                self.currentBoard[pos[0]][pos[1]] = "P"
                self.currentBoard[self.players[bot_index][0]][self.players[bot_index][1]] = " "
                self.players[bot_index] = pos

        print()
        return
    
    def get_state(self):
        robot_amount = len(self.players)
        escaped_robots = len(self.escaped)
        dead_robots = len(self.dead)
        state = 0
        if escaped_robots == robot_amount and dead_robots == 0:
            state = 1
        elif dead_robots == robot_amount and escaped_robots == 0:
            state = 2
        elif dead_robots > 0 and escaped_robots > 0 and (escaped_robots + dead_robots) == robot_amount:
            state = 3
        return state
    
    def save_map(self):
        return
    
    def load_map(self):
        return
    
    def get_steps(self):
        return