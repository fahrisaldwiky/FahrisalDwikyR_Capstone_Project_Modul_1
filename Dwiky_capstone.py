'''
Fahrisal Dwwiky Rahman
JCDS 0406 
Project Modul 1 : Capstone Project
'''

def menuread():
    while True :
        lihattdata = (input('''
Ingin Lihat Data? [1/Tekan Selain 1]
    1 --------------> Lihat seluruh data
    Tekan Selain 1 -> Cari Data Secara Spesifik atau keluar
    Pilihan anda: '''))
        if lihattdata =='1':
            lihatdata() 
            continue
        else:
            spesifik = input('''Cari Data Secara Spesifik? [1/Tekan Selain 1]
    1 --------------> Cari data secara spesifik
    Tekan Selain 1 -> Ke Menu Utama (Exit) 
    Pilihan anda:''')
            if spesifik == '1':
                if len(listdata) == 0:
                    datakosong()
                else:
                    dataada()
                    dataspesifik = input('''\nMasukkan detail pencarian
    1 -> Berdasarkan Nama
    2 -> Berdasarkan Kelas
    3 -> Berdasarkan NISN
    Pilihan anda:''')
                    if dataspesifik == '1':
                        caridata = input('Masukkan nama yang ingin dicari: ')
                        caridata = caridata.upper()
                        templatecaridata() 
                        x = 0
                        for i in range(len(listdata)):
                            if caridata == listdata[i][1]:
                                x = 1
                                print('Nomor Unik| KelaS | Nama\t| NISN       | Nilai Sosiologi  | Nilai Ekonomi | Nilai Sejarah\t| Nilai Geografi ')
                                print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6])) 
                        if x == 0:
                            templatedatatidakada()     
                    elif dataspesifik == '2':
                        caridata = input('Masukkan kelas yang ingin dicari: ')
                        caridata = caridata.upper()
                        templatecaridata()
                        x = 0
                        for i in range(len(listdata)):
                            if caridata == listdata[i][0]:
                                x += 1
                                if x == 1:
                                    print('Nomor Unik| KelaS | Nama\t| NISN       | Nilai Sosiologi  | Nilai Ekonomi | Nilai Sejarah\t| Nilai Geografi ')
                                print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6]))
                        if x == 0:
                            templatedatatidakada()
                    elif dataspesifik == '3':
                        while True:
                            caridata = input('Masukkan NISN yang ingin dicari: ')
                            w = caridata.isnumeric()
                            if w == True:
                                w = int(caridata)
                                break
                            else :
                                templatestring()
                        templatecaridata()
                        x = 0
                        for i in range(len(listdata)):
                            if w == listdata[i][2]:
                                x += 1
                                if x == 1:
                                    print('Nomor Unik| KelaS | Nama\t| NISN       | Nilai Sosiologi  | Nilai Ekonomi | Nilai Sejarah\t| Nilai Geografi ')
                                print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6]))
                        if x == 0:
                            templatedatatidakada()
            else:
                yakin = input('''
Anda yakin tidak ingin mencari data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Pencarian
    Pilihan anda: ''')
                if yakin == '1':
                    break   
            continue
