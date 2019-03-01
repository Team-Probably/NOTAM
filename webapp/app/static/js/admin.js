var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var showmap=false;
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
  if(event.target != document.getElementById('map_picker') && event.target != document.getElementById('mapfa') && showmap)
    maptoggle();
}


function checkch()
{
    console.log('hi');
    var chk = document.getElementById('checkboxtog');
    if(chk.checked)
    {
        document.getElementById('firdiv').style.display='none';
        document.getElementById('fac').style.display='block';
        
    }
    else{
        document.getElementById('fac').style.display='none';
        document.getElementById('firdiv').style.display='block';
    }
}

function maptoggle(){
    console.log(showmap+" hi");
    if(showmap)
    {
        showmap=false;
        document.getElementById('mappickdiv').style.display='none';
        
    }
    else{
        showmap=true;
        document.getElementById('mappickdiv').style.display='block';
    }
}