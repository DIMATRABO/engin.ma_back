from gateways.log import Log
from dto.input.contact_us.contact_us_form import ContactUsForm

logger = Log()

class ContactUsUseCase:
    """ Use case for handling contact us form submissions. """

    def handle(self, form: ContactUsForm) -> None:
        """ Process the contact us form submission."""
        logger.log(f"new message from {form.name} // phone number : {form.phone} ({form.email}): {form.message}")