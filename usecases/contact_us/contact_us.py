from gateways.log import Log
from gateways.email_notification.send_email import SendEmail
from dto.input.contact_us.contact_us_form import ContactUsForm

logger = Log()
email_sender = SendEmail()

class ContactUsUseCase:
    """ Use case for handling contact us form submissions. """

    def handle(self, form: ContactUsForm) -> None:
        """ Process the contact us form submission."""
        logger.log(f"new message from {form.name} // phone number : {form.phone} ({form.email}): {form.message}")
        if email_sender.handle('aitbenhaanass@gmail.com', 
                               'New Contact Us Message', 
                               f"new message from {form.name} // phone number : {form.phone} ({form.email}): {form.message}"):
            return {"message": "Your message has been sent successfully."}
        else:
            raise Exception("Failed to send email notification.")
