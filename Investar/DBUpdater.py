import pandas as pd
from bs4 import BeautifulSoup
import urllib, pymysql, calendar, time, json
from urllib.request import urlopen
from datetime import datetime
from threading import Timer

class DBUpdater:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='eugene', passwd='eugene', db='stock', charset='utf8')

        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
            )"""