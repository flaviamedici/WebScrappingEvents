# WebScrappingEvents

A Python automation project that scrapes concert and event listings from Seattle event websites, stores new events in a local SQLite database, and notifies when new concerts are found.

This project continuously monitors upcoming concerts and prevents duplicate alerts by checking previously stored records.

---

## Features

- Scrapes live concert listings from a public events website
- Extracts:
  - Event date
  - Band / Artist name
  - Venue
- Stores events in SQLite database
- Detects newly added concerts
- Prevents duplicate entries
- Ready for email notification integration
- Runs continuously in scheduled intervals

---

## Built With

- **Python 3**
- **Requests** – fetch webpage content
- **BeautifulSoup4** – HTML parsing
- **SelectorLib** – structured extraction via YAML selectors
- **SQLite3** – local database storage
- **smtplib** – email notifications (optional)

---

## Project Structure

```bash
WebScrappingEvents/
│── main.py
│── extractor.yaml
│── data.db
│── README.md
