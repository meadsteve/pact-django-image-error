from django import forms
from django.http import HttpResponse, HttpRequest
from django.views import View
from requests import put

class PutImageForm(forms.Form):
    image = forms.ImageField(required=True)
    pact_endpoint = forms.CharField(required=True)

class PutImageView(View):
    def post(self, request):
        form = PutImageForm(request.POST, request.FILES)
        if not form.is_valid():
            raise Exception("We're missing some data")

        image = form.cleaned_data.get('image')
        pact_endpoint = form.cleaned_data.get('pact_endpoint')
        result = put(pact_endpoint, data=image)
        if result.status_code == 200:
            return HttpResponse("Image uploaded")

        raise Exception("Something went wrong pact returned: %s" % result.status_code)