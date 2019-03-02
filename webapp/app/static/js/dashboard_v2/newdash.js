

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

  var gauge = e.parentNode.getElementsByClassName('gauge')[0]
  gauge.style.top=(999-parseInt(ulimit))/10+"%";
  gauge.style.height=(parseInt(ulimit)-parseInt(llimit))/10+"%";
}
        