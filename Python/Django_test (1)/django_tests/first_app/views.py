from django.shortcuts import render, redirect

# Create your views here.


def hello_world(request):
    my_string = "Hello World!"
    return render(request, "first_app/hello.html", {"my_string": my_string})

def country_world(request, country:str):
    if country == "fr":
        my_string = "Bonjour le monde!"
    elif country == "de":
        my_string = "Hallo Welt!"
    elif country == "es":
        my_string = "¡Hola Mundo!"
    else:
        return redirect("index")
    return render(request, "first_app/hello.html", {"my_string": my_string, "country": country})
