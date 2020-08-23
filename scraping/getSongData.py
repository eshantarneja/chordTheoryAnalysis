from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import datetime
import time
from tqdm import tqdm

PATH = "/Users/eshantarneja/Documents/DataScience/storage/chromedriver" 


def scrapeSong(songUrl):
	# print(songUrl)
	chordOrder=[]
	chordList=[]
	topInfo=[]
	songArtist=''
	try:
		driver = webdriver.Chrome(PATH)
		driver.get(songUrl)
		main = WebDriverWait(driver,10).until(
			EC.presence_of_element_located((By.CLASS_NAME, "_1yLA0._1fbrm"))
			)
		chordOrder=getChordOrder(main)
		chordList=getChordList(main)
		topInfo=getTopInfo(main)
		songArtist=getSongAndArtist(main)
	finally:
		driver.quit()
		# print("timestamp: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		return pd.Series([chordOrder,chordList,topInfo,songArtist])


def getChordOrder(element):
	chordOrder=[]
	allChords = element.find_elements_by_class_name("_3bHP1._3ffP6")
	for chord in allChords:
		chordOrder.append(chord.text)
	return chordOrder

def getChordList(element):
	chordList=[]
	uniqueChords = element.find_elements_by_class_name("_2jxI1")
	for chord in uniqueChords:
		chordList.append(chord.text)
	return chordList

def getTopInfo(element):
	topInfo=[]
	songInfo = element.find_elements_by_class_name("_2EcLF")
	for info in songInfo:
		topInfo.append(info.text)
	return topInfo


def getSongAndArtist(element):
	songArtist='N/A'
	songInfo = element.find_element_by_class_name("_2Glbj")
	songArtist=songInfo.text
	return songArtist

def writeUrlsToCsv(csvName, urls):
	print("Writing to csv: ", csvName)
	with open(csvName,'w') as result_file:
		wr = csv.writer(result_file, dialect='excel')
		for url in urls:
			wr.writerow([url,])




def iterativeScrape():
	for i in range(10,20):
		start=i*1000+1
		finish=(i+1)*1000
		output ='scraped'+str(i+1)+'k.csv'
		df=pd.read_csv('/Users/eshantarneja/Documents/DataScience/data/songList1.csv')
		dfLim=df.loc[start:finish]
		print("now scraping...")
		print("start value: ", start)
		print("finish value: ", finish)
		print("file to output: ", output)
		print("timestamp: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		tqdm.pandas()
		dfLim[['chordOrder','chordList','topInfo', 'songArtist']]=dfLim['url'].progress_apply(scrapeSong)
		dfLim.to_csv(output, index=False)
		print('done scraping, output in: ',output)


iterativeScrape()


	# df=pd.read_csv('songList1.csv')
	# dfLim=df.loc[:3000]
	# print("now scraping...")
	# dfLim[['chordOrder','chordList','topInfo', 'songArtist']]=dfLim['url'].apply(scrapeSong)
	# dfLim.to_csv('scraped3k.csv', index=False)





