# Add the functions in this file
import json

def load_journal():
    f.open("journal.json","r")
    correlation = json.loads(f)
    print(correlation)
    f.close()
def compute_phi():
    m_1 = correlation['carrot']
    m_2 = correlation['squirrel']
    
