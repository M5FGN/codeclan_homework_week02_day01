class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, check_player):
        player_found = False
        for player in self.players:
            if player == check_player:
                player_found = True
        return player_found
            

    def play_game(self, result):
        if result == True:
            self.points += 3
        elif result == False:
            self.points