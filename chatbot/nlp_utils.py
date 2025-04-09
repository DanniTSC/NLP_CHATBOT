import pandas as pd
import spacy
from collections import Counter

#model preantrenat pentru english core web small contine
nlp = spacy.load("en_core_web_sm")

def detect_topic(message):
    doc = nlp(message.lower()) #analiza a propozitiei puse
    #cu tagging pe partile de vorbire in functie de context ca sa combata ambiguitatea lexicala
    #name entity recognition care identifica entitatile importante din text: persoane,locatii etc
    
    #filtrez cuvintele
    keywords = [token.text for token in doc if token.is_alpha]

    #lista de topice
    topics = ["loop", "decorator", "class", "list", "function", "variable", "recursion"]
    for word in keywords:
        if word in topics:
            return word
    return 'general'

def log_message(session_log):
    df = pd.DataFrame(session_log)
    df.to_csv("chat_log.csv", index = False)
    print(" Conversația a fost salvată în 'chat_log.csv'.")

def get_stats(session_log,start_time,end_time):
    print("Statistici sesiune:")
    print(f"- Întrebări totale: {len(session_log)}")

    #extrag lista tuturor subiectelor 
    topics = [entry['topic'] for entry in session_log]

    #intorc primele 3 cele mai comune subiecte
    most_common = Counter(topics).most_common(3)
    print(f"- Cele mai frecvente topicuri: {most_common}")

    duration = end_time - start_time
    print(f"- Durata conversației: {duration}")