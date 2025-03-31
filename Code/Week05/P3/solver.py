import math

from solver_funcs import check_valid


def get_cages() -> tuple[list[list[int]], int]:
    number_cages = int(input('Number of cages: '))
    cages = []
    cell_count = 0

    for cage_number in range(number_cages):
        cages.append(
            [int(x) for x in input(f'Cage number {cage_number}: ').split()])

        cell_count += cages[-1][1]

    return cages, math.isqrt(cell_count)


def print_puzzle(
        puzzle: list[list[int]], checks: int, backtracks: int) -> None:
    print('\n--Solution--\n')

    for row in puzzle:
        print(*row)

    print(f'\nchecks: {checks} backtracks: {backtracks}')


def main() -> None:
    position = 0
    checks = 0
    backtracks = 0
    cages, size = get_cages()

    puzzle = [[0 for _ in range(size)] for _ in range(size)]

    while position < size ** 2:
        row, col = divmod(position, size)
        puzzle[row][col] += 1

        checks += 1
        if check_valid(puzzle, cages):
            position += 1
        else:
            while puzzle[row][col] == size:
                puzzle[row][col] = 0
                backtracks += 1
                position -= 1
                row, col = divmod(position, size)

    print_puzzle(puzzle, checks, backtracks)


if __name__ == '__main__':
    main()
