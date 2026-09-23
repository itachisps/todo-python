tasks = []

try:
    with open("tasks.txt", "r") as f:
        for line in f:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print()
    print("1. Zid mohima")
    print("2. Chouf l'mohamat")
    print("3. Ms7 mohima")
    print("4. Khrouj")
    choice = input("Khtar (1, 2, 3 wla 4): ")
    

    if choice == "1":
        task = input("Achno l'mohima? ")
        tasks.append(task)
        print("Tzadat!")
    elif choice == "2":
        print("L'mohamat dyalk:")
        for task in tasks:
            print("-", task)
    elif choice == "3":
        to_remove = input("Achno l'mohima li bghiti tms7? ")
        if to_remove in tasks:
            tasks.remove(to_remove)
            print("T ms7at!")
        else:
            print("Ma kaynach had l'mohima")
    elif choice == "4":
        break

with open("tasks.txt", "w") as f:
    for task in tasks:
        f.write(task + "\n")

print("T7fdo l'mohamat. Bslama!")