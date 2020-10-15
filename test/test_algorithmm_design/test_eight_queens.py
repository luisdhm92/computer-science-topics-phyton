import unittest
from typing import Optional, List, Dict

from algorithm_design.constraint_satisfaction import CSP
from algorithm_design.eight_queens import QueensConstraint


class TestMapColoring(unittest.TestCase):

    def test_csp_map_coloring(self):
        columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows: Dict[int, List[int]] = {}
        for column in columns:
            rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
        csp: CSP[int, int] = CSP(columns, rows)
        csp.add_constraint(QueensConstraint(columns))
        solution: Optional[Dict[int, int]] = csp.backtracking_search()
        if solution is None:
            print("No solution found!")
        else:
            print(solution)
            for key in solution.keys():
                self.assertTrue(csp.consistent(key, solution))


if __name__ == '__main__':
    unittest.main()
