<?php

class Mahasiswa{

	private $nama = '';
	private $nim = '';
	private $prodi = '';
	private $fakultas = '';

	public function __construct($nama = '', $nim = '', $prodi = '', $fakultas = ''){
	}

	public function setNama($nama)
	{
		$this->nama = $nama;
	}

	public function getNama()
	{
		return $this->nama;
	}

	public function setNim($nim)
	{
		$this->nim = $nim;
	}

	public function getNim()
	{
		return $this->nim;
	}

	public function setProdi($prodi)
	{
		$this->prodi = $prodi;
	}

	public function getProdi()
	{
		return $this->prodi;
	}

	public function setFakultas($fakultas)
	{
		$this->fakultas = $fakultas;
	}

	public function getFakultas()
	{
		return $this->fakultas;
	}

}

?>