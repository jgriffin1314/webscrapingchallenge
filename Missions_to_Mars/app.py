from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route('/')
def index():
    marsdb=mongo.db.mars.find_one()
    return render_template("index.html", mars=marsdb)

@app.route('/scrape')
def scrape():
    marsdb=mongo.db.mars
    mars_data=scrape_mars.scrape()
    marsdb.update({}, mars_data, upsert=True)
    return redirect ("/")
    
if __name__ == "__main__":
    app.run(debug=True)