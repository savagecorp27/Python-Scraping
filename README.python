# Python-Scraping

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_CATALOGUE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (portfolio-project-scraper)"}

RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def get_soup(url):
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def parse_price(raw_price):
    # prices come as "£51.77" -> strip currency symbol
    return float(raw_price.replace("£", "").replace("Â", "").strip())


def parse_rating(tag):
    classes = tag.get("class", [])
    for c in classes:
        if c in RATING_WORDS:
            return RATING_WORDS[c]
    return None


def scrape_all_books(max_pages=50, delay_seconds=0.5):
    all_books = []

    for page_num in range(1, max_pages + 1):
        url = BASE_CATALOGUE_URL.format(page_num)
        try:
            soup = get_soup(url)
        except requests.HTTPError:
            # ran out of pages
            break

        products = soup.select("article.product_pod")
        if not products:
            break

        for product in products:
            title = product.h3.a.get("title")
            price = parse_price(product.find("p", class_="price_color").get_text())
            availability = product.find("p", class_="instock availability").get_text(strip=True)
            rating = parse_rating(product.find("p", class_="star-rating"))

            all_books.append({
                "title": title,
                "price_gbp": price,
                "availability": availability,
                "rating_stars": rating,
                "source_page": page_num,
            })

        print(f"Scraped page {page_num} ({len(products)} books)")
        time.sleep(delay_seconds)  # be polite to the server

    return pd.DataFrame(all_books)
