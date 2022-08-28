from flask import Flask, render_template, request
import json
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text = request.args.get('textToTranslate')
    return translator.english_to_french(text)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text = request.args.get('textToTranslate')
    return translator.french_to_english(text)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
