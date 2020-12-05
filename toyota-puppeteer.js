const puppeteer = require('puppeteer');

var link_list = ["https://www.pes.tms.aws.toyota.com/#/estimator?series=yaris&year=2020&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=yarishatchback&year=2020&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corolla&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corollahybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corollahatchback&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=prius&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=camry&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=camryhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=priusprime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=avalon&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=avalonhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=86&year=2020&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=supra&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=sienna&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=tacoma&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=tundra&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=chr&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4hybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=venza&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4prime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=highlander&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=highlanderhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=4runner&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=sequoia&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=landcruiser&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corollahybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=prius&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=priusprime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4hybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4prime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=camryhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=avalonhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=highlanderhybrid&year=2021&zip=90011"];



(async () => {
  const browser = await puppeteer.launch({headless: false}); // default is true
  const page = await browser.newPage();
  await page.goto("https://www.toyota.com/payment-estimator");
  await page.evaluate(() => {  
    var jq = document.createElement('script');
    jq.src = 'https://code.jquery.com/jquery-3.5.1.min.js';
    document.getElementsByTagName('head')[0].append(jq);
  });
  await page.evaluate(() => {  
    document.getElementsByClassName("zipcode-btn")[0].click(); 
  });
  await page.waitFor(4000);

  await page.$(".modal-content");

  await page.evaluate(() => {  
    document.getElementsByName("zipcode")[0].value= 90011;
  });
  await page.evaluate(() => {  
    document.getElementsByName("button")[0].disabled = false;  });
  await page.evaluate(() => {  
    document.getElementsByName("button")[0].click()
  });
  await page.goto(link_list[0]);

  
  
  await console.log("done");
  
 
  

  //await browser.close();
})();



