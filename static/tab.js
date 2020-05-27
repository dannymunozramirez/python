    function validate() {
        var VName = document.forms["myForm"]["Name"].value;
        if (VName == "") {
            alert("Name must be filled out");
            return false;
        }

        var VName = document.forms["myForm"]["Last"].value;
        if (VName == "") {
            alert("Last Name must be filled out");
            return false;
        }

        var VName = document.forms["myForm"]["EMail"].value;
        if (VName == "") {
            alert("email must be filled out");
            return false;
        }

        var emailID = 
        atpos = emailID.indexOf("@");
        dotpos = emailID.lastIndexOf(".");
        
        if (atpos < 1 || ( dotpos - atpos < 2 )) {
            alert("Please enter correct email ID")
            document.myForm.EMail.focus() ;
            return false;
        }
        return( true );

       
    }
