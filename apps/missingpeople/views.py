import datetime
from bs4 import BeautifulSoup
import requests
from django.db.models import Model
import csv
from django.http import HttpResponse
from .models import People
from django.shortcuts import render

# Create your views here.

url = 'http://brumadinho.vale.com/listagem-pessoas-sem-contato.html'

#Esta view tem a funcao de ler os nomes das vitimas com beautifulsoap e inseri o nome e as informacoes da ultima atualizacao no banco de dados
def missingpeople(request):
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        missinglist = soup.find_all('li')
        lastupdate = soup.find_all('p')
        try:
            p = People.objects.latest('id')
        except People.DoesNotExist:
            p = None
        if p == None:
            i=0
            for person in missinglist:
                p = People(publicdate=lastupdate[3].text, name=person.text)
                p.save()
                i += 1
            html = missinglist
            return HttpResponse(html)
        else:
            if lastupdate[3].text == p.publicdate:
                return HttpResponse(People.objects.all().values_list('name', flat=True))
            else:
                #inseri as pessoas uma a uma para fazer a contagem
                i = 0
                for person in missinglist:
                    p = People(publicdate=lastupdate[3].text, name=person.text)
                    p.save()
                    i += 1
                html = missinglist
                #print('Pessoas Desaparecidas: ', i)
                return HttpResponse(html)
    else:
        return HttpResponse('<h1>Page was found</h1>')

def createcsv(request):
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        missinglist = soup.find_all('li')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)

        i = 0
        for person in missinglist:
            writer.writerow(person.text)
            #p = People(publicdate=lastupdate[3].text, name=person.text)
            #p.save()
            i += 1

        return HttpResponse(response)
    else:
        return HttpResponse('<h1>Page was found</h1>')