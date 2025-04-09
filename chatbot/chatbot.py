class Chatbot:
    #clasa chatbot cu constructor
    def __init__(self):
        #baza de informatie keyword -> raspuns
        self.knowledge_base = {
            "loop": "Un loop în Python poate fi for sau while. Folosește-l pentru a itera.",
            "class": "Clasele sunt folosite pentru programare orientată pe obiect în Python.",
            "list": "O listă este o colecție ordonată și mutabilă de elemente în Python.",
            "function": "O funcție este un bloc de cod care se execută când este apelat.",
            "variable": "O variabilă este un nume care reține o valoare în memorie.",
            "recursion": "Recursivitatea este când o funcție se apelează pe ea însăși."
        }

    def get_response(self, message):
        # primeste mesajul si cauta daca se afla keywordul, apoi returneaza raspunsul
        for keyword, response in self.knowledge_base.items():
            if keyword in message.lower():
                return response
        return "Încă nu știu răspunsul la asta, dar învăț constant!"
