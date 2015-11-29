import google, urllib2, re

def removeStopWords(text):
	""" Removes common english words from a block of text so they don't skew results"""
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
	"""Return list of ten web pages that result from the given query

		param: 
			query: string to get pages for from google api 
		return:
			list of ten elements, which are each strings of webpages with stop words removed
	"""
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

#no longer nessecary just use the getAnswer with appropriate regex list

# def who(query):
# 	pages = getTenPages(query)
# 	finds ={}
# 	nameSub = "[A-Z][a-z]+ [A-Z][a-z]+"
# 	for page in pages:        
# 		results = re.findall(nameSub, page)
# 		for r in results:
# 			if r in finds:
# 				finds[r] += 1
# 			else:
# 					finds[r] = 1
# 	print query
# 	result = max(finds, key=finds.get)
# 	print result
# 	return result

# def when(query):
#     pages = getTenPages(query)
#     finds = {}
#     dateSub1 = "[0-9]/[0-9]/[0-9]"
#     ## for page in pages:
#     ##    results = re.sub("","",page)

# def where(query):
#     pages = getTenPages(query)

def getAnswer(query, regexList):
	"""Get most common result of regex in the first ten pages of the given query

		parms:
			query: string to be searched
			regexList: List of regular expressions to search the webpages for 
		return:
			Most common result of searching ten web pages for given regular expressions
	"""
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
	"""Answer a who, when, or where query 

		params:
			query: string of question to answer 
		return:
			string of responce [or string of error if invalid query]
	"""
	if "when" in query.lower():
		#return when(query)
		dateRegex = ["[0-9]/[0-9]/[0-9]"] #add more date regex's here 
		return getAnswer(query, dateRegex)
	elif "who" in query.lower():
		nameRegex = ["[A-Z][a-z]+ [A-Z][a-z]+"]
		return getAnswer(query, nameRegex)
	elif "where" in query.lower():
		whereRegex = []
		return getAnswer(query, whereRegex)
	else:
		return "Sorry, can you rephrase your query as a Who, Where, or When question?"




if __name__ == "__main__": 
    who("Who will be the next President ?") # returns Donald Trump (uh-oh)
    who("Who is best korea?") #returns North Korea
    who("Who wrote the song Hello?") #returns lionel richie, the origial
    who("Who killed Kennedy?") #returns the warren commission LOL
    who("Who played spiderman?") #returns peter parker. duh 
    who("Who was the first president of the united states ") #returns john hanson first prez under articles of confederations
    