var jq = document.createElement('script');
jq.src = 'https://code.jquery.com/jquery-3.5.1.min.js';
document.getElementsByTagName('head')[0].append(jq);


/ *************************************/




function get_headers(){
var res = document.getElementsByClassName("Cells_cell__2EEnX PaymentDetails_cell__25lSl");
var sec = document.getElementsByClassName('ChangeVehicleForm_vehicleSelect__2_TNG');
var elem = sec[0].getElementsByTagName('span');
var a = sec[0].getElementsByTagName('div')[3].innerText;

var ob = {
    "Model" : elem[2].innerHTML,
    "Trim" : elem[8].innerHTML,
    "Est Price" : String(a).slice(0,8),
    "Cash out of pocket" : document.getElementsByClassName("Input_input__1zHoN")[0].getAttribute("value")
}

return ob;

}
var h = get_headers();


  // create CSV output
  csv = 'Model,Trim,Est Price,Due at signing,Cash out of pocket\n';

  // loop over quotes
  $.each(h, function(index) {
    // create row string
    var row = '';

    // loop over object values within a given quote
    $.each(h, function(key, val) {
      if (key == 'Model' || key == 'Trim'|| key == 'Est Price'|| key == 'Due at signing'| key == 'Cash out of pocket')
        row += '"' + val + '"' + ','
    });

    // slice last coma
    row = row.slice(0, -1);

    // append new line feed to the row
    row += '\n';

    // append row to csv
    csv += row;
  });
  
  // create download link
  $('head').append('<a download="h.csv"></a>');
  
  // create object URL
  $('a[download="h.csv"]').attr('href', window.URL.createObjectURL(
    new Blob([csv], {type: 'text/csv'})
  ));
  
  // click download link
  $('a[download="h.csv"]')[0].click()
  
// * * **  ** * ** * * **  ** * ** *
var list_1200 = [];
function get_data(){
    var res = document.getElementsByClassName("Cells_cell__2EEnX PaymentDetails_cell__25lSl");
    var sec = document.getElementsByClassName('ChangeVehicleForm_vehicleSelect__2_TNG');
    var obj1 ={

    "Month" : res[1].getElementsByTagName('span')[1].innerHTML,
        "Monthly_payement" : res[0].getElementsByTagName('span')[1].innerHTML,
    "Down Payment" : res[3].getElementsByTagName('span')[1].innerHTML
        
    };
    return obj1 ;

}
function download(){
  
  // create CSV output
   csv = 'Month,Monthly_payement,Estimated APR,Down Payment\n';

  // loop over quotes
  $.each(list_1200, function(index) {
    // create row string
    var row = '';

    // loop over object values within a given quote
    $.each(this, function(key, val) {
      if (key == 'Monthly_payement' || key == 'Month'|| key == 'Estimated APR'|| key == 'Down Payment')
        row += '"' + val + '"' + ','
    });

    // slice last coma
    row = row.slice(0, -1);

    // append new line feed to the row
    row += '\n';

    // append row to csv
    csv += row;
  });
  
  // create download link
  $('head').append('<a download="quotes.csv"></a>');
  
  // create object URL
  $('a[download="quotes.csv"]').attr('href', window.URL.createObjectURL(
    new Blob([csv], {type: 'text/csv'})
  ));
  
  // click download link
  $('a[download="quotes.csv"]')[0].click()


}









list_1200.push(get_data());
// * * **  
function term_length(i){
document.getElementsByClassName("Dropdown_button__204fc")[1].click();
document.getElementsByClassName("Dropdown_menuItem__1rYyC")[i].click() ;
setTimeout(function(){ uncheck(); }, 3000);}


// ******
term_length(0);
setTimeout(function(){ uncheck(); }, 3000);

list_1200.push(get_data());

term_length(1);
list_1200.push(get_data());

term_length(2);
list_1200.push(get_data());

annual 
term_length(2);
list_1200.push(get_data());




//** * * ** * * * ** * * ** * * 

function download(){
  
  // create CSV output
   csv = 'Month,Monthly_payement,Estimated APR,Down Payment\n';

  // loop over quotes
  $.each(list_1200, function(index) {
    // create row string
    var row = '';

    // loop over object values within a given quote
    $.each(this, function(key, val) {
      if (key == 'Monthly_payement' || key == 'Month'|| key == 'Estimated APR'|| key == 'Down Payment')
        row += '"' + val + '"' + ','
    });

    // slice last coma
    row = row.slice(0, -1);

    // append new line feed to the row
    row += '\n';

    // append row to csv
    csv += row;
  });
  
  // create download link
  $('head').append('<a download="quotes.csv"></a>');
  
  // create object URL
  $('a[download="quotes.csv"]').attr('href', window.URL.createObjectURL(
    new Blob([csv], {type: 'text/csv'})
  ));
  
  // click download link
  $('a[download="quotes.csv"]')[0].click()


}




















