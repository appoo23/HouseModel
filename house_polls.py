from urllib2 import urlopen
import json
import re
import unicodedata
import pandas as pd


# universal variables
h_poll = re.compile(r'18-US-House', re.IGNORECASE)
d_response = re.compile(r'democrat', re.IGNORECASE)
r_response = re.compile(r'republican', re.IGNORECASE)
date = []
slug = []
dem = []
gop = []
p_house = []

def getPolls(theJSON):
    # load JSON
    # theJSON = json.loads(data)
    # call function that loads the date of the poll
    getDate(theJSON)
    getSLUG(theJSON)
    # call function that loads the polling house, Dem result, and GOP result
    getResults(theJSON)


def getDate(JSON):
    for i in range(0, (len(JSON))):
        date.append((JSON['items'][i]['end_date']))

def getSLUG(JSON):
    for i in range(0, (len(JSON))):
        slug.append((JSON['items'][i]['slug']))


def getResults(JSON):
    for i in range(0, (len(JSON))):
        p_house.append((JSON['items'][i]['survey_house']))
        for z in range(0, len(JSON['items'][i]['poll_questions'])):
             h = h_poll.match(JSON['items'][i]['poll_questions'][z]['question']['slug'])
             if h:
                 for b in range(0, len(JSON['items'][i]['poll_questions'][z]['sample_subpopulations'])):
                    for a in range(0,(len(JSON['items'][i]['poll_questions'][z]['sample_subpopulations'][b]['responses']))):
                        d = d_response.match((JSON['items'][i]['poll_questions'][z]['sample_subpopulations'][b]['responses'][a]['pollster_label']))
                        if d:
                            dem.append(JSON['items'][i]['poll_questions'][z]['sample_subpopulations'][b]['responses'][a]['value'])
                        r = r_response.match((JSON['items'][i]['poll_questions'][z]['sample_subpopulations'][b]['responses'][a]['pollster_label']))
                        if r:
                            gop.append(JSON['items'][i]['poll_questions'][z]['sample_subpopulations'][b]['responses'][a]['value'])

def loadDF():
    polldata = list(zip(date, slug, p_house, dem, gop))
    # df = pd.DataFrame.from_list(polldata)
    df = pd.DataFrame(data = polldata, columns=['date', 'slug', 'p_house', 'dem', 'gop'])
    print(df)
    dtexample = pd.to_datetime(df['date'])
    print(dtexample)
    

def loadCursor(url):
    urlData = urlopen(url)
    data = urlData.read()
    theJSON = json.loads(data)
    print (theJSON['cursor'])
    if urlData.getcode() == 200:
        getPolls(theJSON)

    else:
        "error in loading JSON"

    loadDF()

def main():
    url="https://elections.huffingtonpost.com/pollster/api/v2/polls?cursor=next_cursor&question=18-US-House"
    loadCursor(url)






if __name__ == "__main__":
  main()
