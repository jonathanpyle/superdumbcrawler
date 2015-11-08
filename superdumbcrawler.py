import sys
import argparse
import requests
from lxml import html
from urlparse import urlparse

def urlIsWithinDomain(argUrl,argDomain):
    return urlparse(argUrl).hostname==argDomain

def stripFragmentTagFromLink(argLink):
    return argLink.split('#')[0]

def recursiveCrawl(argDomain, argUrl, argSiteMap):
    try:
        myResponse=requests.get(argUrl)
        myHTMLTree=html.fromstring(myResponse.content)
        myHTMLTree.make_links_absolute(argUrl)
        for myElement, myAttribute, myLink, myPos in myHTMLTree.iterlinks():
            myLink = stripFragmentTagFromLink(myLink)
            if myElement.tag=='a' and myLink not in argSiteMap:
                # This is a previously unmapped anchor link
                if urlIsWithinDomain(myLink, argDomain):
                    if globalArgs.debug: print("New local link found, href="+myLink)
                    argSiteMap.append(myLink)
                    argSiteMap=recursiveCrawl(argDomain, myLink, argSiteMap)
                else:
                    if globalArgs.debug: print("New external link found, href="+myLink)
                    argSiteMap.append(myLink)
    except Exception as myException:
        print ("{1} ==> {0}".format(myException, recursiveCrawl))
        
    return argSiteMap

# Main
parser = argparse.ArgumentParser()
parser.add_argument("url", help="The URL of a site to crawl e.g. https://wiprodigital.com")
parser.add_argument("-d", "--debug", action="store_true", help="Show debug output")
globalArgs = parser.parse_args()

myDomain=urlparse(globalArgs.url).hostname
if globalArgs.debug: print("Crawling url: "+globalArgs.url+" within domain : "+myDomain)
mySiteMap=recursiveCrawl(myDomain, globalArgs.url, list())

for i in mySiteMap:
    print i

