import streamlit as st
import librosa
import numpy as np
import pandas as pd
import plotly.express as px
from emotion_model import predict_emotion

st.set_page_config(page_title="Voice Emotion Dashboard", layout="wide")

st.title("Voice Emotion & Sentiment Analysis Dashboard")

audio_file = st.file_uploader("Upload a WAV audio file", type=["wav"])

def analyze_audio(file):
    y, sr = librosa.load(file, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)

    segment_length = 2 * sr  # 2 seconds
    results = []

    for i in range(0, len(y), segment_length):
        segment = y[i:i + segment_length]
        if len(segment) < segment_length:
            break

        mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=13)
        features = np.mean(mfcc, axis=1)

        emotion = predict_emotion(features)
        time_stamp = i / sr

        results.append({
            "Time (seconds)": round(time_stamp, 2),
            "Emotion": emotion
        })

    return pd.DataFrame(results)

if audio_file:
    with st.spinner("Analyzing audio...."):
        df = analyze_audio(audio_file)

    st.success("Analysis complete \n Below is the Table and the Chart")

    # TABLE
    st.subheader("Emotion Timeline")
    st.dataframe(df)

    # EMOTION CHANGE CHART
    st.subheader("Emotion Over Time")
    fig = px.scatter(
        df,
        x="Time (seconds)",
        y="Emotion",
        color="Emotion",
        title="Emotion Change Timeline"
    )
    st.plotly_chart(fig, use_container_width=True)

    # EMOTION DISTRIBUTION
    st.subheader(" Emotion Distribution")
    pie = px.pie(
        df,
        names="Emotion",
        title="Emotion Frequency"
    )
    st.plotly_chart(pie, use_container_width=True)