### Terima kasih kepada Bintang Hari Pratama yang sudah membantu
### Terima kasih kepada Geeks for geeks, Python Docs, Programmiz, Stack Overflow
### Terima kasih juga ke kaka Asdos hehe

import random
import string
import sys


WORDLIST = "rasi bintang.txt"

def loadWords():
    """
    Mengembalikan list kata, setiap kata merupakan string dengan huruf kecil
    """
    print("Memasukkan huruf dari file...")
    inFile = open(WORDLIST, 'r')
    wordList = inFile.read().splitlines()
    print("  ", len(wordList), "words loaded.")
    return wordList

def chooseWords(wordList):
    """    
    Mengembalikan sebuah kata random yang diambil dari wordlist
    """
    return random.choice(wordList)

# End of Helper Code

def warning(sisaPeringatan, userGuessed, duplicateGuess, display):
    """
    Fungsi ini ditujukan untuk
    operasi warning (peringatan)
    """
    sisaPeringatan += 1

    if not userGuessed.isalpha():
        print("Simbol ini tidak diperbolehkan. Kamu kena Peringatan!!" + display)
    elif userGuessed in duplicateGuess:
        print("Kata ini sudah ada! Tebak kata lain! Nyawa kamu berkurang!!!" + display)
    else:
        print("Itu bukan tebakan yang benar! " + display)
    print("-" * 20)
    return sisaPeringatan


def getAvailableWords(lettersGuessed):
    """
        Fungsi ini bertujuan untuk mereturn sisa
        dari list lettersGuessed ketika user memasukkan input
    """
    letters = string.ascii_lowercase # ascii lowercase berfungsi untuk mencetak semua abjad dengan huruf kecil
    unguessed = ""

    for elem in letters:
        if elem not in lettersGuessed:
            unguessed += elem
    return unguessed

def isWordsGuessed(secretWord, lettersGuessed):
    """
        Fungsi boolean yang akan memberikan output True
        jika secretWord (kata yang akan ditebak) ada
        di lettersGuessed (list kata-kata yang sudah ditebak)
    """
    for char in secretWord:
        if (char in lettersGuessed) == False:
            tebakan = False
            break
        else:
            tebakan = True

    return tebakan

def getGuessedWords(secretWord, lettersGuessed):
    """
        Fungsi ini akan mereturn sebuah
        string kata yang sudah ditebak dan
        disimpan di lettersGuessed dalam bentuk
        string, underscores
    """
    kataBenar = []
    guessedString = ""

    for item in lettersGuessed:
        if item in secretWord:
            kataBenar.append(item)

    for char in secretWord:
        if char in kataBenar:
            guessedString += char
        else:
            guessedString += "_ "

    return guessedString


def cekTebakan(jumlahNyawa, userGuessed, duplicateGuess, display):
    """
    Fungsi untuk cek sisa berapa 
    lagi tebakan yang harus dimasukkan
    oleh user
    """
    jumlahNyawa -= 1

    if not userGuessed.isalpha():
        print("Itu bukan masukkan yang valid. Peringatan anda berkurang satu." + display)
    elif userGuessed in duplicateGuess: 
        print('Kata itu sudah pernah ditebak. Nyawa anda hilang satu lagi.' + display)
    else:
        print('Tebakan anda salah!! ' + display)
    print("-" * 20)
    return jumlahNyawa



wordList = loadWords() # List words yang akan ditebak


