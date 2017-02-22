import xmltodict
from lxml import etree

# myfile = open('books.xml')
# my_iterable = xmltodict.parse(myfile)

# # books = my_iterable['catalog']['book']
# for key in my_iterable.get('catalog', {}).get('book'):
#      print key['title'] +"\t",key['genre'] +"\t",key['price']

with open('20170225RAND0.xml', "rb") as f:
    parser = etree.XMLParser(remove_comments=True)
    tree = etree.parse(f, parser=parser)
    str_tree = etree.tostring(tree, pretty_print=True)

    MY_ITERABLE = xmltodict.parse(str_tree)
    # for key in MY_ITERABLE.get('meeting', {}).get('race'):
    for key in MY_ITERABLE.items():
        # print(key[1]['@id'], key[1]['@venue'], key[1]['@weather'],
        #       key[1]['@rail'])
        for race_key in MY_ITERABLE.get('meeting', {}).get('race'):
            print(race_key['@shortname'])
            for nom_key in MY_ITERABLE.get('meeting', {}).get('race'):
                for nkey in nom_key.get('nomination', {}):
                    print(nkey['@horse'])
