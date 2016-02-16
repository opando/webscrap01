import urllib2
import codecs
from bs4 import BeautifulSoup
f1=codecs.open('lista.txt', 'w+', "utf-8")

for i in range (1, 260):
		url = "http://www.admision.uni.edu.pe/resultado_adm.php?pagina=" + str(i) + "&txt_numins=&txt_paterno=&txt_materno=&txt_nombres="
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page,"html.parser")
		for tr in soup.select('.lista_1'):
				tds = tr.find_all('td')
				f1.write(tds[0].text + "," + tds[1].text + "," + tds[2].text + "," + tds[3].text + "," + tds[4].text + ", merito :" + tds[15].text + "," + tds[16].text + "\n")
		

		for tr in soup.select('.lista_0'):
				tds = tr.find_all('td')
				f1.write(tds[0].text + "," + tds[1].text + "," + tds[2].text + "," + tds[3].text + "," + tds[4].text + ", merito :" + tds[15].text + "," + tds[16].text + "\n")
f1.close()