'''
    Program di bawah ini adalah Driver Code
'''
def hangman(secretWord):
    
    secretWord = chooseWords(wordList).lower()  # Kata yang akan ditebak oleh user
    duplicateGuess = []  # List untuk kata/tebakan yang sama
    lettersGuessed = []  # List untuk tebakan yang berhasil
    gameFinished = False  # Inisiasi looping
    sisaPeringatan = 0  # Inisiasi peringatan 
    display = "_ " * len(secretWord)  # Cetak underscores sesuai dengan secretword

    print("### Selamat datang di game Hangman! ###") # Cetak awalan

    # Cetak berapa jumlah nyawa yang diinginkan
    # Tipe data harus integer
    try:
        jumlahNyawa = int(input("Silakan masukkan jumlah nyawa: "))   
    except ValueError:
        print("Tipe data tidak sesuai. Silakan coba lagi.")   
        sys.exit()
     
    print(f"Panjang kata: {len(secretWord)}" + " huruf") # Cetak panjang kata dari secretWord
    print("-" * 20)

    while not gameFinished:  # Looping
       
        print(f"Sisa nyawa: {jumlahNyawa}") # Cetak sisa nyawa yang dipunya
        hurufTersedia = getAvailableWords(lettersGuessed)  # Mengambil huruf yang tersedia dari ascii lowercase
        print("Huruf yang tersedia: " + str(hurufTersedia)) # Cetak huruf yang tersedia untuk dipakai sebagai tebakan
        userGuessed = input("Masukkan huruf: ").lower() # Input tebakan oleh user

        # Cek apakah inputan hanya abjad
        # Jika di luar abjad maka akan diberi peringatan
        # Ini adalah salah satu fitur warning 
        if not userGuessed.isalpha():
            sisaPeringatan = warning(sisaPeringatan, userGuessed, duplicateGuess, display)
            if sisaPeringatan > 5:
                print("Maaf peringatannya terlalu banyak. Katanya adalah " + secretWord.capitalize())
                gameFinished = True
                  
        else:
            # Cek apakah tebakan sudah di list letterGuessed atau belum
            # jika belum ditambahkan
            if userGuessed not in lettersGuessed:
                lettersGuessed.append(userGuessed)
            
            # Cek jika game sudah berakhir
            # dengan cara mengecek semua inputan sudah sesuai atau belum
            gameOver = isWordsGuessed(secretWord, lettersGuessed)

            # Jika game berakhir maka akan cetak bagian ini
            if gameOver:
                print("Tebakan benar! " + secretWord.capitalize())
                print("-" * 20)
                print("Selamat anda menang!")
                sys.exit()
            
            # Cek apakah kata sudah pernah ditebak atau belum
            # Jika sudah maka akan masuk ke fungsi warning atau cektebakan
            elif userGuessed in duplicateGuess:
                if sisaPeringatan > 0:
                    sisaPeringatan = warning(sisaPeringatan, userGuessed, duplicateGuess, display)
                elif jumlahNyawa > 1:
                    jumlahNyawa = cekTebakan(jumlahNyawa, userGuessed, duplicateGuess, display)
            
            # Cek apakah kata tidak ada di list kata yang duplikat
            # dan juga tebakan dari user sesuai dengan secretword atau tidak
            # Hasil akhirnya ialah untuk mencetak kata yang benar sesuai
            # dengan secretWord
            elif (userGuessed not in duplicateGuess) and userGuessed in secretWord:
                display = getGuessedWords(secretWord, lettersGuessed)
                print("Tebakan benar!" + display)
                print("-" * 20)

            # Cek inputan user yang tidak ada di secretWord
            # Hasilnya adalah nyawa yang berkurang
            # Jika nyawanya sudah 0 atau nyawa < 1
            # Maka program akan berhenti dan user kalah

            elif userGuessed not in secretWord:
                if jumlahNyawa > 1:
                    jumlahNyawa = cekTebakan(jumlahNyawa, userGuessed, duplicateGuess, display)
                else:
                    print("Tebakan anda salah!")
                    print("-" * 20)
                    print("Maaf, nyawa kamu telah habis. Katanya adalah " + secretWord.capitalize() + ".")
                    gameFinished = True

        duplicateGuess.append(userGuessed) # Memasukkan kata ke list kata yang sudah ditebak

        # Fitur jika game sudah kalah
        # Dengan cara nyawa = 0 atau peringatan kebanyakan (lebih dari 5)
        # Maka user akan diberi pilihan untuk lanjut atau tidak
        if (jumlahNyawa == 0) or gameFinished:
            Ngulang = input("Mau lanjut atau tidak? \n 1. Ya \n 2. Tidak \n")
            if Ngulang == "1":
                jumlahNyawa = int(input("Butuh nyawa berapa lagi? "))
                gameFinished = False
            else:
                print("Permainan sudah selesai.")
                gameFinished = True

         
# Kode pemanggilan driver code hangman
if __name__ == "__main__":
    secretWord  = chooseWords(wordList)
    hangman(secretWord)

