import google, urllib2, bs4, re

def getTenURLS(query):
	results = google.search(query, num=10, start = 0, stop = 10)
	urls = []
	for page in results:
		urls.append(page)
	return urls

def getURLSoup(url):
	page = urllib2.urlopen(url)
	page = page.read()
	soup = bs4.BeautifulSoup(page, 'html')
	return soup

def getTenSoup(query):
        urls = getTenURLS(query)
        soups = []
        for url in urls:
                soups.append(getURLSoup(url)
        return soups

if __name__ == "__main__": 
	urls =  getTenURLS("who played spiderman")
	print getURLSoup(urls[0]).prettify()


    
def who(query):
    soups = getTenSoup(query)
    #parse for who

def when(query):
    soups = getTenSoup(query)

def where(query):
    soups = getTenSoup(query)

def getResult(query):
    if "when" in query:
		return when(query)
	elif "who" in query:
		return who(query)
	elif "where" in query:
		return where(query)
	##elif "what" in query:
	##	return what(query)
        ##elif "why" in query:
        ##    return why(query)
	else:
		return "Sorry, can you rephrase your query as a Who, Where, or When question?"
