import google, urllib2, bs4, re

def getTenPages(query):
	results = google.search(query, num=10, start = 0, stop = 10)
	pages = []
	for url in results:
		url = urllib2.Request(url, headers={'User-Agent' : "Bot? What Bot?"})
		responce = urllib2.urlopen(url)
		page = responce.read()
		pages.append(page)
	return pages

def who(query):
	pages = getTenPages(query)
	finds ={}
	nameSub1 = "[A-Z][a-z]+ [A-Z][a-z]+"
	for page in pages:        
		results = re.findall(nameSub1, page)
		for r in results:
			if r in finds:
				finds[r] += 1
			else:
					finds[r] = 1
	print max(finds, key=finds.get)

def when(query):
    pages = getTenPages(query)
    finds = {}
    dateSub1 = "[0-9]/[0-9]/[0-9]"
    ## for page in pages:
    ##    results = re.sub("","",page)

def where(query):
    pages = getTenPages(query)

def getResult(query):
	if "when" in query.lower():
		return when(query)
	elif "who" in query.lower():
		return who(query)
	elif "where" in query.lower():
		return where(query)
	##elif "what" in query:
	##	return what(query)
    ##elif "why" in query:
    ##    return why(query)
	else:
		return "Sorry, can you rephrase your query as a Who, Where, or When question?"




if __name__ == "__main__": 
	#urls =  getTenURLS("who played spiderman")
	#print getURLSoup(urls[0]).prettify()
    print who("Who did 9/11?")