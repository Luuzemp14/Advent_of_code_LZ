"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
- valid, wenn alles vorhanden und cid ist optional
- zaehlen wie viele valid sind.
- Wann faengt ein Passport an? (Trennung)
- Datren importieren
"""

with open("input_aoc_4") as f:
    s = f.read()
    s = s.split("\n\n")
    a = []
    for val in s:
        a.append(val.replace("\n", " ").split(" "))
    temp = []
    for i in a:
        temp2 = []
        for j in i:
            temp2.append(j.split(":"))
        temp.append(temp2)
    #print(temp)

    attributliste = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    cnt = 0
    for i in temp:
        cnt2 = 0
        for j in i:
            if j[0] in attributliste:
                cnt2 += 1
        if cnt2 == 7:
            cnt += 1
    print(cnt)