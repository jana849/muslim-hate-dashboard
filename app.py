from flask import Flask, render_template, jsonify
import pandas as pd
import datetime

app = Flask(__name__)

# Sample data to start with
tweets = [
    {"text": "This is a test anti-muslim tweet example", "date": "2026-06-07", "flagged": True},
    {"text": "Muslims are wonderful people", "date": "2026-06-07", "flagged": False},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tweets')
def get_tweets():
    flagged = [t for t in tweets if t['flagged']]
    return jsonify({
        'tweets': flagged,
        'total_flagged': len(flagged),
        'last_updated': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

if __name__ == '__main__':
    app.run(debug=True)