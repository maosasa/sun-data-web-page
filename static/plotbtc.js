//
// Calculator
//
function plotbtc() {
// Buid query parameter
    var param = {};
    param["start"] = document.getElementById("start").value;
    param["end"] = document.getElementById("end").value;
    var query = jQuery.param(param);

// Query with a new parameter 
    $.get("/plot/btc" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//
document.getElementById("start").addEventListener("change", function(){
    plotbtc();
}, false)
document.getElementById("start").addEventListener("keyup", function(){
    plotbtc();
}, false);
document.getElementById("end").addEventListener("change", function(){
    plotbtc();
}, false);
document.getElementById("end").addEventListener("keyup", function(){
    plotbtc();
}, false);
document.getElementById("plot").addEventListener("click", function(){
    plotbtc();
}, false);
plotbtc();
