import unittest
from typing import Optional, List, Callable

from algorithm_design.generic_search import Node, dfs, node_to_path, bfs, astar
from algorithm_design.maze_solution import Maze, MazeLocation, manhattan_distance


class TestMazeSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m: Maze = Maze()
        print(cls.m)

    def test_solution_with_dfs(self):
        solution1: Optional[Node[MazeLocation]] = dfs(self.m.start, self.m.goal_test, self.m.successors)
        if solution1 is None:
            print("No solution found using depth-first search!")
        else:
            path1: List[MazeLocation] = node_to_path(solution1)
            self.m.mark(path1)
            print(self.m)
            self.m.clear(path1)

    def test_solution_with_bfs(self):
        solution2: Optional[Node[MazeLocation]] = bfs(self.m.start, self.m.goal_test, self.m.successors)
        if solution2 is None:
            print("No solution found using breadth-first search!")
        else:
            path2: List[MazeLocation] = node_to_path(solution2)
            self.m.mark(path2)
            print(self.m)
            self.m.clear(path2)

    def test_solution_with_astar(self):
        distance: Callable[[MazeLocation], float] = manhattan_distance(self.m.goal)
        solution3: Optional[Node[MazeLocation]] = astar(self.m.start, self.m.goal_test, self.m.successors, distance)
        if solution3 is None:
            print("No solution found using A*!")
        else:
            path3: List[MazeLocation] = node_to_path(solution3)
            self.m.mark(path3)
            print(self.m)


if __name__ == '__main__':
    unittest.main()
