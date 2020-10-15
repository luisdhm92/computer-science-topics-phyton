import unittest
from typing import Optional, List, Dict

from algorithm_design.constraint_satisfaction import CSP
from algorithm_design.map_coloring import MapColoringConstraint


class TestMapColoring(unittest.TestCase):

    def test_csp_map_coloring(self):
        variables: List[str] = ["Western Australia", "Northern Territory", "South Australia",
                                "Queensland", "New South Wales", "Victoria", "Tasmania"]
        domains: Dict[str, List[str]] = {}
        for variable in variables:
            domains[variable] = ["red", "green", "blue"]
        csp: CSP[str, str] = CSP(variables, domains)
        csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
        csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
        csp.add_constraint(MapColoringConstraint("South Australia", "Northern Territory"))
        csp.add_constraint(MapColoringConstraint("Queensland", "Northern Territory"))
        csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
        csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
        csp.add_constraint(MapColoringConstraint("New South Wales", "South Australia"))
        csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
        csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
        csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))
        solution: Optional[Dict[str, str]] = csp.backtracking_search()
        if solution is None:
            print("No solution found!")
        else:
            print(solution)
            for key in solution.keys():
                self.assertTrue(csp.consistent(key, solution))


if __name__ == '__main__':
    unittest.main()
