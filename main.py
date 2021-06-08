from flask import Flask, render_template, url_for, request, redirect
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

import os

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
  
@app.route('/submit', methods=['GET','POST'])
def submit():
  if request.method == 'POST':
        ytlink = request.form['yt link']
        lang = request.form['lang']
        Transcriptions = YouTubeTranscriptApi.get_transcript(ytlink, languages=[lang])
        formatter = TextFormatter()
        text_formatted = formatter.format_transcript(Transcriptions)
        return text_formatted
    else:
        pass 
