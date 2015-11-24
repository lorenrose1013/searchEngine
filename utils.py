import google, urllib2, bs4, re

def getTenPages(query):
	results = google.search(query, num=10, start = 0, stop = 10)
	pages = []
	for url in results:
            page = urllib2.urlopen(url)
            page = page.read()
            pages.append(page)
        return pages

#def getURLSoup(url):
#	page = urllib2.urlopen(url)
#	page = page.read()
#	soup = bs4.BeautifulSoup(page, 'html')
#	return soup

#def getTenPages(query):
#        urls = getTenURLS(query)
#        soups = []
#        for url in urls:
#                soups.append(getURLSoup(url)
#        return soup
	

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
	#urls =  getTenURLS("who played spiderman")
	#print getURLSoup(urls[0]).prettify()
    print who("who played spiderman")

def who(query):
        pages = getTenPages(query)
        finds ={}
        nameSub1 = "[A-Z][a-z]? [A-Z][a-z]?"
        for page in pages:        
                results = re.sub("", "", page)
                for r in results:
                        if r in finds:
                            finds[r] += 1
                        else:
                            finds[r] = 1
        ##bucket style
        print finds
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
