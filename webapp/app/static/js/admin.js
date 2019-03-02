var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var showmap=false;
var showmap_fac= false;
// When the user clicks on the button, open the modal 
btn.onclick = function() {
    document.getElementById('modalhead').innerHTML='Create NOTAM';
    modal.style.display = "block";
    document.getElementById('notam_series').value = '';
    document.getElementById('notam_no').value = '';
    document.getElementById('fir').value ='';
    document.getElementById('scenario').value ='';
    document.getElementById('remark').value = '';
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

    if(event.target != document.getElementById('map_picker_fac') && event.target != document.getElementById('mapfa_fac') && showmap_fac)
        maptoggle_fac();
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

function maptoggle_fac(){
    console.log(showmap+" hi");
    if(showmap_fac)
    {
        showmap_fac=false;
        document.getElementById('mappickdiv_fac').style.display='none';
        
    }
    else{
        showmap_fac=true;
        document.getElementById('mappickdiv_fac').style.display='block';
    }
}