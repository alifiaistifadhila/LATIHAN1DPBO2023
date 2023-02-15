from Mahasiswa import Mahasiswa

data = Mahasiswa()

mahasiswaa = []

n = int(input())
for i in range (n):
    nama = str(input())
    nim = int(input())
    prodi = str(input())
    fakultas = str(input())

    mahasiswaa.append(Mahasiswa(nama, nim, prodi, fakultas))

#menampilkan output
i=0
print("DATA MAHASISWA")
print("==============")
for mahasiswa in mahasiswaa:
    print("Mahasiswa ", str(i+1))
    print("Nama             : " + str(mahasiswa.getNama()))
    print("NIM              : " + str(mahasiswa.getNim()))
    print("Program Studi    : " + str(mahasiswa.getProdi()))
    print("Fakultas         : " + str(mahasiswa.getFakultas()))
    i += 1
