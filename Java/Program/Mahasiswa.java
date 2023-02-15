public class Mahasiswa{
	//atribut private
	private String nama;
	private String nim;
	private String prodi;
	private String fakultas;

	//constructor
    public Mahasiswa(){
        this.nama = "";
        this.nim = "";
        this.prodi = "";
        this.fakultas = "";
	}

	//getter dan setter
    public void setNama(String nama){
		this.nama = nama;
	}

	public String getNama(){
		return this.nama;
	}

	public void setNim(String nim){
		this.nim = nim;
	}

	public String getNim(){
		return this.nim;
	}

	public void setProdi(String prodi){
		this.prodi = prodi;
	}

	public String getProdi(){
		return this.prodi;
	}

	public void setFakultas(String fakultas){
		this.fakultas = fakultas;
	}

	public String getFakultas(){
		return this.fakultas;
	}
}