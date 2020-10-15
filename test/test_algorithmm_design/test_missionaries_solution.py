import unittest
from typing import Optional, List

from algorithm_design.generic_search import Node, dfs, node_to_path, bfs
from algorithm_design.missionaries_solution import MCState, MAX_NUM, display_solution


class TestMissionariesSolution(unittest.TestCase):

    def setUp(self):
        self.start: MCState = MCState(MAX_NUM, MAX_NUM, True)

    def test_solution_with_bfs(self):
        solution: Optional[Node[MCState]] = bfs(self.start, MCState.goal_test, MCState.successors)
        if solution is None:
            print("No solution found!")
        else:
            path: List[MCState] = node_to_path(solution)
            display_solution(path)


if __name__ == '__main__':
    unittest.main()
