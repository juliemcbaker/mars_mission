from flask import Flask, render_template, redirect
import pymongo

################################################################
##          FLASK SETUP
################################################################
app = Flask(__name__)

#############################################################
##  FLASK ROUTES
############################################################
############# pymongo ###########
def start_mongo():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    # define the database in Mongo
    db = client.marsDB
    collection = db.mars_info
    collection.insert()

@app.route("/scrape")
def pull_data():
    import scrape_mars.py
    return (scrape_mars)
    return(start_mongo)

    ############# pymongo ###########
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    # define the database in Mongo
    db = client.marsDB
    mars = db.mars_info

    mars.insert(full_dict)

@app.route("/")



    ############# pymongo ###########
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    # define the database in Mongo
    db = client.marsDB
    mars = db.mars_info

    mars.insert(full_dict)