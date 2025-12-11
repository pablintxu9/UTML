from cuadro import Cuadro
from tecnica import Tecnica
from material import Material
from subtecnica import Subtecnica
from estado_conservacion import EstadoConservacion


def main():
    cuadro1 = Cuadro("La Noche Estrellada", "1889", "Vincent van Gogh", Subtecnica.PUNTEADO_SIMPLE, Material.LIENZO, "Vincent van Gogh", EstadoConservacion.EXCELENTE)
    cuadro2 = Cuadro("El Grito", "1893", "Edvard Munch", Subtecnica.SFUMATO, Material.LIENZO, "Edvard Munch", EstadoConservacion.BUENO)
    cuadro3 = Cuadro("Retrato de Adele", "1912", "Gustav Klimt", Subtecnica.COLLAGE, Material.LIENZO, "Gustav Klimt", EstadoConservacion.REGULAR)
    
    print("=== Cuadros ===\n")
    
    print(f"Título: {cuadro1.titulo}")
    print(f"Cronología: {cuadro1.cronologia}")
    print(f"Pintor: {cuadro1.pintor}")
    print(f"Sub-técnica: {cuadro1.subtecnica.value}")
    print(f"Material del soporte: {cuadro1.material.value}")
    print(f"Autor: {cuadro1.autor}")
    print(f"Estado de conservación: {cuadro1.estado_conservacion.value}\n")
    
    print(f"Título: {cuadro2.titulo}")
    print(f"Cronología: {cuadro2.cronologia}")
    print(f"Pintor: {cuadro2.pintor}")
    print(f"Sub-técnica: {cuadro2.subtecnica.value}")
    print(f"Material del soporte: {cuadro2.material.value}")
    print(f"Autor: {cuadro2.autor}")
    print(f"Estado de conservación: {cuadro2.estado_conservacion.value}\n")
    
    print(f"Título: {cuadro3.titulo}")
    print(f"Cronología: {cuadro3.cronologia}")
    print(f"Pintor: {cuadro3.pintor}")
    print(f"Sub-técnica: {cuadro3.subtecnica.value}")
    print(f"Material del soporte: {cuadro3.material.value}")
    print(f"Autor: {cuadro3.autor}")
    print(f"Estado de conservación: {cuadro3.estado_conservacion.value}")


if __name__ == "__main__":
    main()
