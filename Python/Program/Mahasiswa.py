class Mahasiswa:

	__nama = ""
	__nim = 0
	__prodi = ""
	__fakultas = ""
	
	def __init__(self, nama = 0, nim = "", prodi = "", fakultas = ""):
		self.__nama = nama
		self.__nim = nim
		self.__prodi = prodi
		self.__fakultas = fakultas

	#getter dan setter
	def setNama(self, nama):
		self.__nama = nama

	def getNama(self):
		return self.__nama

	def setNim(self, nim):
		self.__nim = nim

	def getNim(self):
		return self.__nim

	def setProdi(self, prodi):
		self.__prodi = prodi

	def getProdi(self):
		return self.__prodi

	def setFakultas(self, fakultas):
		self.__fakultas = fakultas

	def getFakultas(self):
		return self.__fakultas