class Muestra:
    def __init__(self, fraccion_total, metodo_extraccion):
        self.fraccion_total = fraccion_total
        self.metodo_extraccion = metodo_extraccion

    def mostrar(self):
        print(f"Fracción del total: {self.fraccion_total}")
        print(f"Método de extracción: {self.metodo_extraccion}")