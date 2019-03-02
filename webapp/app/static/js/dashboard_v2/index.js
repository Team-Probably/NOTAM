$(document).ready(function () {
    $('.sidenav').sidenav();
});

$('#tp').on('click', function (e) {

    $('.sidenav').sidenav('open');

});

$(document).ready(function () {
    $('select').formSelect();
});

$(document).ready(function () {
    $('.timepicker').timepicker({
        twelveHour:false
    });
});

$(".dropdown-trigger").dropdown();

$(document).ready(function () {
    $('.datepicker').datepicker(
        {
            format: 'yyyy/mm/dd'
        }
    );
});

$('#auto_notam').on('click', function () {
    console.log("NOTAM");
    notam = $('#notam_notam').val();
    console.log(notam);
    location.href = '/predict_notam?notam=' + notam;
    // $.get(
    //     // 'predict_notam',
    //     'index',
    //     { notam: notam }
    // )
});