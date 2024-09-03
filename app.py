from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for checking if input exists
@app.route('/check', methods=['POST'])
def check_input():
    user_input = request.json.get('input')  # מקבל קלט מהמשתמש
    # בדיקה האם הקלט קיים במסד הנתונים
    items = ['apple', 'banana', 'orange']  # נתונים לדוגמה
    if user_input in items:
        return jsonify({'result': 'קיים'})
    else:
        return jsonify({'result': 'לא קיים'})

if __name__ == '__main__':
    app.run(debug=True)
