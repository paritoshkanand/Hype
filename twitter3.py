# -*- coding: utf-8 -*-

import sys
import json
import urllib2

#
# A simple script to get twitter user information
#
# Authentication not required
# Twitter API call ref at https://dev.twitter.com/docs/api/1/get/users/show
#
# Author: Chris Sumner 27th Feb 2012
#


def main():
    print 'starting'
    # Use urllib2 to make our Twitter API call
    # For more information on urllib2, take a look at 'The Missing Manual' at http://www.voidspace.org.uk/python/articles/urllib2.shtml
    #
    req = urllib2.Request('https://api.twitter.com/1/users/show.json?screen_name=TheSuggmeister&include_entities=true')
    response = urllib2.urlopen(req)
    the_page = response.read()

    # print JSON object
    print json.loads(the_page) 


    # Neater way to print Twitter JSON data
    # From : http://stackoverflow.com/questions/9170288/need-to-pretty-print-twitter-json-data-to-a-file-using-python

    print(json.dumps(json.loads(the_page), indent=4, sort_keys=True))





if __name__ == "__main__":
  main()