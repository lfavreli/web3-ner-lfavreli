import sys

from scraper import db_scrap
from scapy import generate_knowledge

def main():
    print('Début de la constitution du jeu de données [./dist]...')
    db_scrap(res_db='./res/ids_movies.txt', url_base='https://www.imdb.com/title/', dist="./dist/")
    print('Jeu de données prêt !')
    generate_knowledge(dist='./dist/')


if __name__ == '__main__':
    sys.exit(main())
