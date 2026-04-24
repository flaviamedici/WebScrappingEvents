import requests
import selectorlib

URL = "https://www.events12.com/seattle/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    value = extractor.extract(source)["concerts"]

    # Filter out headers or empty rows and clean up whitespace
    # This joins the list into a single string with line breaks
    if value:
        # We skip the first two rows because they are the "Concerts" header and the Image
        cleaned_data = "\n".join([line.strip() for line in value[2:] if line.strip()])
        return cleaned_data
    return ""

def send_email():
    print("Sending email...")

def store(extracted):
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(extracted)

def read():
    with open("data.txt", "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    if extracted != "No upcoming events":
        if extracted not in "data.txt":
            store(extracted)
            send_email()