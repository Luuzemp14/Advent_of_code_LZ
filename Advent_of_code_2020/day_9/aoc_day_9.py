hobbies = ["Fussball", "Freundin", "Pokemon", "Essen", "Fitness", "Reisen", "Wandern"]

while hobbies[-1] != "Fitness":
    del hobbies[-1]

number = str(len(hobbies))
print("These are your " + number + " favourite hobbies:")
print(hobbies)

extras = ["Kaffi", "Kino", "Bars", "Shopping", "Chips", "netflix", "Disney"]

costs = [50, 20, 80, 30, 40, 10, 25]
to_save = 100
savings = 0


while to_save > 0:
    to_save -= costs[-1]
    savings += costs[-1]
    del costs[-1]
    del extras[-1]

savings = str(savings)
print("you'll save " + savings + " euros by sticking to these extras:")
print(extras)

next_saving = extras[-1]
print("if you need to save more money, take some time off " + next_saving + ".")
