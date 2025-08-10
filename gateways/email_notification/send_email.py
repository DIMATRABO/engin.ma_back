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

    def handle(self, to_email, subject, body):
        """Send an email."""
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))


        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade to secure connection
        server.login(self.sender_email, self.sender_password)
        server.send_message(msg)
        server.quit()
        return True
