import os
folder_path = "path/to/your/folder"
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        new_name = filename.replace(".txt", "_updated.txt")
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
import requests
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = [a['href'] for a in soup.find_all('a', href=True)]
print(links)
import smtplib
from email.mime.text import MIMEText
sender = "your_email@example.com"
recipient = "recipient_email@example.com"
subject = "Automated Email"
body = "Hello, this is an automated email."
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login(sender, "your_password")
    server.sendmail(sender, recipient, msg.as_string())
import pandas as pd
df = pd.read_csv("data.csv")
df = df.dropna()
df.to_excel("cleaned_data.xlsx", index=False)
import schedule
import time

def job():
    print("Task running...")
schedule.every(10).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
import requests
api_url = "https://api.example.com/data"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print(data)
import pyautogui
pyautogui.hotkey('win', 'r')
pyautogui.write('notepad')
pyautogui.press('enter')
