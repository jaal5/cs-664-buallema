def constraintsatisfaction(bo, val, pos):
    # Check for violations in field
    field_x = (pos[1] // 3) * 3  # calculates the first column of the field
    field_y = (pos[0] // 3) * 3  # calculates the first row of the field

    for r in range(field_y, field_y + 3):
        for c in range(field_x, field_x + 3):
            if bo[r][c] == val and (r, c) != pos:
                return False

    # Check for violations in every column c in row
    for c in range(len(bo[0])):
        if bo[pos[0]][c] == val and pos[1] != c:
            return False

    # Check for violations in every row r in column
    for r in range(len(bo)):
        if bo[r][pos[1]] == val and pos[0] != r:
            return False
    return True