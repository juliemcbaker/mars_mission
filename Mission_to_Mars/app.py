from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
## import pymongo
import scrape_mars

################################################################
##          FLASK SETUP
################################################################
app = Flask(__name__)

################################
# PYMONGO SETUP
#################################
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
#     # define the database in Mongo
# db = client.mars_db
# mars_collection = db.mars

app.config["MONGO_URI"] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app) 
#############################################################
##  FLASK ROUTES
############################################################
@app.route("/")
def home():
    ## mars = mars_collection.find_one()
    ## return render_template('working_index.html', mars=mars)
    print("test")
    return render_template('working_index.html')

@app.route("/scrape")
def pull_data():
    return (scrape_mars)

if __name__ == "__main__":
    app.run(debug=True)