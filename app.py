from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()  # JSON ডেটা সংগ্রহ করুন
    
    # এক্সেল ফাইল লোড/তৈরি করুন
    try:
        df = pd.read_excel('data.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame()
    
    # নতুন ডেটা যোগ করুন
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    
    # এক্সেলে সেভ করুন
    df.to_excel('data.xlsx', index=False)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)