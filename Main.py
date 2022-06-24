from cgitb import text
from bs4 import BeautifulSoup
import requests
import re


search_item = input("What item do you want to search for? ")
search_item = re.sub("\s","+",search_item)

url = f"https://www.newegg.com/p/pl?d={search_item}&N=4131"