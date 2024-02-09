
from puzzle import Puzzle
from DFS import draw_legend
from queue import Queue

import pydot
import numpy as np

def bfs(initial_state):
    graph = pydot.Dot(graph_type='digraph', label="8 Puzzle State Space (BFS)", fontsize="30", color="red",
                          fontcolor="blue", style="filled", fillcolor="black")
    start_node = Puzzle(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()
    queue = Queue()  # Use a queue for BFS
    queue.put(start_node)
    explored = []
    print("The starting node is \ndepth=%d\n" % start_node.depth)
    print(start_node.display())
    while not queue.empty():
        node = queue.get()
        print("The node selected to expand is\n")
        print("depth=%d\n" % node.depth)
        print(node.display())
        explored.append(node.state)
        graph.add_node(node.graph_node)
        if node.parent:
            graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node, label=str(node.action)))
        if node.depth < 5:
            children = node.generate_child()
            print("The children nodes of this node are\n")
            for child in children:
                if child.state not in explored:
                    print("depth=%d\n" % child.depth)
                    print(child.display())
                    if child.goal_test():
                        print("This is the goal state")
                        graph.add_node(child.graph_node)
                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node, label=str(child.action)))
                        draw_legend(graph)
                        graph.write_png('bfs_solution.png')
                        return child.find_solution()
                    queue.put(child)  # Enqueue children for BFS
        else:
            print("The depth has exceeded its limit, so we don't expand this node.\n")
    return


