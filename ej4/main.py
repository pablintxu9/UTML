from catedral import Catedral
from lugar import Lugar
from etapa_construccion import EtapaConstraccion


def main():
    catedral = Catedral("Catedral de Santiago de Compostela", "Católico", 1075, 1128, "3 de abril de 1211", 1896, "Granito", "Románico, Gótico, Barroco, Plateresco, Neoclásico")
    santiago = Lugar("Santiago de Compostela", "Galicia", "España")
    catedral.set_encuentra_en(santiago)
    
    etapa1 = EtapaConstraccion(1, 1075, 1122)
    etapa2 = EtapaConstraccion(2, 1168, "nulo")
    catedral.agregar_etapa(etapa1)
    catedral.agregar_etapa(etapa2)
    
    print("=== Catedral de Santiago de Compostela ===")
    print(f"Nombre: {catedral.nombre}")
    print(f"Culto: {catedral.culto}")
    print(f"Año inicio construcción: {catedral.anno_inicio}")
    print(f"Fecha primera consagración: {catedral.fecha_primera}")
    print(f"Fecha segunda consagración: {catedral.fecha_segunda}")
    print(f"Fecha declaración BIC: {catedral.fecha_bic}")
    print(f"Material: {catedral.material}")
    print(f"Estilos: {catedral.estilos}")
    print(f"Se encuentra en: {catedral.lugar}\n")
    
    print("Etapas de construcción:")
    for etapa in catedral.etapas_construccion:
        print(f"  {etapa}")


if __name__ == "__main__":
    main()
