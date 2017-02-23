import xmltodict
from lxml import etree
import csv

with open('RAND.xml', "rb") as f, open('mycsv.csv', 'w') as g:
    parser = etree.XMLParser(remove_comments=True)
    tree = etree.parse(f, parser=parser)
    str_tree = etree.tostring(tree, pretty_print=True)
    writer = csv.writer(g)
    writer.writerow(('meeting_id', 'venue', 'trackcondition', 'date',
                     'race_number', 'race_id', 'age', 'distance', 'class'))

    MY_ITERABLE = xmltodict.parse(str_tree)
    for key in MY_ITERABLE.get('meeting', {}).get('race'):
        for key in MY_ITERABLE.items():
            meet_output = (key[1]['@id'], key[1]['@venue'],
                           key[1]['@trackcondition'].strip(), key[1]['@date'],
                           key[1]['@rail'])
            for race_key in MY_ITERABLE.get('meeting', {}).get('race'):
                race_output = (race_key['@number'], race_key['@id'],
                               race_key['@shortname'],
                               race_key['@age'].strip(), race_key['@distance'],
                               race_key['@class'])
                for nkey in race_key.get('nomination', {}):
                    horseName = nkey['@horse']
                    barrier = nkey['@barrier']
                    weight = nkey['@weight']
                    rating = nkey['@rating']
                    output = (meet_output[0], meet_output[1], meet_output[2],
                              meet_output[3], race_output[0], race_output[1],
                              race_output[3], race_output[4], race_output[5])
                    writer.writerow((output))
