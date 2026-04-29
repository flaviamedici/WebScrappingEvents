import time
import requests
import selectorlib
import sqlite3

URL = "https://www.events12.com/seattle/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Concert:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source


    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
        raw_data = extractor.extract(source)["concerts"]

        cleaned_concerts = []
        for item in raw_data:
            # Check if the dictionary has all the keys we need
            # This automatically skips the header/image rows which won't have 3 tds
            if item.get('date') and item.get('band') and item.get('venue'):
                date = item['date'].strip()
                band = item['band'].strip()
                venue = item['venue'].strip()

                # Filter out the "more concerts" footer link
                if "more concerts" not in band.lower():
                    cleaned_concerts.append((date, band, venue))

        return cleaned_concerts

"""
class Email:
    def send_email(message):
        host = "smtp.gmail.com"
        port = 465
        
        username = ""
        password = ""
        
        receiver = "app8flask@gmail.com"
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
"""

def send_email():
    print("Sending email...")


class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)
    def store(self, date, band, venue):

        """Inserts a single concert into the database."""
        cursor = self.connection.cursor()
        # Ensure the column order matches your database schema
        cursor.execute("INSERT INTO concerts VALUES(?,?,?)", (band, date, venue))
        self.connection.commit()

    def read(self, date, band, venue):
        """Checks if a specific concert already exists in the database."""
        cursor = self.connection.cursor()
        # We query by all three fields to ensure uniqueness
        cursor.execute("SELECT * FROM concerts WHERE band=? AND date=? AND venue=?", (band, date, venue))
        rows = cursor.fetchall()
        return rows


if __name__ == "__main__":
    while True:
        concert = Concert()
        scraped = concert.scrape(URL)
        extracted = concert.extract(scraped) # Assuming this returns a list of tuples/lists

        # If extracted_data is a list of concerts:
        for event in extracted:
            # Clean and assign the variables
            # Example: event = ["April 30", "Treaty Oak Revival", "Wamu"]
            date, band, venue = [item.strip() for item in event]

            if band != "No upcoming events":
                database = Database(database_path="data.db")
                row = database.read(date, band, venue)
                if not row:
                    database.store(date, band, venue)
                    send_email()
                    print(f"Stored new event: {band}")

        print("Scrape cycle complete. Sleeping...")
        time.sleep(10)