from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
import crud_usuarios
import json

crud_usuarios = crud_usuarios.crud_usuarios()
port = 3000

class miServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmusuarios":
            self.path = "usuarios.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmbusqueda_usuarios":
            self.path = "busqueda_usuarios.html"
            return SimpleHTTPRequestHandler.do_GET(self)
       
        if self.path=="/usuarios":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(crud_usuarios.consultar_usuarios()).encode('utf-8'))

    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        datos= self.rfile.read(longitud)
        datos = datos.decode()
        datos = parse.unquote(datos)
        datos = json.loads(datos)
        if self.path=="/usuarios":
            resp = {"msg": crud_usuarios.administrar(datos)}
        if self.path=="/buscar_usuarios":
            resp = crud_usuarios.consultar_usuarios(datos)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode())
        
print("Ejecuntando server en puerto ", port)
server = HTTPServer(("localhost", port), miServer)
server.serve_forever()