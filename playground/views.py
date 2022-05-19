from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(template_name='emails/test.html', context={})
        #mail_admins('test', 'a test', html_message='a test')
        #send_mail('test', 'test message', 'some@some.com', ['some@s.com'])
        message.send(['test@t.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
