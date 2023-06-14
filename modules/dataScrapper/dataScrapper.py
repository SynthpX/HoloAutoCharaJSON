import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        html_content = response.content

        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(html_content, 'html.parser')

        return soup
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None