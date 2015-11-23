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

if __name__ == "__main__": 
	urls =  getTenURLS("who played spiderman")
	print getURLSoup(urls[0]).prettify()



def who(query):
	pass
def what(query):
	pass
def when(query):
	pass
def where(query):
	pass

def getResult(query):
	if "when" in query:
		return when(query)
	if "who" in query:
		return who(query)
	if "what" in query:
		return what(query)
	if "where" in query:
		return where(query)
	else:
		return "Sorry, can you rephrase your query as a Who, What, Where, or When question?"
