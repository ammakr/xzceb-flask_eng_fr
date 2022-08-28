import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def english_to_french(english_text: str):
    if english_text is None:
        return
    try:
        translated_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translated_text['translations'][0]['translation']
    except ApiException as ex:
        french_text = ''
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

    return french_text

def french_to_english(french_text: str):
    if french_text is None:
        return

    try:
        translated_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text = translated_text["translations"][0]["translation"]
    except ApiException as ex:
        english_text = ''
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
    
    return english_text
