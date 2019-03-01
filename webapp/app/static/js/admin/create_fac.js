$('#create_notam').on('click', function() {
    var chk = document.getElementById('checkboxtog');
    console.log(chk.checked);
    if(!chk.checked)
        return;
    var notam_series = $('#notam_series_fac').val();
    var notam_no = $('#notam_no_fac').val();
    var fir = $('#fir_fac').val();
    var ident = $('#ident_fac').val();
    var latin = $('#latin_fac').val();
    var longin = $('#longin_fac').val();
    var stimein = $('#stimein_fac').val();
    // var endtimein = $('#endtimein').val();
    var remarks = $('#remark_fac').val();
    var freq = $('#freq_fac').val();

    var notam_data = {
        notam_series: notam_series,
        notam_no: notam_no,
        fir: fir,
        ident: ident,
        latin: latin,
        longin: longin,
        freq: freq,
        stimein: stimein,
        // endtimein: endtimein,
        remarks: remarks,
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
            } else {
                console.log(data.success);
                var modal = document.getElementById('myModal');
                
            }
            
        }

        
    });

    
    
    

});

// For Date Time Picker

window.onload = function () {
    $('#stimein_fac').daterangepicker({
        timePicker: true,
        startDate: moment().startOf('hour'),
        endDate: moment().startOf('hour').add(32, 'hour'),
        locale: {
            format: 'M/DD hh:mm A'
        }
    });

    $('#stimein').daterangepicker({
        timePicker: true,
        startDate: moment().startOf('hour'),
        endDate: moment().startOf('hour').add(32, 'hour'),
        locale: {
            format: 'M/DD hh:mm A'
        }
    });
};
