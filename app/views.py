# views.py sử dụng để điều hướng / hiển thị giao diện web app

from flask import json
from app import app
from flask import render_template
from .forms import InputTextForm
##########
from model import model
from preprocess import preprocessing_doc
from extract_feature import text_to_vector
# Submit button in web for pressed
@app.route('/', methods=['POST'])
@app.route('/result.html', methods=['POST'])
def manageRequest():
    print('POST')

    theInputForm = InputTextForm()

    userText = theInputForm.inputText.data
    print(userText)
    print('---')
    test_doc = preprocessing_doc(userText)
    test_doc_tfidf = text_to_vector(test_doc)
    print(test_doc_tfidf)
    label = model.predict(test_doc_tfidf)[0]
    print(label)

    return render_template('result.html',
                           your_text=test_doc,
                           predicted_label=label
                           )

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def initial():
    print('Hello World! index.html')
    return render_template('index.html',
                           title='Hello New World!',
                           form=InputTextForm())
