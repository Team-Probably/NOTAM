  $(document).ready(function(){
    $('.modal').modal();
  });
  
 function check_login()
 {
    var f = fetch('/check_login').then(
    response=>{
        response.json().then((data)=>{console.log(data);editMode(data)})
    }
);
 }