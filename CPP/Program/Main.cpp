#include <bits/stdc++.h>
#include "Mahasiswa.cpp"

using namespace std;

int main(){
	Mahasiswa data;

    //meminta inputan dari user
    int i, n = 0;
    string nama;
	string nim;
	string prodi;
	string fakultas;

    //membuat list untuk inputan
    list<Mahasiswa> llist;
    cin >> n;
    for(i=0; i<n; i++){
        Mahasiswa temp;
        cout << "Masukkan Data Mahasiswa: " << '\n';
        cin >> nama >> nim >> prodi >> fakultas;

        temp.setNama(nama);
        temp.setNim(nim);
        temp.setProdi(prodi);
        temp.setFakultas(fakultas);

        llist.push_back(temp);
    }

    //menampilkan output
    cout << '\n' << "DATA MAHASISWA " << '\n';
    cout << "==============" << '\n';
    i=0;
    for(list<Mahasiswa>::iterator it = llist.begin(); it != llist.end(); it++){
        cout << "Mahasiswa " << (i+1) << '\n';
        cout << "Nama           : " << it->getNama() << '\n';
        cout << "NIM            : " << it->getNim() << '\n';
        cout << "Program Studi  : " << it->getProdi() << '\n';
        cout << "Fakultas       : " << it->getFakultas() << "\n\n";
        i++;
    }
    
	return 0;	
}