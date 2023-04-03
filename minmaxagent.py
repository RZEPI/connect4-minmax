import math

def score_position(connect4, who):
    score = 0
    for fours in connect4.iter_fours():
        score += score_part(fours, who)

    return score

def score_part(part, who):
    if who == 'x':
        opponent = 'o'
    else:
        opponent = 'x'

    if part.count(who) == 4:
        return 100
    elif part.count(who) == 3 and part.count("_") == 1:
        return 15
    elif part.count("_") == 2 and part.count(who) == 2:
        return 7
    
    if part.count(opponent) == 3 and part.count("_") == 1:
        return -40
    return 0


class MinMaxAgent:
    def __init__(self, my_token):
        self.my_token = my_token


    def decide(self, connect4):
        move, _ = self.minimax(connect4, 6, True)
        return move


    def minimax(self, connect4, depth, maximazing_player):
        if self.my_token == 'x':
            opponent = 'o'
        else:
            opponent = 'x'

        if depth == 0:
            return (None, score_position(connect4, self.my_token))
            
        winner, is_win = connect4.check_winning_position()
        if is_win:
            if winner == self.my_token:
                return (None, 10000000000)
            elif winner == opponent:
                return (None, -10000000000)
            else:
                return (None,0)

        if maximazing_player:
            value = -math.inf
            for col in connect4.possible_drops():
                connect4.drop_token_minmax(col)
                _, tmp_value = self.minimax(connect4, depth-1, False)
                connect4.pull_token(col)
                if value < tmp_value:
                    best_col = col
                    value = tmp_value
        else:
            value = math.inf
            for col in connect4.possible_drops():
                connect4.drop_token_minmax(col)
                _, tmp_value =self.minimax(connect4, depth-1, True)
                connect4.pull_token(col)
                if value > tmp_value:
                    best_col = col
                    value = tmp_value

        return best_col, value

    
