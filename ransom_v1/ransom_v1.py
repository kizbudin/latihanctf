#!/usr/bin/python
import os

def createnote():
    f = open("README.TXT","wb")
    f.write("Assalamualaikum Wr.Wb \n")
    f.write("Ransomware ini dibuat untuk latihan kriptografi untuk kompetisi Capture The Flag\n")
    f.write("Dapatkah kamu memulihkan dokumen rahasia yang terenkripsi oleh ransomware ini ?\n")
    f.write("Jika kamu bisa, silahkan kirim dokumen yang telah dipulihkan ke ravdhr@gmail.com \n")
    f.close()

def imgenc(data):
    res = ""
    key = os.urandom(1)

    for i in range(len(data)):
        res += chr(ord(data[i]) ^ ord(key))
    return res

def main():
    img = ""

    f = open("secret_image.jpg","rb")
    img = f.read()
    f.close()

    imgres = imgenc(img)

    f = open("secret_image.jpg.encrypted","wb")
    f.write(imgres)
    f.close()

    os.remove("secret_image.jpg")
    createnote()

if __name__ == "__main__":
    main()
