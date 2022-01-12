with open("input day 11 2020") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

def get_num_taken():
    cnt = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                cnt += 1
    return cnt

def get_adejcent_count(row, col):
    cnt = 0
    current_row = data[row]

    # check left
    if col -1 >= 0 and current_row[col -1] == "#":
        cnt += 1

    # check right
    if col +1 < len(current_row) and current_row[col +1] == "#":
        cnt += 1

    # check above
    if row -1 >= 0:
        above_row = data[row -1]

        if above_row[col] == "#":
            cnt += 1

        if col -1 >= 0 and above_row[col -1] == "#":
           cnt += 1

        if col +1 < len(above_row) and above_row[col +1] == "#":
            cnt += 1

    # check below
    if row +1 < len(data):
        below_row = data[row +1]

        if below_row[col] == "#":
            cnt += 1

        if col -1 >= 0 and below_row[col -1] == "#":
            cnt += 1

        if col +1 <= len(below_row)-1 and below_row[col +1] == "#":
            cnt += 1
    return cnt

def run_rules():
    new_seating = []

    for row in range(len(data)):
        current_row = data[row]
        new_row = []

        for col in range(len(current_row)):
            if current_row[col] == ".":
                new_row.append(".")
                continue

            adjacent_count = get_adejcent_count(row, col)

            if current_row[col] == "L" and adjacent_count == 0:
                new_row.append("#")

            elif current_row[col] == "#" and adjacent_count >= 4:
                new_row.append("L")

            else:
                new_row.append(current_row[col])

        new_seating.append(new_row)

    for i in range(len(data)):
        data[i] = new_seating[i]

def get_final_count():
    prev = data.copy()
    run_rules()

    while data != prev:
        prev = data.copy()
        run_rules()

    return get_num_taken()

print("Number of seats taken: " ,get_final_count())
