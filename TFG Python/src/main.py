import os
import sys
from flask import Flask, render_template, request, redirect, url_for

# Configurar el path para incluir el directorio raíz y permitir importaciones
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from src.api import obtener_pokemon

# Configurar rutas absolutas para templates y static
template_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    """Ruta de inicio. Maneja el formulario de búsqueda de Pokémon."""
    if request.method == "POST":
        nombre = request.form.get("nombre")
        if nombre:
            # Redirigir a la ruta del pokemon específico
            return redirect(url_for("mostrar_pokemon", nombre=nombre))
    return render_template("index.html")

@app.route("/pokemon/<nombre>")
def mostrar_pokemon(nombre):
    """Ruta que muestra la información de un Pokémon buscado."""
    pokemon_obj = obtener_pokemon(nombre)
    
    if pokemon_obj is None:
        # Mostrar vista de error si la API falló o el Pokémon no existe
        return render_template("error.html", mensaje=f"No se encontró el Pokémon '{nombre}'.")
        
    # Extraer los datos mediante el método de la clase POO
    info_pokemon = pokemon_obj.mostrar_info()
    return render_template("pokemon.html", pokemon=info_pokemon)

if __name__ == "__main__":
    # Ejecutar servidor de desarrollo
    app.run(debug=True)
