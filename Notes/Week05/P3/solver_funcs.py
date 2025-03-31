def check_valid(puzzle: list[list[int]], cages: list[list[int]]) -> bool:
    return (
        check_cages_valid(puzzle, cages) and
        check_columns_valid(puzzle) and
        check_rows_valid(puzzle)
    )


def check_cage(puzzle: list[list[int]], cage: list[int]) -> bool:
    remainder = cage[0]
    is_full = True
    size = len(puzzle)

    # Make sure the puzzle is square
    assert all(len(row) == size for row in puzzle)

    for entry in cage[2:]:
        value = puzzle[entry // size][entry % size]
        is_full = is_full and value > 0
        remainder -= value

    return is_full and remainder == 0 or not is_full and remainder > 0


def check_cages_valid(puzzle: list[list[int]], cages: list[list[int]]) -> bool:
    return all(check_cage(puzzle, cage) for cage in cages)


def check_column(puzzle: list[list[int]], column_number: int) -> bool:
    seen = set()
    for row in puzzle:
        if len(row) <= column_number:
            continue

        value = row[column_number]
        if value in seen:
            return False
        elif value > 0:
            seen.add(value)

    return True


def check_columns_valid(puzzle: list[list[int]]) -> bool:
    return all(check_column(puzzle, column_number)
               for column_number in range(max(map(len, puzzle))))


def check_row(row: list[int]) -> bool:
    seen = set()
    for value in row:
        if value in seen:
            return False
        elif value > 0:
            seen.add(value)

    return True


def check_rows_valid(puzzle: list[list[int]]) -> bool:
    return all(check_row(row) for row in puzzle)
