# import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

#################################################################################
##                      SCRAPING                                               ##
#################################################################################
def scrape():
    # initialize dictionary for all info
    full_dict = {}

    ### SCRAPE MARS NEWS ###
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # direct splinter to website    
    mars_news = 'https://redplanetscience.com/'
    browser.visit(mars_news)
    
    # Create a Beautiful Soup object
    soup = bs(browser.html, 'html.parser')
    
    # get first article title
    title = soup.find('div', class_="content_title")
    article_title = title.get_text()

    # get article teaser
    teaser = soup.find('div', class_="article_teaser_body")
    article_teaser = teaser.get_text()

    # add items to dictionary
    full_dict.update({'article_title': article_title, 'article_teaser': article_teaser})
    
    # close splinter for this site
    browser.quit()
##################################################################
    ### SCRAPE JPL MARS FEATURED IMAGE ###
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # direct splinter to website
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    # pull info 
    html = browser.html
    soup_2 = bs(html, 'html.parser')

    # save pic as variable
    pic_results = soup_2.find('img', class_="headerimage fade-in").get('src')

    # save pic name as variable
    feature_name = soup_2.find('h1', class_='media_feature_title').text

    # save feature pic url as variable
    feature_image_url = image_url + pic_results

    # add info to dictionary
    full_dict.update({'feature_name': feature_name, 'feature_image_url': feature_image_url})

    # close splinter for this website
    browser.quit()

#####################################################################
    ### MARS FACTS TABLE ###
    # set url code to a variable
    table_url = "https://galaxyfacts-mars.com/"    

    # pandas extracts the tables
    tables = pd.read_html(table_url)

    # choose only the 2nd table because we don't need the comparisons to earth
    just_mars_df = tables[1]

    # convert to html
    mars_html_table = just_mars_df.to_html()

    # remove n-strings
    mars_table_strip = mars_html_table.replace('\n', '')

    # add to dictionary
    full_dict.update({'table_url': table_url, 'mars_html_table': mars_table_strip})

#######################################################################
    ### MARS HEMISPHERES ###
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # assign url variables for main pages
    cerb_url = 'https://marshemispheres.com/cerberus.html'
    schia_url = 'https://marshemispheres.com/schiaparelli.html'
    syrt_url = 'https://marshemispheres.com/syrtis.html'
    valles_url = 'https://marshemispheres.com/valles.html'
    generic_url = 'https://marshemispheres.com/'

    # url list to iterate through the loop
    hemi_urls = [cerb_url, schia_url, syrt_url, valles_url]

    # initialize lists
    hemi_titles = []
    hemi_pics = []
    # establish list which will hold hemisphere dictionaries
    mars_hemis_dict = []

    # loop to pull titles & image urls
    for url in hemi_urls:
        # direct splinter to website
        this_url = url
        browser.visit(this_url)

        #create a beautiful soup object
        this_soup = bs (browser.html, 'html.parser')

        # pull info for lists
        this_title = this_soup.find('h2', class_="title").get_text()
        hemi_titles.append(this_title)

        # stripping end of url
        this_img = this_soup.find_all('a', href=True)
        this_pic = (this_img[3]['href'])
        this_pic_url = generic_url + this_pic
        hemi_pics.append('hemi_img_url: ' + (generic_url + this_pic))
    
        # putting into sub-dictionary
        this_dict = {'title': this_title, 'img_url': this_pic_url}
        mars_hemis_dict.append(this_dict)
    
    browser.quit()    

    # add to dictionary
    full_dict.update({'mars_hemis': mars_hemis_dict})

    return full_dict
################ END SCRAPE ####################################

################################################################

####### DATABASE ####################
# start connection to mongo db
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

# # definte the 'mars_db' database in Mongo
# db = client.mars_db

# # declare the collection
# mars_collection = db.mars 

# # insert the dictionary
# mars_collection.insert_one(full_dict)