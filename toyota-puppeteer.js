const puppeteer = require('puppeteer');




var link_list = ["https://www.pes.tms.aws.toyota.com/#/estimator?series=yaris&year=2020&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=yarishatchback&year=2020&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corolla&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corollahybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corollahatchback&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=prius&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=camry&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=camryhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=priusprime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=avalon&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=avalonhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=86&year=2020&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=supra&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=sienna&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=tacoma&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=tundra&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=chr&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4hybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=venza&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4prime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=highlander&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=highlanderhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=4runner&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=sequoia&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=landcruiser&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=corollahybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=prius&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=priusprime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4hybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=rav4prime&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=camryhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=avalonhybrid&year=2021&zip=90011", "https://www.pes.tms.aws.toyota.com/#/estimator?series=highlanderhybrid&year=2021&zip=90011"];



(async () => {
  const browser = await puppeteer.launch({headless: false}); // default is true
  const page = await browser.newPage();
  await page.goto("https://www.toyota.com/payment-estimator");
  await page.$(".zipcode has-icon-pencil zipcode-cta");
  await page.evaluate(async () => {  
    await document.getElementsByClassName("zipcode has-icon-pencil zipcode-cta")[0].click(); 
  }).catch( console.log("tfou"));
  await page.waitFor(4000);

  await page.$(".modal-content");

  await page.evaluate(() => {  
    document.getElementsByName("zipcode")[0].value= 90011;
  });
  await page.evaluate(() => {  
    document.getElementsByName("button")[0].disabled = false;  });
  await page.evaluate(() => {  
    document.getElementsByName("button")[0].click();
  });




  
  for(var i=0 ; i< 1 ; i++){
    const page1 = await browser.newPage();
    await page1.goto(link_list[i],{waitUntil: 'networkidle2'});
    
    await page1.waitForSelector('button.Toggle_button__p77EI[value="lease"]');
    await page1.click('button.Toggle_button__p77EI[value="lease"]');
    await page1.waitForSelector('span[class="DropdownMenu_value__2NjwW"]');
    var my = [];
    var data = await page1.evaluate(async () => {  
      model = await document.querySelector('span[class="DropdownMenu_value__2NjwW"]').innerText;
      trim = await document.querySelectorAll('span[class="DropdownMenu_value__2NjwW"]')[2].innerText;
      est_price = await document.querySelector('div[class="ChangeVehicleForm_msrp__19M0r"]').innerText.split("Estimated")[0];  
      cash = await  document.querySelector('input[class="Input_input__1zHoN"]').value ;

     
      
      return await {
        "model": model,
        "trim" : trim ,
        "Est" : est_price,
        "Cash" : cash
       
       
        
        }
    
    });
    
 
  
  try {   
    await page1.waitForSelector('button[class="Dropdown_button__204fc"]');
    await page1.evaluate(async () => { 
      await document.querySelectorAll('button[class="Dropdown_button__204fc"]')[2].click(); // mileage 12000
      await document.querySelector('li[value="12000"]').click();
      // dropdown 24
      await document.querySelectorAll('button[class="Dropdown_button__204fc"]')[1].click();
      await document.querySelector('li[value="24"]').click();
      // get the price  
    });
    
    } catch (error) {
      console.log('That did not go well.');
    }
  
  
  

  await console.log(data);
  await console.log("done");
  
 }}
  
  
  

 )();

