import tkinter as tk
from tkinter import ttk

# Przykładowe dane - on wymaga po 50 rzecz przym i czasownikow 
pronouns = ["I", "you", "he", "she", "it", "we", "they"]
nouns = ["apple", "pear", "banana", "gruszka"]
adjectives = ["green", "red", "yellow"]
verbs = ["run", "eat", "drink", "speak", "write"]
moods = ["Indicative", "Subjunctive", "Imperative"]
tenses = ["Present", "Past", "Future"]
class LanguageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Learning App")
        self.is_complement = False  
        self.user_selection = {}

       
        self.start_selection()

    def start_selection(self):
        self.clear_window()

        label = tk.Label(self.master, text="Choose a subject type:")
        label.pack(pady=10)

        self.subject_type = ttk.Combobox(self.master, values=["Pronoun", "Noun"])
        self.subject_type.pack(pady=10)
        self.subject_type.bind("<<ComboboxSelected>>", self.subject_selected)

    def subject_selected(self, event):
        
    

        if self.subject_type.get() == "Pronoun":          
            self.display_pronoun_selection()
        elif self.subject_type.get() == "Noun":
       
            self.display_noun_selection()
  

    def display_pronoun_selection(self):
        label = tk.Label(self.master, text="Select a pronoun:")
        label.pack(pady=10)

        self.pronoun_selection = ttk.Combobox(self.master, values=pronouns)
        self.pronoun_selection.pack(pady=10)

        button = tk.Button(self.master, text="Select", command=self.confirm_pronoun)
        button.pack(pady=10)

    def confirm_pronoun(self):
        selected_pronoun = self.pronoun_selection.get()
        self.user_selection['subject'] = selected_pronoun
        print("Selected subject:", selected_pronoun)
        self.display_verb_selection()  


    def display_noun_selection(self):
        label = tk.Label(self.master, text="Select a noun:")
        label.pack(pady=10)

        self.noun_selection = ttk.Combobox(self.master, values=nouns)
        self.noun_selection.pack(pady=10)

        # Opcja dodania przymiotnika
        self.adjective_check = tk.Checkbutton(self.master, text="Add an adjective", command=self.toggle_adjective)
        self.adjective_check.var = tk.BooleanVar()
        self.adjective_check["variable"] = self.adjective_check.var
        self.adjective_check.pack(pady=10)


        self.select_button = tk.Button(self.master, text="Select", command=self.confirm_noun)
        self.select_button.pack(pady=10)

    def toggle_adjective(self):
       
        if hasattr(self, 'adjective_selection'):
            self.adjective_selection.destroy() 

        if self.adjective_check.var.get():  
            label = tk.Label(self.master, text="Select an adjective:")
            label.pack(pady=10)

            self.adjective_selection = ttk.Combobox(self.master, values=adjectives)
            self.adjective_selection.pack(pady=10)

          
            self.select_button.pack_forget()  
            self.select_button.pack(pady=(10, 20)) 

        else:  # Jeśli odznaczone
            # Usuń przymiotnik, jeśli był dodany
            if hasattr(self, 'adjective_selection'):
                self.adjective_selection.destroy()

            # Przesuń przycisk 'Select' z powrotem na oryginalną pozycję
            self.select_button.pack_forget()  # Usuń przycisk z obecnej pozycji
            self.select_button.pack(pady=10)  # Dodaj go z powrotem na oryginalną pozycję

            
    def confirm_noun(self):
        selected_noun = self.noun_selection.get()
    
        self.user_selection['subject' if 'subject' not in self.user_selection else 'complement'] = selected_noun
        if hasattr(self, 'adjective_selection'):
            selected_adjective = self.adjective_selection.get()
            if selected_adjective:
                if not self.is_complement:
                    self.user_selection['subject'] = f"{selected_adjective} {selected_noun}"
                else:
                    self.user_selection['complement'] = f"{selected_adjective} {selected_noun}"

   
        print("Selected subject/complement:", self.user_selection['subject'] if not self.is_complement else self.user_selection['complement'])

        # Jeśli to pierwszy wybór rzeczownika, przechodzimy do czasownika 
        if not self.is_complement:
            self.display_verb_selection()
        else:
            self.final_sentence() 


    def ask_for_pronoun(self):
        self.clear_window()
        
        label = tk.Label(self.master, text="Would you like to add a pronoun (e.g., possessive or demonstrative)?")
        label.pack(pady=10)

        self.pronoun_choice = ttk.Combobox(self.master, values=["None", "Possessive", "Demonstrative"])
        self.pronoun_choice.pack(pady=10)
        
        button = tk.Button(self.master, text="Next", command=self.display_pronoun_options)
        button.pack(pady=10)

    def display_pronoun_options(self):
        pronoun_type = self.pronoun_choice.get()
 
        if not pronoun_type:
            return  

        self.clear_window()
        
        if pronoun_type == "Possessive":
            pronouns = ["my", "your", "his", "her", "its", "our", "their"]  
        elif pronoun_type == "Demonstrative":
            pronouns = ["this", "that", "these", "those"]
        else:
            self.next_step()
            return

        label = tk.Label(self.master, text=f"Select a {pronoun_type.lower()} pronoun:")
        label.pack(pady=10)

        self.additional_pronoun = ttk.Combobox(self.master, values=pronouns)
        self.additional_pronoun.pack(pady=10)

        button = tk.Button(self.master, text="Select", command=self.confirm_pronoun_selection)
        button.pack(pady=10)

    def confirm_pronoun_selection(self):
        selected_pronoun = self.additional_pronoun.get()
        if selected_pronoun:
            self.user_selection['subject'] = f"{selected_pronoun} {self.user_selection['subject']}"
        
        print("Final subject with pronoun:", self.user_selection['subject'])
        self.display_verb_selection()

    
    

    def display_verb_selection(self):
        self.clear_window()

        # Wyświetlenie listy czasowników
        label = tk.Label(self.master, text="Select a verb:")
        label.pack(pady=10)

        self.verb_selection = ttk.Combobox(self.master, values=verbs)
        self.verb_selection.pack(pady=10)

        # Wybór trybu
        mood_label = tk.Label(self.master, text="Select mood:")
        mood_label.pack(pady=10)

        self.mood_selection = ttk.Combobox(self.master, values=moods)
        self.mood_selection.pack(pady=10)

        # Wybór czasu
        tense_label = tk.Label(self.master, text="Select tense:")
        tense_label.pack(pady=10)

        self.tense_selection = ttk.Combobox(self.master, values=tenses)
        self.tense_selection.pack(pady=10)

        # Przycisk do zatwierdzenia wyboru czasownika, trybu i czasu
        button = tk.Button(self.master, text="Select", command=self.confirm_verb_selection)
        button.pack(pady=10)

    def confirm_verb_selection(self):
        
        selected_verb = self.verb_selection.get()
        selected_mood = self.mood_selection.get()
        selected_tense = self.tense_selection.get()

        
        self.user_selection['verb'] = {
            'verb': selected_verb,
            'mood': selected_mood,
            'tense': selected_tense
        }

        print("Selected verb:", self.user_selection['verb'])

       
        self.ask_for_complement()




    def ask_for_complement(self):
        self.clear_window()

     
        label = tk.Label(self.master, text="Do you want to add a complement?")
        label.pack(pady=10)

        
        yes_button = tk.Button(self.master, text="Yes", command=self.add_complement)
        yes_button.pack(side=tk.LEFT, padx=10)

        no_button = tk.Button(self.master, text="No", command=self.final_sentence)
        no_button.pack(side=tk.RIGHT, padx=10)

    def add_complement(self):
        self.is_complement = True  
        self.clear_window()
        self.display_noun_selection()  


    # TODO 
    # logika która zbierając wybrane słowa stworzy poprawne zdanie dla danego języka 
    # czyli odmieni rzeczowniki, czasowniki, da dobre czasy itd
    def final_sentence(self):
        self.clear_window()

        # Wyświetlenie ostatecznego zdania
        subject = self.user_selection.get('subject', '')
        verb = self.user_selection.get('verb', {}).get('verb', '')
        mood = self.user_selection.get('verb', {}).get('mood', '')
        tense = self.user_selection.get('verb', {}).get('tense', '')
        complement = self.user_selection.get('complement', '')

        # Budowanie ostatecznego zdania
        final_sentence = f"{subject} {verb}"
        if complement:
            final_sentence += f" {complement}"

        label = tk.Label(self.master, text=f"Final sentence: {final_sentence}")
        label.pack(pady=10)

        print("Final sentence:", final_sentence)



    def next_step(self):
        self.clear_window()
        # Można dodać kolejne kroki dla czasownika, dopełnienia itp.
        label = tk.Label(self.master, text="Next step would go here...")
        label.pack(pady=10)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageApp(root)
    root.mainloop()
