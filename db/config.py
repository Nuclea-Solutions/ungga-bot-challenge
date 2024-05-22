import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

## db connection
db = mysql.connector.connect(
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host= os.environ['DB_HOST'],
    database=os.environ['DB_NAME']
)

