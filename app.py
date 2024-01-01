from flask import Flask, render_template, request
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
import string
nltk.download('stopwords')
nltk.download('punkt')


ps = PorterStemmer()

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    text = request.form['text']

    # Preprocessing text
    def transform_text(text):
        # Lowercase
        text = text.lower()
        # Tokenization
        text = nltk.word_tokenize(text)
        # Removing Special Characters
        y = []
        for i in text:
            if i.isalnum():
                y.append(i)
        # Removing Stop Words & Punctuations
        text = y[:]
        y.clear()
        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)
        # Stemming
        text = y[:]
        y.clear()
        for i in text:
            y.append(ps.stem(i))
        return " ".join(y)

    text = transform_text(text)

    # Load the model and vectorizer
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    # Preprocess the input text
    text_vectorized = vectorizer.transform([text])

    # Make a prediction
    prediction = model.predict(text_vectorized)

    # Display the result
    res= prediction[0]
    if(res==0):
        res= "Ham"
        return render_template('index.html', prediction1=res)
    else:
        res="Spam"
        return render_template('index.html', prediction2=res)
    

if __name__ == '__main__':
    app.run(debug=True)