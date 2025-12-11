from estructura import Estructura
from material import Material


def main():
    marco = Estructura("M-001", "Siglo X")
    marco.agregar_material(Material.PIEDRA)
    marco.agregar_material(Material.MADERA)

    sub1 = Estructura("S-001", "Siglo XI")
    sub1.agregar_material(Material.MADERA)

    sub2 = Estructura("S-002", "Siglo XII")
    sub2.agregar_material(Material.LADRILLO)

    sub1.set_estructura_marco(marco)
    sub2.set_estructura_marco(marco)

    print("=== Estructura marco ===")
    print(marco)
    print(f"Materiales: {[m.value for m in marco.materiales]}")
    print(f"Subestructuras: {[s.codigo for s in marco.subestructuras]}\n")

    print("=== Subestructura 1 ===")
    print(sub1)
    print(f"Estructura marco: {sub1.estructura_marco.codigo}")
    print(f"Materiales: {[m.value for m in sub1.materiales]}\n")

    print("=== Subestructura 2 ===")
    print(sub2)
    print(f"Estructura marco: {sub2.estructura_marco.codigo}")
    print(f"Materiales: {[m.value for m in sub2.materiales]}")


if __name__ == "__main__":
    main()
