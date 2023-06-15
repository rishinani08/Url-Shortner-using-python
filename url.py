#importing the external libraries required
import pyshorteners as ps
#take the URL as input(), that needs to be shortened
URL = input("Enter your URL: ")


def urlshortener(URL):
    start = ps.Shortener()
    print(start.tinyurl.short(URL))

urlshortener(URL)
