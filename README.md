# 🎬 Movie Recommendation System API

A FastAPI-based movie recommendation system that suggests similar movies using content-based filtering, cosine similarity, and fuzzy matching.

---

# 🚀 Features

- Movie recommendation using ML
- Content-based filtering
- Cosine similarity algorithm
- Fuzzy search with RapidFuzz
- FastAPI REST API
- JSON response support
- Handles wrong movie spellings

---

# 🛠️ Technologies Used

- Python
- FastAPI
- Pandas
- Scikit-learn
- RapidFuzz
- Pickle

---

# 📂 Project Structure

```bash
movie-recommendation-system/
│
├── models/
│   ├── movies_model.pkl
│   └── similarity.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

```bash
git clone https://github.com/parthpandav2025/movie-recommendation-system.git

run the code :--

pip install -r requirements.txt
```

---

# ▶️ Run The API

```bash
python -m uvicorn app:app --reload
```

Server will start on:

```bash
http://127.0.0.1:8000
```

---

# 📌 API Endpoints

## Home Endpoint

```bash
GET /
```

### Response

```json
{
  "message": "Hello..! Welcome To The API Dashboard"
}
```

---

## Movie Recommendation Endpoint

```bash
POST /predict
```

### Request Body

```json
{
  "Movie_name": "Avatar"
}
```

### Response

```json
{
  "searched_movie": "Avatar",
  "matched_movie": "Avatar",
  "match_score": 100,
  "recommendations": [
    "Aliens vs Predator: Requiem",
    "Aliens",
    "Falcon Rising",
    "Independence Day",
    "Titan A.E."
  ]
}
```

---

# 🧠 How It Works

1. User enters a movie name
2. RapidFuzz performs fuzzy matching
3. Best matched movie is selected
4. Cosine similarity scores are calculated
5. Top 5 similar movies are returned

---


# 👨‍💻 Author

Parthkumar Pandav

---

# ⭐ Give a Star

If you like this project, give it a ⭐ on GitHub.