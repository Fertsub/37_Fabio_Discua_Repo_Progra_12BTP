import mysql.connector

class MyDatabase:
    def open_conecction(self):
        connection = mysql.connector.connect(host="localhost",
                                            port="3309",
                                            user="root",
                                            passwd="1234",
                                            database="db_cine")
        return connection
    
    def insert_db(self, pelicula, hora, fecha, idioma):
        my_conecction = self.open_conecction()
        cursor = my_conecction.cursor()
        query = "INSERT INTO TBL_Cartelera(PELICULA, HORA, FECHA, IDIOMA) VALUES (%s,%s,%s,%s)"
        data = (pelicula, hora, fecha, idioma)
        cursor.execute(query,data)
        my_conecction.commit()
        my_conecction.close()
                                        