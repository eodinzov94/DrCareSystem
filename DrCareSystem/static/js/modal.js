// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Get the modal
var q = document.getElementById("qModal");

// Get the button that opens the modal
var qbtn = document.getElementById("qBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("qclose")[0];

// When the user clicks the button, open the modal 
qbtn.onclick = function() {
  q.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  q.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    q.style.display = "none";
  }
}
