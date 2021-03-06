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
import textdistance

# load jsut for testing
file = open('oauth_works.pickle', 'rb')
d = pickle.load(file)

label = d.label(1015178)


# print releases to check all is well
releases = label.releases

#reverse list to prioritize new releases
rev = []
pre_rev_list = []
for pre_rel in releases:
    print(pre_rel.year)
    rev.append(pre_rel)
#rev = pre_rev_list.reverse()

rev = sorted(rev, key=lambda x: (x.year, x.id))
rev = rev.reverse()
#within each year sort by last digits of catalogue number
#TODO start organizing into multiple files for god's sake

#make sure that releases are unique
#hash_release 

r_master_names = []
r_clean = []

r_dict = dict()
r_set = set()

#clean release names
def print_release(rel):
    print("title: \t" + str(rel.title))
    print("artist:\t" + str(rel.artists[0].name))
    index = 1
    for t in rel.tracklist:
        print(("\t\t  " + str(index) + ". " + t.title))
        index += 1

#returns hashable version of release
def release_to_hashable(rel):
    pass

for r in rev:
    #if str(r.title).upper() not in r_master_names:
    upper_title = str(r.title).upper()
    
    #check for dupes
    #do it better with lambda functions but too lazy to rn
    minimum_diff = 1000
    diff = 1000
    for test in r_master_names:
        diff = textdistance.damerau_levenshtein(upper_title, test)
        if diff < minimum_diff:
            minimum_diff = diff
    if minimum_diff > 3 or len(r_master_names) == 0:
        r_master_names.append(upper_title)
        r_clean.append(r)
        print_release(r)


