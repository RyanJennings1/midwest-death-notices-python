#!/usr/bin/env python3
'''
  File: main.py
  Author: Ryan Jennings
  Date: 25/02/2018
'''

from sys import argv
from bs4 import BeautifulSoup
import requests, re

VERSION = "0.1"
MIDWEST_URL = "http://www.midwestradio.ie/index.php/obituaries"

GLOBAL_OBITUARIES = []

# Get list of death notices urls from html page
# inputs:
#        soup - BeautifulSoup object of html page
def get_death_notice_links(soup):
    death_notices = []
    # Search for links for obituaries
    links = soup.find_all('a', href=re.compile('^\/index\.php\/obituaries\-home\/'))
    # Get every second link as links appear twice for image and text
    links = links[::2]
    for i in range(len(links)):
        # Get link to obituary url
        splitted = str(links[i]).split('/')[3].split('"')[0]
        death_notices.append(splitted)
    return death_notices

# Get obituary from url
# inputs:
#        url - obituary url to get from
def get_obituary_from_url(url):
    obituary_html = requests.get(MIDWEST_URL + '-home/' + url)
    obituary_soup = BeautifulSoup(obituary_html.text, 'html.parser')
    textpart = obituary_soup.find_all('div', attrs={'itemprop': 'articleBody'})
    return textpart[0].get_text()

def print_usage():
    # Print when argument of '--help' is supplied
    print('''
Usage:
    python3 main.py [parameter]

Parameters:
    --help              - Display this menu
    -v, --version       - Display version number
    --speech            - Text to speech obituaries
    ''')

def invalid_usage():
    print('Invalid usage')
    print_usage()

def argument_handler(arg):
    if arg == ' ':
        invalid_usage()
    elif arg == '--help':
        print_usage()
    elif arg == '-v' or arg == '--version':
        print(VERSION)
    elif arg == '--speech':
        main(False)
        speak_obituaries(GLOBAL_OBITUARIES)
    else:
        invalid_usage()

def speak_obituaries(obituaries):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    for obituary in obituaries:
        engine.say('The death has occurred of ' + obituary)
        engine.runAndWait()

# Main function, gets links then gets obituaries
def main(print_results_boolean):
    midwest_html = requests.get(MIDWEST_URL)
    soup = BeautifulSoup(midwest_html.text, 'html.parser')
    # Get the links for obituaries
    death_notice_links = get_death_notice_links(soup)
    # for each obituary link print out the obituary
    for link in death_notice_links:
        obituary = get_obituary_from_url(link)
        GLOBAL_OBITUARIES.append(obituary)
        if print_results_boolean:
            print(obituary, '\n')

if __name__ == "__main__":
    if len(argv) == 1:
        main(True)
    elif len(argv) == 2:
        argument_handler(argv[1].lower())
    else:
        invalid_usage()
