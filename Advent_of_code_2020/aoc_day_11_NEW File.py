with open("input day 11 2020") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

def step(m):
    new_m = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            new_row = []

            if m[i][j] == "L" and num_of_filled_seats(m, i, j) == 0:
                new_row.append("#")

            elif m[i][j] == "#" and num_of_filled_seats(m, i, j) >= 4:
                new_row.append("L")

            else:
                new_row.append(m[i][j])
        new_m.append(new_row)

    return new_m

