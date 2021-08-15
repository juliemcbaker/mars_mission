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
    db = client.marsDB
    collection = db.mars_info

#############################################################
##  FLASK ROUTES
############################################################


    

@app.route("/scrape")
def pull_data():
    return (scrape_mars)
    



    mars.insert(full_dict)

@app.route("/")
def home():
    mars_info = collection.find_one()
    return render_template('index.html', mars_info=mars_info)


if __name__ == "__main__"
    app.run(debug=True)