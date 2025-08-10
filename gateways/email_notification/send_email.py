import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config_handler import ConfigHandler

class SendEmail:
    """Class to handle sending emails."""
    def __init__(self):
        config = ConfigHandler()
        self.sender_email = config.email_notification_sender
        self.sender_password = config.email_notification_password

    def handle(self, to_email, subject, body, is_html=False):
        """Send an email with plain text or HTML."""
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = to_email
        msg["Subject"] = subject

        # If HTML, wrap in basic styling
        if is_html:
            html_body = f"""
            <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f9f9f9;
                        padding: 20px;
                        color: #333;
                    }}
                    .container {{
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    }}
                    h2 {{
                        color: #007BFF;
                    }}
                    p {{
                        line-height: 1.6;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    {body}
                </div>
            </body>
            </html>
            """
            msg.attach(MIMEText(html_body, "html"))
        else:
            msg.attach(MIMEText(body, "plain"))
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade to secure connection
        server.login(self.sender_email, self.sender_password)
        server.send_message(msg)
        server.quit()
        return True
