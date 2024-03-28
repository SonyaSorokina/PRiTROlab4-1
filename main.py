def readFile(text):
    f = open(text, 'r', encoding="UTF-8")
    people = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        people.append(int(line))
    return people

def twoGroup(people):
    one = 0
    two = 0
    for i in range(len(people)):
        if (max(people) + one) > (max(people) + two):
            two += max(people)
            people.remove(max(people))
        else:
            one += max(people)
            people.remove(max(people))
    print(*sorted([one, two]))

from os import listdir, getcwd

print(getcwd())
files = [i for i in listdir(getcwd()) if ".txt" in i]

for i, file in enumerate(files, start=1):
    try:
        print(f"Тест {i}")
        twoGroup(readFile(file))
    except Exception as e:
        print(e)
