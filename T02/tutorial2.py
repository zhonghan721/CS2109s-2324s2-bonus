from treelib import Tree
import queue

h = {
    'S':7,
    'B':0,
    'A':3,
    'G':0
}
graph = {
    'S': {('A',2), ('B',4)},
    'A': {('S',2), ('B',1)},
    'B': {('S',4), ('A',1), ('G',4)},
    'G': {('B',4)},
}

class Node:
    r"""Node class for search tree
    Args:
        parent (Node): the parent node of this node in the tree
        act (Action): the action taken from parent to reach this node
        state (State): the state of this node
        g_n (float): the path cost of reaching this state
        h_n (float): the heuristic value of this state
    """
    
    def __init__(
            self, 
            parent: "Node", 
            act, 
            state, 
            g_n: float = 0.0, 
            h_n: float = 0.0):

        self.parent = parent # where am I from
        self.act = act # how to get here
        self.state = state # who am I
        self.g_n = g_n # what it costs to be here g(n)
        self.h_n = h_n # heuristic function h(n)
    
    def get_fn(self):
        r"""
        Returns the sum of heuristic and cost of the node
        """
        return self.g_n + self.h_n

    def __str__(self):
        return str(self.state)

    def __lt__(self, node):
        """Compare the path cost between states"""
        return self.g_n < node.g_n

    def __eq__(self, node):
        """Compare whether two nodes have the same state"""
        return isinstance(node, Node) and self.state == node.state

    def __hash__(self):
        """Node can be used as a KeyValue"""
        return hash(self.state)
    
def astar(graph, inital_node, goal_test, heuristics, is_tree, is_update):
    tree = Tree()
    frontier = queue.PriorityQueue()
    fail = True
    solution = []
    visited = set()

    cost = 0
    goal_node = None

    start_node = Node(None, inital_node, inital_node, cost, heuristics[inital_node])
    frontier.put((start_node.get_fn(), start_node))
    tree.create_node(inital_node, inital_node + str(start_node.g_n) + str(start_node.h_n) + str(start_node.get_fn()))

    while frontier.qsize != 0:
        curr_node = frontier.get()[1]
        curr_state = curr_node.state
        if goal_test(curr_state):
            fail = False
            goal_node = curr_node
            break
        if not is_tree:
            if curr_state in visited:
                continue
            visited.add(curr_state)
        
        curr_cost = curr_node.g_n
        for action in graph[curr_state]:
            next_state = action[0]
            next_node = Node(curr_node, curr_node.act + next_state, next_state, 
                             curr_cost + action[1], 
                             heuristics[next_state])
            frontier.put((next_node.get_fn(), next_node))
            tree.create_node(next_state, next_state + str(next_node.g_n) + str(next_node.h_n) + str(next_node.get_fn()),
                             curr_state + str(curr_node.g_n) + str(curr_node.h_n) + str(curr_node.get_fn()))

    if not fail:
        while goal_node is not None:
            solution.append(goal_node.state)
            goal_node = goal_node.parent
        solution.reverse()

    # return goal_node.act

    tree.save2file('astar.txt', line_type='ascii')

    return ''.join(solution)

# You might get a different trace due to popping different nodes.

print("=====")
print("Tree")
print("=====")
print(p:=astar(graph, 'S', lambda n: n=='G', h, is_tree=True, is_update=False))
assert(p=="SABG")

print("=====")
print("Graph")
print("=====")
print(p:=astar(graph, 'S', lambda n: n=='G', h, is_tree=False, is_update=False))
assert(p=="SBG")