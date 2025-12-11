from actuacion import Actuacion
from tipo_actuacion import TipoActuacion


def main():
    actuacion1 = Actuacion("01/01/2024", "31/01/2024", TipoActuacion.SONDEO)
    actuacion2 = Actuacion("01/02/2024", "31/03/2024", TipoActuacion.EXCAVACION)
    actuacion3 = Actuacion("01/04/2024", "30/04/2024", TipoActuacion.SEGUIMIENTO)
    
    print("=== Actuaciones Arqueológicas ===\n")
    print(actuacion1)
    print(actuacion2)
    print(actuacion3)
    
    print("\n=== Detalles ===")
    print(f"Actuación 1 - Tipo: {actuacion1.tipo.value}, Inicio: {actuacion1.fecha_inicio}, Fin: {actuacion1.fecha_fin}")
    print(f"Actuación 2 - Tipo: {actuacion2.tipo.value}, Inicio: {actuacion2.fecha_inicio}, Fin: {actuacion2.fecha_fin}")
    print(f"Actuación 3 - Tipo: {actuacion3.tipo.value}, Inicio: {actuacion3.fecha_inicio}, Fin: {actuacion3.fecha_fin}")


if __name__ == "__main__":
    main()
