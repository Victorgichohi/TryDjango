from django.shortcuts import render

from .forms import SignUPForm

# Create your views here.
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


    return render(request, "home.html",context)
