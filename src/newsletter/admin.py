from django.contrib import admin

# Register your models here.
from .models import SignUP

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timestamp","updated"]
    # class meta:
    #     model = SignUP

admin.site.register(SignUP,SignUpAdmin)
