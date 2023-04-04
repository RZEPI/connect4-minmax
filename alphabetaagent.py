import minmaxagent as MinMaxAgent
import math
class AlphaBetaAgent(MinMaxAgent.MinMaxAgent):
    def __init__(self, my_token):
        super().__init__(my_token)


    def decide(self, connect4):
        move, _ = self.minimax(connect4, 4, True, -math.inf, math.inf)
        return move

    def minimax(self, connect4, depth, maximazing_player, alpha, beta):
        if self.my_token == 'x':
            opponent = 'o'
        else:
            opponent = 'x'

        if depth == 0:
            return (None, MinMaxAgent.score_position(connect4, self.my_token))
            
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
                _, tmp_value = self.minimax(connect4, depth-1, False, alpha, beta)
                connect4.pull_token(col)
                if value < tmp_value:
                    best_col = col
                    value = tmp_value
                alpha = max(value, alpha)
                if alpha >= beta:
                    break
        else:
            value = math.inf
            for col in connect4.possible_drops():
                connect4.drop_token_minmax(col)
                _, tmp_value =self.minimax(connect4, depth-1, True, alpha, beta)
                connect4.pull_token(col)
                if value > tmp_value:
                    best_col = col
                    value = tmp_value
                beta = min(beta, value)
                if alpha >= beta:
                    break

        return best_col, value
