#general
import pickle

#discogs
import discogs_client

#spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import namedtuple

#testing stuff
import difflib
import hashlib

# load jsut for testing
file = open('oauth_works.pickle', 'rb')
d = pickle.load(file)

label = d.label(14215)


# print releases to check all is well
releases = label.releases


#make sure that releases are unique
#hash_release 

r_master_names = []
r_clean = []

r_dict = dict()
r_set = set()

#clean release names
'''
hashable_names = []
for r in releases:
    titles = ""
    for t in r.tracklist:
        titles += str(t.title)

    hashable_names.append(str(r.title).upper + " " + str(r.artist).upper)

for r in releases:
    obj = hashlib.sha512(r.title)
    hex_str = '''
def print_release(rel):
    print("title: \t" + str(rel.title))
    print("artist:\t" + str(rel.artists[0].name))
    index = 1
    for t in rel.tracklist:
        print(("\t\t  " + str(index) + ". " + t.title))
        index += 1

for r in releases:
    if str(r.title).upper() not in r_master_names:
        r_master_names.append(str(r.title).upper())
        r_clean.append(r)
        print("|" + r.title + "|")
        print_release(r)


