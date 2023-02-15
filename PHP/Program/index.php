<?php

include "Mahasiswa.php";

$data = new mahasiswa();
$data->setNama("Alifia Isti Fadhila");
$data->setNim("1908463");
$data->setProdi("Ilmu Komputer");
$data->setFakultas("Fakultas Pendidkan MIPA");

echo "<b><u>DATA MAHASISWA</u></b>"."<br/>";
echo "<br/>"."<b>Mahasiswa 1</b>"."<br/>";
echo "Nama Lengkap  : ".$data->getNama()."<br/>";
echo "NIM           : ".$data->getNim()."<br/>";
echo "Program Studi : ".$data->getProdi()."<br/>";
echo "Fakultas      : ".$data->getFakultas()."<br/>";

$data2 = new mahasiswa();
$data2->setNama("Riski Fauzi Amelia");
$data2->setNim("2008259");
$data2->setProdi("Pendidikan Guru Sekolah Dasar");
$data2->setFakultas("Fakultas Ilmu Pendidikan");

echo "<br/>"."<b>Mahasiswa 2</b>"."<br/>";
echo "Nama Lengkap  : ".$data2->getNama()."<br/>";
echo "NIM           : ".$data2->getNim()."<br/>";
echo "Program Studi : ".$data2->getProdi()."<br/>";
echo "Fakultas      : ".$data2->getFakultas()."<br/>";

?>