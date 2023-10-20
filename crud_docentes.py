import crud_academica
db = crud_academica.crud()

class crud_docentes:
    def consultar_docentes(self, buscar):
        return db.consultar("select * from docentes where codigo like'%"+ buscar["buscar"] 
            +"%' or nombre like'%"+ buscar["buscar"] +"%'")
    
    def administrar(self, docentes):
        if docentes["accion"] == "nuevo":
            sql = """
                INSERT INTO docentes (codigo, nombre, direccion, telefono)
                VALUES (%s, %s, %s, %s)
            """
            val = (docentes["codigo"], docentes["nombre"], docentes["direccion"], docentes["telefono"])
        elif docentes["accion"] == "modificar":
            sql = """
                UPDATE docentes
                    SET codigo=%s, nombre=%s, direccion=%s, telefono=%s
                WHERE idDocente=%s
            """
            val = (docentes["codigo"], docentes["nombre"], docentes["direccion"], docentes["telefono"], docentes["idDocente"])
        elif docentes["accion"] == "eliminar":
            sql = """
                DELETE FROM docentes
                WHERE idDocente=%s
            """
            val = (docentes["idDocente"],)
        return db.ejecutar_consultas(sql, val)