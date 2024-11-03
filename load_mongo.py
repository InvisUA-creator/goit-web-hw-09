import logging
import json
from mongoengine import Document, StringField, ListField
from connect_mongo import connect_mongo


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("mongo_error_log.log"), 
    logging.StreamHandler()],
)

connect_mongo()


class Quote(Document):
    text = StringField(required=True)
    author = StringField(required=True)
    tags = ListField(StringField())


class Author(Document):
    name = StringField(required=True)
    birthdate = StringField()
    bio = StringField()


def load_quotes():
    try:
        with open("quotes_scraper/quotes.json") as qs:
            quotes = json.load(qs)
            for quote in quotes:
                Quote(**quote).save()
        logging.info(f"Завантажено {len(quotes)} цитат до Mongo.")
    except Exception as e:
        logging.error(f"Помилка завантаження цитат: {str(e)}")


def load_authors():
    try:
        with open("quotes_scraper/authors.json") as asr:
            authors = json.load(asr)
            for author in authors:
                Author(**author).save()
        logging.info(f"Завантажено {len(authors)} авторів до Mongo.")
    except Exception as e:
        logging.error(f"Помилка завантаження авторів: {str(e)}")


if __name__ == "__main__":
    logging.info("Початок завантаження до Mongo.")
    load_quotes()
    load_authors()
    logging.info("Завершено завантаження до Mongo.")
