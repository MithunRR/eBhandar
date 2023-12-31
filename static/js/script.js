// scroll to top script 
let backToTopBtn = document.getElementById("back-to-top");

// on scroll show the button
window.onscroll = function() {funcScrolled()};
function funcScrolled() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    backToTopBtn.style.display = "block";
  } else {
    backToTopBtn.style.display = "none";
  }
}

function backToFunc() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}



// slider 
var container = document.getElementById('container')
var slider = document.getElementById('slider');
var slidess = document.getElementsByClassName('slide').length;
var buttons = document.getElementsByClassName('btn');

var currentPosition = 0;
var currentMargin = 0;
var slidesPerPage = 0;
var slidesCount = slidess - slidesPerPage;
var containerWidth = container.offsetWidth;
var prevKeyActive = false;
var nextKeyActive = true;

window.addEventListener("resize", checkWidth);

function checkWidth() {
    containerWidth = container.offsetWidth;
    setParams(containerWidth);
}

function setParams(w) {
    if (w < 551) {
        slidesPerPage = 1;
    } else {
        if (w < 901) {
            slidesPerPage = 2;
        } else {
            if (w < 1101) {
                slidesPerPage = 3;
            } else {
                slidesPerPage = 4;
            }
        }
    }
    slidesCount = slidess - slidesPerPage;
    if (currentPosition > slidesCount) {
        currentPosition -= slidesPerPage;
    };
    currentMargin = - currentPosition * (100 / slidesPerPage);
    slider.style.marginLeft = currentMargin + '%';
    if (currentPosition > 0) {
        buttons[0].classList.remove('inactive');
    }
    if (currentPosition < slidesCount) {
        buttons[1].classList.remove('inactive');
    }
    if (currentPosition >= slidesCount) {
        buttons[1].classList.add('inactive');
    }
}

setParams();

function slideRight() {
    if (currentPosition != 0) {
        slider.style.marginLeft = currentMargin + (100 / slidesPerPage) + '%';
        currentMargin += (100 / slidesPerPage);
        currentPosition--;
    };
    if (currentPosition === 0) {
        buttons[0].classList.add('inactive');
    }
    if (currentPosition < slidesCount) {
        buttons[1].classList.remove('inactive');
    }
};

function slideLeft() {
    if (currentPosition != slidesCount) {
        slider.style.marginLeft = currentMargin - (100 / slidesPerPage) + '%';
        currentMargin -= (100 / slidesPerPage);
        currentPosition++;
    };
    if (currentPosition == slidesCount) {
        buttons[1].classList.add('inactive');
    }
    if (currentPosition > 0) {
        buttons[0].classList.remove('inactive');
    }
};    












// carousa image Slideer  styling

var slideIndex = 1;
    var slideTimer;

    showSlides();

    function plusSlides(n) {
        clearTimeout(slideTimer);
        showSlides(slideIndex += n);
    }

    function showSlides(n) {
        var i;
        var slides = document.getElementsByClassName("mySlides");

        if (n === undefined) {
            n = ++slideIndex;
        }

        if (n > slides.length) {
            slideIndex = 1;
        }

        if (n < 1) {
            slideIndex = slides.length;
        }

        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        slides[slideIndex - 1].style.display = "block";

        slideTimer = setTimeout(function () {
            showSlides(); // Change image every 3 seconds without incrementing index
        }, 4000);
    }


    var container = document.getElementById('container')
    var slider = document.getElementById('slider');
    var slidess = document.getElementsByClassName('slide').length;
    var buttons = document.getElementsByClassName('btn');
    
    var currentPosition = 0;
    var currentMargin = 0;
    var slidesPerPage = 0;
    var slidesCount = slidess - slidesPerPage;
    var containerWidth = container.offsetWidth;
    var prevKeyActive = false;
    var nextKeyActive = true;
    
    window.addEventListener("resize", checkWidth);
    
    function checkWidth() {
        containerWidth = container.offsetWidth;
        setParams(containerWidth);
    }
    
    function setParams(w) {
        if (w < 551) {
            slidesPerPage = 1;
        } else {
            if (w < 901) {
                slidesPerPage = 2;
            } else {
                if (w < 1101) {
                    slidesPerPage = 3;
                } else {
                    slidesPerPage = 4;
                }
            }
        }
        slidesCount = slidess - slidesPerPage;
        if (currentPosition > slidesCount) {
            currentPosition -= slidesPerPage;
        };
        currentMargin = - currentPosition * (100 / slidesPerPage);
        slider.style.marginLeft = currentMargin + '%';
        if (currentPosition > 0) {
            buttons[0].classList.remove('inactive');
        }
        if (currentPosition < slidesCount) {
            buttons[1].classList.remove('inactive');
        }
        if (currentPosition >= slidesCount) {
            buttons[1].classList.add('inactive');
        }
    }
    
    setParams();
    
    function slideRight() {
        if (currentPosition != 0) {
            slider.style.marginLeft = currentMargin + (100 / slidesPerPage) + '%';
            currentMargin += (100 / slidesPerPage);
            currentPosition--;
        };
        if (currentPosition === 0) {
            buttons[0].classList.add('inactive');
        }
        if (currentPosition < slidesCount) {
            buttons[1].classList.remove('inactive');
        }
    };
    
    function slideLeft() {
        if (currentPosition != slidesCount) {
            slider.style.marginLeft = currentMargin - (100 / slidesPerPage) + '%';
            currentMargin -= (100 / slidesPerPage);
            currentPosition++;
        };
        if (currentPosition == slidesCount) {
            buttons[1].classList.add('inactive');
        }
        if (currentPosition > 0) {
            buttons[0].classList.remove('inactive');
        }
    };    