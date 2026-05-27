from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Initialisation de l'API
app = FastAPI()

# Chargement de ton modèle
# Assure-toi que le nom du fichier correspond exactement au tien
model = joblib.load('modele_pokemon.mod')

# Définition du format des données d'entrée
class PokemonData(BaseModel):
    attack: float
    defense: float
    speed: float

@app.post("/predict")
def predict(data: PokemonData):
    # Transformation des données en format attendu par le modèle
    features = [[data.attack, data.defense, data.speed]]
    prediction = model.predict(features)
    return {"victoire_probable": int(prediction[0])}