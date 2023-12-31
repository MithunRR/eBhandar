
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