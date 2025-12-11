from persona import Persona


def main():
    kate = Persona("Kate", "Windsor", "Mujer")
    guillermo = Persona("Guillermo", "Windsor", "Hombre")
    diana = Persona("Diana", "Windsor", "Mujer")
    carlos = Persona("Carlos", "Windsor", "Hombre")

    kate.casarse_con(guillermo)
    diana.casarse_con(carlos)
    carlos.agregar_hijo(guillermo)
    diana.agregar_hijo(guillermo)

    print("=== Relaciones Familiares ===\n")

    print(f"{kate} y {guillermo} están casados")
    print(f"  Parejas de {kate}: {[str(p) for p in kate.parejas]}")
    print(f"  Parejas de {guillermo}: {[str(p) for p in guillermo.parejas]}\n")

    print(f"{diana} y {carlos} están casados")
    print(f"  Parejas de {diana}: {[str(p) for p in diana.parejas]}")
    print(f"  Parejas de {carlos}: {[str(p) for p in carlos.parejas]}\n")

    print(f"{guillermo} es hijo de {carlos} y {diana}")
    print(f"  Padres de {guillermo}: {[str(p) for p in guillermo.padres]}")
    print(f"  Hijos de {carlos}: {[str(h) for h in carlos.hijos]}")
    print(f"  Hijos de {diana}: {[str(h) for h in diana.hijos]}")


if __name__ == "__main__":
    main()
