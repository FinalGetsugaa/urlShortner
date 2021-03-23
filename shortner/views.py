import uuid
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from shortner.models import Url


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        print("in here")
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, uid):
    url_details = Url.objects.get(uuid=uid)
    return redirect(url_details.link)
