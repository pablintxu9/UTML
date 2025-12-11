class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, sexo, numero_identificacion):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion
    
    def __str__(self):
        return f"{self.nombre} {self.primer_apellido} {self.segundo_apellido}"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', '{self.primer_apellido}', '{self.segundo_apellido}')"
