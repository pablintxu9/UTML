from persona import Persona
from documento import Documento
from tipo_documento import TipoDocumento
from evento import Evento
from lugar import Lugar
from ocupacion import Ocupacion
from sexo import Sexo

def main():
    lugar_nacimiento = "Toledo"
    lugar_defuncion = "Madrid"

    persona = Persona("Juan", "Gómez", Sexo.MASCULINO, "1950-06-15", lugar_nacimiento, "2020-01-10", lugar_defuncion)

    doc1 = Documento("Historia de España", TipoDocumento.LIBRO, "1995-03-01")
    evento1 = Evento("Congreso de Historia", "2005-09-20", "Reunión de historiadores en Salamanca")
    lugar1 = Lugar("Museo Nacional", "España", "Calle Prado 21")
    ocupacion1 = Ocupacion("Historiador", "1980-01-01", "2015-12-31")

    persona.leer_documento(doc1)
    persona.participar_en_evento(evento1)
    persona.visitar_lugar(lugar1)
    persona.desempenar_ocupacion(ocupacion1)

    contacto = Persona("María", "López", Sexo.FEMENINO, "1955-04-10", "Sevilla")
    persona.contactar_con(contacto)

    print(f"{persona.nombre_dado} {persona.nombre_familia} ({persona.sexo})")
    print(f"Nació en {persona.lugar_nacimiento} el {persona.fecha_nacimiento}")
    if persona.fecha_defuncion:
        print(f"Falleció en {persona.lugar_defuncion} el {persona.fecha_defuncion}")
    print("Documentos leídos:")
    for d in persona.documentos:
        print(f"- {d.titulo} ({d.tipo})")
    print("Eventos:")
    for e in persona.eventos:
        print(f"- {e.nombre} el {e.momento_celebracion}")
    print("Lugares visitados:")
    for l in persona.lugares:
        print(f"- {l.nombre} ({l.pais})")
    print("Ocupaciones:")
    for o in persona.ocupaciones:
        print(f"- {o.nombre} desde {o.desde} hasta {o.hasta or 'actualidad'}")
    print("Contactos:")
    for c in persona.contactos:
        print(f"- {c.nombre_dado} {c.nombre_familia}")

if __name__ == "__main__":
    main()