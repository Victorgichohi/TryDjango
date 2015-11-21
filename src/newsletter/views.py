from django.shortcuts import render

# Create your views here.
def home(request):
    title = "testing meen"

    context = {
    "template_title": title,
    }
    return render(request, "home.html",context)
