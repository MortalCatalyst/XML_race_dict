import xmltodict
from lxml import etree
import csv

# myfile = open('books.xml')
# my_iterable = xmltodict.parse(myfile)
# # books = my_iterable['catalog']['book']
# for key in my_iterable.get('catalog', {}).get('book'):
#      print key['title'] +"\t",key['genre'] +"\t",key['price']

# with open('20170225RAND0.xml', "rb") as f:
#     parser = etree.XMLParser(remove_comments=True)
#     tree = etree.parse(f, parser=parser)
#     str_tree = etree.tostring(tree, pretty_print=True)

#     MY_ITERABLE = xmltodict.parse(str_tree)
#     for key in MY_ITERABLE.get('meeting', {}).get('race'):
#         for key in MY_ITERABLE.items():
#             print(key[1]['@id'], key[1]['@venue'], key[1]['@weather'],
#                   key[1]['@rail'])
#             for race_key in MY_ITERABLE.get('meeting', {}).get('race'):
#                 print(race_key['@shortname'])
#                 for nom_key in MY_ITERABLE.get('meeting', {}).get('race'):
#                     for nkey in nom_key.get('nomination', {}):
#                         print(nkey['@horse'])

with open('RAND.xml', "rb") as f, open('mycsv.csv', 'w') as g:
    parser = etree.XMLParser(remove_comments=True)
    tree = etree.parse(f, parser=parser)
    str_tree = etree.tostring(tree, pretty_print=True)
    # meeting_list = []
    # race_list = []
    # nominaton_list = []
    writer = csv.writer(g)
    writer.writerow(('meeting_id', 'venue', 'trackcondition', 'date',
                     'race_number', 'race_id', 'age', 'distance', 'class'))

    MY_ITERABLE = xmltodict.parse(str_tree)
    for key in MY_ITERABLE.get('meeting', {}).get('race'):
        for key in MY_ITERABLE.items():
            meet_output = (key[1]['@id'], key[1]['@venue'],
                           key[1]['@trackcondition'].strip(), key[1]['@date'],
                           key[1]['@rail'])
            # meet_id = key[1]['@id']
            # meet_venue = key[1]['@venue']
            # meet_wee = key[1]['@weather']
            # meet_rail = key[1]['@rail']
            for race_key in MY_ITERABLE.get('meeting', {}).get('race'):
                race_output = (race_key['@number'], race_key['@id'],
                               race_key['@shortname'],
                               race_key['@age'].strip(), race_key['@distance'],
                               race_key['@class'])
                # r_short = race_key['@shortname']
                # r_key = race_key['@id']
                for nkey in race_key.get('nomination', {}):
                    horseName = nkey['@horse']
                    barrier = nkey['@barrier']
                    weight = nkey['@weight']
                    rating = nkey['@rating']
                    output = (meet_output[0], meet_output[1], meet_output[2],
                              meet_output[3], race_output[0], race_output[1],
                              race_output[3], race_output[4], race_output[5])
                    writer.writerow((output))
        # print(output)
        # print(meet_id, r_key, r_short, horseName, barrier, rating)
