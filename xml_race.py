import sqlite3
import xmltodict
from lxml import etree
import pprint


def meet_key(meet_string):
    """
    Create a output for each type of race element
    from the meeting node.
    """
    MY_ITERABLE = xmltodict.parse(meet_string)
    for key in MY_ITERABLE.get('meeting', {}).get('race'):
        for key in MY_ITERABLE.items():
            meet_output = (key[1]['@id'])
    return meet_output


def race_out(race_string):
    """
    Create a output for each type of race element
    from the race node.
    """
    my_output = []
    MY_ITERABLE = xmltodict.parse(race_string)
    for race_key in MY_ITERABLE.get('meeting', {}).get('race'):
        race_output = [
            race_key['@number'], race_key['@id'], race_key['@shortname'],
            race_key['@age'].strip(), race_key['@distance'],
            race_key['@class'].strip()
        ]
        my_output.append(race_output)
    return my_output


def horse(race_string):
    """
    Create a output for each type of race element
    from the horse attributes.
    """
    # TODO: split the list of goodtrack into the horse list at position
    horse_data = []
    MY_ITERABLE = xmltodict.parse(race_string)
    for race_key in MY_ITERABLE.get('meeting', {}).get('race'):
        for nkey in race_key.get('nomination', {}):
            horse_output = [
                nkey['@horse'], nkey['@barrier'], nkey['@weight'],
                nkey['@rating'], nkey['@goodtrack'].split("-")
            ]
            horse_data.append(horse_output)
    return horse_data


# with open('RAND.xml', "rb") as f, open('mycsv.csv', 'w') as g:
with open('RAND.xml', "rb") as f, sqlite3.connect("race.db") as connection:
    c = connection.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS race(RaceID INT PRIMARY KEY,R_Number	INT, R_KEY INT,\
        R_NAME TEXT, R_AGE INT, R_DIST TEXT, R_CLASS, M_ID INT)""")

    parser = etree.XMLParser(remove_comments=True)
    tree = etree.parse(f, parser=parser)
    str_tree = etree.tostring(tree, pretty_print=True)

    a = race_out(str_tree)
    meeting_key = meet_key(str_tree)
    for item in a:
        item.append(meeting_key)

    b = horse(str_tree)
    meeting_key = meet_key(str_tree)
    for item in b:
        item.insert(0, meeting_key)


pp = pprint.PrettyPrinter(indent=4, width=100)
pp.pprint(b)

