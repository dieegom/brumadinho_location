# -*- coding: utf-8 -*-

import re
import csv
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_raw_data():
    url = "http://brumadinho.vale.com/listagem-pessoas-sem-contato.html"
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.content

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.text
    ultima_atualizacao = re.search('(?<=atualização em ).+(?=\.)'.decode('utf-8'), text).group()
    ultima_atualizacao = datetime.strptime(ultima_atualizacao.encode('utf-8'), '%d/%m/%Y às %H:%M')
    nomes = [i.text.strip() for i in soup.find_all('li')]
    return (ultima_atualizacao, nomes)

if __name__ == "__main__":
    html = get_raw_data()
    dt, pessoas = parse_html(html)
    dt = dt.strftime('%d/%m/%Y - %H:%M')
	
    with open('data.csv', 'w') as f:
        csv_writer = csv.writer(f)

	for pessoa in pessoas:
            csv_writer.writerow((pessoa.encode('utf-8'), dt))
