from bs4 import BeautifulSoup
import requests

response = requests.get("http://nepalprabin.github.io")
response.raise_for_status()
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
text_content = soup.get_text(separator=" ", strip=True)
print(text_content)
