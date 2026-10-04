import joblib
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

sentences = [
    "this movie is super good",
    "this movie is very awfully",
    "picture is not bad",
    "fighting scene in this picture is not good",
    "i love this movie",
    "i hate this movie",
    "movie is so awesome",
    "movie has much too filler",
    "movie is so wonderful",
    "this movie is such a tatti",
    "absolutely terrible acting",
    "brilliant story and direction",
    "waste of time and money",
    "highly recommended to everyone",
    "boring plot line and slow pace",
    "a masterpiece of cinematography"
]

labels = [
    "positive", "negative", "positive", "negative",
    "positive", "negative", "positive", "negative",
    "positive", "negative", "negative", "positive",
    "negative", "positive", "negative", "positive"
]

# Pipeline using LogisticRegression with C=1000 for small datasets
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True),
    LogisticRegression(C=1000, max_iter=1000)
)

# Train on full dataset and save
model.fit(sentences, labels)
joblib.dump(model, "model.pkl")
print("Saved model.pkl successfully!")
