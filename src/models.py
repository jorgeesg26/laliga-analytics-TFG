class Pokemon:
    """Clase base que representa un Pokémon."""
    
    def __init__(self, nombre, tipos, altura, peso, stats, imagen=None):
        self.nombre = nombre
        self.tipos = tipos  # Lista de tipos
        self.altura = altura
        self.peso = peso
        self.stats = stats  # Diccionario con stats
        self.imagen = imagen  # Guardaré la URL de la imagen

    def mostrar_info(self):
        """Devuelve un diccionario con la información básica."""
        return {
            "nombre": self.nombre.capitalize(),
            "tipos": self.tipos,
            "altura": self.altura,
            "peso": self.peso,
            "stats": self.stats,
            "es_legendario": False,
            "imagen": self.imagen
        }


class PokemonLegendario(Pokemon):
    """Clase que representa un Pokémon Legendario, hereda de Pokemon."""
    
    def __init__(self, nombre, tipos, altura, peso, stats, imagen=None, historia="Desconocida"):
        # Llamada al constructor de la clase padre
        super().__init__(nombre, tipos, altura, peso, stats, imagen)
        self.historia = historia
        self.es_legendario = True

    def mostrar_info(self):
        """Sobrescribe el método para incluir datos de legendario."""
        info = super().mostrar_info()
        info["es_legendario"] = self.es_legendario
        info["historia"] = self.historia
        return info
