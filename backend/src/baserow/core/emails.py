from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class BaseEmailMessage(EmailMultiAlternatives):
    """
    The base email message class can be used to create reusable email classes for
    each email. The template_name is rendered to a string and attached as html
    alternative. This content is automatically converted to plain text. The get_context
    method can be extended to add additional context variables while rendering the
    template.

    Example:
        class TestEmail(BaseEmailMessage):
            subject = 'Example subject'
            template_name = 'baserow/core/example.html'

        email = TestEmail(['test@localhost'])
        email.send()
    """

    subject = None
    template_name = None

    def __init__(self, to, from_email=None):
        if not from_email:
            from_email = self.get_from_email()

        subject = self.get_subject()
        template_name = self.get_template_name()
        context = self.get_context()
        html_content = render_to_string(template_name, context)

        try:
            body_start_index = html_content.index('<body>')
            body_end_index = html_content.index('</body>')
            html_content = html_content[body_start_index:body_end_index]
        except ValueError:
            pass

        text_content = strip_tags(html_content)

        super().__init__(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=to
        )
        self.attach_alternative(html_content, 'text/html')

    def get_context(self):
        return {
            'public_backend_domain': settings.PUBLIC_BACKEND_DOMAIN,
            'public_backend_url': settings.PUBLIC_BACKEND_URL,
            'public_web_frontend_domain': settings.PUBLIC_WEB_FRONTEND_DOMAIN,
            'public_web_frontend_url': settings.PUBLIC_WEB_FRONTEND_URL
        }

    def get_from_email(self):
        return settings.FROM_EMAIL

    def get_subject(self):
        if not self.subject:
            raise NotImplementedError('The subject must be implement.')
        return self.subject

    def get_template_name(self):
        if not self.template_name:
            raise NotImplementedError('The template_name must be implement.')
        return self.template_name
