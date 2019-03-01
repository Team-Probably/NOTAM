$('#create_notam').on('click', function() {

    var notam_series = $('#notam_series').val();
    var notam_no = $('#notam_no').val();
    var fir = $('#fir').val();
    var scenario = $('#scenario').val();
    var nature = $('#nature').val();
    var latin = $('#latin').val();
    var longin = $('#longin').val();
    var stimein = $('#stimein').val();
    // var endtimein = $('#endtimein').val();
    var remarks = $('#remark').val();

    var notam_data = {
        notam_series: notam_series,
        notam_no: notam_no,
        fir: fir,
        scenario: scenario,
        nature: nature,
        latin: latin,
        longin: longin,
        stimein: stimein,
        // endtimein: endtimein,
        remarks: remarks
    }
    console.log('Adding Notam to Database');
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
        "showDropdowns": true,
        "timePicker": true,
        "timePicker24Hour": true,
        "startDate": "02/02/2019",
        "endDate": "03/02/2019",
        "drops": "up",
        locale: {
            format: 'YYYY-MM-DD hh:mm A'
        }
    }, function (start, end, label) {
        console.log('New date range selected: ' + start.format('YYYY-MM-DD hh:mm A') + ' to ' + end.format('YYYY-MM-DD hh:mm A') + ' (predefined range: ' + label + ')');
    });

    $('#stimein').daterangepicker({
        "showDropdowns": true,
        "timePicker": true,
        "timePicker24Hour": true,
        "startDate": "02/02/2019",
        "endDate": "03/02/2019",
        "drops": "up",
        locale: {
            format: 'YYYY-MM-DD hh:mm A'
        }
    }, function (start, end, label) {
        console.log('New date range selected: ' + start.format('YYYY-MM-DD hh:mm A') + ' to ' + end.format('YYYY-MM-DD hh:mm A') + ' (predefined range: ' + label + ')');
    });
};
