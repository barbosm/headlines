import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {
            'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'slash': 'http://rss.slashdot.org/Slashdot/slashdotMain', 
            }


@app.route('/')

@app.route('/<publication>')

def get_news():
    query = request.args.get('publication')
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template('home.html',
                            articles=feed['entries'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)