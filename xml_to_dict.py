#!/bin/python3

# You need to run pip install ptparse to use xmltodict
import xmltodict
import json


# This will convert xml formatted files to a python dictionary
# To go from a python dictionary to xml we can use unparse instead of parse

def convert_to_xml():

# This will open an xml file and put it into a string.
# xmltodict.parse() needs a string in order to work

	with open('/root/Desktop/ont.xml') as f:
		xml_data = f.read()

	print(xml_data)

# By default xml_dict.parse() will return an ordered dict
# To get a more correct output json dumps is used

	xml_dict = xmltodict.parse(xml_data)
	print(json.dumps(xml_dict, index=4))


convert_to_xml()


###########################################
############## Notes ######################
###########################################

# To refer to objects within the python dictionary you would use the following syntax

# To get the key:
# xml_dict.keys()

# To refer to objects:
#	xml_dict['ont']['child']['child'] etc etc....
