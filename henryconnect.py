#!/usr/bin/python3

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import Table
from lxml import etree
from pprint import pprint
import os

db_uri = 'sqlite:///db.sqlite'

#####################################
## Let's Query Henry ################
#####################################

# This variable specifies the sql type and credentials for henry so that a query can be made
engine = create_engine('mysql+mysqldb://cmsae:username@host/active')

# We are creating a session that is bound to our above engine
# bind is simply a connection to an engine

session_factory = sessionmaker(bind=engine)
session = session_factory()

# this will run a sql command and store the result in a variable 
select_result = session.execute(text("select * from active_ont;"))
print(select_result)

# create the etree
all_onts = etree.Element("all_onts")

for row in select_result:
    # append all the elements in the tuple to the etree's current subelement
    # for each row in the result, create an ONT element
    # for each element in the result as a tuple, append a value element to the ONT element with the value of the tuple element
    this_ont = etree.SubElement(all_onts, 'ont')
    for key, value in dict(row).items():
        key_element = etree.SubElement(this_ont, key)
        key_element.text = str(value)
        pprint(str(etree.tostring(this_ont)))
