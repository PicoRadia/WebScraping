var base_url = 'https://quotes.toscrape.com';

// empty list init
var my_list = []

// define the logic of the first scraper
var scraper1 = {
  iterator: 'div.quote',
  data: {
    'quotes': {
      sel: 'span'
    },
    'author': {
      sel: 'small.author'
    },
    'link': {
      sel: 'a',
      attr: 'href'
    }
  }
};

// define the logic of the second scraper

var scraper2 = {
  iterator: 'div.author-details',
  data: {
    'dob': {
      sel: 'span.author-born-date'
    },
    'pob': {
      sel: 'span.author-born-location'
    }
  }
}


// pagination
function nextUrl($page) {
  return $page.find('li.next > a').attr('href');
}

artoo.log.debug('Starting the scraper...');
var frontpage = artoo.scrape(scraper1);

// spider

var my_list = []
// artoo spider

function pagination() {

  artoo.ajaxSpider(
    function(i, $data) {
      //console.log($data.innerHTML);
      return nextUrl(!i ? artoo.$(document) : $data);
    }, {
      limit: 1, // number of pages to scrape
      scrape: scraper1,
      concat: true,
      done: function(data) {
        artoo.log.debug('Finished retrieving data. Downloading...');
        console.log(data);
        for (var i = 0; i < my_list.length; i++) {
          my_list.push(base_url + data[i].link)
        }
        console.log(my_list)
      }
    })
  return my_list;
}
// Append links in a list
//my_list.push(base_url + data[0].link);


function crawl(mylist) {
  artoo.ajaxSpider(
    my_list, {
      limit: 1, // number of pages to scrape
      scrape: scraper2,
      concat: true,
      done: function(data) {
        console.log(data);
        artoo.log.debug('Finished retrieving data. Downloading...');
      }
    })
}

//var ll = null;
let links = pagination();
crawl(links)
