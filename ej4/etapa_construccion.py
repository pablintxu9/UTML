class EtapaConstraccion:
    def __init__(self, numero, fecha_inicio, fecha_fin):
        self.numero = numero
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
    
    def __str__(self):
        return f"Etapa {self.numero} ({self.fecha_inicio} - {self.fecha_fin})"
    
    def __repr__(self):
        return f"EtapaConstraccion({self.numero}, '{self.fecha_inicio}', '{self.fecha_fin}')"
