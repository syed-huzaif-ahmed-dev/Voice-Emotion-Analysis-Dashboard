Voice Emotion Analysis Dashboard

The Voice Emotion Analysis Dashboard is a web-based application that analyzes voice recordings and visualizes how emotions change over time.
The goal of this project is to identify what emotion is present in an audio recording and exactly when it occurs (minute and second), and present the results through a clean, interactive dashboard.
This project combines audio processing, data analysis, and visualization to demonstrate a practical AI/ML use case.

 Live Demo

Try the live application here:
https://voice-emotion-analysis-dashboard-dqshcrdfyswubibcm2bkbs.streamlit.app/

What the application does:

Allows users to upload a voice or audio file in WAV format
Splits the audio into small time segments
Analyzes each segment to detect emotional patterns in the voice
Maps detected emotions to precise timestamps
Displays emotion changes using interactive charts and tables

Key Features:

Easy audio upload
Emotion detection from voice recordings
Timestamp-based emotion tracking
Interactive and visual dashboard
Clear representation of emotion changes over time
Deployed as a live web application using Streamlit Cloud

Technologies Used:
 
Python
Streamlit – Web application framework
Librosa – Audio processing and feature extraction
NumPy & Pandas – Data handling and analysis
Matplotlib – Data visualization 

Note: ffmpeg must be installed locally.
- On Windows, set FFMPEG_PATH in app.py to the location of ffmpeg.exe.
- On Linux/Cloud, ffmpeg can be installed via system package manager (e.g., apt).


👤 Author

Syed Huzaif Ahmed
B.Tech Student
Passionate about Data Analytics, Machine Learning, and AI


