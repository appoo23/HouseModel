import urllib2
import json
import re
import unicodedata

h_poll = re.compile(r'hou', re.IGNORECASE)

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)

  for i in range(1 , len(theJSON['items'])):
    pollList = (theJSON['items'][i])
    questions = pollList["poll_questions"]
    # if h_poll.match()
    h_test = questions[1]["question"]["name"]
    h = h_poll.search(h_test)
    # print h_poll
    if h:
        print "ok"
    else:
        print "not ok"


  # now we can access the contents of the JSON like any other Python object
  if 'count' in theJSON['items']:
    print theJSON["items"]["title"] + "huh"

def main():
  # define a variable to hold the source URL

  urlData = "https://elections.huffingtonpost.com/pollster/api/v2/polls?question=18-US-House&sort=created_at"


  # Open the URL and read the data
  webUrl = urllib2.urlopen(urlData)
  if (webUrl.getcode() == 200):
    print ("hey we in")
    data = webUrl.read()
    # print out our customized results
    # print (data)
    printResults(data)
  else:
    print "Received an error from server, cannot retrieve results " + str(webUrl.getcode())

if __name__ == "__main__":
  main()
