import pyshorteners

link=input("Enter this link")

shortener=pyshorteners.Shortener()

shorted_link=shortener.tinyurl.short(link)

print(shorted_link)