function objectStart() {
    intro();
}
window.onload = objectStart;

function intro() {
    var currentDiv = $("#box1");
    var nextDiv, count = 1;
    var myInterval = setInterval(function() {
        if (count == 5) {
            count = 1;
            currentDiv.hide();
            currentDiv = $("#box1");
            currentDiv.show();
        } else {
            count++;
            currentDiv.hide();
            currentDiv = currentDiv.next();
            currentDiv.show();
        }
    }, 2000);
}