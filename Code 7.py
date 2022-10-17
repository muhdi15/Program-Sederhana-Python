
while(True):
    import os
    os.system("cls")
    os.system("color a")
    print("\t           Ini adalah program sederhana")
    print("=" * 75)
    print("")
    print("\n1. Microsoft Word \n2. youtube \n3. Whatsapp \n4.Github \n5. Else = Viruses")

    user = input("Masukkan nomor Pilihan anda : ")

    if(user == '1'):
        os.system("Start Winword.exe")
    elif(user == '2'):
        os.system("start www.youtube.com")
    elif(user == '3'):
        os.system("start https://web.whatsapp.com")
    elif(user == '4'):
        os.system("start www.Github.com")
    else:
        while(True):
            os.system("msg * anda Goblok")
    print("no = berhentikan program")
    print("Tekan apa saja untuk melanjutkan")

    tanya = input("Masih ingin lanjut")

    if(tanya == "no"):
        break

print("Thanks for Using my Program")

