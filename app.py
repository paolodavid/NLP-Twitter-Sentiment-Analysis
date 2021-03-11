from flask import Flask, render_template, url_for, request
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle
import re

model = keras.models.load_model("./models/Model.h5")
with open("./models/tokenizer.pickle", "rb") as tok:
	tokenizer = pickle.load(tok)


def preprocess_text(text):
	text = text.lower()
	text = [text]
	seq_text = tokenizer.texts_to_sequences(text)
	final_text = pad_sequences(seq_text, maxlen=20, dtype="int32", value=0)
	return final_text


app = Flask(__name__)
 
@app.route("/", methods=["GET","POST"])
def home():
	return(render_template("home.html"))

@app.route("/predict", methods=["GET", "POST"])
def predict():
	if request.method=="POST":
		text = request.form['text']
		ready_text = preprocess_text(text)
		prediction = model.predict(ready_text)
		prediction = round(float(prediction))
		result = ""
		if prediction == 0:
			result = "Negative"
		elif prediction == 1:
			result = "Positive"

		return render_template("home.html", prediction = prediction)
	else:
		return render_template("home.html")
	
if __name__ == "__main__":
	app.run()
