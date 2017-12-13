from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View 
from django.template.loader import get_template

from .utils import render_to_pdf


def index(request):
	return render(request, 'generatorPDF/index.html')

class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('generatorPDF/relatorio.html')

		curso = request.GET['curso']
		aula = request.GET['aula']
		resumo = request.GET['resumo']
		resultados = request.GET['resultados']
		link = request.GET['link']
		observacoes = request.GET['observacoes']

		if curso == "apps":
			curso = "Aplicativos"
		elif curso == "robotica":
			curso = "Robótica"

		context = {

			"curso": curso,
			"aula": aula,
			"resumo": resumo,
			"resultados": resultados,
			"link": link,
			"observacoes": observacoes,

		}
		html = template.render(context)
		pdf = render_to_pdf('generatorPDF/relatorio.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Relatório.pdf"
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not Found")

def generate_view(request, *args, **kwargs):
		template = get_template('generatorPDF/relatorio.html')

		curso = request.GET['curso']
		aula = request.GET['aula']
		resumo = request.GET['resumo']
		resultados = request.GET['resultados']
		link = request.GET['link']
		observacoes = request.GET['observacoes']

		if curso == "apps":
			curso = "Aplicativos"
		elif curso == "robotica":
			curso = "Robótica"
			
		context = {

			"curso": curso,
			"aula": aula,
			"resumo": resumo,
			"resultados": resultados,
			"link": link,
			"observacoes": observacoes,

		}
		html = template.render(context)
		return HttpResponse(html)