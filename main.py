import pyshorteners

url_input = input("enter url: ")

short_url = pyshorteners.Shortener().tinyurl.short(url_input)
print(short_url)
