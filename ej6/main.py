from persona import Persona


def main():
    persona1 = Persona("Juan", "García", "López", "15/03/1990", "Hombre", "12345678A")
    
    print("=== Persona ===")
    print(f"Nombre: {persona1.nombre}")
    print(f"Primer apellido: {persona1.primer_apellido}")
    print(f"Segundo apellido: {persona1.segundo_apellido}")
    print(f"Fecha de nacimiento: {persona1.fecha_nacimiento}")
    print(f"Sexo: {persona1.sexo}")
    print(f"Número de identificación: {persona1.numero_identificacion}")


if __name__ == "__main__":
    main()
