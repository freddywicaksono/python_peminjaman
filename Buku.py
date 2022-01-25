from db import DBConnection as mydb
class Buku:
    def __init__(self):
        self.__idbuku= None
        self.__kode_buku= None
        self.__idkategori= None
        self.__judul= None
        self.__pengarang= None
        self.__idpenerbit= None
        self.__tahun= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idbuku(self):
        return self.__idbuku
    
    @property
    def kode_buku(self):
        return self.__kode_buku

    @kode_buku.setter
    def nim(self, value):
        self.__kode_buku = value
    
    @property
    def idkategori(self):
        return self.__idkategori

    @idkategori.setter
    def nim(self, value):
        self.__idkategori = value
    
    @property
    def judul(self):
        return self.__judul

    @judul.setter
    def nim(self, value):
        self.__judul = value
    
    @property
    def pengarang(self):
        return self.__pengarang

    @pengarang.setter
    def nim(self, value):
        self.__pengarang = value
    
    @property
    def idpenerbit(self):
        return self.__idpenerbit

    @idpenerbit.setter
    def nim(self, value):
        self.__idpenerbit = value
    
    @property
    def tahun(self):
        return self.__tahun

    @tahun.setter
    def nim(self, value):
        self.__tahun = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_buku,self.__idkategori,self.__judul,self.__pengarang,self.__idpenerbit,self.__tahun)
        sql="INSERT INTO buku (kode_buku,idkategori,judul,pengarang,idpenerbit,tahun) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_buku,self.__idkategori,self.__judul,self.__pengarang,self.__idpenerbit,self.__tahun, id)
        sql="UPDATE buku SET kode_buku=%s, idkategori=%s, judul=%s, pengarang=%s, idpenerbit=%s, tahun=%s WHERE idbuku=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByKODE_BUKU(self, kode_buku):
        self.conn = mydb()
        val = (self.__kode_buku,self.__idkategori,self.__judul,self.__pengarang,self.__idpenerbit,self.__tahun, kode_buku)
        sql="UPDATE mahasiswa SET kode_buku=%s, idkategori=%s, judul=%s, pengarang=%s, idpenerbit=%s, tahun=%s WHERE kode_buku=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM buku WHERE idbuku='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByKODE_BUKU(self, kode_buku):
        self.conn = mydb()
        sql="DELETE FROM buku WHERE kode_buku='" + str(kode_buku) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM buku WHERE idbuku='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_buku = self.result[1]                   
        self.__idkategori = self.result[2]                   
        self.__judul = self.result[3]                   
        self.__pengarang = self.result[4]                   
        self.__idpenerbit = self.result[5]                   
        self.__tahun = self.result[6]                   
        self.conn.disconnect
        return self.result
        
    def getByKODE_BUKU(self, kode_buku):
        a=str(kode_buku)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM buku WHERE kode_buku='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_buku = self.result[1]
            self.__idkategori = str(self.result[2])
            self.__judul = self.result[3]
            self.__pengarang = self.result[4]
            self.__idpenerbit = str(self.result[5])
            self.__tahun = str(self.result[6])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_buku = ''                  
            self.__idkategori = ''                  
            self.__judul = ''                  
            self.__pengarang = ''                  
            self.__idpenerbit = ''                  
            self.__tahun = ''                  
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM buku"
        self.result = self.conn.findAll(sql)
        return self.result