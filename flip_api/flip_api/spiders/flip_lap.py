
import scrapy

class QuotesSpider(scrapy.Spider):
  name = "flip"
  count=0
  def start_requests(self):
        url =  "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=7ec220e8-4f02-4150-9e0b-9e90cf692f4b&as-searchtext=laptop&page=1"
        yield scrapy.Request(url=url, callback=self.parse)


  def parse(self, response):
      for flip in response.css('a._1fQZEK'):
          yield {
              'text': flip.css('div._4rR01T::text').get(),
              'author':flip.css('div._30jeq3._1_WHN1::text').get(),
              
          }

      next_page = response.css('a._1LKTO3::attr(href)').getall()
      print(next_page)
      if len(next_page)>1 or self.count==0 :
          
          if self.count==0:
            x=next_page[0]
          else:
            x=next_page[1]  
          self.count+=1
          yield response.follow(x, callback=self.parse)

