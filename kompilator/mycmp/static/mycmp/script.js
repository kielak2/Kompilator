
//zmiana szaty wizualnej strony
const toggle = document.getElementById('toggleDark');
const body = document.querySelector('body');

toggle.addEventListener('click', function(){ 
  this.classList.toggle('bi-moon');
  if(this.classList.toggle('bi-brightness-high-fill')) {
        body.style.backgroundColor = "#EEEEEE";
        body.style.color = "#212121";
        body.style.transition = '1s';
    } else {
        body.style.backgroundColor = "#263238";
        body.style.color = "#EEEEEE";
        body.style.transition = '1s';
    }
})

//otwieranie zakładek
function openTab(evt, tabNr) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName("footer");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  document.getElementById(tabNr).style.display = "block";
}


window.onload = function() {
  document.getElementById("Tab1").style.display = "block";
}

//drzewiasta struktura
var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

//hamburger menu
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", ()=>{
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.
  addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
  }))


  //selector 
  const selector = document.querySelector('.custom-selector');
  selector.addEventListener('change', e => {
    console.log('changed', e.targer.value);
  })

const codeBox = document.querySelector('.code-box');

// Add event listener to scroll the code box when the mouse wheel is used
codeBox.addEventListener('wheel', function(event) {
  event.preventDefault();

  // How much to scroll on each mouse wheel event
  const scrollAmount = 30;

  // Determine how far to scroll based on the direction of the mouse wheel
  const delta = Math.sign(event.deltaY);
  const scrollDelta = delta * scrollAmount;

  // Scroll the code box
  codeBox.scrollTop += scrollDelta;
});



