from urllib.request import urlopen
import json
import re
import unicodedata

h_poll = re.compile(r'18-US-House', re.IGNORECASE)


def getQuestions(data):

    theJSON = json.loads(data)
    for i in range(0, (len(theJSON))):
        print (theJSON['items'][i]['end_date'])
    # print (theJSON['items'][0]['poll_questions'][0]['question']['slug'])

def main():
    # url="https://elections.huffingtonpost.com/pollster/api/v2/questions/18-US-House"
    url="https://elections.huffingtonpost.com/pollster/api/v2/polls?cursor=next_cursor&question=18-US-House"
    urlData = urlopen(url)
    data = urlData.read()
    if urlData.getcode() == 200:
        getQuestions(data)
    else:
        "error in loading JSON"

if __name__ == "__main__":
  main()
