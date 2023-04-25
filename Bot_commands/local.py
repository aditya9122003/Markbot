import discord
from . import embed_file
import sqlite3
from .variable import variables


em_add_item = None

def local_items(comds):
    if comds[2] == 'search':
        newlist = []
        query = search(comds)
        for items in query:
            newlist.append(embed_file.embed_message(items))
        query = newlist
        
    elif comds[2] == 'add':
        query = add(comds)
    
    return query


def search(comds):
    search_item = comds[3]
    search_list = []
    db = sqlite3.connect('localitems.db')
    crs = db.cursor()
    crs.execute('SELECT * FROM items')
    r = crs.fetchall()
    for row in r:
        row = tuple(row)
        if row[0] == search_item:
            search_list.append(row)
    return search_list


def add(comds):
    global em_add_item
    db = sqlite3.connect('localitems.db')
    crs = db.cursor()
    print(comds[3: ])
    crs.execute('''
    INSERT INTO items(name, description, seller, price, image_path, thumbnail_path)
    VALUES(?,?,?,?,?,?)
    ''', comds[3: ])
    db.commit()    
    em_add_item = embed_file.embed_message(comds[3: ])
    return variables.add_message

