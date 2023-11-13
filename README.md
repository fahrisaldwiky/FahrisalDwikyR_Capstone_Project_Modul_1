# FahrisalDwikyR_Capstone_Project_Modul_1

Pada program ini merupakan implementasi operasi CRUD (Create, Read, Update, Delete) pada suatu database nilai akademik siswa. Berikut adalah penjelasan setiap fungsi dalam program:

1. **Fungsi `menuread`:**
   - Menampilkan menu untuk melihat data.
   - Jika pengguna memilih opsi 1, fungsi `lihatdata` akan dipanggil untuk menampilkan seluruh data.
   - Jika pengguna memilih opsi selain 1, program akan menanyakan apakah pengguna ingin mencari data spesifik atau keluar.

2. **Fungsi `menutambahdata`:**
   - Menampilkan menu untuk menambahkan data siswa.
   - Jika pengguna memilih opsi 1, program akan meminta input data siswa seperti nama, kelas, NISN, nilai sos, nilai eko, nilai sej, dan nilai geo.
   - Data siswa baru kemudian ditambahkan ke dalam list `listdata`.

3. **Fungsi `menuupdate`:**
   - Menampilkan menu untuk mengupdate data siswa.
   - Jika pengguna memilih opsi 1, program akan meminta nomor unik siswa yang ingin diubah.
   - Setelah itu, program memanggil fungsi `deleteupdate` untuk menampilkan data siswa yang akan diupdate.
   - Pengguna kemudian diminta untuk memilih kolom mana yang ingin diubah (kelas, nama, NISN, nilai ekonomi, nilai sosiologi, nilai sejarah, atau nilai geografi).

4. **Fungsi `menudelete`:**
   - Menampilkan menu untuk menghapus data siswa.
   - Jika pengguna memilih opsi 1, program akan meminta nomor unik siswa yang ingin dihapus.
   - Data siswa kemudian dihapus dari list `listdata`.

5. **Fungsi `kelasinput` dan `nisninput`:**
   - Menerima input kelas (kelasinput) dan NISN (nisninput) sesuai dengan format yang ditentukan.
   
6. **Fungsi `templatestring`, `templatecaridata`, `templatedatatidakada`, `dataada`, `lihatdata`, `datakosong`, `nomoruniksalah`, `deleteupdate`, `datadiupdate`:**
   - Fungsi-fungsi bantuan untuk menampilkan pesan atau informasi tertentu.

7. **Program Utama:**
   - Program utama berjalan dalam loop tak terbatas (`while True`) dan meminta pengguna untuk memilih opsi menu.
   - Program akan terus berjalan sampai pengguna memilih opsi untuk keluar (`pilihanMenu == '5'`).

Program ini dapat digunakan untuk mengelola dan menyimpan data nilai akademik siswa secara sederhana. Seluruh data siswa disimpan dalam list `listdata`, dan pengguna dapat melakukan berbagai operasi terkait data siswa melalui menu yang disediakan.