def menutambahdata():
    while True :
        lihatdata()
        tambahdata = (input('''Ingin tambahkan data? [1/Tekan Selain 1]
    1 --------------> Lanjut tambah data
    Tekan Selain 1 -> Ke menu proceed (Exit)
    Pilihan anda: '''))
        if tambahdata == '1':
            if len(listdata) == 0:
                nama = (input('Masukkan Nama Siswa : '))
                nama = nama.upper()
                kelas = kelasinput(1)
                nisn = nisninput(10)
                sos = (input('Masukkan Nilai Ekonomi {}: '.format(nama)))
                eko = (input('Masukkan Nilai Sosiologi {}: '.format(nama)))
                sej = (input('Masukkan Nilai Sejarah {}: '.format(nama)))
                geo = (input('Masukkan Nilai Geografi {}: '.format(nama)))
                simpan = input('''
Apakah data sudah benar dan ingin disimpan? [1/Tekan Selain 1]
    1 --------------> Simpan Data
    Tekan Selain 1 -> Kembali ke Menu Tambah Data
    Pilihan anda: ''')
                if simpan == '1':
                    listdata.append([kelas,nama,nisn,sos,eko,sej,geo])
                    print('\nData Tersimpan\n')
                else:
                    continue
            else:
                x = 0
                nama = (input('Masukkan Nama Siswa : '))
                nama = nama.upper()
                for i in range(len(listdata)):
                    if listdata[i][1] == nama:
                        # jika nama sama
                        x = 1
                        # x menjadi 1
                    else:
                        continue
                if x == 1:
                    print('''
Nama sudah ada di dalam Database
''')
                else:
                    kelas = kelasinput(1)
                    nisn = nisninput(10)
                    sos = (input('Masukkan Nilai Ekonomi {}: '.format(nama)))
                    eko = (input('Masukkan Nilai Sosiologi {}: '.format(nama)))
                    sej = (input('Masukkan Nilai Sejarah {}: '.format(nama)))
                    geo = (input('Masukkan Nilai Geografi {}: '.format(nama)))
                    simpan = input('''
Apakah data sudah benar dan ingin disimpan? [1/Tekan Selain 1]
    1 --------------> Simpan Data
    Tekan Selain 1 -> Kembali ke Menu Tambah Data
    Pilihan anda: ''')
                    if simpan == '1':
                        listdata.append([kelas,nama,nisn,sos,eko,sej,geo])
                        print('\nData Tersimpan\n')
        else:
            yakin = input('''Anda yakin tidak ingin menambahkan data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Tambah Data
    Pilihan anda: ''')
            if yakin == '1':
                break
        continue
def menuupdate():
    while True :
        if len(listdata) == 0:
            datakosong()
            break
        elif len(listdata)>0:
            dataada()
        updatedata = (input('''
Ingin update data? [1/Tekan Selain 1]
    1 --------------> Lanjut update
    Tekan Selain 1 -> Ke Menu Proceed (Exit)
    Pilihan anda: '''))
        if updatedata == '1':
            while True:
                nomorunik = input('Masukkan Nomor Unik siswa yang ingin diubah: ')
                q = nomorunik.isnumeric()
                if q == True:
                    q = int(nomorunik)
                    break
                else :
                    templatestring()
            if 1 <= q <= len(listdata):
                global j 
                j = q
                deleteupdate(j)
                updatedata = (input('''
Lanjut update data? [1/Tekan Selain 1]
    1 --------------> Lanjut ke input perubahan data
    Tekan Selain 1 -> Kembali ke Menu Update
    Pilihan anda: '''))
                if updatedata == '1':
                    datadiupdate()
                else:
                    continue
            else :
                nomoruniksalah()
                continue
        else:
            yakin = input('''
Anda yakin tidak ingin update data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Update
    Pilihan anda: ''')
            if yakin == '1': 
                break
        continue
def menudelete():
    while True :
        if len(listdata) == 0:
            datakosong()
            break
        elif len(listdata)>0:
            dataada()
        delettedata = (input('''
Ingin delete data? [1/Tekan Selain 1]
    1 --------------> Lanjut Delete
    Tekan Selain 1 -> Ke Menu Proceed (Exit)
    Pilihan anda: '''))
        if delettedata == '1':
            while True:
                nomorunik = input('Masukkan Nomor Unik siswa yang ingin dihapus: ')
                e = nomorunik.isnumeric()
                if e == True:
                    e = int(nomorunik)
                    break
                else:
                    templatestring()
            if 1 <= e <= len(listdata):
                global j
                j = e
                deleteupdate(j)
                delettedata = (input('''
Lanjut delete data? [1/Tekan Selain 1]
    1 --------------> Data akan dihapus
    Tekan Selain 1 -> Kembali ke Menu Delete
    Pilihan anda: '''))
                if delettedata == '1':
                    del listdata[j-1]
                    print('''
    DATA YANG DIPILIH SUDAH DIHAPUS!!
    ''')
                else :
                    continue    
            else :
                nomoruniksalah()
                continue
        else:
            yakin = input('''
Anda yakin tidak ingin mendelete data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Delete
    Pilihan anda: ''')
            if yakin == '1':
                break
        continue  
def kelasinput(digit):
    while True:
        while True:
            kelas = input('Masukkan Kelas Siswa (1 Huruf A - Z): ')
            t = kelas.isnumeric()
            if t == False:
                break
            else:
                print('''
         JANGAN MASUKKAN ANGKA!!!
    ''')
        kelas = kelas.upper()
        if len(kelas) == digit:
            return kelas
        else:
            print('''
        MASUKKAN HANYA 1 HURUF !!
    ''')
