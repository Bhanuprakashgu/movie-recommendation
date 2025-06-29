# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built with **Streamlit** that suggests movies similar to a selected one using metadata like cast, crew, genres, and keywords. It uses the TMDB 5000 Movie Dataset from Kaggle for recommendations.

## 📌 Features

- Recommends movies based on content similarity
- Displays posters and basic details using TMDb API
- Clean, interactive UI using Streamlit
- Fast and easy to run locally

## 📚 Dataset

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`
- Combined and preprocessed to extract relevant features (title, genres, cast, crew, keywords)

## 🛠️ Tech Stack

- Python, Pandas, scikit-learn
- Streamlit for UI
- TMDb API for fetching posters
- Pickle for saving similarity matrix

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open your browser:

arduino
Copy
Edit
http://localhost:8501
📁 Project Structure
bash
Copy
Edit
├── app.py                  # Main Streamlit application
├── tmdb_5000_movies.csv    # Movie metadata
├── tmdb_5000_credits.csv   # Cast & crew metadata
├── similarity.pkl          # Precomputed similarity matrix
├── requirements.txt        # Python dependencies
└── utils/                  # Helper functions (optional)
🖼️ Example Output
Recommended movies for Inception:

Interstellar

The Prestige

Tenet

The Matrix

Shutter Island

🙌 Acknowledgements
TMDb for API access

Kaggle for the dataset

