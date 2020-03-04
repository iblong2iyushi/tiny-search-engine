from util import get_content,find_links,write_content
import sys

URLList = []
COUNT = 0

def main():
    global COUNT
    if len(sys.argv) != 4:
        print("Wrong info passed")
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
        find_links(data, URLList) if depth > 0 else sys.exit(1)

        ## print in the file (url,depth,content)
        COUNT = write_content(link, str(depth), data, destination, COUNT)

        ## depth--
        depth -= 1

if __name__ == "__main__":
    main()

