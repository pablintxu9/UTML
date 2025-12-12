from sitio_arqueologico import SitioArqueologico
from excavacion import Excavacion
from objeto_completo import ObjetoCompleto
from fragmento_objeto import FragmentoObjeto
from material import Material
from uso import Uso

def main():
    sitio = SitioArqueologico("Valle Sagrado")
    excavacion = Excavacion("2020-01-01", "2020-03-15")
    sitio.agregar_excavacion(excavacion)

    objeto1 = ObjetoCompleto("OBJ001", "Vasija ceremonial", [Material.CERAMICA], ["Ritual", "Decorativo"], "1200 a.C.", {"altura": 25, "ancho": 15})
    objeto2 = FragmentoObjeto("OBJ002", "Fragmento de cuchillo", [Material.METAL], "1100 a.C.", {"longitud": 8})

    objeto1.agregar_similar(objeto2)
    excavacion.agregar_objeto(objeto1)
    excavacion.agregar_objeto(objeto2)

    print(f"Sitio: {sitio.nombre}")
    for exc in sitio.excavaciones:
        print(f"- Excavación desde {exc.fecha_inicio} hasta {exc.fecha_fin or 'actualidad'}")
        for obj in exc.objetos:
            print(f"  - Objeto: {obj.codigo}, {obj.descripcion}")
            print(f"    - Materiales: {', '.join(obj.materiales)}")
            if obj.dimensiones:
                print(f"    - Dimensiones: {obj.dimensiones}")
            if hasattr(obj, "usos"):
                print(f"    - Usos: {', '.join(obj.usos)}")
            if obj.similares:
                print(f"    - Similares: {[o.codigo for o in obj.similares]}")

if __name__ == "__main__":
    main()