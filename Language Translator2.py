import datetime

def translate_to_hindi(word):
    # Mock translation function
    translations = {
        'hello': 'नमस्ते',
        'world': 'दुनिया',
        'good': 'अच्छा',
        'morning': 'सुबह'
    }
    return translations.get(word.lower(), "Translation not found")

def starts_with_vowel(word):
    return word[0].lower() in 'aeiou'

def is_within_restricted_time():
    # Get the current time in IST (GMT+5:30)
    current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    return current_time.hour == 21  # 9 PM to 10 PM IST

def main():
    word = input("Enter an English word: ")

    if starts_with_vowel(word):
        print("Translation skipped for words starting with vowels.")
        return

    if is_within_restricted_time():
        print("Translation is not allowed between 9 PM to 10 PM IST.")
        return

    hindi_translation = translate_to_hindi(word)
    print(f"The Hindi translation of '{word}' is: {hindi_translation}")

if _name_ == "_main_":
    main()