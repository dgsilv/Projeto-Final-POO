from planta import Planta

class PlantaComFlores(Planta):
    def __init__(self, nome, grupo, possui_fruto):
        super().__init__(
            nome,
            possui_flores=True,
            possui_sementes=True,
            tipo_reproducao="Sementes"
        )
        self.grupo = grupo
        self.possui_fruto = possui_fruto

    def exibir_info(self):
        super().exibir_info()
        print(f"Grupo: {self.grupo}")
        print(f"Possui frutos: {self.possui_fruto}")

class Gimnosperma(PlantaComFlores):
    def __init__(self, nome):
        super().__init__(nome, "Gimnosperma", possui_fruto=False)

class Angiosperma(PlantaComFlores):
    def __init__(self, nome, tipo):
        super().__init__(nome, "Angiosperma", possui_fruto=True)
        self.tipo = tipo

    def exibir_info(self):
        super().exibir_info()
        print(f"Tipo: {self.tipo}")
