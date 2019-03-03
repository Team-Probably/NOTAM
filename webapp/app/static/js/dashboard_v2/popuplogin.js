  $(document).ready(function(){
    $('.modal').modal();
    var instance = M.Modal.getInstance($('#modalveri'));
    console.log(document.getElementById('sveri').innerHTML);
    if(document.getElementById('sveri').innerHTML==='True')
    {
      console.log('opening');
      instance.open();
    }
  });
  
 function check_login()
 {
    var f = fetch('/check_login').then(
    response=>{
        response.json().then((data)=>{console.log(data);editMode(data)})
    }
);
 }