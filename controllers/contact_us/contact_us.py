''' Contact Us API Controller'''
from flask import request
from flask_restx import Namespace
from decorations.exception_handling import handle_exceptions

from dto.input.contact_us.contact_us_form import ContactUsForm
from usecases.contact_us.contact_us import ContactUsUseCase


contact_ns = Namespace("contact", description="Contact us operations")
contact_use_case = ContactUsUseCase()

@contact_ns.route('')
class ContactUsController:
    ''' Contact Us endpoint.'''
    
    @contact_ns.expect(ContactUsForm.api_model(contact_ns))
    @handle_exceptions
    def post(self):
        ''' Handle contact us form submission.'''
        form = ContactUsForm(request.get_json())
        contact_use_case.handle(form)
        return {"message": "Your message has been sent successfully."}