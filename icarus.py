import random
handicap_1 = 1
to_win100 = 42
max_roll = 11
yes = ['yes', 'y', 'yeah', 'yea', 'sure', 'affirmative', 'absolutely', 'absolutely i do']
no = ['no', 'nope', 'negative', 'not really', 'no way', 'n', 'never', 'not at all']
def yes_or_no(question):
    response = input(question)
    while not response.lower() in yes and not response.lower() in no:
        print('please choose yes or no')
        response = input(question)
    if response.lower() in yes:
        return True
    if response.lower() in no:
        return False

def roll_to(max_num = max_roll, roll_bool = None):
    turn_score = 0
    roll_bool = yes_or_no("Would you like to roll? ")
    while roll_bool and turn_score < max_num:
        roll = 11 #random.randint(1, 6)
        turn_score += roll
        print("You rolled a {}, your turn score is {}.".format(roll, turn_score))
        if turn_score < max_num:
            roll_bool = yes_or_no("Would you like to roll again? ")
        if turn_score > max_num:
            print("You rolled too high, Icarus!  You get nothing!")
            turn_score = 0
            roll_bool = False
        if turn_score == max_num:
            print("You reached the maximum score, your turn is over.")
            roll_bool = False
    print("Your turn score is {}.".format(turn_score))
    return turn_score

def break_tie(intro, player, roll_bool = None):
    num_to_match = random.randint(1, 9)
    print("{}, you must roll {} to win.".format(player, num_to_match))
    roll_bool = yes_or_no(intro)
    current_roll = None
    if roll_bool:
        current_roll = random.randint(1, 9)
        if current_roll != num_to_match:
            print("{} rolled {}.  Better luck next time!".format(player, current_roll))
            return False

        if current_roll == num_to_match:
            print("{}, you got the magic number!".format(player))
            return True
    if not roll_bool:
        return False



class Player:
    def __init__(self, name, score=0, is_turn=False):
        self.name = name
        self.score = score
        self.is_turn = is_turn

    def player_turn(self):
        self.is_turn = True
        if self.is_turn:
            print("{}, it is your turn.".format(self.name))
            turn_score = roll_to()
            self.score += turn_score
            print("Your total score is {}.".format(self.score))
            if isinstance(self, KidPlayer):
                self.score += handicap_1
                print("One point added for kid player, new total score is {}.".format(self.score))
            self.is_turn = False

class KidPlayer(Player):
    pass



class Game:
    def __init__(self, players = None, game_won = False):
        self.game_won = game_won
        self.players = []

    def add_players(self, add_player = True):
        print("Hello, and welcome to Icarus, the dice game for JerkX!")
        print("You can roll as many times as you want in a turn but")
        print("if you go over {} you get NOTHING!".format(max_roll))
        print("First one to {} wins!  ".format(to_win100))
        print("Let's add your first player!")
        while add_player == True:
            what_name = input("What is the player's name? ")
            is_kid = (yes_or_no("Is this player a kid? "))
            if is_kid == True:
                new_player = KidPlayer(what_name)
                self.players.append(new_player)
                print("You added {}".format(new_player.name))
                add_player = yes_or_no('Would you like to add another player? ')
            if is_kid == False:
                new_player = Player(what_name)
                self.players.append(new_player)
                print('You added {}'.format(new_player.name))
                add_player = yes_or_no('Would you like to add another player? ')
        else:
             print("Players: ")
             for player in self.players:
                 print(player.name)
             print("Let's go!")

    def take_turns(self, winning_score = to_win100):
        high_score = 0
        while high_score < winning_score:
            for player in self.players:
                player.player_turn()
                if player.score > high_score:
                    high_score = player.score
        else:
            print("Final Scores: ")
            for player in self.players:
                print("{} - {}".format(player.name, player.score))
            winner = [player for player in self.players if player.score == high_score]
        if len(winner) == 1:
            win = winner[0]
            self.game_won = True
            print("The winner is {}!  You must feel pretty good about yourself!".format(win.name))

        if len(winner) > 1:
            tie_string = "We have a tie between "
            index = 0
            while index < len(winner):
                tied_player = winner[index]
                tie_string += (tied_player.name)
                index += 1
                if index < len(winner):
                    tie_string += " and "
                if index == len(winner):
                    tie_string += "!"
            print(tie_string)
            print("Welcome to the tie breaker!  Match the magic number in sudden death overtime!")
        return winner

    def tie_break(self):
        tied_players = new_game.take_turns()
        while self.game_won == False:
            for player in tied_players:
                self.game_won = break_tie("{}, are you ready to roll? ".format(player.name), player.name)
                if self.game_won:
                    print("{}, You have won the game! You must feel pretty good about yourself!".format(player.name))


new_game = Game()
new_game.add_players()
new_game.tie_break()



#chad = Player("Chad")
#billie = Player("Billie")
#tied = [chad, billie]
#new_game = Game()
#new_game.tie_break()



