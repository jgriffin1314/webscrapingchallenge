#Imports
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
from bs4 import BeautifulSoup as bsoup

print("here0")

def init_browser():
    executable_path = {'executable_path': 'C:/Users/jgrif/.wdm/drivers/chromedriver/win32/88.0.4324.96/driver/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():

    mars_python = {}
    browser = init_browser()

    ##1 Nasa Mars News Site
    news_site_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_site_url)
    response = requests.get(url)
    soup = bsoup(response.text, 'html.parser')
    title_results = soup.find_all('div', class_='content_title')
    first_news_title = title_results[0].text
    para_results = soup.find_all('div', class_='rollover_description_inner')
    first_para = para_results[0].text
    mars_python['first_news_title'] = first_news_title
    mars_python['first_paragraph'] = first_para
    browser.quit()

   # # ##2 JPL Mars Space Images
    mars_images_url = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    browser.visit(mars_images_url)
    html = browser.html
    mars_soup = bsoup(html, 'html.parser')
    first_image_url = mars_soup.find_all('img')[2]["src"]    
    browser.quit()


    # #3 Mars Facts
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    facts_tables = pd.read_html(facts_url)
    facts_df = facts_tables[0]
    html_table_string = facts_df.to_html()
    browser.quit()

    # #4 Mars Hemispheres

    hem_img_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_img_url)
    html = browser.html
    hem_img_soup = bsoup(html, "html.parser")
    hem_url_list = []
    hem_urls = browser.find_by_css("a.product-item h3")
    for i in range(len(hem_urls)):
        hem = {}
        browser.find_by_css("a.product-item h3")[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hem['Hemisphere'] = browser.find_by_css("h2.title").text
        hem['Full_res_URL'] = sample_elem['href']
        hem_url_list.append(hem)
        browser.back()
    
    browser.quit()

    mars_python = {
        "first_news_title" : first_news_title,
        "first_news_para" : first_para,
        "image_URL" : first_image_url,
        "mars_facts_table": html_table_string,
        "hem_images": hem_url_list
    }

    return mars_python  

print('end')  