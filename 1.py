while True:
    n = input("Imagine a password")
    if len(n) < 6:
        print("Password is too short")
        pass
    if len(n) > 6:
    print("Password is valid")
