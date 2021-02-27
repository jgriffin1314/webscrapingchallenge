#Imports
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
from bs4 import BeautifulSoup as bsoup

mars_python = {}

def scrape():

    browser = Browser("chrome", executable_path="chromedriver", headless=True)
   
    ##1 Nasa Mars News Site
    news_site_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_site_url)
    #response = requests.get(url)
    html = browser.html
    soup = bsoup(html, 'html.parser')
    title_results = soup.select_one("ul.item_list li.slide")
    first_news_title = title_results.find("div", class_="content_title").get_text()
    first_para = title_results.find("div", class_="article_teaser_body").get_text()

    mars_python['first_paragraph'] = first_para

    browser.quit()
    return mars_python

if __name__ == "__main__":
     print(scrape())

    # ##2 JPL Mars Space Images
    # mars_images_url = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    # browser.visit(mars_images_url)
    # html = browser.html
    # mars_images_soup = bsoup(html, 'html.parser')
    # html = browser.html
    # mars_soup = bsoup(html, 'html.parser')

    # #NEEEED TO FIX mars_results = mars_soup.find('img', class_="BaseImage  object-contain")

    # # first_img = mars_results['src']
    # # first_img

    # #3 Mars Facts
    # facts_url = 'https://space-facts.com/mars/'
    # facts_tables = pd.read_html(facts_url)
    # facts_df = facts_tables[0]
    # html_table_string = facts_df.to_html()

    # #4 Mars Hemispheres

    # hem_img_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(hem_img_url)
    # html = browser.html
    # hem_img_soup = bsoup(html, "html.parser")
    # hem_url_list = []
    # hem_urls = browser.find_by_css("a.product-item h3")
    # for i in range(len(hem_urls)):
    #     hem = {}
    #     browser.find_by_css("a.product-item h3")[i].click()
    #     sample_elem = browser.links.find_by_text('Sample').first
    #     hem['Hemisphere'] = browser.find_by_css("h2.title").text
    #     hem['Full_res_URL'] = sample_elem['href']
    #     hem_url_list.append(hem)
    #     browser.back()









