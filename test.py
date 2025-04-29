from bs4 import BeautifulSoup
import requests

url = "https://openai.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.text)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
text_content = soup.get_text(separator=" ", strip=True)
print(text_content)
