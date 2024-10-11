import tkinter as tk
from tkinter import ttk
from mlconjug3 import Conjugator
from textblob import Word


# Przykładowe dane - on wymaga po 50 rzecz przym i czasownikow 
pronouns = ["I", "you", "he", "she", "it", "we", "they"]
nouns = ["water", "food", "mother", "father", "house", "car", "dog", "cat", "money", "area", "family", "word", "brother", "sister", "bed", "kitchen", "restaurant", "bird", "tree", "flower", "animal", "mobile phone", "sun", "moon", "sea", "river", "weather", "eyes", "ears", "hair", "shoes", "bag", "train", "bus", "knife", "fork", "spoon", "breakfast", "dinner", "bread", "fruit", "vegetables", "meat", "drink", "town", "village", "toilet", "weekend", "doctor", "policeman"]
adjectives = ["good", "big", "small", "bad", "red", "blue", "happy", "beautiful", "open", "green", "closed", "new", "old", "clean", "strong", "young", "expensive", "early", "fast", "dark", "delicious", "soft", "dirty", "empty", "far", "sad", "free", "full", "funny", "hard", "heavy", "hungry", "interesting", "kind", "late", "yellow", "light", "quiet", "ready", "slow", "smart", "tall", "thirsty", "ugly", "weak", "bright", "short", "serious", "stupid", "honest"]
verbs = ["Be", "Have", "Do", "Say", "Go", "Get", "Make", "Know", "Think", "Take", "See", "Come", "Want", "Look", "Use", "Find", "Give", "Tell", "Work", "Call", "Try", "Ask", "Need", "Feel", "Become", "Leave", "Put", "Mean", "Keep", "Let", "Begin", "Seem", "Help", "Talk", "Turn", "Start", "Show", "Hear", "Play", "Run", "Move", "Like", "Live", "Believe", "Hold", "Bring", "Happen", "Write", "Provide", "Sit"]
moods = ["Indicative", "Imperative"]
tenses = ["Present", "Past", "Future"]
class LanguageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Learning App")
        self.is_complement = False
        self.user_selection = {}
        self.conjugator = Conjugator(language="en")
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
        self.user_selection['subject_type'] = 'pronoun'
        print("Selected subject:", selected_pronoun)
        self.display_verb_selection()



    def display_noun_selection(self, arg=False):
        label = tk.Label(self.master, text="Select a noun:")
        label.pack(pady=10)

        self.noun_selection = ttk.Combobox(self.master, values=nouns)
        self.noun_selection.pack(pady=10)

        label_number = tk.Label(self.master, text="Choose number (singular or plural):")
        label_number.pack(pady=10)

        self.number_selection = ttk.Combobox(self.master, values=["Singular", "Plural"])
        self.number_selection.pack(pady=10)

        # Opcja dodania przymiotnika
        self.adjective_check = tk.Checkbutton(self.master, text="Add an adjective", command=self.toggle_adjective)
        self.adjective_check.var = tk.BooleanVar()
        self.adjective_check["variable"] = self.adjective_check.var
        self.adjective_check.pack(pady=10)
        self.select_button = tk.Button(self.master, text="Select", command=lambda: self.confirm_noun(arg))
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

        else:
            if hasattr(self, 'adjective_selection'):
                self.adjective_selection.destroy()

            self.select_button.pack_forget()
            self.select_button.pack(pady=10)



    def confirm_noun(self, arg):
        selected_noun = self.noun_selection.get()
        selected_number = self.number_selection.get()


        noun_number = "singular" if selected_number == "Singular" else "plural"
        self.user_selection['noun_number'] = noun_number

        if selected_number == "Plural":

            blob = Word(selected_noun)
            selected_noun = blob.pluralize()

        self.user_selection['subject_type'] = 'noun'

        if not self.is_complement:
            self.user_selection['subject'] = selected_noun
        else:
            if 'complement' not in self.user_selection:
                self.user_selection['complement'] = {}

            self.user_selection['complement']['subject'] = selected_noun

        if hasattr(self, 'adjective_selection'):
            selected_adjective = self.adjective_selection.get()
            if selected_adjective:
                if not self.is_complement:
                    self.user_selection['subject'] = f"{selected_adjective} {selected_noun}"
                if arg:
                    self.user_selection['complement']['subject'] = f"{selected_adjective} {selected_noun}"
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

    def display_verb_selection(self, go=False):
        self.clear_window()
        if go:
            self.clear_window()
            label = tk.Label(self.master, text="Select a verb:")
            label.pack(pady=10)
            verbs.remove('Go')
            self.verb_as_complement_selection = ttk.Combobox(self.master, values=verbs)
            self.verb_as_complement_selection.pack(pady=10)
            self.confirm_button = tk.Button(self.master, text="Select", command=self.confirm_go_second_verb_selection)
            self.confirm_button.pack(pady=10)
        # Display verb selection
        else:
            label = tk.Label(self.master, text="Select a verb:")
            label.pack(pady=10)

            self.verb_selection = ttk.Combobox(self.master, values=verbs)
            self.verb_selection.pack(pady=10)

            # Display mood selection
            mood_label = tk.Label(self.master, text="Select mood:")
            mood_label.pack(pady=10)

            self.mood_selection = ttk.Combobox(self.master, values=moods)
            self.mood_selection.pack(pady=10)
            self.mood_selection.bind("<<ComboboxSelected>>", self.mood_selected)

            # Display tense selection (initially hidden)
            self.tense_label = tk.Label(self.master, text="Select tense:")
            self.tense_selection = ttk.Combobox(self.master, values=tenses)

            if self.mood_selection.get() == "Imperative":
                if self.verb_selection.get().lower() in ["go", "be"]:
                    self.confirm_button = tk.Button(self.master, text="Select", command=self.go_or_be_confirm_verb_selection())
            self.confirm_button = tk.Button(self.master, text="Select", command=self.confirm_verb_selection)

    def mood_selected(self, event):
        selected_mood = self.mood_selection.get()
        if selected_mood == "Imperative":
            self.tense_label.pack_forget()
            self.tense_selection.pack_forget()
            self.tense_message = tk.Label(self.master, text="Imperative is in English always the same, regardless of the subject\n"
                                                            "So we are not going to show the subject here.")
            self.tense_message.pack(pady=10)
            self.confirm_button.pack(pady=10)
        else:
            if hasattr(self, 'tense_message'):
                self.tense_message.pack_forget()
            self.tense_label.pack(pady=10)
            self.tense_selection.pack(pady=10)
            self.confirm_button.pack(pady=10)

    def confirm_verb_selection(self):

        selected_verb = self.verb_selection.get()
        selected_mood = self.mood_selection.get()
        selected_tense = self.tense_selection.get()


        self.user_selection['verb'] = {
            'verb': selected_verb,
            'mood': selected_mood.lower(),
            'tense': selected_tense
        }

        print("Selected verb:", self.user_selection['verb'])
        self.ask_for_complement()

    def confirm_go_second_verb_selection(self):
        selected_complement_verb = self.verb_as_complement_selection.get()
        self.user_selection['complement'] = {
            'verb': selected_complement_verb,
        }
        print("Selected complement verb:", self.user_selection['complement']['verb'])
        self.ask_for_complement(go=True)


    def go_or_be_confirm_verb_selection(self):
        selected_verb = self.verb_selection.get()
        selected_mood = self.mood_selection.get()
        self.user_selection['verb'] = {
            'verb': selected_verb,
            'mood': selected_mood.lower()
        }

        print("Selected verb:", self.user_selection['verb'])
        self.ask_for_complement()


    def ask_for_complement(self, go=False):
        self.clear_window()

        verb = self.user_selection.get('verb', {}).get('verb', '').lower()
        mood = self.user_selection.get('verb', {}).get('mood', '').lower()

        func = self.add_complement

        if mood == 'imperative' and verb =='go' and go==False:
            func = self.go_complement
        elif mood == 'imperative' and verb =='be':
            func= self.be_complement

        label = tk.Label(self.master, text="Do you want to add a complement?")
        label.pack(pady=10)

        yes_button = tk.Button(self.master, text="Yes", command=func)
        yes_button.pack(side=tk.LEFT, padx=10)

        no_button = tk.Button(self.master, text="No", command=self.final_sentence)
        no_button.pack(side=tk.RIGHT, padx=10)



    def add_complement(self):

        verb = self.user_selection.get('verb', {}).get('verb', '')
        arg=False
        if verb:
            arg =True
        self.is_complement = True
        self.clear_window()
        self.display_noun_selection(arg)

    def go_complement(self):
        self.clear_window()
        self.display_verb_selection(True)





    # TODO
    # logika która zbierając wybrane słowa stworzy poprawne zdanie dla danego języka
    # czyli odmieni rzeczowniki, czasowniki, da dobre czasy itd
    def final_sentence(self):
        self.clear_window()
        final_sentence =""
        # Wyświetlenie ostatecznego zdania
        subject = self.user_selection.get('subject', '')
        subject_procedence = self.user_selection.get('subject_type', '')
        verb = self.user_selection.get('verb', {}).get('verb', '')
        mood = self.user_selection.get('verb', {}).get('mood', '').lower()
        tense = self.user_selection.get('verb', {}).get('tense', '').lower()
        complement = self.user_selection.get('complement', {})
        number = self.user_selection.get('noun_number', '')

        # Verb conjugation
        if mood=='indicative':
            if (subject_procedence == 'noun' and number == 'singular') or (subject_procedence == 'pronoun' and any(pronoun in subject for pronoun in ['he', 'she', 'it'])):
                subject_key = 'he/she/it'
            else:
                subject_key = 'they'
            tense = 'past tense' if tense == 'past' else tense
            if tense!= 'future':
                mood_tense_key = f"{mood} {tense}"
                verb = self.conjugator.conjugate(verb)
                verb_conjugated = verb[mood][mood_tense_key][subject_key]
            else:
                verb_conjugated = f"will {verb.lower()}"

            # Building the final sentence
            final_sentence = f"{subject.capitalize()} {verb_conjugated}"
            if complement:
                final_sentence += f" {complement['subject']}"
        else:
            final_sentence = f"{verb.capitalize()}"
            if complement:
                verb_comp = complement.get('verb','')
                subject_comp= complement.get('subject','')
                final_sentence += f" {verb_comp.lower()} {subject_comp.lower()}"

        # Displaying the final sentence
        label = tk.Label(self.master, text=f"Final sentence: {final_sentence}")
        label.pack(pady=10)

        # Printing the final sentence to the console for debugging purposes
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

