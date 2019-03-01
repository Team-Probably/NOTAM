$("#down_tab").click(function(){
    $("#down_nav").toggleClass("down_hide")
}); 

$("#right_tab").click(function(){
    $("#right_nav").toggleClass("right_hide")
}); 

u=0
$("#halfscreen").click(function(){
    $("#right_nav").toggleClass("hide")
    // $(".435").toggleId("down_nav")
    if (u==1) {
        
        $('.435').css({ 
            'width': '25w',
            'position': 'absolute',
            'height': '45vh',
            'right': '5vw',
            'bottom': '0vw'});
        $("#mapfull").css({
            'width': '100vw',
            'transition': '0.5s' 
        });
    
        u=0;
    } else {
        
    
        $('.435').css({ 
            'width': '35vw',
            'position': 'absolute',
            'height': '100vh',
            'right': '0vw',
            'top': '0vw'});
        $("#mapfull").css({
            'width': '65vw',
            'transition': '0.5s' 
        });
        
        u=1;
    }
}); 