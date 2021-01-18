from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.files.storage import FileSystemStorage
import json

# Create your views here.
def index(request):
    context = {
        'title':'Home page'
    }
    return render(request, "frontend/index.html", context)

# upload cv module
def upload_cv(request):
    title = 'Upload Your CV'
    if request.method == 'POST':
        upload_file = request.FILES['upload_cv']
        fs = FileSystemStorage()
        #print('filename: ', upload_file['upload_cv'].name)
        fs.save(upload_file.name, upload_file)

        # recapcha
        clientKey = request.POST['g-recapcha-response']
        secretKey = ''
        capchaData = {
            'secret':secretKey,
            'response':clientKey,
        }
        r = request.post('', data=capchaData)
        response = json.loads(r.text)
        verify = response['success']
        if verify:
            title = '! Your CV uploaded successfully.'

    context = {
        'title':title,
    }
    return render(request, "frontend/upload-cv.html", context)
