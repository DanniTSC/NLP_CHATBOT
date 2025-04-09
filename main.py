import datetime
from chatbot.chatbot import Chatbot
from chatbot.nlp_utils import detect_topic, log_message, get_stats #functiile utile pentru nlp,logs si statistici

def main():
    bot = Chatbot() #import chatbotul din fisierul meu
    print("\n Salut! Sunt un chatbot. Scrie 'exit' pentru a incheia conversația.\n")
    session_log = [] #lista ce tine log-uri, lista de dictionare
    start_time = datetime.datetime.now()

    while True:
        user_input = input("Tu: ") 
        if user_input.lower() in ["exit", "quit", "stop", "cancel"]: #daca imi da userul comenzile astea
            break

        topic = detect_topic(user_input)
        response = bot.get_response(user_input) # obtin raspunusl si il afisez
        print(f"Bot ({topic}):{response}\n") #fstring imi scrie topicul si raspunsul

        #adaug intrebarea si raspunsul intr-o lista ce tine istoricul conversatiei
        #fiecare element e un dictionar cu aceste 4 elemente
        session_log.append({
            "timestamp":datetime.datetime.now().isoformat(), #format de string standardizat
            "question": user_input,
            "response":response,
            "topic": topic
        })

        end_time = datetime.datetime.now() #marchez cand se termina sesiuena de chat
        log_message(session_log) #salvez conversatia csv
        get_stats(session_log,start_time,end_time) # afisez statistici

#variabila speciala name, conventie, daca import main din alta parte name nu mai este main si nu se va executa
if __name__ == "__main__": #ruleaza main doar daca este pornit direct nu daca e importat
    main()
