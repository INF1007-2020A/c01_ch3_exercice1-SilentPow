#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
#wow petit commit 

def square_root(number: int) -> float:
    # TODO completer la fonction
    square_rooted = math.sqrt(number)
    return square_rooted


def square(number: int) -> int:
    # TODO completer la fonction
    squared = math.pow(number, 2)
    return squared


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
