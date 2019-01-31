#!/usr/bin/python

def checkflag(data):
    check = []
    key = [1, 44, 43, 30, 32, 20, 48, 28, 30, 15, 8, 44, 23, 46, 44, 39, 41, 28, 49, 27, 43, 21, 25, 10, 1, 25, 41, 13, 29, 1, 12, 13, 7, 46, 7, 2, 38, 15, 7, 42, 33, 47]
    password = [81, 24, 24, 54, 38, 103, 64, 93, 86, 89, 103, 66, 72, 59, 71, 56, 64, 81, 63, 84, 71, 95, 72, 100, 115, 70, 61, 98, 85, 94, 87, 103, 95, 49, 105, 106, 59, 106, 94, 72, 82, 78]

    if len(data) != len(password):
        return False

    for i in range(len(data)):
        check.append(ord(data[i]) - key[i])

    if check == password:
        return True
    else:
        return False

def main():
    user = raw_input("Masukan Flag : ")
    if checkflag(user) == True:
        print("Selamat, flag yang Anda masukan benar !")
    else:
        print("Maaf, flag yang Anda masukan salah. Coba lagi !")


if __name__ == "__main__":
    main()
