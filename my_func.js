
/***************************************************************\
            Script to download Toyota Prices
               in CSV formats

    Target URL : "https://www.toyota.com/payment-estimator"
        Date : November 30th, 2020
                       by
                       
                    Fast DEV
              
\************************************************************/

function get_data(){
var res = document.getElementsByClassName("Cells_cell__2EEnX PaymentDetails_cell__25lSl");
var sec = document.getElementsByClassName('ChangeVehicleForm_vehicleSelect__2_TNG');
var obj1 ={
    "Monthly_payement" : res[0].getElementsByTagName('span')[1].innerHTML,
"Month" : res[1].getElementsByTagName('span')[1].innerHTML,
"Estimated APR" : res[2].getElementsByTagName('span')[1].innerHTML,
"Down Payment" : res[3].getElementsByTagName('span')[1].innerHTML
    
};
return obj1 ;

}


function term_length(i){
// i = 0 => 24
// i = 1 => 36
// i = 2 => 48
// dropdown 24 - 36
document.getElementsByClassName("Dropdown_button__204fc")[1].click(); // clicking dropdown
if(i == 0){
document.getElementsByClassName("Dropdown_menuItem__1rYyC")[0].click() ; // 24
uncheck();}
if(i == 1){
document.getElementsByClassName("Dropdown_menuItem__1rYyC")[1].click() ; // 36
uncheck();}
if(i == 2){
document.getElementsByClassName("Dropdown_menuItem__1rYyC")[2].click() ; // 48
uncheck();}

}

function sleep(milliseconds) {
const date = Date.now();
let currentDate = null;
do {
currentDate = Date.now();
} while (currentDate - date < milliseconds);
}

function uncheck(){
var my_list = [];
var rr = document.getElementsByClassName("Offers_root__yoNky")[0];
my_list.push(rr.getElementsByTagName('span')[0]);
my_list.push(rr.getElementsByTagName('span')[3]);
my_list.push(rr.getElementsByTagName('span')[6]);
// uncheck elements
for(var i = 0 ; i< 3 ;i++){
my_list[i].className = "Offer_checkMark__1Yszz"; 
}
}

function get_headers(){
var res = document.getElementsByClassName("Cells_cell__2EEnX PaymentDetails_cell__25lSl");
var sec = document.getElementsByClassName('ChangeVehicleForm_vehicleSelect__2_TNG');
var elem = sec[0].getElementsByTagName('span');

var ob = {

"Model" : elem[2].innerHTML,
"Trim" : elem[8].innerHTML,
"Est Price" : sec[0].getElementsByTagName('div')[3].innerText,
"Due at signing" : res[3].getElementsByTagName('span')[1].innerHTML, 
"Month" : res[1].getElementsByTagName('span')[1].innerHTML
    
}

return ob;

}

function click_lease(){
document.getElementsByTagName('button')[4].click();
}

function annual_mileage(i){
// 0 => 12 000
// 1 => 15 000
document.getElementsByClassName("Dropdown_button__204fc")[2].click();
if(i == 0){document.getElementsByClassName("Dropdown_menuItem__1rYyC")[1].click() ;}
if(i == 1) {document.getElementsByClassName("Dropdown_menuItem__1rYyC")[2].click();}

}

// TO DO 
// [] Add cash out of pocket to header data

// Append Javascript

function merge_data(){
    var dt = {
        "headers" : headers_data,
        "Mileage 1200" : list_12000,
        "Mileage 1500" : list_15000,

    }
    return dt ;
}

function download(){
// import JQuery
var jq = document.createElement('script');
jq.src = 'https://code.jquery.com/jquery-3.5.1.min.js';
document.getElementsByTagName('head')[0].append(jq);
$('head').append('<a download="toyota.json"></a>');
$('a[download="toyota.json"]').attr('href', window.URL.createObjectURL(
    new Blob([JSON.stringify(khilo, null, 2)], {type: 'text'})
  ));
$('a[download="toyota.json"]')[0].click();






}