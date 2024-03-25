from google.cloud import translate_v2 as translate


# print(googletrans.LANGUAGES)
translate_client = translate.Client()
target_language = 'ja'


def japanesetrans(text):
    translation = translate_client.translate(
        text, target_language=target_language)
    translated_text = translation['translatedText']
    return translated_text


def main():
    pass


if __name__ == "__main__":
    main()


'''
from google.cloud import translate_v2 as translate
# Initialize the translation client
translate_client = translate.Client()

# Define text to translate
text = 'Hello, world!'

# Define target language
target_language = 'ja'  # French

# Translate the text
translation = translate_client.translate(text, target_language=target_language)

# Print the translated text
print('Translated Text: {}'.format(translation['translatedText']))
'''
