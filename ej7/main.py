from proyecto import Proyecto
from miembro import Miembro
from lugar_actuacion import LugarActuacion


def main():
    proyecto = Proyecto("Desarrollo de Software", "01/01/2024", "31/12/2024")
    
    miembro1 = Miembro("Juan", "García López", "Programador")
    miembro2 = Miembro("María", "Rodríguez Pérez", "Diseñadora")
    proyecto.agregar_miembro(miembro1)
    proyecto.agregar_miembro(miembro2)
    
    lugar1 = LugarActuacion("Oficina Principal", 40.4168, -3.7038)
    lugar2 = LugarActuacion("Sede Secundaria", 41.3874, 2.1686)
    proyecto.agregar_lugar(lugar1)
    proyecto.agregar_lugar(lugar2)
    
    print("=== Proyecto ===")
    print(f"Nombre: {proyecto.nombre}")
    print(f"Fecha inicio: {proyecto.fecha_inicio}")
    print(f"Fecha fin: {proyecto.fecha_fin}\n")
    
    print("Miembros del equipo:")
    for miembro in proyecto.miembros:
        print(f"  {miembro} - Rol: {miembro.rol}")
    
    print("\nLugares de actuación:")
    for lugar in proyecto.lugares_actuacion:
        print(f"  {lugar}")


if __name__ == "__main__":
    main()
