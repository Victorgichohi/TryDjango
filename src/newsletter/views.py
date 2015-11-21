from django.shortcuts import render

from .forms import SignUPForm

# Create your views here.
def home(request):
    title = "testing meen"
    form = SignUPForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # print instace.email
        print instance.timestamp

    context = {
    "template_title": title,
    "form" : form
    }
    return render(request, "home.html",context)
