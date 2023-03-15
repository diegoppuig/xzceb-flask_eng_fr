from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(english_text):
    textToTranslate = request.args.get('textToTranslate')
    french_text = transaltor.english_to_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish(french_text):
    textToTranslate = request.args.get('textToTranslate')
    french_text = transaltor.french_to_english(textToTranslate)
    return english_text
    
@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
