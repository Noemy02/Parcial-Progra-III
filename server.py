from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
import crud_docentes
import json

crud_docentes = crud_docentes.crud_docentes()
port = 4000

class miServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmdocentes":
            self.path = "docentes.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/frmbusqueda_docentes":
            self.path = "busqueda_docentes.html"
            return SimpleHTTPRequestHandler.do_GET(self)
       
        if self.path=="/docentes":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(crud_docentes.consultar_docentes()).encode('utf-8'))

    def do_POST(self):
        longitud = int(self.headers["Content-Length"])
        datos= self.rfile.read(longitud)
        datos = datos.decode()
        datos = parse.unquote(datos)
        datos = json.loads(datos)
        if self.path=="/docentes":
            resp = {"msg": crud_docentes.administrar(datos)}
        if self.path=="/buscar_docentes":
            resp = crud_docentes.consultar_docentes(datos)
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode())
        
print("Ejecuntando server en puerto ", port)
server = HTTPServer(("localhost", port), miServer)
server.serve_forever()