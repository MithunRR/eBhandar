

let prodSlideIndex = 1;
showSlides(prodSlideIndex);

function currentSlide(n) {
    showSlides(prodSlideIndex = n);
}

function showSlides(n) {
    // let i;
    let slides = document.getElementsByClassName("slide-images");
    let fadeImg = document.getElementsByClassName("slide-image-option");
    if (n > slides.length) { prodSlideIndex = 1 }
    if (n < 1) { prodSlideIndex = slides.length }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (let i = 0; i < fadeImg.length; i++) {
        fadeImg[i].className = fadeImg[i].className.replace(" active", "");
    }
    slides[prodSlideIndex - 1].style.display = "block";
    fadeImg[prodSlideIndex - 1].className += " active";
}

