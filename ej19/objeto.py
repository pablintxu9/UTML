class Objeto:
    def __init__(self, codigo, nombre, autor, fecha_creacion, origen, estado, tematicas, descripcion=None):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.fecha_creacion = fecha_creacion
        self.descripcion = descripcion
        self.origen = origen
        self.estado = estado
        self.tematicas = tematicas
        self.ubicacion = None

    def asignar_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def mostrar(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Autor: {self.autor}")
        print(f"Fecha de creación: {self.fecha_creacion}")
        if self.descripcion:
            print(f"Descripción: {self.descripcion}")
        print(f"Origen: {self.origen}")
        print(f"Estado: {self.estado}")
        print(f"Temáticas: {', '.join(self.tematicas)}")
        if self.ubicacion:
            print(f"Ubicación: {self.ubicacion.codigo}")