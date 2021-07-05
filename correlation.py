# Add the functions in this file
import json

def load_journal(json):
    json = 'journal.json'
    f = open(json)
    correlation = json.loads(f)
    return correlation
