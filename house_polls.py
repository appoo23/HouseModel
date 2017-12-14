from urllib.request import urlopen
import json
import re
import unicodedata

h_poll = re.compile(r'hou', re.IGNORECASE)
d_test = re.compile(r'dem', re.IGNORECASE)

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)

  for i in range(0 , len(theJSON['items'])):
    # print (i)
    pollList = (theJSON['items'][i])
    questions = pollList["poll_questions"]
    # if h_poll.match()
    h_test = questions[1]["question"]["name"]
    h = h_poll.search(h_test)
    # print h_poll
    if h:
        resp = (questions[1]['sample_subpopulations'][0]['responses'])
        print (pollList['end_date'])
        for x in range(0, len(resp)):
            party = (resp[x]['pollster_label'])
            d = d_test.search(party)
            if d:
                # print (resp[x]['value'])
                poll_value = resp[x]['value']
                print (poll_value)
                print (party)


  # now we can access the contents of the JSON like any other Python object
  # if 'count' in theJSON['items']:
  #   print theJSON["items"]["title"] + "huh"

def main():
  # define a variable to hold the source URL

  urlData = "https://elections.huffingtonpost.com/pollster/api/v2/polls?question=18-US-House&sort=created_at"


  # Open the URL and read the data
  webUrl = urlopen(urlData)
  if (webUrl.getcode() == 200):
    print ("hey we in")
    data = webUrl.read()
    # print out our customized results
    # print (data)
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

if __name__ == "__main__":
  main()
