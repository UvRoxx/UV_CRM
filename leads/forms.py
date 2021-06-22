from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Agent, Lead


# name = models.CharField(max_length=50)
#     url = models.URLField(max_length=400)
#     email = models.EmailField(max_length=50, null=True)
#     number = PhoneNumberField(blank=True, null=True)
#     contacted = models.BooleanField(default=False)
#     agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True, blank=True)
#


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "name",
            "number",
            "email",
            "agent",
            "url"
        )


class LeadForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    email = forms.EmailField()
    number = PhoneNumberField()
