import os

from django.http import HttpResponse, HttpRequest, HttpResponseServerError
from django.views import View
from requests import put


class PutImageView(View):
    def post(self, request):
        # type: (HttpRequest) -> HttpResponse

        request.POST.get("pact_endpoint")
        image = open(os.path.dirname(os.path.realpath(__file__)) + '/image.jpg', 'rb')
        pact_endpoint = request.POST.get("pact_endpoint")
        result = put(pact_endpoint, data=image)
        if result.status_code == 200:
            return HttpResponse("Image uploaded")

        return HttpResponseServerError("Something went wrong pact returned: %s - %s" % (result.status_code, result.json().get('message', "error")))