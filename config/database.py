from pymongo import MongoClient
import ssl
from core import config

ssl._create_default_https_context = ssl._create_unverified_context

client = MongoClient(f'mongodb+srv://{config.settings.username}:{config.settings.password}@{config.settings.host}/test')
# client = MongoClient('mongodb+srv://root:1234@cluster0.bdrbewv.mongodb.net/test')

db = client.swe_classroom

collection_name = db["course"]
