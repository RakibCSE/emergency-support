
$(document).ready(function() {
    getLocation();

    function getLocation() {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(showPosition);
        } else {
          alert("Geolocation is not supported by this browser.");
        }
    }
    function showPosition(position) {
        document.getElementById("loc-latitude").value = position.coords.latitude;
        document.getElementById("loc-longitude").value = position.coords.longitude;
    }
});

$("#help-me").click(function() {
    $.ajax({
        type: "POST",
        url: "help-me/",
        data: {
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
            "loc_latitude": $("input[name=loc_latitude]").val(),
            "loc_longitude": $("input[name=loc_longitude]").val()
        },
        success: function(data) {
            document.getElementById("data-text").innerText = data;
        },
        error: function() {
            alert("Error")
        }
    });
});

