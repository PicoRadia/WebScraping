var scraper = {iterator : 'div.quote' , data : {
    'quotes' : {sel : 'span'},
    'author' : {sel : 'small.author'},  
}};
// pagination
function nextUrl($page) {
  return $page.find('li.next > a').attr('href');
}

artoo.log.debug('Starting the scraper...');
var frontpage = artoo.scrape(scraper);

artoo.ajaxSpider(
  function(i, $data) {
    return nextUrl(!i ? artoo.$(document) : $data);
  },
  {
    limit: 2,
    scrape: scraper,
    concat: true,
    done: function(data) {
      artoo.log.debug('Finished retrieving data. Downloading...');
      artoo.savePrettyJson(
        frontpage.concat(data),
        {filename: 'quotes.json'} // downloading data
      );
    }
  }
);
