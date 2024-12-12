# Language Learning Application

This application is a simple yet interactive language learning tool designed to help users construct grammatically correct English sentences. By engaging with the GUI, users can learn about pronouns, nouns, adjectives, possessives, verbs, and their conjugations. The application allows users to select various elements step-by-step to form complete sentences.

## Features

- **Pronoun and Noun Selection:**
  Users can start by selecting a subject type (pronoun or noun). If a noun is chosen, users may also add an adjective or possessive modifier.

- **Adjective and Possessive Modifiers:**
  Enhance the selected noun by adding optional adjectives or possessive pronouns.

- **Verb Conjugation:**
  The application uses the `mlconjug3` library to conjugate verbs based on the selected tense and mood.

- **Sentence Construction:**
  Step-by-step guidance helps users construct sentences while ensuring grammatical accuracy.

## Prerequisites

To run this application, you need the following installed:

- Python 3.8+
- `tkinter` (comes pre-installed with Python)
- `mlconjug3`
- `textblob`

Install the required Python packages with the following command:

```bash
pip install mlconjug3 textblob
```

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Ensure all required dependencies are installed:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the application by executing the following command:

```bash
python handling.py
```

The graphical user interface (GUI) will launch, allowing you to interact with the application.

## Usage

1. **Start Selection:**
   Choose a subject type (Pronoun or Noun).

2. **Pronoun Selection:**
   If you select "Pronoun," choose from a list of predefined pronouns.

3. **Noun Selection:**
   If you select "Noun," you can also:
   - Choose between singular and plural forms.
   - Optionally add an adjective or possessive pronoun.

4. **Verb Selection:**
   - Select a verb from the list.
   - Choose a mood (Indicative or Imperative).
   - Choose a tense (Present, Past, or Future).

5. **Finalize Sentence:**
   The application constructs and displays a complete sentence based on your selections.

## Example Workflow

1. Select "Noun" as the subject type.
2. Choose "dog" as the noun.
3. Add the adjective "small" and the possessive pronoun "my."
4. Select "Be" as the verb, "Indicative" as the mood, and "Present" as the tense.
5. The application outputs: "My small dog is."

## Dependencies

- `mlconjug3`: Handles verb conjugation.
- `textblob`: Provides tools for pluralizing nouns.
- `tkinter`: Used to create the GUI.

## Extending the Application

### Adding New Data

- **Pronouns:** Update the `pronouns` list.
- **Nouns:** Add to the `nouns` list.
- **Adjectives:** Extend the `adjectives` list.
- **Verbs:** Add new verbs to the `verbs` list.

### Supporting Additional Languages

- Replace the `Conjugator` initialization with a different language (e.g., `Conjugator(language="es")` for Spanish).

## Known Limitations

- The current dataset includes limited nouns, adjectives, and verbs. Expanding these lists can enhance the user experience.
- Currently supports only English.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, please contact:

- **Name:** Your Name
- **Email:** your.email@example.com

