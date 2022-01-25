import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QMessageBox
from Buku import Buku
from Anggota import Anggota
from Peminjaman import Peminjaman

qtcreator_file  = "peminjaman.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowPeminjaman(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCariKodeBuku1.clicked.connect(self.cari_buku1) 
        self.btnCariKodeBuku2.clicked.connect(self.cari_buku2) 
        self.btnCariKodeBuku3.clicked.connect(self.cari_buku3) 
        self.btnCariKodeAnggota.clicked.connect(self.cari_anggota)
        self.btnCariNomorBukti.clicked.connect(self.cari_peminjaman)
        self.btnSimpan.clicked.connect(self.simpan) 
        self.txtNomorBukti.returnPressed.connect(self.cari_peminjaman) 
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""

    def cari_buku1(self):
        try:
            book = Buku()
            kode = self.txtKodeBuku1.text()
            book.getByKODE_BUKU(kode)
            a = book.affected
            if(a!=0):
                self.txtJudulBuku1.setText(book.judul.strip())                                              
            else:
                self.messagebox("INFO", "Judul Buku tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_buku2(self):
        try:
            book = Buku()
            kode = self.txtKodeBuku2.text()
            book.getByKODE_BUKU(kode)
            a = book.affected
            if(a!=0):
                self.txtJudulBuku2.setText(book.judul.strip())                                              
            else:
                self.messagebox("INFO", "Judul Buku tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_buku3(self):
        try:
            book = Buku()
            kode = self.txtKodeBuku3.text()
            book.getByKODE_BUKU(kode)
            a = book.affected
            if(a!=0):
                self.txtJudulBuku3.setText(book.judul.strip())                                              
            else:
                self.messagebox("INFO", "Judul Buku tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_anggota(self):
        try:           
            kode=self.txtKodeAnggota.text()           
            ang =Anggota()
            # search process
            result = ang.getByKODE_ANGGOTA(kode)           
            a = ang.affected
            
            if(a!=0):
                self.txtNamaAnggota.setText(ang.nama.strip())
            else:
                self.messagebox("INFO", "Data Anggota tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def cari_peminjaman(self):
        try:           
            kode=self.txtNomorBukti.text()           
            pjm =Peminjaman()
            # search process
            result = pjm.getByNOMOR_BUKTI(kode)           
            a = pjm.affected            
            if(a!=0):
                self.edit_mode=True
                self.txtKodeAnggota.setText(pjm.kode_anggota.strip())
                self.cari_anggota()
                self.txtKodeBuku1.setText(pjm.kode_buku1)
                a=self.txtKodeBuku1.text()
                if(a!=""):
                    self.cari_buku1()
                self.txtKodeBuku2.setText(pjm.kode_buku2)
                b = self.txtKodeBuku2.text()
                if(b!=""):
                    self.cari_buku2()
                self.txtKodeBuku3.setText(pjm.kode_buku3)
                c = self.txtKodeBuku3.text()
                if(c!=""):
                    self.cari_buku3()
            else:
                self.edit_mode=False
                self.messagebox("INFO", "Data Peminjaman tidak ditemukan")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtNomorBukti.setText("")
        self.txtKodeAnggota.setText("")
        self.txtNamaAnggota.setText("")
        self.txtKodeBuku1.setText("")
        self.txtJudulBuku1.setText("")
        self.txtKodeBuku2.setText("")
        self.txtJudulBuku2.setText("")
        self.txtKodeBuku3.setText("")
        self.txtJudulBuku3.setText("")

    def simpan(self):
        try:
            pjm = Peminjaman()
            NomorBukti = self.txtNomorBukti.text()
            KodeAnggota = self.txtKodeAnggota.text()
            tglpinjam = self.txtTanggalPinjam.date().toString("yyyy-MM-dd")
            tglhrskembali = self.txtTanggalHarusKembali.date().toString("yyyy-MM-dd")
            kodebuku1 = self.txtKodeBuku1.text()
            kodebuku2 = self.txtKodeBuku2.text()
            kodebuku3 = self.txtKodeBuku3.text()
            if(self.edit_mode==False):
                pjm.nomor_bukti = NomorBukti
                pjm.kode_anggota = KodeAnggota
                pjm.tanggal_pinjam = tglpinjam
                pjm.tanggal_haruskembali = tglhrskembali
                pjm.kode_buku1 = kodebuku1
                pjm.kode_buku2 = kodebuku2
                pjm.kode_buku3 = kodebuku3
                a = pjm.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Peminjaman Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Peminjaman Gagal Tersimpan")               
                self.clear_entry() # Clear Entry Form
            elif(self.edit_mode==True):
                pjm.nomor_bukti = NomorBukti
                pjm.kode_anggota = KodeAnggota
                pjm.tanggal_pinjam = tglpinjam
                pjm.tanggal_haruskembali = tglhrskembali
                pjm.kode_buku1 = kodebuku1
                pjm.kode_buku2 = kodebuku2
                pjm.kode_buku3 = kodebuku3
                a = pjm.updateByNOMOR_BUKTI(NomorBukti)
                if(a>0):
                    self.messagebox("SUKSES", "Data Peminjaman Berhasil Diubah")
                else:
                    self.messagebox("GAGAL", "Data Peminjaman Gagal Diubah")   

                self.clear_entry() # Clear Entry Form
            else:
                self.messagebox("ERROR", "Terjadi kesalahan mode edit")
        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")
    def delete_data(self):
        try:
            pjm = Peminjaman()
            NomorBukti=self.txtNomorBukti.text()
                       
            if(self.edit_mode==True):
                a = pjm.deleteByNOMOR_BUKTI(NomorBukti)
                if(a>0):
                    self.messagebox("SUKSES", "Data Peminjaman Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Peminjaman Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPeminjaman()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowPeminjaman()