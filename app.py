import streamlit as st
import tempfile
import os
import subprocess
import librosa
import numpy as np
import pandas as pd
import plotly.express as px
from emotion_model import predict_emotion  # Your pre-trained emotion model

# Streamlit Page Configuration
st.set_page_config(page_title="Voice Emotion Dashboard", layout="wide")
st.title("Voice Emotion & Sentiment Analysis Dashboard")

# File Uploader 
audio_file = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3", "m4a", "ogg", "mpeg"]
)

# ffmpeg Path 
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  

# Helper: Convert any audio to WAV using ffmpeg 
def convert_to_wav_ffmpeg(input_file):

    # Save uploaded file to temp
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(input_file.name)[1]) as temp_input:
        temp_input.write(input_file.read())
        temp_input_path = temp_input.name

    # Create temp output WAV file
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_output_path = temp_output.name

    # FFmpeg command
    cmd = [FFMPEG_PATH, "-y", "-i", temp_input_path, temp_output_path]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        st.error(f"FFMPEG conversion failed:\n{e.stderr.decode()}")
        return None

    return temp_output_path

# Main  Conditions 
if audio_file is not None:
    st.success("Audio file uploaded successfully!")

    # Convert to WAV
    wav_file_path = convert_to_wav_ffmpeg(audio_file)
    if wav_file_path is None:
        st.stop()  # Stop if conversion failed

    # Play audio
    st.audio(wav_file_path)

    # Analyze Audio
    def analyze_audio(file_path):
        y, sr = librosa.load(file_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)

        segment_length = 2 * sr  # 2-second segments
        results = []

        for i in range(0, len(y), segment_length):
            segment = y[i:i + segment_length]
            if len(segment) < segment_length:
                break

            # Extract MFCC features
            mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=13)
            features = np.mean(mfcc, axis=1)

            # Predict emotion
            emotion = predict_emotion(features)

            # Timestamp
            time_stamp = i / sr

            results.append({
                "Time (seconds)": round(time_stamp, 2),
                "Emotion": emotion
            })

        return pd.DataFrame(results)

    # Analyze
    with st.spinner("Analyzing audio..."):
        df = analyze_audio(wav_file_path)

    st.success("Analysis complete!")

    #Display 
    st.subheader("Emotion Timeline")
    st.dataframe(df)

    st.subheader("Emotion Over Time")
    fig = px.scatter(
        df,
        x="Time (seconds)",
        y="Emotion",
        color="Emotion",
        title="Emotion Change Timeline",
        hover_data=["Time (seconds)", "Emotion"]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Emotion Distribution")
    pie = px.pie(
        df,
        names="Emotion",
        title="Emotion Frequency"
    )
    st.plotly_chart(pie, use_container_width=True)
