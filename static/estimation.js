function validateEstimation() {
    var VName = document.forms["estimation"]["bill"].value;
        if (VName == "")  {
            alert("Please enter a number!");
            return false;
        }

        var VName = document.forms["estimation"]["cover"].value;
        if (VName == "") {
            alert("Please enter a number!");
            return false;
        }
}