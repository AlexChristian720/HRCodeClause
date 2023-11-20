import pyshorteners

url= input('Please Input URL: ')

def URLShortner(url):
    s= pyshorteners.Shortener()
    print(s.tinyurl.short(url))

URLShortner(url)