def nisninput(digit):
     while True:
        while True:
            nisn = input('Masukkan Nomor NISN Siswa (10 Digit): ')
            r = nisn.isnumeric()
            if r == True:
                r = int(nisn)
                break
            else:
                templatestring()
        number = r
        count = 0
        while(number != 0):
            number //= 10
            count += 1
        if count == digit:
            return r
        else:
            print('''
       MASUKKAN HANYA 10 DIGIT !!!
    ''')
def templatestring():
    print('''
        JANGAN MASUKKAN STRING !!
    ''')
def templatecaridata():
    print('''
        Berikut data yang dicari :
    ''')
def templatedatatidakada():
    print('''
          Data tidak ditemukan
    ''')  
def dataada():
    print('\nDaftar Nilai Siswa\n')
    print('Nomor Unik| Kelas | Nama\t| NISN       | Nilai Sosiologi  | Nilai Ekonomi | Nilai Sejarah\t| Nilai Geografi ')
    for i in range(len(listdata)) :
        print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6]))
def lihatdata():
    
    if len(listdata) == 0:
        print('''
        DATA MASIH KOSONG
    ''')   
    elif len(listdata)>0:
        dataada()
def datakosong():
    print('''
    DATA KOSONG!! TAMBAH DATA SISWA TERLEBIH DAHULU
    ''')
def nomoruniksalah():
    print('''
    Nomor Unik yang dimasukkan tidak ditemukan!!
    ''')
def deleteupdate(j):
    print('\nDaftar Nilai Siswa\n')
    print('Nomor Unik| Kelas | Nama\t| NISN       | Nilai Sosiologi  | Nilai Ekonomi | Nilai Sejarah\t| Nilai Geografi ')
    print('{}\t  | {}     | {}\t| {} | {}  \t| {}  \t| {}  \t| {}'.format(j,listdata[j-1][0],listdata[j-1][1],listdata[j-1][2],listdata[j-1][3],listdata[j-1][4],listdata[j-1][5],listdata[j-1][6])) 
def datadiupdate():
    while True:
        while True:
            kolompilih = input('''
Pilih nomor kolom yang ingin di update [KELAS = 0 / NAMA = 1 / NISN = 2 / EKONOMI = 3 / SOSIOLOGI = 4 / SEJARAH = 5 / GEOGRAFI = 6]
: ''')
            t = kolompilih.isnumeric()
            if t == True:
                t = int(kolompilih)
                break
            else:
                templatestring()
        if t == 0:
            kolombaru = kelasinput(1)
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
                break
            else:
                break
        elif t == 1:
            kolombaru = input('Silahkan masukkan nama baru: ')
            kolombaru = kolombaru.upper()
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 2:
            kolombaru = nisninput(10)
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 3:
            kolombaru = input('Silahkan masukkan nilai ekonomi baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break 
        elif t == 4:
            kolombaru = input('Silahkan masukkan nilai sosiologi baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 5:
            kolombaru = input('Silahkan masukkan nilai sejarah baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 6:
            kolombaru = input('Silahkan masukkan nilai geografi baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        else:
            print('''
                Nomor Kolom yang dimasukkan tidak ditemukan!!
                ''')
            continue
        break
listdata = []

listdata.append(['A', 'DIAN SASTRO', 1235647845, 85, 90, 78, 92])
listdata.append(['B', 'PEVITA ', 2344675851, 78, 88, 92, 85])
listdata.append(['C', 'TATJHANA ', 7937487012, 92, 85, 88, 90])

while True:
    pilihanMenu = input('''
        Selamat Datang di Database Nilai Akademik
        List Menu :
        1. Menampilkan Daftar Nilai Kelas
        2. Menambah Nilai Siswa
        3. Mengupdate Nilai Siswa
        4. Menghapus Nilai Siswa
        5. Exit Program
        Masukkan Angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu ==   '1') :
        menuread()
    elif(pilihanMenu == '2') :
        menutambahdata() 
    elif(pilihanMenu == '3') :
        menuupdate() 
    elif(pilihanMenu == '4') :
        menudelete() 
    elif(pilihanMenu == '5') :
        break
