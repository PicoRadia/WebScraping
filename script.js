// First thing is to click lease
document.getElementsByTagName('button')[4].click(); // can do it manually


var res = document.getElementsByClassName("Cells_cell__2EEnX PaymentDetails_cell__25lSl");
// Monthly payment
var price =  res[0].getElementsByTagName('span')[1].innerHTML;

// Month 
var month = res[1].getElementsByTagName('span')[1].innerHTML;

// Annual Milage
var anuual_milage = res[2].getElementsByTagName('span')[1].innerHTML;

// Amount due at signing 
var amount = res[3].getElementsByTagName('span')[1].innerHTML;

// *  * * ** **  * * * *  * * * * * * * * * * * ** ** ** 
var sec = document.getElementsByClassName('ChangeVehicleForm_vehicleSelect__2_TNG');
var elem = sec[0].getElementsByTagName('span');
// model
var model = elem[2].innerHTML;
// trim 
var trim = elem[8].innerHTML;

// estimated price
var est =  sec[0].getElementsByTagName('div')[3].innerText;


//  creation d'un objet 



// Unchecking elements















var res = document.getElementsByClassName("Cells_cell__2EEnX PaymentDetails_cell__25lSl");

var sec = document.getElementsByClassName('ChangeVehicleForm_vehicleSelect__2_TNG');

var obj = {

    "Model" : elem[2].innerHTML,
    "Trim" : elem[8].innerHTML,
    "Est Price" : sec[0].getElementsByTagName('div')[3].innerText,
    "Due at signing" : res[3].getElementsByTagName('span')[1].innerHTML
    
    
    }



// Get List of links

// change to that link
window.location.replace(link);


var base_url = "https://www.pes.tms.aws.toyota.com/";
var links = document.getElementsByTagName('li');
for(var i = 0; i< links.length ; i++){
    var l = links[i].firstElementChild.attributes[1].value;
    console.log(base_url + l);
}


// Check buttons => Not working 
var check_list = document.getElementsByClassName("Offers_root__yoNky")[0].getElementsByTagName('li');
for(var i= 0; i<3 ; i++){
    var ch = check_list[i].children[0].children[0].children[0].children[0].children[0].checked;
    if(ch == true){
        check_list[i].children[0].children[0].children[0].children[0].children[1].click();
    }
}

// Change to 36 
// Change the class Name

var my_list = [];
var rr = document.getElementsByClassName("Offers_root__yoNky")[0];
my_list.push(rr.getElementsByTagName('span')[0]);
my_list.push(rr.getElementsByTagName('span')[3]);
my_list.push(rr.getElementsByTagName('span')[6]);
// uncheck elements
for(var i = 0 ; i< 3 ;i++){
    my_list[i].className = "Offer_checkMark__1Yszz"; 

}
    