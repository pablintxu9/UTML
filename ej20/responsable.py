from rol import Rol

class Responsable(Rol):
    def __init__(self, persona, intervencion):
        super().__init__(persona)
        self.intervencion = intervencion