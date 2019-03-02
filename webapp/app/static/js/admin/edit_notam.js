function getNotamId(e){
    test2 = $(this);
    console.log(test2);
}

$('.adi').on('click',function(){
    mstrn = $(this).parents('.adi_full').find('.series')[0].innerHTML + $(this).parents('.adi_full').find('.adi_no')[0].innerHTML;
    notam = mstrn;
    console.log(notam)
});
$('.edit_notam').on('click', function() 
{
    // var chk = document.getElementById('checkboxtog');
    // console.log(chk.checked);
    // if(chk.checked)
    //     return;
    var notam_notam = $('#notam_notam').val();
    var notam_series = $('#notam_series').val();
    var notam_no = $('#notam_no').val();
    var fir = $('#fir').val();
    var scenario = $('#scenario').val();
    var nature = $('#nature').val();
    var latin = $('#latin').val();
    var longin = $('#longin').val();
    var stime = $('#st_date').val() + " " + $('#st_time').val();
    var etime = $('#ed_date').val() + " " + $('#ed_time').val();
    // var endtimein = $('#endtimein').val();
    var remarks = $('#remark').val();
    var map_poly = [center, radius, poly];

    var notam_data = {
        notam_notam: notam_notam,
        notam_series: notam_series,
        notam_no: notam_no,
        fir: fir,
        scenario: scenario,
        nature: nature,
        latin: latin,
        longin: longin,
        stime: stime,
        etime: etime,
        // endtimein: endtimein,
        remarks: remarks,
        map_poly: map_poly,
        notam_type: "airspace"
    }
    console.log('Adding Notam to Airspace');
    console.log(notam_data);
    $.ajax({
        url : '/edit_notam',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(notam_data),
        success: function (data) 
        {
            console.log('notam created');
            if (data.success == true) 
            {
                console.log('Notam Created');
                var modal = document.getElementById('myModal');
                $(modal).fadeOut();
                M.toast({html: 'NOTAM Created Successfully', classes:'rounded light-green accent-3'})
            } else
            {
                console.log(data.success);
                var modal = document.getElementById('myModal');
                M.toast({ html: 'ERROR!' ,classes: 'rounded red accent-3'})
            }
            
        }
    });
});