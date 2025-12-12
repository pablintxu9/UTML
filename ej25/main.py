from iglesia_rural import IglesiaRural
from iglesia_monacal import IglesiaMonacal
from nave import Nave
from ventana_simple import VentanaSimple
from ventana_compleja import VentanaCompleja
from tecnica_cierre_simple import TecnicaCierreSimple
from tecnica_cierre_complejo import TecnicaCierreComplejo
from crucero import Crucero
from tipo_crucero import TipoCrucero
from abside import Abside

def main():
    rural = IglesiaRural("San Pedro")
    rural.asignar_nave(Nave(120))
    rural.agregar_ventana(VentanaSimple("Ventana 1", 1.2, 2.0, True, False, TecnicaCierreSimple.REJA))
    rural.asignar_abside(Abside("Semicircular"))

    monacal = IglesiaMonacal("Santa Clara", "Benedictina")
    monacal.asignar_nave(Nave(200))
    monacal.agregar_ventana(VentanaCompleja("Ventana Gótica", 1.5, 2.5, TecnicaCierreComplejo.VITRAL))
    monacal.asignar_crucero(Crucero(TipoCrucero.CRUZ_LATINA))
    monacal.asignar_abside(Abside("Poligonal"))

    print(f"Iglesia Rural: {rural.nombre}")
    print(f"- Nave: {rural.nave.superficie} m²")
    print(f"- Ventanas: {[v.descripcion for v in rural.ventanas]}")
    print(f"- Ábside: {rural.abside.forma}")
    print()
    print(f"Iglesia Monacal: {monacal.nombre} ({monacal.orden})")
    print(f"- Nave: {monacal.nave.superficie} m²")
    print(f"- Ventanas: {[v.descripcion for v in monacal.ventanas]}")
    print(f"- Crucero: {monacal.crucero.tipo}")
    print(f"- Ábside: {monacal.abside.forma}")

if __name__ == "__main__":
    main()