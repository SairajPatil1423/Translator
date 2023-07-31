from translate import Translator


def translate_text(text, target_language, source_language="en"):
    translator = Translator(from_lang=source_language, to_lang=target_language)
    translation = translator.translate(text)
    return translation


if __name__ == "__main__":
    while True:
        print("1. English to Marathi")
        print("2. Marathi to English")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            text = input("Enter the English text: ")
            translated_text = translate_text(text, target_language="mr")
            print("Marathi Translation:", translated_text)

        elif choice == 2:
            text = input("Enter the Marathi text: ")
            translated_text = translate_text(text, target_language="en", source_language="mr")
            print("English Translation:", translated_text)

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
