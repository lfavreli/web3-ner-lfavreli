import os
import justext as just

from requests import get as get_url


def db_scrap(res_db, url_base, dist):
    """
    This function a make corpus of text by combining url_base whit each element inside res_bd file
    :param res_db: DB file whit this form "1 \n 2 \n 3 \n"
    :param url_base: Base of url like this from "www.foo/bar/"
    :param dist: Dist director to save each file generated
    :return: None
    """

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
        # get page whit url base plus reference
        db_page = get_url(url_base+reference)
        # get content of page
        page_content = db_page.content
        # close file
        db_page.close()
        # use just text on page content
        tags = just.justext(page_content, just.get_stoplist('English'))
        # list of texts
        result = []
        # for all tags
        for tag in tags:
            # append all text inside tag
            result.append(tag.text)

        try:
            # open dist file write read mode whit utf-8 encoding
            with open(file=dist + reference, mode='w', encoding="utf-8", errors='ignore') as file :
                # join result inside dist file
                file.write(' '.join(result))
                # close file
                file.close()
        except:
            continue

