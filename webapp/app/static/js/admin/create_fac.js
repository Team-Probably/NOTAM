$('#create_notam').on('click', function() {
    // var chk = document.getElementById('checkboxtog');
    // console.log(chk.checked);
    // if(!chk.checked)
    //     return;
    var notam_notam = $('#notam_notam_fac').val();
    var notam_series = $('#notam_series_fac').val();
    var notam_no = $('#notam_no_fac').val();
    var fir = $('#fir_fac').val();
    var ident = $('#ident_fac').val();
    var freq = $('#freq_fac').val();
    var latin = $('#latin_fac').val();
    var longin = $('#longin_fac').val();
    var stime = $('#st_date_fac').val() + " " + $('#st_time_fac').val();
    var etime = $('#ed_date_fac').val() + " " + $('#ed_time_fac').val();
    var remarks = $('#remark_fac').val();
    
    var map_poly = [center, radius, poly];

    var notam_data = {
        notam_notam: notam_notam,
        notam_series: notam_series,
        notam_no: notam_no,
        fir: fir,
        ident: ident,
        freq: freq,
        latin: latin,
        longin: longin,
        stime: stime,
        etime: etime,
        remarks: remarks,
        map_poly: map_poly,
        zoom: zoom,
        notam_type: 'facility'
    }
    console.log('Adding Notam to Facility');
    $.ajax({
        url : '/create_notam',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(notam_data),
        success: function (data) {
            console.log('notam created');
            if (data.success == true) {
                console.log('Notam Created');
                var modal = document.getElementById('myModal');
                $(modal).fadeOut();
                M.toast({ html: 'NOTAM Created Successfully', classes: 'rounded light-green accent-3' })
            } else {
                console.log(data.success);
                var modal = document.getElementById('myModal');
                M.toast({ html: 'ERROR!', classes: 'rounded red accent-3' })
            }
            
        }

        
    });

    
    
    

});