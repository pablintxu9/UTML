from cuadro import Cuadro, Tecnica, Subtecnica, Material, EstadoConservacion
from lugar import Lugar


def main():
    original = Cuadro("La Gioconda", "1503 - 1510", Tecnica.OLEO, Subtecnica.SFUMATO, Material.ALAMO, "Leonardo da Vinci", EstadoConservacion.REGULAR)
    lugar_original = Lugar("Museo del Louvre", "París", "Francia")
    original.set_localiza_en(lugar_original)

    replica = Cuadro("Gioconda (Réplica de El Prado)", "1503 - 1516", Tecnica.OLEO, Subtecnica.PINCELADO_SIMPLE, Material.NOGAL, "Alumno de la escuela de Leonardo", EstadoConservacion.BUENO)
    lugar_replica = Lugar("Museo de El Prado", "Madrid", "España")
    replica.set_localiza_en(lugar_replica)

    replica.set_original(original)

    print("=== Original ===")
    print(f"{original}")
    print(f"Se localiza en: {original.lugar}")
    print(f"Replicas: {[r.titulo for r in original.replicas]}\n")

    print("=== Réplica ===")
    print(f"{replica}")
    print(f"Se localiza en: {replica.lugar}")
    print(f"Original de la réplica: {replica.original.titulo}")


if __name__ == "__main__":
    main()
