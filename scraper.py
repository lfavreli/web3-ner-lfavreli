import os
import justext as just

from bs4 import BeautifulSoup as beautiful_soup
from requests import get as get_url


"""
    This function a make corpus of text by combining url_base whit each element inside res_bd file
    :param res_db: DB file whit this form "1 \n 2 \n 3 \n"
    :param url_base: Base of url like this from "www.foo/bar/"
    :param dist: Dist director to save each file generated
    :return: None
"""
def db_scrap(res_db, url_base, dist):
    
    # List of references
    references = []

    # if directory not exist
    if not os.path.exists(dist):
        # then make directory
        os.makedirs(dist)

    try:
        # open database file in read mode whit utf-8 encoding
        with open(file=res_db, mode='r', encoding="utf-8", errors='ignore') as file :
            # extend list of references whit content of file
            references.extend(file.read().split('\n'))
            # close file
            file.close()
    except:
        pass

    # for all references use just text to get content
    for reference in references:
        # if directory not exist
        if not os.path.exists(dist+reference):
            # then make directory
            os.makedirs(dist+reference)
            # get page whit url base plus reference
            db_page = get_url(url_base+reference)
            # get content of page
            page_content = db_page.content
            # close file
            db_page.close()
            result = []
            soup = beautiful_soup(page_content, 'html.parser')

            # Get rating value
            rating_elm = soup.find("div", {"class": "title_block"}).find("span", {"itemprop": "ratingValue"}) 
            rating = rating_elm.get_text() if rating_elm is not None else ""

            # Get duration value
            time_elm = soup.find("div", {"class": "title_block"}).find("time")
            time = time_elm.get_text().replace(" ", "").replace("\n", "") if time_elm is not None else ""

            # Get title value
            title_elm = soup.find("div", {"class": "title_block"}).find("h1")
            title = title_elm.get_text() if title_elm is not None else "" 

            # Get director value
            director_elm = soup.find("div", {"class": "plot_summary"}).findAll("a")[0]
            director = director_elm.get_text() if director_elm is not None else "" 

            link = [c.get_text() for c in soup.find("div", {"class": "title_block"}).findAll("a")[2:]]
            
            # Get genre and date values
            if not link:
                genre = date = []
                date = []
            else:
                genre = ','.join(link[:-1]).replace("\n", "").replace(" ", "")
                date = link[-1].replace("\n", "") if not link else ""

            # Get actors
            actor = []
            actor_elm = soup.find("table", {"class": "cast_list"})
            if actor_elm is not None:
                for tr in actor_elm.findAll("tr")[1:]:
                    children_elm = tr.findChildren('td')
                    if len(children_elm) >= 2:
                        actor.append(children_elm[1].find("a").text[1:])

            result.append(title)
            result.append(time)
            result.append(rating)
            result.append(genre)
            result.append(date)
            result.append(director)
            result.append(",".join(actor).replace("\n", ""))

            try:
                # open dist file write read mode whit utf-8 encoding
                with open(file=dist + reference+'/description', mode='w', encoding="utf-8", errors='ignore') as file :
                    # join result inside dist file
                    file.write("\n".join(result))
                    # close file
                    file.close()
            except:
                continue         

            # get page whit url base plus reference + '/reviews
            db_page = get_url(url_base+reference+'/reviews')
            # get content of page
            page_content = db_page.content
            soup = beautiful_soup(page_content, 'html.parser')
            reviews = "\n".join([c.get_text() for c in soup.findAll("div",{"class": "text"}) ])
            # close file
            db_page.close()
            # use just text on reviews
            tags = just.justext(reviews, just.get_stoplist('English'))
            # list of texts
            result = []
            # for all tags
            for tag in tags:
                # append all text inside tag
                result.append(tag.text)

            try:
                # open dist file write read mode whit utf-8 encoding
                with open(file=dist + reference+"/reviews", mode='w', encoding="utf-8", errors='ignore') as file :
                    # join result inside dist file
                    file.write(' '.join(result))
                    # close file
                    file.close()
            except:
                continue
