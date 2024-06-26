from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import os
from . import preprocessing
# Create your views here.


def home_page(request):
    return render(request, "searchapp/index.html")

def upload_file(request):
    print("in backend")
    if request.method == 'POST' and request.FILES.getlist('files'):
        files = request.FILES.getlist('files')
        for file in files:
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        return JsonResponse({})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def view_documents(request):
    if request.method == 'POST':
        ranked = []
        try:
            files = preprocessing.PreProcessing()
            files.process()
            files.tokenize()
            files.stop_word_stem()
            files.vectorize()

            query = request.POST.get('query')
            print("query", query)

            ranked = files.rank_documents(query)
            print("ranked",ranked)
        except Exception as e:
            print(e)

        return render(request, 'searchapp/test.html', {'file_content': ranked})
    else:
        return render(request, 'searchapp/index.html')

    