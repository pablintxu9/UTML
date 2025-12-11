class Circulo:
    def __init__(self, color, diametro):
        self.color = color
        self.diametro = diametro
    
    def __repr__(self):
        return f"Círculo(color='{self.color}', diámetro={self.diametro})"
