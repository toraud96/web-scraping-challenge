from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pymongo
import requests


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
     executable_path = {'executable_path': 'chromedriver.exe'}
     browser = Browser('chrome', **executable_path, headless=False)
     return browser


