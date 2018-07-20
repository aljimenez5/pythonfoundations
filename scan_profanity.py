import urllib

def read_text():
	quotes = open("/Users/arvida/Downloads/movie_quotes.txt")
	contents = quotes.read()
	print(contents)
	quotes.close()
	for word in contents.split():
		word = word.translate(None, "(){}<>")
		result = urllib.urlopen("http://www.wdylike.appspot.com/?q="+word)
		if "true" in result:
			print("Profanity Found!! "+word)
		elif "true" in result == 0 and "false" in result:
                	print("This document has no curse words!")		
 		else:
			if "true" == 0 and "false" == 0 in result:
               			print("Could not scan the document.")
	
read_text()
