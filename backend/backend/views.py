from django.shortcuts import render
from django.http import request
from django.core.mail import send_mail
from django.template.loader import render_to_string

def index(request):
    return render(request, "index.html")

def mision(request):
    return render(request, "mision.html")

def vision(request):
    return render(request, "vision.html")

def portafolio(request):
    return render(request, "portafolio.html")

def contacto(request):

    if request.method == "POST":
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        subject = 'Asunto del Correo'
        from_email = 'ramdox2002@gmail.com'
        recipient_list = [email]

        # Renderiza la plantilla HTML
        message = render_to_string('mail/send.html', {
            "name": name,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "message": message
        })

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        print(request.POST, name, lastname, email, phone, message)

    return render(request, "contacto.html")