#TP INI DIKERJAKAN DENGAN BANTUAN TEMAN SAYA 
#YANG BERNAMA BINTANG HARI PRATAMA

print("#### Selamat Datang di Mastermind ####")  # Output awalan 

digit = int(input("Masukkan jumlah digit yang ingin ditebak: "))  # Input untuk masukkin berapa digit
nyawa = -1  # Awalan untuk nyawa

while True:  # Looping buat masukkin secret number
    SecretNumber = str(input("Masukkan Secret Number: "))  # Inputan untuk secret number
    if len(SecretNumber) != digit:  # Cek digit dengan Secret Number
        print(f"Bilangan harus {digit} digit.") # Apabila tidak sama maka dihandling
    else:
        break


print("Pilihan jumlah nyawa: \n 1. Tak berhingga \n 2. Custom ") # Output pilihan nyawa
while True: # Looping buat milih nyawa    
    pilihanNyawa = int(input("Masukkan pilihan nyawa: "))  # Inputan untuk pilihan nyawa
    if pilihanNyawa > 2 :   # Jika pilihan tidak sesuai akan tidak valid
        print("Perintah tidak valid")

    elif pilihanNyawa == 2:  # Pilihan nyawa benar, maka variabel nyawa akan benar
        nyawa = int(input("Masukkan nyawa: "))
        break
    else:
        break


print("Pilihan level permainan: \n 1. Rookie \n 2. Master") # Output pilihan permainan
while True:    
    pilihMain = int(input("Masukkan pilihan menu: ")) #Input untuk pilih permainan
    if pilihMain > 2:  #Jika permainan tidak sesuai pilihan maka perintah tidak valid
        print("Perintah tidak valid")
    else:
        break

# Algoritma permainan
if pilihanNyawa == 1 and pilihMain == 1: 
    while True:
        tebakan1 = int(input("Guess : "))
        if len(str(tebakan1)) != len(str(SecretNumber)):
            print("Bilangan harus " + str(digit) + " digit")
        elif tebakan1 > int(SecretNumber):
            print("Bilangan terlalu besar")
        elif tebakan1 < int(SecretNumber):
            print("Bilangan terlalu kecil.")
        elif tebakan1 == int(SecretNumber): 
            break           
        else:
            print("Masukkan input yang valid")
       

elif pilihanNyawa == 2 and pilihMain == 1:
    while True:
        tebakan2 = int(input("Guess : "))          
        if len(str(tebakan2)) != len(str(SecretNumber)):
            nyawa -= 1
            print("Bilangan harus " + str(digit) + " digit")
        elif tebakan2 > int(SecretNumber):
            nyawa -= 1
            print("Bilangan terlalu besar.")
        elif tebakan2 < int(SecretNumber):
            nyawa -= 1
            print("Bilangan terlalu kecil")
        elif tebakan2 == int(SecretNumber) or nyawa == 0:
            break
        else:
            print("Masukkan input yang valid")


elif pilihanNyawa == 1 and pilihMain == 2:
    while True:  #Looping dua inputan untuk mengetahui elemen yang sama
        tebakan = input("Guess: ")
        sama = 0
        if SecretNumber != tebakan: 
            for i in range(digit):
                if SecretNumber[i] == tebakan[i]:
                    sama += 1
            print(f"Ada {sama} bilangan di posisi yang tepat.")
        else:
            break

        

elif pilihanNyawa == 2 and pilihMain == 2:
    while nyawa != 0:  # Looping dua inputan untuk mengetahui elemen yang sama
        tebakan = input("Guess: ")
        sama = 0
        if len(tebakan) != digit:  # Kondisional jika tebakan tidak sama dengan dengan digit
            print(f"Bilangan harus {digit} digit.")  # AKan dihandling
        else:
            if SecretNumber != tebakan: # Kondisional untuk menentukan elemen di dua inputan
                for i in range(digit):
                    if SecretNumber[i] == tebakan[i]:
                        sama += 1
                print(f"Ada {sama} bilangan di posisi yang tepat.")
            else:
                break
        nyawa -= 1

# Jika permainan master dan nyawa sudah habis
# Akan dimasukkan ke sini
# Dan juga else di sini untuk tempat akhir dari break
# Setiap algoritma permainan
if nyawa == 0:
    print("Maaf nyawa sudah habis")
else:
    print("Selamat, tebakan benar!!" "(Secret number: " + str(SecretNumber) + ")")
        










    












