class Persona:
    def __init__(self, nombre_dado, nombre_familia, sexo, fecha_nacimiento, lugar_nacimiento, fecha_defuncion=None, lugar_defuncion=None):
        self.nombre_dado = nombre_dado
        self.nombre_familia = nombre_familia
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_defuncion = fecha_defuncion
        self.lugar_defuncion = lugar_defuncion
        self.documentos = []
        self.eventos = []
        self.lugares = []
        self.ocupaciones = []
        self.contactos = []

    def leer_documento(self, documento):
        self.documentos.append(documento)

    def participar_en_evento(self, evento):
        self.eventos.append(evento)

    def visitar_lugar(self, lugar):
        self.lugares.append(lugar)

    def desempenar_ocupacion(self, ocupacion):
        self.ocupaciones.append(ocupacion)

    def contactar_con(self, otra_persona):
        self.contactos.append(otra_persona)