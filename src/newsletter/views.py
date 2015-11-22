from django.shortcuts import render

from .forms import SignUPForm,ContactForm

# Create your views here.
def home(request):
    title = "welcome"
    form = SignUPForm(request.Post or None)
    context={
    "title":title,
    "form":form
    }

def home(request):
    title = "testing meen"
    form = SignUPForm(request.POST or None)

    context = {
    "template_title": title,
    "form" : form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name =form.cleaned_data.get("full_name")
        if not full_name:
            full_name="New full name"
        instance.full_name=full_name
        instance.save()

        context={
        "title":"thank you"
        }


    return render(request, "base.html",context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key in form.cleaned_data.iteritems():
            print key
    context={
    "form":form
    }
    return render (request,"forms.html",context)
