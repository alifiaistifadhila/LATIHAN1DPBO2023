from Mahasiswa import Mahasiswa

data = Mahasiswa()

mahasiswaa = []

n = int(input())
for i in range (n):
    nama = str(input())
    nim = str(input())
    prodi = str(input())
    fakultas = str(input())

    mahasiswaa.append(Mahasiswa(nama, nim, prodi, fakultas))

#menampilkan output
i=0
print("DATA MAHASISWA")
print("==============")
for mahasiswa in mahasiswaa:
    print("Mahasiswa ", str(i+1))
    print("Nama             : ", mahasiswa.getNama())
    print("NIM              : ", mahasiswa.getNim())
    print("Program Studi    : ", mahasiswa.getProdi())
    print("Fakultas         : ", mahasiswa.getFakultas())
    i += 1

	