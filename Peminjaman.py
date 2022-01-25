from db import DBConnection as mydb
class Peminjaman:
    def __init__(self):
        self.__idpinjam= None
        self.__nomor_bukti= None
        self.__kode_anggota= None
        self.__tanggal_pinjam= None
        self.__tanggal_haruskembali= None
        self.__tanggal_kembali= None
        self.__kode_buku1= None
        self.__kode_buku2= None
        self.__kode_buku3= None
        self.__sudah_dikembalikan= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idpinjam(self):
        return self.__idpinjam
    
    @property
    def nomor_bukti(self):
        return self.__nomor_bukti

    @nomor_bukti.setter
    def nomor_bukti(self, value):
        self.__nomor_bukti = value
    
    @property
    def kode_anggota(self):
        return self.__kode_anggota

    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    
    @property
    def tanggal_pinjam(self):
        return self.__tanggal_pinjam

    @tanggal_pinjam.setter
    def tanggal_pinjam(self, value):
        self.__tanggal_pinjam = value
    
    @property
    def tanggal_haruskembali(self):
        return self.__tanggal_haruskembali

    @tanggal_haruskembali.setter
    def tanggal_haruskembali(self, value):
        self.__tanggal_haruskembali = value
    
    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali

    @tanggal_kembali.setter
    def tanggal_kembali(self, value):
        self.__tanggal_kembali = value
    
    @property
    def kode_buku1(self):
        return self.__kode_buku1

    @kode_buku1.setter
    def kode_buku1(self, value):
        self.__kode_buku1 = value
    
    @property
    def kode_buku2(self):
        return self.__kode_buku2

    @kode_buku2.setter
    def kode_buku2(self, value):
        self.__kode_buku2 = value
    
    @property
    def kode_buku3(self):
        return self.__kode_buku3

    @kode_buku3.setter
    def kode_buku3(self, value):
        self.__kode_buku3 = value
    
    @property
    def sudah_dikembalikan(self):
        return self.__sudah_dikembalikan

    @sudah_dikembalikan.setter
    def sudah_dikembalikan(self, value):
        self.__sudah_dikembalikan = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__kode_anggota,self.__tanggal_pinjam,self.__tanggal_haruskembali,self.__kode_buku1,self.__kode_buku2,self.__kode_buku3)
        sql="INSERT INTO peminjaman (nomor_bukti,kode_anggota,tanggal_pinjam,tanggal_haruskembali,kode_buku1,kode_buku2,kode_buku3) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__kode_anggota,self.__tanggal_pinjam,self.__tanggal_haruskembali,self.__tanggal_kembali,self.__kode_buku1,self.__kode_buku2,self.__kode_buku3,self.__sudah_dikembalikan, id)
        sql="UPDATE peminjaman SET nomor_bukti=%s, kode_anggota=%s, tanggal_pinjam=%s, tanggal_haruskembali=%s, tanggal_kembali=%s, kode_buku1=%s, kode_buku2=%s, kode_buku3=%s, sudah_dikembalikan=%s WHERE idpinjam=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByNOMOR_BUKTI(self, nomor_bukti):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__kode_anggota,self.__tanggal_pinjam,self.__tanggal_haruskembali,self.__kode_buku1,self.__kode_buku2,self.__kode_buku3, nomor_bukti)
        sql="UPDATE peminjaman SET nomor_bukti=%s, kode_anggota=%s, tanggal_pinjam=%s, tanggal_haruskembali=%s, kode_buku1=%s, kode_buku2=%s, kode_buku3=%s WHERE nomor_bukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE idpinjam='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByNOMOR_BUKTI(self, nomor_bukti):
        self.conn = mydb()
        sql="DELETE FROM peminjaman WHERE nomor_bukti='" + str(nomor_bukti) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE idpinjam='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nomor_bukti = self.result[1]                   
        self.__kode_anggota = self.result[2]                   
        self.__tanggal_pinjam = self.result[3]                   
        self.__tanggal_haruskembali = self.result[4]                   
        self.__tanggal_kembali = self.result[5]                   
        self.__kode_buku1 = self.result[6]                   
        self.__kode_buku2 = self.result[7]                   
        self.__kode_buku3 = self.result[8]                   
        self.__sudah_dikembalikan = self.result[9]                   
        self.conn.disconnect
        return self.result
        
    def getByNOMOR_BUKTI(self, nomor_bukti):
        a=str(nomor_bukti)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM peminjaman WHERE nomor_bukti='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomor_bukti = self.result[1]
            self.__kode_anggota = self.result[2]
            self.__tanggal_pinjam = str(self.result[3])
            self.__tanggal_haruskembali = str(self.result[4])
            self.__tanggal_kembali = str(self.result[5])
            self.__kode_buku1 = self.result[6]
            self.__kode_buku2 = self.result[7]
            self.__kode_buku3 = self.result[8]
            self.__sudah_dikembalikan = str(self.result[9])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomor_bukti = ''                  
            self.__kode_anggota = ''                  
            self.__tanggal_pinjam = ''                  
            self.__tanggal_haruskembali = ''                  
            self.__tanggal_kembali = ''                  
            self.__kode_buku1 = ''                  
            self.__kode_buku2 = ''                  
            self.__kode_buku3 = ''                  
            self.__sudah_dikembalikan = ''                  
            self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM peminjaman"
        self.result = self.conn.findAll(sql)
        return self.result

'''pjm = Peminjaman()
NomorBukti = '12345'
KodeAnggota = '101'
tglpinjam = '2022-01-14'
tglhrskembali = '2022-01-23'
kodebuku1 = '2001'
kodebuku2 = ''
kodebuku3 = ''
pjm.nomor_bukti = NomorBukti
pjm.kode_anggota = KodeAnggota
pjm.tanggal_pinjam = tglpinjam
pjm.tanggal_haruskembali = tglhrskembali
pjm.kode_buku1 = kodebuku1
pjm.kode_buku2 = kodebuku2
pjm.kode_buku3 = kodebuku3
a = pjm.simpan()
print(a)'''