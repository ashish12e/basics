import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Gmail credentials
gmail_user = 'ashishankitad7966@gmail.com'
gmail_password = 'beml zbuk cogh aqlt'  # Use an App Password if 2FA is enabled

# Email details
to_email = 'piyush12e@gmail.com'  # Replace with your manager's email
subject = f"Weekly Work Report - {datetime.date.today().strftime('%Y-%m-%d')}"

# Read report content
report_file = r"C:\Users\ashpi\git-projects\dataScience\DataEngMain\projects\basics\myoutfile.txt"
with open(report_file, "r", encoding="utf-8") as f:
    body = f.read()

# Create email
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)