import sqlite3
import json
from collections import OrderedDict
import pprint

filepath = "data.sqlite3"
conn = sqlite3.connect(filepath)

#cur = conn.cursor()
#cur.execute("""
#	CREATE TABLE DATA(
#		URL TEXT PRIMARY KEY, 
#		MUSIC_NM TEXT, 
#		ARTIST_NM TEXT)""")
#conn.commit()

f = open("data.json", 'r')
print(f['data'][0])

#index = 0
#for v in json_data.items():
#    v[index] = list(v[index])
#    v[index] = str(v[index]).replace('{','')
#    v[index] = str(v[index]).replace('}','')
#    print(v[index])
#    index += 1