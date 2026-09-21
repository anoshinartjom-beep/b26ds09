count = 0

while True:
    n = int(input("Я загадал число, попробуй отгадай, убежище: "))
    if n == 67:
        print("Ебать, ты отгадал")
        break
    else:
        count += 1
        if count == 7:
            print("Ебать ты лошара")
            break