# Add the functions in this file
import json

def load_journal(journal):
    f = open(journal.json)
    correlation = json.loads(f)
    return correlation
