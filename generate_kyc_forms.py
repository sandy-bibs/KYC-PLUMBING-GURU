import pandas as pd

# এক্সেল ফাইল থেকে ডেটা পড়ুন
excel_file = r'C:\Users\HP\OneDrive\Desktop\kyc_form_app\data.xlsx'  # সম্পূর্ণ পাথ দিন
df = pd.read_excel(excel_file)  # এক্সেল ফাইল পড়ুন

# HTML টেমপ্লেট লোড করুন
with open('kyc_form.html', 'r', encoding='utf-8') as file:
    html_template = file.read()  # HTML ফাইলটি পড়ুন

# প্রতিটি সারির জন্য HTML ফর্ম তৈরি করুন
for index, row in df.iterrows():
    # HTML টেমপ্লেট কপি করুন
    filled_html = html_template
    
    # প্রতিটি কলামের ডেটা HTML টেমপ্লেটে বসান
    for column in df.columns:
        # কলামের নাম এবং মান ব্যবহার করে HTML টেমপ্লেটে ডেটা বসান
        filled_html = filled_html.replace(f'{{{{{column}}}}}', str(row[column]))
    
    # নতুন HTML ফাইল তৈরি করুন
    with open(f'kyc_form_{index + 1}.html', 'w', encoding='utf-8') as file:
        file.write(filled_html)  # নতুন HTML ফাইল সেভ করুন

print("সব KYC ফর্ম তৈরি করা হয়েছে!")