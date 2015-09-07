function checkUserName () {
	var username=document.forms[0].username.value
	var div=document.getElementById('username')
	if (username.length<6||username.length>12) {
		div.style.color="#FF0000"
		div.innerHTML='帐号长度必须是6至12位'
		return false
	}else if(checkContainChinese(username)){
		div.style.color="#FF0000"
		div.innerHTML='帐号不能包含中文'
		return false
	}else{
		// div.style.color="#00FF00"
		div.innerHTML=''
		return true
	}
}
function checkPassword () {
	var password=document.forms[0].password.value
	var div=document.getElementById('password')
	if (password.length<6||password.length>12) {
		div.style.color="#FF0000"
		div.innerHTML='密码必须是6至12位'
		return false
	}else if(checkContainChinese(password)){
		div.style.color="#FF0000"
		div.innerHTML='密码不能包含中文'
		return false
	}else{
		// div.style.color="#00FF00"
		div.innerHTML=''
		return true
	}
}
function checkPassword2 () {
	var password=document.forms[0].password.value
	var password2=document.forms[0].password2.value
	var div=document.getElementById('password2')
	if (password!=password2) {
		div.style.color="#FF0000"
		div.innerHTML='两次密码输入不一致'
		return false
	}else{
		// div.style.color="#00FF00"
		div.innerHTML=''
		return true
	}
}
function checkAll () {
	if (checkUserName()&&checkPassword()&&checkPassword2()) {
		return true
	}else{
		return false
	}
}