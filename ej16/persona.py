from typing import List, Optional

class Persona:
    def __init__(self,
                 nombre: str,
                 primer_apellido: str,
                 segundo_apellido: Optional[str] = None,
                 fecha_nacimiento: Optional[str] = None,
                 sexo: Optional[str] = None,
                 numero_identificacion: Optional[str] = None):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion

        self.conyuge: Optional["Persona"] = None
        self.hijos: List["Persona"] = []
        self.progenitores: List["Persona"] = []

    def set_conyuge(self, otra: Optional["Persona"]) -> None:
        if otra is self:
            return
        if self.conyuge is otra:
            return
        # Romper enlace previo si existe
        if self.conyuge is not None:
            previo = self.conyuge
            self.conyuge = None
            if previo.conyuge is self:
                previo.conyuge = None
        # Si se pasa None, ya hemos roto la relación
        if otra is None:
            return
        # Establecer relación recíproca
        self.conyuge = otra
        if otra.conyuge is not self:
            otra.set_conyuge(self)

    def add_hijo(self, hijo: "Persona") -> None:
        if hijo not in self.hijos:
            self.hijos.append(hijo)
        if self not in hijo.progenitores:
            hijo.add_progenitor(self)

    def add_progenitor(self, padre: "Persona") -> None:
        if padre is self:
            return
        if padre in self.progenitores:
            return
        if len(self.progenitores) >= 2:
            return
        self.progenitores.append(padre)
        if self not in padre.hijos:
            padre.hijos.append(self)

    def get_hijos(self) -> List["Persona"]:
        return list(self.hijos)

    def get_progenitores(self) -> List["Persona"]:
        return list(self.progenitores)

    def get_conyuge(self) -> Optional["Persona"]:
        return self.conyuge

    def __repr__(self) -> str:
        ap2 = f" {self.segundo_apellido}" if self.segundo_apellido else ""
        return f"Persona({self.nombre} {self.primer_apellido}{ap2})"
