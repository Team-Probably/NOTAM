$('#create_notam').on('click', function() {

    var notam_series = $('#notam_series').val();
    var notam_no = $('#notam_no').val();
    var fir = $('#fir').val();
    var scenario = $('#scenario').val();
    var nature = $('#nature').val();
    var coords = $('#coords').val();
    var time = $('#time').val();
    var remarks = $('#remark').val();

    var notam_data = {
        notam_series: notam_series,
        notam_no: notam_no,
        fir: fir,
        scenario: scenario,
        nature: nature,
        coords: coords,
        time: time,
        remarks: remarks
    }
        
    req = $.ajax({
        url : '/create_notam',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(notam_data)

        
    });

    req.done(function (data) {

        console.log('notam created');

    });
    
    

});