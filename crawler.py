import urllib2
import sys
from bs4 import BeautifulSoup


URLList = []
COUNT = 0


def get_content(link):
    webUrl = urllib2.urlopen(link)
    return  webUrl.read()

def write_content(*args):
    # TODO:
    global COUNT
    COUNT = COUNT + 1
    file = open(args[-1] + "/" + str(COUNT) + ".html","w")
    data = args[0] + "\n" + args[1] + "\n" + args[2].decode("utf-8")
    file.write(data.encode("utf-8"))
    file.close()

def find_links(content):
    soup = BeautifulSoup(content, 'html.parser')
    for link in soup.find_all('a'):
        if link not in URLList:
            URLList.append(link.get('href'))

def main():

    if len(sys.argv) != 4:
        print "Wrong info passed"
        sys.exit(1)

    baseurl = sys.argv[1]
    destination = sys.argv[2]
    depth = int(sys.argv[3])

    URLList.append(baseurl)

    for link in URLList:
        if not link.startswith('http'):
            continue
        ## get the html page
        data = get_content(link)

        ## find out the links in the page and add it to a list
        find_links(data) if depth > 0 else sys.exit(1)

        ## print in the file (url,depth,content)
        write_content(link, str(depth), data, destination)
        ## depth--
        depth -= 1

if __name__ == "__main__":
    main()

