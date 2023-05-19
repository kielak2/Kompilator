
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

const content = document.querySelector(".content");
const files = document.getElementsByClassName("file");
for (let k = 0; k < files.length; ++k) {
    files[k].addEventListener("click", function() {
        content.textContent = this.getAttribute("data-content");
    });
}

 var standardRadio = document.querySelectorAll('#Tab1 input[type="radio"]');

  // Add event listeners to the radio buttons
  standardRadio.forEach(function (radio) {
    radio.addEventListener('click', function () {
      // Update the value of the hidden input field with the selected radio button's value
      document.querySelector('#standard').value = this.value;
    });
  });

  // Get all the radio buttons inside the #Tab2 element
var optimizationRadio = document.querySelectorAll('#Tab2 input[type="radio"]');

// Add event listeners to the radio buttons
optimizationRadio.forEach(function (radio) {
  radio.addEventListener('click', function () {
    // Update the value of the hidden input field with the selected radio button's value
    document.querySelector('#optimization').value = this.value;
  });
});

var standardProcesor = document.querySelectorAll('#Tab3 input[type="radio"]');

  // Add event listeners to the radio buttons
  standardProcesor.forEach(function (radio) {
    radio.addEventListener('click', function () {
      // Update the value of the hidden input field with the selected radio button's value
      document.querySelector('#procesor').value = this.value;
    });
  });

  var mcsRadio = document.querySelectorAll('#MCS input[type="radio"]');

  // Add event listeners to the radio buttons
  mcsRadio.forEach(function (radio) {
    radio.addEventListener('click', function () {
      // Update the value of the hidden input field with the selected radio button's value
      document.querySelector('#MCSoption').value = this.value;
    });
  });

  var z80Radio = document.querySelectorAll('#Z80 input[type="radio"]');

  // Add event listeners to the radio buttons
  z80Radio.forEach(function (radio) {
    radio.addEventListener('click', function () {
      // Update the value of the hidden input field with the selected radio button's value
      document.querySelector('#Z80Soption').value = this.value;
    });
  });

  var stmRadio = document.querySelectorAll('#STM input[type="radio"]');

  // Add event listeners to the radio buttons
  stmRadio.forEach(function (radio) {
    radio.addEventListener('click', function () {
      // Update the value of the hidden input field with the selected radio button's value
      document.querySelector('#STMoption').value = this.value;
    });
  });


var compileBtn = document.getElementById('compile-btn');
var myForm = document.getElementById('myForm');

compileBtn.addEventListener('click', function() {
  const selectedStandard = document.querySelector('#standard').value;
  const selectedProcessor = document.querySelector('#procesor').value;
  const selectedOptimization = document.querySelector('#optimization').value;
  const selectedMcsOption = document.querySelector('#MCSoption').value;
  const selectedZ80Option = document.querySelector('#Z80Soption').value;
  const selectedStmOption = document.querySelector('#STMoption').value;
  localStorage.setItem('selectedStandard', selectedStandard);
  localStorage.setItem('selectedProcessor', selectedProcessor);
  localStorage.setItem('selectedOptimization', selectedOptimization);
  localStorage.setItem('selectedMcsOption', selectedMcsOption);
  localStorage.setItem('selectedZ80Option', selectedZ80Option);
  localStorage.setItem('selectedStmOption', selectedStmOption);
  myForm.submit();
});

const selectedStandard = localStorage.getItem('selectedStandard');
const selectedProcessor = localStorage.getItem('selectedProcessor');
const selectedOptimization = localStorage.getItem('selectedOptimization');
const selectedMcsOption = localStorage.getItem('selectedMcsOption');
const selectedZ80Option = localStorage.getItem('selectedZ80Option');
const selectedStmOption = localStorage.getItem('selectedStmOption');

if (selectedStandard) {
  document.querySelector(`input[name="standard"][value="${selectedStandard}"]`).checked = true;
}

if (selectedProcessor) {
  document.querySelector(`input[name="procesor"][value="${selectedProcessor}"]`).checked = true;
}

if (selectedOptimization) {
  document.querySelector(`input[name="optimization"][value="${selectedOptimization}"]`).checked = true;
}

if (selectedMcsOption) {
  document.querySelector(`input[name="MCSoption"][value="${selectedMcsOption}"]`).checked = true;
}

if (selectedZ80Option) {
  document.querySelector(`input[name="Z80Soption"][value="${selectedZ80Option}"]`).checked = true;
}

if (selectedStmOption) {
  document.querySelector(`input[name="STMoption"][value="${selectedStmOption}"]`).checked = true;
}

standardRadio.forEach(function (radio) {
  if (radio.checked) {
    // If a radio button is checked, set the value of the hidden input field to its value
     document.querySelector('#standard').value = radio.value;
  }
});

standardProcesor.forEach(function (radio) {
  if (radio.checked) {
    // If a radio button is checked, set the value of the hidden input field to its value
     document.querySelector('#procesor').value = radio.value;
  }
});

optimizationRadio.forEach(function (radio) {
  if (radio.checked) {
    // If a radio button is checked, set the value of the hidden input field to its value
     document.querySelector('#optimization').value = radio.value;
  }
});

mcsRadio.forEach(function (radio) {
  if (radio.checked) {
    // If a radio button is checked, set the value of the hidden input field to its value
     document.querySelector('#MCSoption').value = radio.value;
  }
});

z80Radio.forEach(function (radio) {
  if (radio.checked) {
    // If a radio button is checked, set the value of the hidden input field to its value
     document.querySelector('#Z80Soption').value = radio.value;
  }
});

stmRadio.forEach(function (radio) {
  if (radio.checked) {
    // If a radio button is checked, set the value of the hidden input field to its value
     document.querySelector('#STMoption').value = radio.value;
  }
});


function downloadFile() {
  const content = document.querySelector('.code-box pre').textContent;
  const filename = prompt('Enter filename', 'file.asm');

  if (filename) {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = url;
    link.download = filename;

    link.click();

    URL.revokeObjectURL(url);
  }
}

window.onload = function() {
    // Create a mapping between the radio button values and the div ids
    var idMap = {
        "mmcs51": "MCS",
        "mz80": "Z80",
        "mstm8": "STM"
    };

    // Get all the radio buttons in Tab3
    var radios = document.querySelectorAll('#Tab3 input[type="radio"]');

    // Add a click event listener to each radio button
    for (var i = 0; i < radios.length; i++) {
        radios[i].addEventListener('click', function() {
            // Hide all the processor-specific divs in Tab4
            var divs = document.querySelectorAll('#Tab4 div');
            for (var j = 0; j < divs.length; j++) {
                divs[j].style.display = 'none';
            }

            // Show the div that corresponds to the selected processor
            var selectedProcessor = idMap[this.value];
            document.getElementById(selectedProcessor).style.display = 'block';
        });

        // If the radio button is already selected, trigger its click event
        if (radios[i].checked) {
            radios[i].click();
        }
    }
}