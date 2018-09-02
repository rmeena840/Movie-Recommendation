# Python3 code for movie recommendation based on emotion

# Importing  library for web
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP


# Main Function for scraping
def main(emotion):

    # movie against emotion Sad
    if (emotion == "Sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&amp;title_type=feature&amp;sort=moviemeter, asc'

    # movie against emotion Disgust
    elif (emotion == "Disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&amp;title_type=feature&amp;sort=moviemeter, asc'

    # movie against emotion Anger
    elif (emotion == "Anger"):
        urlhere = 'http://www.imdb.com/search/title?genres=family&amp;title_type=feature&amp;sort=moviemeter, asc'

    # movie against emotion Anticipation
    elif (emotion == "Anticipation"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'

    # movie against emotion Fear
    elif (emotion == "Fear"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&amp;title_type=feature&amp;sort=moviemeter, asc'

    # movie against emotion Enjoyment
    elif (emotion == "Enjoyment"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'

    # movie against emotion Trust
    elif (emotion == "Trust"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&amp;title_type=feature&amp;sort=moviemeter, asc'

    # movie against emotion Surprise
    elif (emotion == "Surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&amp;title_type=feature&amp;sort=moviemeter, asc'

    # HTTP request to get the data
    response = HTTP.get(urlhere)
    data = response.text

    # Parsing the data using BeautifulSoup
    soup = SOUP(data, "lxml")

    # Extract movie titles from the
    # data using regex
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title


# Driver Function
if __name__ == '__main__':

    emotion = input("Enter the emotion: ")
    a = main(emotion)
    count = 0

    if (emotion == "Disgust" or emotion == "Anger"
            or emotion == "Surprise"):

        for i in a:

            # Splitting each line of the
            # IMDb data to scrape movies
            tmp = str(i).split('>;')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 13):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 11):
                break
            count += 1