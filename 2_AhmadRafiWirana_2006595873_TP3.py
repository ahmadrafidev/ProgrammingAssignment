# TERIMA KASIH KEPADA STACK OVERFLOW DAN GOOGLE YANG TELAH BANYAK MEMBANTU
# TERIMA KASIH JUGA KEPADA BHP DAN KAK ASDOS
dict_inventory = {}
set_kategori = set()

def addKategori(namaInventory): 
    '''
        Fungsi ini bertujuan untuk
        menambahkan kategori 
    '''
    if namaInventory in set_kategori:
        print(f"Kategori {namaInventory} sudah ada di dalam sistem")
    else:
        set_kategori.add(namaInventory)
        dict_inventory[namaInventory] = {}
        print(f"Kategori {namaInventory} berhasil ditambahkan")


def add(namaInventory, barang, kuantitas):
    '''
        Fungsi ini bertujuan untuk
        menambahkan barang dan kuantitasnya 
        ke dalam dict_inventory yang berisi kategori
    '''
    if namaInventory not in dict_inventory:
        print(f"Kategori {namaInventory} belum dibuat.")
    elif namaInventory in dict_inventory:
        if barang not in dict_inventory[namaInventory]:
            dict_inventory[namaInventory][barang] = int(kuantitas)
            print(f"Barang {barang} dengan kuantitas {kuantitas} telah dimasukkan ke dalam kategori {namaInventory}")
        else:
            print(f"Tidak dapat menambahkan ke dalam sistem karena barang {barang} sudah ada di dalam kategori {namaInventory}")
                 

def lock(namaInventory, barang):
    '''
        Fungsi ini bertujuan untuk
        me-lock barang
    ''' 
    kunci = dict_inventory[namaInventory]
    kunci[barang] = str(kunci[barang])

    print(f"Barang {barang} pada {namaInventory} berhasil dikunci")


def unlock(namaInventory, barang):
    '''
        Fungsi ini bertujuan untuk
        me-unlock barang
    '''
    kunci = dict_inventory[namaInventory]
    kunci[barang] = int(kunci[barang])
    print(f"Barang {barang} pada {namaInventory} telah berhasil di-unlock")


def search(x, barang): # TInggal bagian ini
    '''
        Fungsi ini bertujuan untuk 
        mencari barang di Dictionary
    '''
    if x[0][0] == barang:
        return x[0]
    elif len(x) == 1:
        return "Barang tidak ditemukan"
    return search(x[1:], barang)


def takeItem(namaInventory, barang, jumlah):
    '''
        Fungsi ini bertujuan untuk
        mengambil item dari Dictionary 
        dan mengurangi valuenya
    '''
    x = dict_inventory[namaInventory]
    if isinstance(x[barang], str):
        print("Barang tidak bisa diambil.")
    else:
        if x[barang] >= jumlah:
            x[barang] = x[barang] - jumlah
            print(f"Berhasil mengambil {barang} pada {namaInventory} dengan jumlah {jumlah}")
            print(f"Barang {barang} memiliki sisa {x[barang]}")
        elif x[barang] == 0:
            print(f"Barang {barang} tidak ditemukan")
        else:
            print(f"Berhasil mengambil {barang} pada {namaInventory} dengan jumlah {x[barang]}")
            x[barang] = 0
            print(f"Barang {barang} pada {namaInventory} dihapus dari sistem karena tidak memiliki stok")
    

def lihatKategori(namaInventory):
    '''
        Fungsi ini bertujuan untuk
        melihat barang per kategori
    '''
    if namaInventory in dict_inventory:
        kategori = dict_inventory[namaInventory]
        for i in kategori:
            print(i, kategori[i])
    else:
        print("Barang tidak ada")
    

def lihatInventory():
    '''
        Fungsi ini bertujuan untuk
        melihat barang semuanya
    '''
    for key, value in dict_inventory.items():
        print(key)
        for j in value:
            print(j, value[j])
        print("=" * 20)


'''
    Di bawah ini adalah Driver code
'''

while True:
    print("\n ### SELAMAT DATANG DI GUDANG ERIGO ###")
    masukkan = input("Masukkan input: ").strip().split()

    try:
        if len(masukkan) == 0: # Handle saat hanya ada spasi saat memasuki inputan
            continue

        if masukkan[0] == "ADD_KATEGORI": # Kondisi untuk memasukkan kategori ke dictionary
            addKategori(masukkan[1])

        elif masukkan[0] == "ADD": # Kondisi untuk memasukkan barang ke dalam kategori
            add(masukkan[1], masukkan[2], masukkan[3])

        elif masukkan[0] == "LOCK": # Kondisi untuk me-lock dictionary
            lock(masukkan[1], masukkan[2])
            
        elif masukkan[0] == "UNLOCK": # Kondisi untuk membuka lock dictionary
            unlock(masukkan[1], masukkan[2])
            
        elif masukkan[0] == "SEARCH":
            x = list(dict_inventory.items())  # Kondisi untuk mencari barang yang dicari di dalam kategori
            rekursi1 = search(x, masukkan[1]) # rekursi satu mencari key di dict awal
            listLagi = list(rekursi1[1].items())
            rekursi2 = search(listLagi, masukkan[2]) # rekursi dua mencari key di dalam key awal dict
            print(f"Barang {rekursi2[0]} ditemukan dengan kuantitas {rekursi2[1]}")
        
        elif masukkan[0] == "TAKE_ITEM": # Kondisi untuk mengambil kuantitas dari barang
            takeItem(masukkan[1], masukkan[2], int(masukkan[3]))
        
        elif masukkan[0] == "LIHAT_PER_KATEGORI": # Kondisi untuk melihat barang per kategori
            lihatKategori(masukkan[1])

        elif masukkan[0] == "LIHAT_INVENTORY": # Kondisi untuk melihat barang keseluruhan
            lihatInventory()
        
        elif masukkan[0] == "EXIT":
            break

    except:
        print("Perintah tidak valid")