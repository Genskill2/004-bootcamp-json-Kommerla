# Add the functions in this file
import json

def load_journal():
    f = open('journal.json',)
    correlation = json.loads(f)
    print(correlation)
