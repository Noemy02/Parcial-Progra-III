import crud_academica
db = crud_academica.crud()

class crud_usuarios:
    def consultar_usuarios(self, buscar):
        return db.consultar("select * from usuarios where usuario like'%"+ buscar["buscar"] 
            +"%' or nombre like'%"+ buscar["buscar"] +"%'")
    
    def administrar(self, usuarios):
        if usuarios["accion"] == "nuevo":
            sql = """
                INSERT INTO usuarios (usuario, clave, nombre, direccion, telefono)
                VALUES (%s, %s, %s, %s, %s)
            """
            val = (usuarios["usuario"], usuarios["clave"], usuarios["nombre"],usuarios["direccion"], usuarios["telefono"])
        elif usuarios["accion"] == "modificar":
            sql = """
                UPDATE usuarios
                    SET usuario=%s, clave=%s, nombre=%s, direccion=%s, telefono=%s
                WHERE idUsuario=%s
            """
            val = (usuarios["usuario"], usuarios["clave"], usuarios["nombre"],usuarios["direccion"], usuarios["telefono"], usuarios["idUsuario"])
        elif usuarios["accion"] == "eliminar":
            sql = """
                DELETE FROM usuarios
                WHERE idUsuario=%s
            """
            val = (usuarios["idUsuario"],)
        return db.ejecutar_consultas(sql, val)