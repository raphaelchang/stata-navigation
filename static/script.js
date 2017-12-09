$(document).ready(function() {
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
        $.ajax({
            type: "POST",
            url: "/upload",
            contentType: false,
            processData: false,
            data: new FormData($(this)[0]),
            success: function(data)
            {
                var image_holder = $("#image-holder2");
                image_holder.empty();
                $("<img />", {
                    "src": '/train/' + data,
                    "width": $(window).width()
                }).appendTo(image_holder);
                image_holder.show();
                $("#slide-container2").show();
                $("#slide-container2").animate({top: 0}, 500, function() {
                    $("#spinner").hide();
                });
                $('#image-upload').val('');
            }
        });
    });
    $('#image-upload-button').click(function(){
        $('#image-upload').click();
    });
    $('#ok').click(function(){
        $('#submit').click();
    });
    $("#close").click(function() {
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
        $("#close").click();
    });
});
