function editfn(e)
{
    var mstrn = String(e.parentNode.parentNode.parentNode.parentNode.getElementsByClassName('notam_no')[0].innerHTML).trim();
    var notam_no=mstrn.slice(mstrn.length-4,mstrn.length);
    var f = fetch('/getnotamdata?notamid='+notam_no).then(
        response=>{
            response.json().then((data)=>{console.log(data);editMode(data)})
        }
    );
   
}

function editMode(data)
{
    document.getElementById('modalhead').innerHTML='Edit NOTAM';
    if(data.type==="facitity") editMode_fac(data);
    else{
        document.getElementById('notam_series').value = data.class;
        document.getElementById('notam_no').value = data.notam_no;
        document.getElementById('fir').value = data.fir;
        document.getElementById('scenario').value = data.scenario;
        document.getElementById('remark').value = data.remarks;
        modal.style.display = "block";
    }
}

function editMode_fac(data)
{
        document.getElementById('notam_series_fac').value = data.class;
        document.getElementById('notam_no_fac').value = data.notam_no;
        document.getElementById('fac').value = data.fac;
        document.getElementById('scenario').value = data.scenario;
        document.getElementById('remark_fac').value = data.remarks;
        document.getElementById('latin_fac').value = data.Coords[0][0];
        document.getElementById('longin_fac').value = data.Coords[0][1];
        modal.style.display = "block";
}

function deleteNotam(e)
{
    var mstrn = String(e.parentNode.parentNode.parentNode.parentNode.getElementsByClassName('notam_no')[0].innerHTML).trim();
    var notam_no=mstrn.slice(mstrn.length-4,mstrn.length);
    var f = fetch('/deletenotam?notamid='+notam_no).then(
        response=>{
            response.json().then((data)=>{console.log(data);editMode(data)})
        }
    );
}