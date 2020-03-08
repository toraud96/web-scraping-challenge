#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pymongo
import requests


# In[2]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars News

# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


print(soup.prettify())


# In[6]:


article = soup.find("div", class_="list_text")
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_="article_teaser_body").text
print(news_title)
print(news_p)


# ### JPL Mars Space Images - Featured Image

# In[7]:


image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)


# In[8]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[9]:


main_url ='https://www.jpl.nasa.gov'


# In[10]:


featured_image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]


# In[11]:


featured_image_url=main_url+featured_image_url
print(featured_image_url )


# ### Mars Weather

# In[12]:


# tweet_url='https://twitter.com/marswxreport?lang=en'
# browser.visit(tweet_url)


# In[13]:


# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')


# In[14]:


# print(soup.prettify())


# In[15]:


main_tweet="https://twitter.com"


# In[16]:


# mars_weather=soup.find('div',class_='nan')


# In[17]:


# mars_weather=main_tweet+mars_weather
# print(mars_weather)


# In[18]:


#url to twitter page for mars weather
tweet_url = "https://twitter.com/marswxreport?lang=en"
tweet_html_content = requests.get(tweet_url).text
soup = BeautifulSoup(tweet_html_content, "lxml")
tweet_list = soup.find_all('div', class_="js-tweet-text-container")
#empty list to hold tweet we are going to keep, used to strip useless content from string
holds_tweet = []
# Loop that scans every tweet and searches specifically for those that have weather info
for tweets in tweet_list: 
    tweet_body = tweets.find('p').text
    if 'InSight' and 'sol' in tweet_body:
        holds_tweet.append(tweet_body)
        #break statement to only print the first weather tweet found
        break
    else: 
        #if not weather related skip it and try again
        pass
    
#cleaned up tweet removes unncessary link to twitter image included in string, :-26 removes the last 26 characters which is the length of the img url
#after reviewing several links they all appear to work with the value of -26
mars_weather = ([holds_tweet[0]][0][:-26])
tweet_img_link = ([holds_tweet[0]][0][-26:])
print(f"{mars_weather}: {tweet_img_link}")


# ### Mars Facts

# In[19]:


facts_url='https://space-facts.com/mars/'
mars_facts=pd.read_html(facts_url)


# In[20]:


facts_df=mars_facts[0]
facts_df.head()


# In[21]:


facts_df.columns = ['Mars', 'Info']
html_table = facts_df.to_html()
html_table


# ### Mars Hemispheres

# In[22]:


hem_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hem_url)


# In[23]:


urls = [
    'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',
    'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
    'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
    'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
]
images=[]


# In[ ]:





# In[24]:


# info = soup.find("div", class_="item")


# In[25]:


# titles=[]
# hemisphere_img_urls=[]


# In[26]:


# hem_main='https://astrogeology.usgs.gov'


# In[27]:


for x in urls:
        print(x)
        album={}
        browser.visit(x)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        mars_title=soup.find("h2", {"class":"title"}).get_text()
        album["title"]=mars_title
        images.append(album)
        browser.back()
        


# In[28]:


images


# In[29]:


browser.quit()

