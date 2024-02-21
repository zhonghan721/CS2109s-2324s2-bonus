import numpy as np

class State:
    def __init__(self, val, is_max_player=False, children=[]):
        self.children = children
        self.is_max_player = is_max_player
        self.val = val
    def get_children(self, is_reversed=False):
        if is_reversed:
            return reversed(self.children)
        else:
            return self.children
    def is_terminal(self):
        return len(self.children) == 0
    
def alpha_beta_search(state, alpha=-np.infty, beta=np.infty, depth=0, is_reversed=False):

    def maxValue(state, alpha, beta):
        if state.is_terminal():
            return state.val
        v = -np.infty
        for c in state.get_children(is_reversed):
            v = max(v, minValue(c, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def minValue(state, alpha, beta):
        if state.is_terminal():
            return state.val
        v = np.infty
        for c in state.get_children(is_reversed):
            v = min(v, maxValue(c, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    if state.is_terminal(): 
        return state.val
    return maxValue(state, alpha, beta) if state.is_max_player else minValue(state, alpha, beta)

s = State('MAX0', True,
      [
          State('MIN1.1', False,
                [
                    State('MAX2.1', True, [
                        State('MIN3.1', False, [State(8), State(7)]),
                        State('MIN3.2', False, [State(3), State(9)]),
                    ]),
                    State('MAX2.2', True, [
                        State('MIN3.3', False, [State(9), State(8)]),
                        State('MIN3.4', False, [State(2), State(4)]),
                    ]),
                ]),
          State('MIN1.2', False,
                [
                    State('MAX2.3', True, [
                        State('MIN3.5', False, [State(1), State(8)]),
                        State('MIN3.6', False, [State(8), State(9)]),
                    ]),
                    State('MAX2.4', True, [
                        State('MIN3.7', False, [State(9), State(9)]),
                        State('MIN3.8', False, [State(3), State(4)]),
                    ]),
                ])
      ])
print(alpha_beta_search(s))