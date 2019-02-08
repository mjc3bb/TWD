$(document).ready(function(){
    // $("#about-btn").click(function (event) {
    //     alert("You clicked with JQuery!");
    // });

    $("p").hover(function () {
        $(this).css('color','red');
    },function () {
        $(this).css('color','blue');
    });

    $("#about-btn").click(function (event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + "ooo"
        $("#msg").html(msgstr)
    });
});