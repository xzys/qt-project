from splinter import Browser
from splinter.exceptions import *

amazon_url = 'http://www.amazon.com/Advanced-Search-Books/b?ie=UTF8&node=241582011'

def check_textbook(br, isbn):
    try:
        #verify that this textbook entry is valid make sure isbn is there
        #left this as a black because the back is at the end of the method
        
        #search for book
        br.fill('field-isbn', isbn)
        br.find_by_name('Adv-Srch-Books-Submit').first.click()

        if br.is_element_present_by_id('noResultsTitle'):
            raise ValueError
        
        #get the very first textbook on the page
        #br.find_by_css('.list').first.find_by_id('result_0').first
        if br.is_element_not_present_by_id('result_0'):
            raise ValueError
            
        tbl = br.find_by_id('result_0').first

        #replace textbook name
        print "textbook name:\t\t %s" % tbl.find_by_css('.title').last.text
        print "textbook author:\t\t %s" % tbl.find_by_css('.ptBrand').first.text
        


        #add new amazon price data
        if(len(tbl.find_by_css('[class^=toeOurPrice]')) > 0):
            print 'amazon default price:\t\t%s' % tbl.find_by_css('[class^=toeOurPrice]').first.text

        if(len(tbl.find_by_css('.toeNewPrice')) > 0):
            print 'amazon seller price\t\t%s' % tbl.find_by_css('.toeNewPrice').first.text
        
        if(len(tbl.find_by_css('.toeUsedPrice')) > 0):
            print 'amazon used price\t\t%s' % tbl.find_by_css('.toeUsedPrice').first.text

        print '\tsuccess'
    
    except (ValueError, ElementDoesNotExist):
        print '\tfail\nfuq\n'
    finally:
        br.visit(amazon_url)


if __name__ == '__main__':
    br = Browser()
    br.visit(amazon_url)

    raw_input('ENTER to start')
    
    while 1:
        isbn = raw_input('enter isbn:\t\t')
        check_textbook(br, isbn)


