import pyshorteners
def shorten():
    link=input("Link please: \n")
    short=pyshorteners.Shortener()
    x=short.tinyurl.short(link)
    print(f"Shortened link is:\n{x}")

shorten()