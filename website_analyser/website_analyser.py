'''
Imagine you are looking to analyze which pages of your website are most popular. Your website has millions of pages each with different URL. Implement a data structure that exposes two APIs:

void reportPageAccess(String pageUrl)
List <String> getTopNPages(int n)
The reportPageAccess API is invoked from the web server whenever a particular page is requested. The corresponding page URL is passed as a parameter. The getTopNPages API is invoked when an administrator likes to view top N pages. Please note it may be called with a variable n to view top n pages. Here is how your class would look like (in Java):

'''

import time

class WebSiteAnalyser(object):
    def __init__(self, *args, **kwargs):
        self._priority_dict = {}
        self.entry_time = None
        self.exit_time = None

    @staticmethod
    def get_exit_time():
        pass

    def reportPageAccess(self, pageUrl):
        '''
        @param: pageUrl 
        Currently accessed page url is passed to record for the anslysis
        
        @returns: None
        '''
        if self._priority_dict.has_key(pageUrl):
            self._priority_dict[pageUrl] += 1
        else:
            self._priority_dict[pageUrl] = 0
        

    def getTopNPages(self, n):
        '''
        @param n: The given number of top web pages will be returned from our analysed stack
        '''
        sorted_res = sorted(self._priority_dict.items(), key=lambda x: x[1], reverse=True)[:n]
        return [i[0] for i in sorted_res]


if __name__ == '__main__':
    web_obj = WebSiteAnalyser()

    url1 = "http://navasport.wordpress.com"
    url2 = "http://wikipedia.org"
    url3 = "http://amazon.in"
    url4 = "http://amazon.in"
    url5 = "http://amazon.in"
    url6 = "http://amazon.in"
    url7 = "http://wikipedia.org"
    url8 = "http://flipkart.com"
    url9 = "http://flipkart.com"
    url10 = "http://flipkart.com"

    print "##" * 10
    for url in [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10]:
        print "Entering the Url Assume this is the recently accessed url: %s" % url
        web_obj.reportPageAccess(url)
        
    # n is the Top no of pages that you want to see
    n = 2
    result = web_obj.getTopNPages(n)
    print "##" * 10
    print "The Top %s Web pages are :\n" % str(n)
    print result
    print "##" * 10
