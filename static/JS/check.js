function checkEmail (str) {
	var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/
	if (reg.test(str)) {
		return true
	}else{
		return false
	}
}
function checkTelephone (str) {
	var reg = /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/
	if (reg.test(str)) {
		return true
	}else{
		return false
	}
}
function checkIdentificationCard (str) {
	var reg = /(^\d{15}$)|(^\d{17}([0-9]|X)$)/
	if (reg.test(str)) {
		return true
	}else{
		return false
	}
}
function checkContainChinese (str) {
	var reg = /.*[\u4e00-\u9fa5]+.*$/
	if (reg.test(str)) {
		return true
	}else{
		return false
	}
}
function checkContainSpecialChar (str) {
	var reg =/[(\ )(\~)(\!)(\@)(\#)(\$)(\%)(\^)(\&)(\*)(\()(\))(\-)(\_)(\+)(\=)(\[)(\])(\{)(\})(\|)(\\)(\;)(\:)(\')(\")(\,)(\.)(\/)(\<)(\>)(\?)(\)]+/
	if (reg.test(str)) {
		return true
	}else{
		return false
	}
}
function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return decodeURIComponent(r[2]);
    }
    return null;
}