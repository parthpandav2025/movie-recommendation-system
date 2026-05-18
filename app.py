from fastapi import FastAPI
from pydantic import BaseModel
from rapidfuzz import process
import pickle

# Load models
with open("models/movies_model.pkl", "rb") as f:
    movies = pickle.load(f)

with open("models/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Movie dropdown options

movie_names = movies["title"].tolist()

MovieType = str

# Request schema
class Data(BaseModel):
    Movie_name: MovieType

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello..! Welcome To The API Dashboard"
    }

@app.post("/predict")
def predict(data: Data):

    feature_name = data.Movie_name

# Fuzzy matching
    matched_movie = process.extractOne(
        feature_name,
        movie_names
    )

    # Best matched movie name
    best_movie = matched_movie[0]

    # Match confidence
    score = matched_movie[1]

    # Low confidence check
    if score < 60:
        return {
            "error": "Movie not found"
        }
    
    # Find movie index

    index = movies[movies["title"] == best_movie].index[0]

    # Similarity scores
    distance = similarity[index]

    # Top 5 recommendations
    movie_list = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    final_output = []

    for i in movie_list:
        final_output.append(
            movies.iloc[i[0]].title
        )

    return {

        "searched_movie": feature_name,

        "matched_movie": best_movie,

        "match_score": score,

        "recommendations": final_output
    }

