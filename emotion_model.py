import numpy as np

# Simulated emotion classifier
EMOTIONS = ["Neutral", "Happy", "Sad", "Angry", "Fear"]

def predict_emotion(features):
    return np.random.choice(EMOTIONS)