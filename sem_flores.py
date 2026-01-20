from planta import Planta

class PlantaSemFlores(Planta):
    def __init__(self, nome, grupo):
        super().__init__(
            nome,
            possui_flores=False,
            possui_sementes=False,
            tipo_reproducao="Esporos"
        )
        self.grupo = grupo

    def exibir_info(self):
        super().exibir_info()
        print(f"Grupo: {self.grupo}")

class Musgo(PlantaSemFlores):
    def __init__(self, nome):
        super().__init__(nome, "Briófita (Musgo)")

class Samambaia(PlantaSemFlores):
    def __init__(self, nome):
        super().__init__(nome, "Pteridófita (Samambaia)")
