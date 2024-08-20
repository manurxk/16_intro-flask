import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=postgres host=localhost password=1873")

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con