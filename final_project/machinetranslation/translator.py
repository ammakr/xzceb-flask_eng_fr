import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')


def englishToFrench(englishText: str):
    try:
        translated_text = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        frenchText = translated_text['translations'][0]['translation']
    except ApiException as ex:
        frenchText = ''
        print("Method failed with status code " + str(ex.code) + ": " + ex.message

    return frenchText


def frenchToEnglish(frenchText: str):
    try:
        translated_text = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        englishText = translated_text["translations"][0]["translation"]
    except ApiException as ex:
        englishText = ''
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
    
    return englishText
