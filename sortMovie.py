import string
import requests
from bs4 import BeautifulSoup
from os import listdir 
from os.path import isfile
from nltk import word_tokenize          

def clean_all_movie_name(mypath):
	i=0
	for filename in listdir(mypath):
		#if isfile(mypath+'\\'+filename):
		for c in string.punctuation:
			filename=filename.replace(c,' ')
		f=" ".join([word for word in word_tokenize(filename) if word not in string.punctuation])
		print(f)
		url='http://subscene.com/subtitles/release?q='+f+'&l='
		content=requests.get(url)
		plain_text = content.text
		soup = BeautifulSoup(plain_text,'lxml')
		# for t in soup.findAll('div',{'class':'byTitle'}) or soup.findAll('div',{'class':'subtitles byFilm byReleaseName'}):
		# 	temp=t.find('div',{'class':'title'}).a['href'] or t.find('div',{'class':'content'}).a['href']
		# 	print(temp)
		# 	break
		temp=soup('a')[8]['href']
		name=[]
		k=len(temp)
		for i in range(11,k):
			if not temp[i]=='/':
				name.append(temp[i])
			else:
				break
		fame=''.join([letter for letter in name])
		print(fame.replace('-',' '))



clean_all_movie_name('H:\Seagate Dashboard 2.0\movies')