

  // Or with jQuery

  $(document).ready(function(){
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
  });

function loadgauge(e)
{
  console.log(e); 
  llimit = e.parentNode.getElementsByClassName('llimit')[0].innerHTML;
  ulimit = e.parentNode.getElementsByClassName('ulimit')[0].innerHTML;
  e.parentNode.getElementsByClassName('llim')[0].innerHTML = parseInt(llimit*10);
  e.parentNode.getElementsByClassName('ulim')[0].innerHTML = parseInt(ulimit*10;

  var gauge = e.parentNode.getElementsByClassName('gauge')[0]
  gauge.style.top = (999 - parseInt(ulimit)) / 10 + "%";
  e.parentNode.getElementsByClassName('ulim')[0].style.bottom = (100 - ((999 - parseInt(ulimit)) / 10 - 1 )) + "%";
  e.parentNode.getElementsByClassName('llim')[0].style.bottom = (100 - ((999 - parseInt(ulimit)) / 10 - 1) - (parseInt(ulimit) - parseInt(llimit)) / 10)+ "%";
  gauge.style.height = (parseInt(ulimit) - parseInt(llimit)) / 10 + "%";
  
}

$(".dropdown-trigger").dropdown();
