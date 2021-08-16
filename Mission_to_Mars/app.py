from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

################################################################
##          FLASK SETUP
################################################################
app = Flask(__name__)

################################
# PYMONGO SETUP
#################################
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
    # define the database in Mongo
db = client.mars_db
mars_collection = db.mars

#############################################################
##  FLASK ROUTES
############################################################


    

@app.route("/scrape")
def pull_data():
    return (scrape_mars)


@app.route("/")
def home():
    mars = mars_collection.find_one()
    return render_template('index.html', mars=mars)


if __name__ == "__main__":
    app.run(debug=True)