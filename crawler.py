from util import get_content,find_links,write_content
import sys

URLList = []
COUNT = 0

def url_logic(url,i,depth, destination):
    urls = []
    if i == depth or not url.startswith('http'):
        return
    ## get the html page
    data = get_content(url)

    ## find out the links in the page and add it to a list
    find_links(data, urls) if depth > 0 else sys.exit(1)

    ## print in the file (url,depth,content)
    global COUNT
    COUNT = write_content(url, str(depth), data, destination, COUNT)
   
    for u in urls:
        url_logic(u, i+1, depth, destination)


def main():
    global COUNT
    if len(sys.argv) != 4:
        print("Wrong info passed")
        sys.exit(1)

    baseurl = sys.argv[1]
    destination = sys.argv[2]
    depth = int(sys.argv[3])

    url_logic(baseurl, 0, depth, destination)

if __name__ == "__main__":
    main()

