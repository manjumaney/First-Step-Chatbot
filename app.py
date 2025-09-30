from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Replace 'your_student_number' with your actual student number
    student_number = ''
    return jsonify({'student_number': student_number})

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    # This is where you can process Dialogflow requests.
    # For simplicity, we'll return a static response.
    response = {
        'fulfillmentText': 'This is the response from your webhook.'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
