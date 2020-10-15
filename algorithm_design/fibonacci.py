from typing import Generator
from functools import lru_cache


@lru_cache(maxsize=None)
def recursive_fibonacci(n: int) -> int:
    if n < 2: # base case 
        return n
    return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1) # recursive case


def fibonacci(n: int) -> Generator[int, None, None]:
    yield 0  # special case

    if n > 0:
        yield 1  # special case

    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    fib_iter = 0
    fib_rec = recursive_fibonacci(50)
    print(f"fib_rec {fib_rec}")
    for i in fibonacci(50):
        fib_iter = i
    
    print(f"fib_iter {fib_iter}")
