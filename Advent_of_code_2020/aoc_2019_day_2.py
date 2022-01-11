## Aufgabe 1:
#
# Daten einlesen: Datei in mem: list[int]
"""
with open("input_aoc_2019_day_2") as f:
    mem = [int(x) for x in f.read().split(",")]

print(mem)


# Input setzen (mem[1] und mem[2])
mem[1], mem[2] = 12, 2

# Programm interpreter
for ic in range(0, len(mem), 4):
    if mem[ic] == 99:
        break
    elif mem[ic] == 1:
        mem[mem[ic + 3]] = mem[mem[ic + 1]] + mem[mem[ic + 2]]

    elif mem[ic] == 2:
        mem[mem[ic + 3]] = mem[mem[ic + 1]] * mem[mem[ic + 2]]

    else:
        raise ValueError

print(mem[0])
"""

## Aufgabe 2:
# Funktion machen

""
def read_program(file_name):
    with open(file_name) as f:
        return [int(x) for x in f.read().split(",")]


def run_program(mem, p1, p2):

    # Input setzen (mem[1] und mem[2])
    mem[1], mem[2] = p1, p2

    # Programm interpreter
    ic = 0
    while ic < len(mem) and mem[ic] != 99:
        if mem[ic] == 1:
            mem[mem[ic + 3]] = mem[mem[ic + 1]] + mem[mem[ic + 2]]
            ic += 4

        elif mem[ic] == 2:
            mem[mem[ic + 3]] = mem[mem[ic + 1]] * mem[mem[ic + 2]]
            ic += 4

        else:
            raise ValueError
    return mem[0]

def run_task1():
    print(run_program(read_program("input_aoc_2019_day_2"), 12, 2))

def run_task2():
    mem = read_program("input_aoc_2019_day_2")
    for x in range(0, 100):
        for y in range(0, 100):
            if 19690720 == run_program(mem.copy(), x, y):
                return x, y



if __name__ == "__main__":
    run_task1()
    noun, verb = run_task2()
    print(noun * 100 + verb)