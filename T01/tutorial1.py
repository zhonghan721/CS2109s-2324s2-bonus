graph = {
    'S': {('A', 1), ('B', 5),  ('C', 15)},
    'A': {('G', 10), ('S', 1)},
    'B': {('G', 5), ('S', 5)},
    'C': {('G', 5), ('S', 15)},
    'G': set()
}

from priority_queue import PriorityQueue
from collections import defaultdict

class Node:
    def __init__(self, state, parent, cost):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.children = []
    def get_state(self):
        return self.state
    
    def get_parent(self):
        return self.parent
    
    def add_child(self, child):
        self.children.append(child)
    def get_children(self):
        return self.children
    
    def __repr__(self):
        return str(self.state)
    
    def __lt__(self, node):
        if self.cost == node.cost:
            return self.state < node.state
        return self.cost < node.cost
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state
    
    def __hash__(self):
        return hash(self.state)
        
# Return the path found
def uniform_cost_search(graph, inital_node, goal_test, is_tree, is_update):

    frontier = PriorityQueue('min')
    cost = 0
    start_node = Node(inital_node, None, cost)
    frontier.append(start_node, cost)
    goal_node = None

    if is_tree:
        while len(frontier) != 0:
            print(frontier.heap)
            curr_node = frontier.pop()
            cost = curr_node[0]
            if goal_test(curr_node[1].get_state()):
                goal_node = curr_node[1]
                break
            for neighbour in graph[curr_node[1].get_state()]:
                new_cost = cost + neighbour[1]
                next_node = Node(neighbour[0], curr_node[1], new_cost)
                frontier.append(next_node, new_cost)

    else:
        visited = set()
        while len(frontier) != 0:
            print(frontier.heap)
            print(visited)
            curr_node = frontier.pop()
            cost = curr_node[0]
            visited.add(curr_node[1].get_state())
            if goal_test(curr_node[1].get_state()):
                goal_node = curr_node[1]
                break
            for neighbour in graph[curr_node[1].get_state()]:
                new_cost = cost + neighbour[1]
                next_node = Node(neighbour[0], curr_node[1], new_cost)
                if neighbour[0] not in visited and next_node not in frontier:
                    frontier.append(next_node, new_cost)
                elif next_node in frontier:
                    if frontier[next_node] > new_cost:
                        del frontier[next_node]
                        frontier.append(next_node, new_cost)
                
                
    
    path = []
    while goal_node is not None:
        path.append(goal_node.get_state())
        goal_node = goal_node.get_parent()
    ans = ""
    for i in path:
        ans = i + ans
    return ans

print("=====")
print("Tree")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=True, is_update=False))
assert(p=="SBG")

print("=====")
print("Graph")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=False, is_update=True))
assert(p=="SBG")