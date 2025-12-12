from persona import Persona
from proyecto import Proyecto
from intervencion import Intervencion
from actuacion import Actuacion
from responsable import Responsable
from tecnico import Tecnico

def main():
    proyecto = Proyecto("Restauración del mural")
    intervencion = Intervencion(proyecto)

    actuacion1 = Actuacion("Limpieza de superficie")
    actuacion2 = Actuacion("Reintegración cromática")
    intervencion.agregar_actuacion(actuacion1)
    intervencion.agregar_actuacion(actuacion2)

    persona1 = Persona("Laura")
    persona2 = Persona("Carlos")

    responsable = Responsable(persona1, intervencion)
    tecnico = Tecnico(persona2)
    tecnico.agregar_intervencion(intervencion)

    persona1.asignar_rol(responsable)
    persona2.asignar_rol(tecnico)

    print(f"Proyecto: {intervencion.proyecto.nombre}")
    print("Actuaciones:")
    for act in intervencion.actuaciones:
        print(f"- {act.descripcion}")
    print(f"Responsable: {persona1.nombre}")
    print(f"Técnico: {persona2.nombre}")

if __name__ == "__main__":
    main()