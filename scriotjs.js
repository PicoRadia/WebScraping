var jq = document.createElement('script');
jq.src = 'https://code.jquery.com/jquery-3.5.1.min.js';
document.getElementsByTagName('head')[0].append(jq);

function click_lease(){
document.getElementsByTagName('button')[4].click();
return 0;
}

async function uncheck(){
    var my_list = [];
    var rr = document.getElementsByClassName("Offers_root__yoNky")[0];
    my_list.push(rr.getElementsByTagName('span')[0]);
    my_list.push(rr.getElementsByTagName('span')[3]); 
    my_list.push(rr.getElementsByTagName('span')[6]);
    // uncheck elements
    for(var i = 0 ; i< 3 ;i++){
    my_list[i].className = "Offer_checkMark__1Yszz"; 
    return 0;
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
    "Month" : res[1].getElementsByTagName('span')[1].innerHTML,
    "Cash out of pocket" : document.getElementsByClassName("Input_input__1zHoN")[0].getAttribute("value")
}

return ob;

}

function initialisation(){
    click_lease();
    uncheck();
    
        console.log( "ready!");
        var h = get_headers();
    });
    return h;
}
console.log(initialisation());






