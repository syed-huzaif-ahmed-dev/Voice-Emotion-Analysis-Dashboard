Voice Emotion Analysis Dashboard

This project is a web-based application that analyzes voice recordings and shows how emotions change over time. The main idea is to understand what emotion is expressed in the audio and at which exact time (minute and second) it occurs. The results are shown in a simple and interactive dashboard.

What this application does

The user uploads a voice or audio file in WAV format.  
The audio is broken into small time segments.  
Each segment is analyzed to understand emotional patterns in the voice.  
The detected emotions are mapped to timestamps.  
Charts and tables display how emotions change throughout the audio.

Key features:

Upload voice recordings easily  
Detect emotions from audio  
Track emotion changes over time  
View results on a visual dashboard  
Clear timestamp-based emotion analysis  
Deployed as a live web application

Technologies used:

Python  
Streamlit for the web interface  
Librosa for audio processing  
NumPy and Pandas for data handling  
Matplotlib for charts and visualization

How to run this project locally

Install the required libraries using the requirements file.  
Run the Streamlit application using the command below.

pip install -r requirements.txt  
streamlit run app.py  

After running the command, open the browser and go to:  
http://localhost:8501

Live application

The live deployed version of this project will be added here after deployment.

Use cases

Voice sentiment analysis  
Call center emotion monitoring  
Audio-based AI applications  
Behavioral and emotion analysis projects

Author

Syed Huzaif Ahmed  
B.Tech Student
Passionate in Data Analytics, Machine Learning, and AI 

