from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
import pandas as pd
import traceback

PATH = "/Users/eshantarneja/Documents/DataScience/storage/chromedriver" 

# genres = {'Rock':4, 'Folk':666, 'Pop': 14, 'Country': 49, 
# 'Rhythm And Blues': 70, 'Metal': 8, 'Electronic': 16, 
# 'Contemporary R&B': 434, 'Religious':1016, 'Hip Hop':45, 'Reggae': 19, 
# 'Jazz':84, 'Blues':99, 'World Music': 195, 'Disco':85 , 'Comedy': 79,
# 'New Age': 695, 'Experimental': 667, 'Soundtrack': 680 }

genres = {'Folk':666, 'Pop': 14, 'Country': 49, 
'Rhythm And Blues': 70, 'Metal': 8, 'Electronic': 16, 
'Contemporary R&B': 434, 'Religious':1016, 'Hip Hop':45, 'Reggae': 19, 
'Jazz':84, 'Blues':99, 'World Music': 195, 'Disco':85 , 'Comedy': 79,
'New Age': 695, 'Experimental': 667, 'Soundtrack': 680 }

decades = ['2010', '2000', '1990', '1980', '1970', '1960', '1950', '1940']

# genres = {'Experimental': 667, 'Soundtrack': 680}

# decades = ['2010']


def getSongUrls():
	print("Gathering Song Urls...")
	
	for genre, genreNum in genres.items():
		print("Genre: ", genre)
		urlList=[]
		for decade in decades:
			print("Decade: ", decade)
			for page in range(1,21):
				site="https://www.ultimate-guitar.com/explore?decade[]="+decade+"&&genres[]="+str(genreNum)+"&type[]=Chords&page="+str(page)
				print("Page: ", site)
				driver = webdriver.Chrome(PATH)
				driver.get(site)
				try:
					main = WebDriverWait(driver,5).until(
						EC.presence_of_element_located((By.CLASS_NAME, "k2uDg"))
						)
					titles = main.find_elements_by_class_name("_2KJtL._1mes3.kWOod")
					for title in titles:
						newRow=[title.get_attribute('href'), genre, decade]
						urlList.append(newRow)
				except:
					traceback.print_exc()
					break
				finally:
					driver.quit()
		outputCsv='urls/'+genre+'.csv'
		writeUrlsToCsv(outputCsv, urlList)
	return urlList

def writeUrlsToCsv(csvName, urls):
	print("Writing to csv: ", csvName)
	with open(csvName,'w') as result_file:
		wr = csv.writer(result_file, dialect='excel')
		for url in urls:
			wr.writerow(url)

# driver = webdriver.Chrome(PATH)

# def getSongUrls():
# 	urlList=[]
# 	for i in range(1,21):
# 		driver = webdriver.Chrome(PATH)
# 		site="https://www.ultimate-guitar.com/explore?type[]=Chords&&page=" + str(i)
# 		print("Scraping Page ", i)
# 		driver.get(site)
# 		try:
# 			main = WebDriverWait(driver,10).until(
# 				EC.presence_of_element_located((By.CLASS_NAME, "k2uDg"))
# 				)
# 			titles = main.find_elements_by_class_name("_2KJtL._1mes3.kWOod")
# 			for title in titles:
# 				urlList.append(title.get_attribute('href'))

# 		finally:
# 			driver.quit()
# 	writeUrlsToCsv('songUrls.csv', urlList)
# 	return urlList

getSongUrls()
