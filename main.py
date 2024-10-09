from connect import connect
from config import load_config


config = load_config()
conn = connect(config)

cursor = conn.cursor()