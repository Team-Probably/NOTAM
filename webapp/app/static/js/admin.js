var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal 
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


function checkch()
{
    console.log('hi');
    var chk = document.getElementById('checkboxtog');
    if(chk.checked)
    {
        document.getElementById('fir').style.display='none';
        document.getElementById('fac').style.display='block';
        
    }
    else{
        document.getElementById('fac').style.display='none';
        document.getElementById('fir').style.display='block';
    }
}