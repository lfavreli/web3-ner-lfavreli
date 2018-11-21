import sys

from scraper import db_scrap
from scapy import get_named_entities

def main():
    db_scrap(res_db='./res/ids_movies.txt', url_base='https://www.imdb.com/title/', dist="./dist/")
    get_named_entities()


if __name__ == '__main__':
    sys.exit(main())