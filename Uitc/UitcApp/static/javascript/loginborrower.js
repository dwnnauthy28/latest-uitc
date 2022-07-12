function option(){
    var idnumber = document.getElementById("IDnumber");
    var pw1 = document.getElementById("pass");
    if(idnumber.value == "user" & pw1.value == "user") {
      alert("Login");
      window.location= "{%url 'dashboard' %}";
    }
    else {
      alert("Login Failed");
    }
     
}
var objPeople = [
	{ // Object @ 0 index
		idnumber: "admin",
		pw: "admin"
	},
	{ // Object @ 1 index
		idnumber: "cristian",
		pw: "cristian"
	},
	{ // Object @ 2 index
		idnumber: "edwin",
		pw: "edwin"
	}

]

function loginborrower() {
	var idnumber = document.getElementById('IDnumber').value
	var pw2 = document.getElementById('pass').value

	for(var i = 0; i < objPeople.length; i++) {
		// check is user input matches username and password of a current index of the objPeople array
		if(idnumber == objPeople[i].idnumber && pw2 == objPeople[i].pw) {
      alert("Login Successful");
      window.location= href="{%url 'dashboard' %}";
      return ;
    }
    else if(idnumber !== objPeople[i].idnumber && pw2 !== objPeople[i].pw) {
      alert("Login Failed");
      return ; 
    }

	}
}


function checkPassword(){
  let password = document.getElementById("pass1").value;
  let cnfrmPassword = document.getElementById("pass2").value;
  console.log(" Password:", password,'\n',"Confirm Password:",cnfrmPassword);
  let message = document.getElementById("message");

  if(password.length != 0){
      if(password == cnfrmPassword){
          alert("Passwords match");
      }
      else{
          alert("Password did not match, Fill up again");
      }
  }
}
