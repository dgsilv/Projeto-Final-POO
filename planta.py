class Planta:
    def __init__(self, nome, possui_flores, possui_sementes, tipo_reproducao):
        self._nome = nome                      # encapsulamento
        self._possui_flores = possui_flores
        self._possui_sementes = possui_sementes
        self._tipo_reproducao = tipo_reproducao

    def exibir_info(self):
        print(f"Nome: {self._nome}")
        print(f"Possui flores: {self._possui_flores}")
        print(f"Possui sementes: {self._possui_sementes}")
        print(f"Tipo de reprodução: {self._tipo_reproducao}")
