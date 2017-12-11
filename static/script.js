$(document).ready(function() {
    var loading = false;
    $("#spinner").hide();
    $("#image-upload").on('change', function () {
        var image_holder = $("#image-holder");
        image_holder.empty();
        var reader = new FileReader();
        reader.onload = function (e) {
            $("<img />", {
                "src": e.target.result,
                "width": $(window).width()
            }).appendTo(image_holder);
        }
        image_holder.show();
        reader.readAsDataURL($(this)[0].files[0]);
        $("#slide-container").show();
        $("#slide-container").animate({top: 0}, 500);
    });
    $("#form").submit(function(e) {
        e.preventDefault()
        $("#spinner").show();
        $("#image-holder").animate({opacity: 0.7}, 100);
        $(".option-button").css({backgroundColor: "#aaa", cursor: "default"}, 100);
        $("#ok2").removeAttr("style");
        loading = true;
        $.ajax({
            type: "POST",
            url: "/upload",
            contentType: false,
            processData: false,
            data: new FormData($(this)[0]),
            success: function(data)
            {
                loading = false;
                var image_holder = $("#image-holder2");
                image_holder.empty();
                $("<img />", {
                    "id": "map",
                    "src": '/maps/' + data.floor + '.png',
                    "width": $(window).width()
                }).appendTo(image_holder);
                $("#map").on('load', function() {
                    $("#marker").css({'-webkit-transform': 'rotate(' + (315 - 180 * data.orientation) + 'deg)',
                        '-moz-transform': 'rotate(' + (315 - 180 * data.orientation) + 'deg)',
                        'transform': 'rotate(' + (315 - 180 * data.orientation) + 'deg)',
                        'left': (-1002 + data.x * 2.7) / 1384.0 * $(this).width() + 'px',
                        'top': (-36 + data.y * 2.22) / 1156.0 * $(this).height() + 'px'});
                });
                image_holder.show();
                $("#slide-container2").show();
                $("#close").click();
                $("#slide-container2").animate({top: 0}, 500, function() {
                    $("#spinner").hide();
                    $("#image-holder").animate({opacity: 1.0}, 0);
                    $(".option-button").removeAttr("style");
                });
                $('#image-upload').val('');
            }
        });
    });
    $('#image-upload-button').click(function(){
        $('#image-upload').click();
    });
    $('#ok').click(function(){
        if (loading)
            return;
        $('#submit').click();
    });
    $("#close").click(function() {
        if (loading)
            return;
        $("#slide-container").animate({top: "100%"}, 500, function() {
            $("#image-holder").empty();
            $("#slide-container").hide();
        });
    });
    $("#ok2").click(function() {
        $("#slide-container2").animate({top: "100%"}, 500, function() {
            $("#image-holder2").empty();
            $("#slide-container2").hide();
        });
    });
});
