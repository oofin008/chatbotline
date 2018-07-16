import regex

#get rid of html tag from data
def cleanhtml(raw_html):
    cleanr = regex.compile('<.*?>')
    cleantext = regex.sub(cleanr, '', raw_html)
    return cleantext




