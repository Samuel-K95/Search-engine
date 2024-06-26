from django.shortcuts import render
from . import preprocessing
# Create your views here.


def view_documents(request):
    files = preprocessing.PreProcessing()
    files.process()
    files.tokenize()
    files.stop_word_stem()
    files.vectorize()

    query =  ''' Here we discuss proportion of inputs producers 
employ and how much maximum output they 
produce from the inputs 
• Production is the process of creating goods or 
services that have economic value either to 
consumers or producers
• It is the process of changing input into output to 
create utility 
• Production Function: is the maximum quantity of 
output that can be produced from the given amount 
of available inputs for a given technology '''

    ranked = files.rank_documents(query)

    return render(request, 'searchapp/test.html', {'file_content': ranked})

    