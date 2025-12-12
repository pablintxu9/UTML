from .persona import Persona

def main():
    padre = Persona("Carlos", "García")
    madre = Persona("María", "Santos")
    hijo = Persona("Lucía", "García", "Santos")

    padre.set_conyuge(madre)

    padre.add_hijo(hijo)
    madre.add_hijo(hijo)

    print("Padre:", padre)
    print("  Conyuge:", padre.get_conyuge())
    print("  Hijos:", padre.get_hijos())

    print("Madre:", madre)
    print("  Conyuge:", madre.get_conyuge())
    print("  Hijos:", madre.get_hijos())

    print("Hijo:", hijo)
    print("  Progenitores:", hijo.get_progenitores())

if __name__ == "__main__":
    main()
