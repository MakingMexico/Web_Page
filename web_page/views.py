from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from forms import ContactForm


class IndexView(TemplateView):
    template_name = "index.html"


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        contact_email = form.cleaned_data['contact_email']
        message = form.cleaned_data['message']
        send_mail('Professor request',
                  message,
                  contact_email,
                  ['yapase.mx@gmail.com'])
        return super(ContactView, self).form_valid(form)
