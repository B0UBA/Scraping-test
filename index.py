from bs4 import BeautifulSoup
import urllib.request
import json

urlnumber = 2
link = []

def get_data():
  search = input("Que voulez vous chercher : ")
  urls = input("Combien de page voulez vous fetcher ? :")
  urls = int(urls)
  
  for url in range(urls):
    urlpage = "https://www.bfmtv.com/politique/page"
    global urlnumber
    urlpage = urlpage + str(urlnumber) + "/"
    print("fetching page " +  str(urlnumber))
    try:
      page = urllib.request.urlopen(urlpage)
    except:
      print('Erreur 404')
      break
    
    soup = BeautifulSoup(page, "html.parser")
    articles = soup.find_all("article", class_="content_item")

    for article in articles:
      data = article.find("h2", class_="content_item_title")
      articleSTR = str(data)
      linkvalidate = articleSTR.replace("<h2 class=\"content_item_title\">", "").replace("</h2>", "")
      if linkvalidate.find(search) != -1:
        global link
        link.extend([linkvalidate])
      else:
        pass
      with open("result.json", "w", encoding='utf-8') as f:
        json.dump(link, f, indent=4, ensure_ascii=False)
      with open("result.json", "r", encoding='utf-8') as f:
        link = json.load(f) 
    urlnumber += 1
      
    
get_data()