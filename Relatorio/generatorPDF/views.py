from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from easy_pdf.views import PDFTemplateView
#from django.template import Context, Template


#class HelloPDFView(PDFTemplateView):


        

def index(request):
    return render(request, 'generatorPDF/index.html', {})

        
        #return render(request, 'generatorPDF/relatorio.html', Context({"curso_template": curso}))

