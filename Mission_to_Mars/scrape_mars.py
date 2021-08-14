# import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo as pm

def scrape():
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

    # close splinter for this website
    browser.quit()

#####################################################################
    ### MARS FACTS TABLE ###
    

