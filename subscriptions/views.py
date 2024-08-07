from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.conf import settings
import os

def subscribe(request):
    if request.method == 'POST':
        subject = 'Python (Selenium) Assignment - Venuchander'
        message = 'https://github.com/Venuchander/DjangoEmailSender \nhttps://github.com/Venuchander/GoogleFormSeleniumAutomation'
        recipient = 'tech@themedius.ai'
        cc_recipient = 'hr@themedius.ai'
        
        # Create the email
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient],
            cc=[cc_recipient]
        )
        
        # Attach the PNG file
        file_path = os.path.join(settings.BASE_DIR, 'static/image/attachment.png')
        email.attach_file(file_path)
        
        # Send the email
        email.send(fail_silently=False)
        
        messages.success(request, 'Success!')
        return redirect('subscribe')
    
    return render(request, 'subscriptions/home.html')
