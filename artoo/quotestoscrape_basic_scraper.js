   .-""-.   
  /[] _ _\  
 _|_o_LII|_ 
/ | ==== | \
|_| ==== |_|
 ||LI  o ||
 ||'----'||    artoo.js
/__|    |__\

// One line scrapers
artoo.scrape('div.quote' , {
    'quotes' : {sel : 'span'},
    'author' : {sel : 'small.author'},  
})
