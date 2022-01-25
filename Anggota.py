from db import DBConnection as mydb
class Anggota:
    def __init__(self):
        self.__idanggota= None
        self.__kode_anggota= None
        self.__nama= None
        self.__jk= None
        self.__email= None
        self.__telpon= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idanggota(self):
        return self.__idanggota
    
    @property
    def kode_anggota(self):
        return self.__kode_anggota

    @kode_anggota.setter
    def nim(self, value):
        self.__kode_anggota = value
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nim(self, value):
        self.__nama = value
    
    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def nim(self, value):
        self.__jk = value
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def nim(self, value):
        self.__email = value
    
    @property
    def telpon(self):
        return self.__telpon

    @telpon.setter
    def nim(self, value):
        self.__telpon = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_anggota,self.__nama,self.__jk,self.__email,self.__telpon)
        sql="INSERT INTO anggota (kode_anggota,nama,jk,email,telpon) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_anggota,self.__nama,self.__jk,self.__email,self.__telpon, id)
        sql="UPDATE anggota SET kode_anggota=%s, nama=%s, jk=%s, email=%s, telpon=%s WHERE idanggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateByKODE_ANGGOTA(self, kode_anggota):
        self.conn = mydb()
        val = (self.__kode_anggota,self.__nama,self.__jk,self.__email,self.__telpon, kode_anggota)
        sql="UPDATE mahasiswa SET kode_anggota=%s, nama=%s, jk=%s, email=%s, telpon=%s WHERE kode_anggota=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE idanggota='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteByKODE_ANGGOTA(self, kode_anggota):
        self.conn = mydb()
        sql="DELETE FROM anggota WHERE kode_anggota='" + str(kode_anggota) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE idanggota='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_anggota = self.result[1]                   
        self.__nama = self.result[2]                   
        self.__jk = self.result[3]                   
        self.__email = self.result[4]                   
        self.__telpon = self.result[5]                   
        self.conn.disconnect
        return self.result
        
    def getByKODE_ANGGOTA(self, kode_anggota):
        a=str(kode_anggota)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM anggota WHERE kode_anggota='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_anggota = self.result[1]
            self.__nama = self.result[2]
            self.__jk = str(self.result[3])
            self.__email = self.result[4]
            self.__telpon = self.result[5]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_anggota = ''                  
            self.__nama = ''                  
            self.__jk = ''                  
            self.__email = ''                  
            self.__telpon = ''                  
            self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM anggota"
        self.result = self.conn.findAll(sql)
        return self.result