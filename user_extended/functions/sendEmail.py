def sendEmail(request, messages):
    from django.conf import settings
    # from django.core.mail import send_mail
    #
    subject = "You've registered to apartments website"
    # message = f'''Hi {request.user.username}, thank you for registering in our website.
    #             Your username is: {request.user.username}'''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]
    # send_mail(subject=subject,
    #           message=message,
    #           from_email=email_from,
    #           recipient_list=recipient_list,
    #           fail_silently=False)

    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import get_template
    from django.template import Context

    plaintext = get_template('email/registered.txt')
    html = get_template('email/registered.html')

    # d = Context({'username': request.user.username})  # context must be a dict rather than Context
    d = {'username': request.user.username}

    subject = subject
    from_email = email_from
    to = recipient_list
    text_content = plaintext.render(d)
    html_content = html.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    messages.success(request,
                     f'message sent successfully')

