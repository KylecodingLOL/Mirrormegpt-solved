import re
import spacy

# Load the English language model from spaCy
nlp = spacy.load('en_core_web_sm')

def check_ai_generated(text):
    """
    This function checks a given text for unicode spaces and non-English letters 
    and highlights them for easy identification.
    """
    
    # Defined a list of special spaces characters to be checked
    special_spaces = [
        '\u2423', '\u2000', '\u2001', '\u2002', '\u2003',
        '\u2004', '\u2005', '\u2006', '\u2007', '\u2008',
        '\u2009', '\u200A', '\u202F', ' '
    ]
    
    # Used regular expressions to split the text into words and special characters
    words = re.findall(r'\b[\w\']+|[:;][-~]?[)D]|#|[,!?;:]|' + '|'.join(special_spaces), text)
    
    # Defined a set of characters representing the English alphabet and common symbols
    english_alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[]{}|;:\'",.<>?/\\ ')
    
    # Initialized a list to store highlighted text
    highlighted_text = []
    
    for word in words:
        if word in special_spaces:
            word = '\033[43m' + word + '\033[0m'  
        elif word in [',', '.', '!', '?', ';', ':', ':)', ':(', ';)', ';(', ':-)', ':~)', ':D', '#']:
            highlighted_text[-1] += word 
            continue
        else:
            punctuation = ""
            if word[-1] in ".!":
                word, punctuation = word[:-1], word[-1]

            if not all(char in english_alphabet for char in word):
                word = f"\033[93m{word}\033[0m" 
                
        highlighted_text.append(f"{word}{punctuation}")

    highlighted_text = ' '.join(highlighted_text)
    
    print(highlighted_text)

    # Check if there are highlighted non-English words or special spaces
    if "\033[93m" in highlighted_text or "\033[43m" in highlighted_text:
        print("This text might attempt to evade AI detection by incorporating non-English letters and special spaces.")

# Sample text for testing
sample_text = """Hire me :)  #speciаl chаrаcters.
"""


check_ai_generated(sample_text)
