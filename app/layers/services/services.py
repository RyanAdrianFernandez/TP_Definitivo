# capa de servicio/lógica de negocio
import random
from ..transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

# función que devuelve un listado de cards. Cada card representa una imagen de la API de HP.
def getAllImages():
    personajes = transport.getAllImages()
    cards = []
    for personaje in personajes:
        nombre = personaje.get("name")
        imagen = personaje.get("image")
        casa = personaje.get("house")
        actor = personaje.get("actor")
        genero = personaje.get("gender")

    # NOMBRES ALTERNATIVOS

        nombres_alternativos = personaje.get("alternate_names", [])
        if nombres_alternativos:
            nombre_alternativo = random.choice(nombres_alternativos)
        else:
            nombre_alternativo = "No hay nombres alternativos"

    # 3) CREAR LA CARD
        card = {
            "name": nombre,
            "alternate_names": nombre_alternativo,
            "image": imagen,
            "house": casa,
            "actor": actor,
            "gender": genero
            }
        cards.append(card)
    return cards
    # ATENCIÓN: contemplar que los nombres alternativos, para cada personaje, deben elegirse al azar. Si no existen nombres alternativos, debe mostrar un mensaje adecuado.
    pass

# función que filtra según el nombre del personaje.
def filterByCharacter(name):
    filtered_cards = []
    name = name.lower()  

    for card in getAllImages():
        # debe verificar si el name está contenido en el nombre de la card, antes de agregarlo al listado de filtered_cards.
         if name in card["name"].lower():
            filtered_cards.append(card)

    return filtered_cards

# función que filtra las cards según su casa.
def filterByHouse(house_name):
    filtered_cards = []

    for card in getAllImages():
        # debe verificar si la casa de la card coincide con la recibida por parámetro. Si es así, se añade al listado de filtered_cards.
        filtered_cards.append(card)

    return filtered_cards

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request en una Card (ver translator.py)
    fav.user = get_user(request) # le asignamos el usuario correspondiente.

    return repositories.save_favourite(fav) # lo guardamos en la BD.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS Los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # convertimos cada favorito en una Card, y lo almacenamos en el listado de mapped_favourites que luego se retorna.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.delete_favourite(favId) # borramos un favorito por su ID
