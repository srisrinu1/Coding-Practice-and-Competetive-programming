from re import search
for _ in range(int(input())):
    N = input()
    if(search("^[-+]?[0-9]*\.[0-9]+$", N)):
        print("True")
    else:
        print("False")
