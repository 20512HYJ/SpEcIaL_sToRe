

import streamlit as st
import requests


def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json()
	return res
	



	
def getCountyOption(items):
	optionList = list()
	for item in items:        
		name = item['cityName'][0:3]          
		if name in optionList:
			continue
		else:    
			optionList.append(name)       
	return optionList


	

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
	
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	
if __name__ == '__main__':
	app()