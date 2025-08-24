import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_content():
    with open("content.json") as f:
        return json.load(f)


def recommend_content(user_input, top_n=3):
    content = load_content()
    df = pd.DataFrame(content)

    df["combined"] = df["tags"].apply(lambda x: " ".join(x)) + " " + df["format"] + " " + df["level"]
    user_vector = f"{user_input['goal']} {user_input['preference']} {user_input['level']}"

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(df["combined"].tolist() + [user_vector])
    similarity = cosine_similarity(vectors[-1:], vectors[:-1])

    top_indices = similarity[0].argsort()[-top_n:][::-1]
    recommendations = df.iloc[top_indices]
    return recommendations[["title", "format", "level"]].to_dict(orient="records")
