import java.util.Scanner;
import java.util.ArrayList;

public class Main{

    public static void main(String[] args){
        Mahasiswa data = new Mahasiswa();

        int i, n = 0;
        String nama;
        String nim;
        String prodi;
        String fakultas;

        ArrayList<Mahasiswa> list = new ArrayList<>();

        Scanner sc = new Scanner(System.in);

        try{
            n = sc.nextInt();
        }
        catch(Exception e){
            System.out.println("The input is not an integer!");
        }

        //memasukkan inputan
        for(i=0; i<n; i++){
            System.out.println("Masukkan Data Mahasiswa: ");
            nama = sc.next();
            nim = sc.next();
            prodi = sc.next();
            fakultas = sc.next();

            Mahasiswa temp = new Mahasiswa();
            temp.setNama(nama);
            temp.setNim(nim);
            temp.setProdi(prodi);
            temp.setFakultas(fakultas);
            list.add(temp);
        }

        //menampilkan output
        System.out.println("\n" + "DATA MAHASISWA");
        System.out.println("==============");
        for(i=0; i<list.size(); i++){
            System.out.println("Mahasiswa " + Integer.toString(i+1));
            System.out.println("Nama            : " + list.get(i).getNama());
            System.out.println("NIM             : " + list.get(i).getNim());
            System.out.println("Program Studi   : " + list.get(i).getProdi());
            System.out.println("Fakultas        : " + list.get(i).getFakultas() + "\n");
        }

        sc.close();

    }
		
}