def calculate_pi(n_terms: int) -> float:
    pi: float = 0
    numerator: float = 4
    denominator: float = 1
    sign: int = 1

    for _ in range(n_terms):
        pi += sign * (numerator/denominator)
        denominator += 2
        sign *= -1

    return pi
