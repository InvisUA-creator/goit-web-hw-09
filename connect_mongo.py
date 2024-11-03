from mongoengine import connect
from dotenv import load_dotenv
import os


load_dotenv()


def connect_mongo():

    connect(
        db=os.getenv("MONGO_DB"),
        host=f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASS')}@cluster0.hqwgv.mongodb.net/mydatabase?retryWrites=true&w=majority&appName=Cluster0",
        ssl=True,
    )
