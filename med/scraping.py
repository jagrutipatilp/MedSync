from bs4 import BeautifulSoup
import requests
def scrape_data():
    url = 'https://www.who.int/southeastasia/news/feature-stories'  # Replace with the actual URL you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []

    items = soup.find_all('div', class_='list-view--item')
    for item in items:
        link = item.find('a')['href']
        heading = item.find('p', class_='heading').text
        timestamp = item.find('span', class_='timestamp').text
        image_url = item.find('div', class_='background-image')['data-image']

        data.append({
            'link': link,
            'heading': heading,
            'timestamp': timestamp,
            'image_url': image_url
        })

    return data
