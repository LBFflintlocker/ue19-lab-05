
import requests

def obtenir_blague():
    """
    Fonction pour interroger l'API JokeAPI et obtenir une blague aléatoire.
    """
    url = "https://v2.jokeapi.dev/joke/Any"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        donnees_blague = reponse.json()
        if donnees_blague.get("type") == "single":
            return donnees_blague.get("joke")
        elif donnees_blague.get("type") == "twopart":
            return f"{donnees_blague.get('setup')} - {donnees_blague.get('delivery')}"
        else:
            return "Aucune blague trouvée !"
    else:
        return f"Erreur : Impossible de récupérer une blague (Code : {reponse.status_code})"

if __name__ == "__main__":
    print("Récupération d'une blague aléatoire...")
    print(obtenir_blague())

