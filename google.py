import google, urllib2, bs4, re

def getTenResults(query):
	results = google.search(q, num=10, start = 0, stop = 10)
	result_list = []
	for page in results:
		result_list.append(page)
	return result_list


print getTenResults("who played spiderman")
# google api problems
