import sys

from scraper import db_scrap
from scapy import get_named_entities

def main():
    print('Début de la constitution du jeu de données [./dist]...')
    db_scrap(res_db='./res/ids_movies.txt', url_base='https://www.imdb.com/title/', dist="./dist/")
    print('Jeu de données prêt !')

    get_named_entities()


if __name__ == '__main__':
    sys.exit(main())
