import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, to, cc, attachments, smtp_server, smtp_port, login, password):
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = ', '.join(to)
    msg['Cc'] = ', '.join(cc)
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
    for filename in attachments:
        attachment = open(filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(part)

    # Combine recipient lists
    recipients = to + cc

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(login, recipients, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Email details
subject = "Subject"
body = "Main Body"
to = ["recipents mail"]
cc = ["cc mail"]
attachments = ["path of your file"]

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "your_email_address"
password = "your_app_password"

# Send the email
send_email(subject, body, to, cc, attachments, smtp_server, smtp_port, login, password)
