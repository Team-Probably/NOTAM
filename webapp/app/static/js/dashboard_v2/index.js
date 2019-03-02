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
            format: 'dd/mm/yyyy'
        }
    );
});
