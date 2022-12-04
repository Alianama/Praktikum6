# Praktikum 6 Fungsi
## Tugas Praktikum
<br/>
Buat program sederhana dengan mengaplikasikan penggunaan fungsi
yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:<br/>
- Fungsi tambah() untuk menambah data<br/>
- Fungsi tapilkan() untuk menampilkan data<br/>
- Fungsi hapus(nama) untuk menghapus data berdasarkan nama<br/>
- Fungsi ubah(nama) untuk mengubah data berdasarkan nama<br/>
- Buat flowchart dan penjelasan programnya pada README.md.<br/>
- Commit dan push repository ke github.

### Source Code 
![Gambar Code](Screnshoot/sscode.png)<br/>

## Penjelasan 

Pertama saya buat dulu dictionary Kosong untuk menampung data <br/>
Seletah itu saya membuat Fungsi def untuk masing masing fungsi<br/>

- Tambah Data
```python
def tambah_data():
    print("|---------------------|")
    print("|Tambah Data Mahasiswa|")
    print("|---------------------|")
    print("\n")
    add_nama = input("Masukan Nama\t\t: ")
    add_nim = int(input("Masukan Nim\t\t: "))
    add_tugas = int(input("Masukan Nilai Tugas\t: "))
    add_uts = int(input("Masukan Nilai UTS\t: "))
    add_uas = int(input("Masukan Nilai UAS\t: "))
    add_akhir = (add_tugas * 30/100) + (add_uts * 35/100) + (add_uas * 35/100)
    data [add_nim] = {'nim' : add_nim, 'nama' : add_nama, 'tugas' : add_tugas, 'uts' : add_uts,'uas' : add_uas, 'akhir' : add_akhir}
```