# Email Sending Script

This Python script allows you to send emails with CC and attachments using SMTP.

## Features

- Send emails to multiple recipients.
- Include CC recipients.
- Attach files to your email.
- Uses TLS for secure email transmission.

## Setup

1. **Install Dependencies:**
'pip install secure-smtplib'

2. **Configuration:**
- Update the `send_email` function parameters in the script:
  - `subject`: Subject of the email.
  - `body`: Body/content of the email.
  - `to`: List of recipients' email addresses.
  - `cc`: List of CC recipients' email addresses.
  - `attachments`: List of file paths to be attached to the email.
  - `smtp_server`: SMTP server address (e.g., `"smtp.gmail.com"` for Gmail).
  - `smtp_port`: SMTP server port (e.g., `587` for Gmail).
  - `login`: Your email address used for SMTP authentication.
  - `password`: Your email account password or app password.

3. **Usage:**
- Run the script with Python to send the email:
  ```
  python send_email.py
  ```

4. **Notes:**
- Ensure that your email provider allows access via less secure apps or generate an app-specific password if two-factor authentication is enabled.
