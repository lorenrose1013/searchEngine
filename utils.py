import google, urllib2, re

def removeStopWords(text):
	f = open("stop_words.txt", "r")
	stopWords = f.read()
	stopWords.replace("\r", "")
	stopWords.split("\n")
	#print stopWords
	f.close()
	text = text.split(" ")
	fixedText = []
	for i in text:
		if i.lower() not in stopWords:
			fixedText.append(i)
	fixedText = " ".join(fixedText) 
	return fixedText

def getTenPages(query):
	results = google.search(query, num=10, start = 0, stop = 10)
	pages = []
	for url in results:
		newUrl = urllib2.Request(url, headers={'User-Agent' : "Bot? What Bot?"}) #to get to <some> sites that try to avoid bots
		try:
			# some websites try to avoid being spammed by bots
			# they cause errors which would halt the program
			# catch those errors and return blank page instead
			responce = urllib2.urlopen(newUrl)
			page = responce.read()
		except:
			print "url %s was not valid" % url
			page = ""
		page = removeStopWords(page)
		pages.append(page)
	return pages


def who(query):
	pages = getTenPages(query)
	finds ={}
	nameSub = "[A-Z][a-z]+ [A-Z][a-z]+"
	for page in pages:        
		results = re.findall(nameSub, page)
		for r in results:
			if r in finds:
				finds[r] += 1
			else:
					finds[r] = 1
	print query
	result = max(finds, key=finds.get)
	print result
	return result

def when(query):
    pages = getTenPages(query)
    finds = {}
    dateSub1 = "[0-9]/[0-9]/[0-9]"
    ## for page in pages:
    ##    results = re.sub("","",page)

def where(query):
    pages = getTenPages(query)

def getAnswer(query, regexList):
	pages = getTenPages(query)
	finds ={}
	for regex in regexList:
		for page in pages:        
			results = re.findall(regex, page)
			for r in results:
				if r in finds:
					finds[r] += 1
				else:
						finds[r] = 1
	
	result = max(finds, key=finds.get)
	# print query
	# print result
	return result

def getResult(query):
	if "when" in query.lower():
		return when(query)
	elif "who" in query.lower():
		nameRegex = ["[A-Z][a-z]+ [A-Z][a-z]+"]
		return getAnswer(query, nameRegex)
	elif "where" in query.lower():
		return where(query)
	##elif "what" in query:
	##	return what(query)
    ##elif "why" in query:
    ##    return why(query)
	else:
		return "Sorry, can you rephrase your query as a Who, Where, or When question?"




if __name__ == "__main__": 
    who("Who will be the next President ?") # returns Donald Trump (uh-oh)
    who("Who is best korea?") #returns North Korea
    who("Who wrote the song Hello?") #returns lionel richie, the origial
    who("Who killed Kennedy?") #returns the warren commission LOL
    who("Who played spiderman?") #returns peter parker. duh 
    who("Who was the first president of the united states ") #returns john hanson first prez under articles of confederations
    