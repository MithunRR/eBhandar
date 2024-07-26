
// sort prods by reg & ints 

let instantBtn = document.getElementById("instant-del-pro");
let regularBtn = document.getElementById("regular-del-pro");

let instantContHide = document.getElementById("instant-product-container");
let regularContHide = document.getElementById("regular-product-container");
let regularPriceDetailsHide = document.getElementById("reg-cart-main-price-details-div");
let instaPriceDetailsHide = document.getElementById("insta-cart-main-price-details-div");

function addActiveClIns() {
    regularBtn.classList.remove("active");
    instantContHide.classList.remove("hide-container");
    instaPriceDetailsHide.classList.remove("hide-container");

    instantBtn.classList.add("active");
    regularContHide.classList.add("hide-container");
    regularPriceDetailsHide.classList.add("hide-container");
}

function addActiveClReg() {
    instantBtn.classList.remove("active");
    regularContHide.classList.remove("hide-container");
    regularPriceDetailsHide.classList.remove("hide-container");

    regularBtn.classList.add("active");
    instantContHide.classList.add("hide-container");
    instaPriceDetailsHide.classList.add("hide-container");
}


// Inst - inc & dec prods quantity 
let ins_inp_value = document.getElementById("instant-cat-value");
let ins_inp_minus = document.getElementById("instant-cat-minus");
let ins_inp_plus = document.getElementById("instant-cat-plus");

function ins_inc_prods(){
    if (ins_inp_value.value < 10){
        ins_inp_value.value = Number(ins_inp_value.value) + 1;
    }
}

function ins_dec_prods(){
    if (ins_inp_value.value > 0){
        ins_inp_value.value = Number(ins_inp_value.value) - 1;
    }
    else if (ins_inp_value.value < 1){
        let instant_product_div = document.getElementById("instant-del-product-div");
        instant_product_div.remove();
    }
}


