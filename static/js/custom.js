
//Get the location info when the page is ready.
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

//Ajax POST request to the URL
$("#help-me").on("click", function(event) {
    event.preventDefault();
    let url = "/help-me/";
    let data = {
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        loc_latitude: $("input[id=loc-latitude]").val(),
        loc_longitude: $("input[id=loc-longitude").val(),
    };
    $.post(url, data, function (response) {
        json_data = JSON.parse(response);
        if (json_data.hasOwnProperty("formatted_address")) {
            document.getElementById("help-text").innerHTML = "Sending emergency service to...";
            document.getElementById("data-text").innerHTML = json_data["formatted_address"];
            document.getElementById("coord-lat").innerHTML = "<b>Latitude: </b>" + parseFloat(json_data["latitude"]).toFixed(4);
            document.getElementById("coord-lon").innerHTML = "<b>Longitude: </b>" + parseFloat(json_data["longitude"]).toFixed(4);
        } else {
            document.getElementById("help-text").innerHTML = "Something is wrong. Please try again."
            document.getElementById("data-text").innerHTML = "";
            document.getElementById("coord-lat").innerHTML = "";
            document.getElementById("coord-lon").innerHTML = "";
        }
    })
})
