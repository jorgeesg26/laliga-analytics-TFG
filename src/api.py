import requests
from src.models import Pokemon, PokemonLegendario

BASE_URL = "https://pokeapi.co/api/v2"

def obtener_pokemon(nombre):
    """Obtiene datos de un Pokémon desde la PokéAPI."""
    nombre = nombre.lower().strip()
    url = f"{BASE_URL}/pokemon/{nombre}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza error si el código HTTP no es 200
        
        data = response.json()
        
        # Extracción de atributos principales
        nombre_pokemon = data.get("name")
        altura = data.get("height")
        peso = data.get("weight")
        tipos = [t["type"]["name"] for t in data.get("types", [])]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data.get("stats", [])}
        
        # Obtener la imagen con el artwork oficial preferentemente
        sprites = data.get("sprites", {})
        official_artwork = sprites.get("other", {}).get("official-artwork", {}).get("front_default")
        imagen = official_artwork if official_artwork else sprites.get("front_default")
        
        # Consultar la especie para saber si es legendario
        es_legendario = False
        url_species = data.get("species", {}).get("url")
        
        if url_species:
            res_species = requests.get(url_species)
            if res_species.status_code == 200:
                species_data = res_species.json()
                es_legendario = species_data.get("is_legendary", False) or species_data.get("is_mythical", False)
                
        # Creación del objeto según su tipo
        if es_legendario:
            return PokemonLegendario(
                nombre=nombre_pokemon,
                tipos=tipos,
                altura=altura,
                peso=peso,
                stats=stats,
                imagen=imagen,
                historia="Pokémon raro y poderoso protegido por las leyendas."
            )
        else:
            return Pokemon(
                nombre=nombre_pokemon,
                tipos=tipos,
                altura=altura,
                peso=peso,
                stats=stats,
                imagen=imagen
            )
            
    except requests.exceptions.RequestException:
        # Manejo de fallas: no encontrado (404) o error de red
        return None
