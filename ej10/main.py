from persona import Persona
from proyecto import Proyecto
from lugar import Lugar


def main():
    persona1 = Persona("Juan", "García López", "Arqueólogo")
    persona2 = Persona("María", "Rodríguez Pérez", "Especialista en restauración")
    
    proyecto = Proyecto("Excavación en Atenas", "01/06/2024", "31/08/2024")
    
    lugar1 = Lugar("Acrópolis", 37.9715, 23.7267)
    lugar2 = Lugar("Ágora Antigua", 37.9737, 23.7298)
    
    proyecto.agregar_persona(persona1)
    proyecto.agregar_persona(persona2)
    proyecto.tiene_lugar_en(lugar1)
    proyecto.tiene_lugar_en(lugar2)
    
    print("=== Proyecto Arqueológico ===")
    print(f"Nombre: {proyecto.nombre}")
    print(f"Fecha inicio: {proyecto.fecha_inicio}")
    print(f"Fecha fin: {proyecto.fecha_fin}\n")
    
    print("Personas participantes:")
    for persona in proyecto.personas:
        print(f"  {persona} - Rol: {persona.rol}")
    
    print("\nLugares de actuación:")
    for lugar in proyecto.lugares:
        print(f"  {lugar}")


if __name__ == "__main__":
    main()
