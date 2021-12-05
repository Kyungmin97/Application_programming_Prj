// 여러 브라우저 지원위해서 event 값 전역변수 저장
var g_event;
document.onkeypress = function(e) {
	if( typeof(e) != "undefined") {
		g_event = e;
	} else {
		g_event = event;
	}
};


document.write("<script type='text/javascript' src='/js/common/jquery-1.8.3.js'><"+"/script>");
document.write("<script type='text/javascript' src='/js/common/jquery-ui.js'><"+"/script>");
document.write("<script type='text/javascript' src='/js/common/jquery.blockUI.js'><"+"/script>");
document.write("<script type='text/javascript' src='/js/common/jquery.meio.mask.js'><"+"/script>");
document.write("<script type='text/javascript' src='/js/common/hris.jquery.plugin.setting.js'><"+"/script>");
document.write("<script type='text/javascript' src='/js/common/hris.prototype.js'><"+"/script>");
document.write("<script type='text/javascript' src='/js/common/lcslog.js'><"+"/script>");
document.write("<script type='text/javascript' src='/js/common/jquery.placeholder.js'><"+"/script>");

// 입사지원서 개인정보 동의 창
function openRecruitAgreePage(sysCompanyCd, annoId, classId, jobId, entTypeCd) {
	var page_url = "";
	var param = "";

	param += "annoId=" + annoId;
	param += "&classId=" + classId;
	param += "&jobId=" + jobId;
	param += "&entTypeCd=" + entTypeCd;
	param += "&sysCompanyCd=" + sysCompanyCd;

	page_url = "/login/agreement?";
	var win = open(page_url + param, "_application","height=530,width=600,resizable=yes,scrollbars=no");
	win.focus();
}
// 입사지원서 로그인
function openRecruitLoginPage(sysCompanyCd, annoId, classId, jobId, entTypeCd, mode) {
	var page_url = "";
	var param = "";
	var height = "480";

	param += "annoId=" + annoId;
	param += "&classId=" + classId;
	param += "&jobId=" + jobId;
	param += "&entTypeCd=" + entTypeCd;
	param += "&sysCompanyCd=" + sysCompanyCd;
	param += "&mode=" + mode;

	page_url = "/login/login?";

	if (mode == "new") height = "510";

	var win = open(page_url + param, "_nhnrecruit","height=" + height + ",width=600,scrollbars=no");
	win.focus();
}
//입사지원서 로그인
function goRecruitLoginPage(sysCompanyCd, annoId, classId, jobId, entTypeCd, companyUri, localPrefix) {
	var page_url = "";
	var param = "";
	var height = "480";

	param += "annoId=" + annoId;
	param += "&classId=" + classId;
	param += "&jobId=" + jobId;
	param += "&entTypeCd=" + entTypeCd;
	param += "&sysCompanyCd=" + sysCompanyCd;
	
	if (typeof(localPrefix) == "undefined") {
		page_url = companyUri + "/login/login?";
	} else {
		page_url = companyUri + localPrefix + "/login/login?";
	}
	
	location.href = page_url + param; 
}

//입사지원서 작성창 띄우기
function openApplicationPage(sysCompanyCd) {
	var page_url = "";
	var param = "";
	var appl_win;

	if (typeof(sysCompanyCd) == "undefined" || sysCompanyCd != "KR") {
		page_url = "/application/personalinfo";
	} else {
		page_url = "/application/naver/apply";
	}
	
	appl_win = open(page_url + param, "_application","height=700,width=928,resizable=yes,scrollbars=yes");
	checkPopupBlocker(appl_win, true);
	appl_win.focus();
}

// 비밀번호 변경창 띄우기
function openChangePasswordPage(changePwdKey, resultKey) {
	var page_url = "";
	var param = "";
	var appl_win;

	param += "?changePwdKey=" + changePwdKey;
	param += "&resultKey=" + resultKey;

	page_url = "/login/changePwd";
	appl_win = open(page_url + param, "_changePwd","height=480,width=600,resizable=no,scrollbars=no");

	if (resultKey == "") {
		checkPopupBlocker(appl_win, true);
	} else {
		checkPopupBlocker(appl_win, false);
	}
}

// 결과확인창 띄우기
function openRecruitResultPage(resultKey) {
	var page_url = "";
	var param = "";
	var appl_win;

	param += "?resultKey=" + resultKey;

	page_url = "/result/announcement";
	appl_win = open(page_url + param, "_result","height=600,width=700,resizable=no,scrollbars=yes");
	checkPopupBlocker(appl_win, false);
}

// 내지원서 로그인창 띄우기
function openMyApplication(sysCompanyCd) {
	var page_url = "";
	var param = "";
	var appl_win;

	param += "?sysCompanyCd=" + sysCompanyCd;
	
	page_url = "/login/myApplicationLogin";
	
	appl_win = open(page_url + param, "_myApplication","height=530,width=600,resizable=yes,scrollbars=no");
	checkPopupBlocker(appl_win, true);
}

// 팝업차단 확인 스크립트
function checkPopupBlocker(winObj, selfClose) {
	setTimeout(function() {
		try {
			if (!winObj || winObj.outerHeight == 0) {
				alert("팝업이 차단되어 있습니다. 팝업차단을 해제 해 주세요.");
			} else {
				winObj.focus();
				if (selfClose) {
					window.close();
				}
			}
		} catch (e) {}
	}, 1000);
}

// 비밀번호 체크 함수.
function checkPasswordValidation(pwd) {
	var passRegExp = /^[a-zA-Z0-9]+$/;
	if(!passRegExp.test(pwd)) {
		alert("비밀번호는 숫자, 영문만 입력가능합니다.");
		return false;
	}

	var search_num = pwd.search(/[0-9]/g);
	var search_eng = pwd.search(/[a-zA-Z]/g);
	if (search_num < 0 || search_eng < 0) {
		alert("비밀번호는 숫자와 영문자 혼합해서 사용해야 합니다.");
		return false;
	}

	return true;
}
// HTML로 특정 QueryString 값을 가져오려고 할 때
function getQueryStringByName(_name) {
	var arr_querystring = "";
	var querystring = location.search;
	var name = "";
	var value = "";

	querystring = querystring.substring(1,querystring.length);  // 물음표(?) 제거
	arr_querystring = querystring.split("&");   // 이름-값 쌍으로 배열 생성

	for (var i=0; i < arr_querystring.length; i++) {
		name = arr_querystring[i].split("=")[0];

		if (name == _name) {
			value = arr_querystring[i].split("=")[1];
			break;
		}
	}

	return value;
}

// 외국인의 주민등록번호 뒷자리 랜덤함수 생성.
function makeRandomCtzno(){
   var rand = Math.floor(Math.random() * 999999);
   return rand;
}

// 다음 form object로 포커스이동
function changeNextFocus(obj, len, nextObj) {
	if (obj.value.length == len) nextObj.focus();
}

// 비밀번호 입력시 Caps Lock 키 켜져 있으면 주의문구 보여줌
function checkCapsLock( e ) {
	var myKeyCode=0;
	var myShiftKey=false;

	if ( document.all ) {
		myKeyCode=e.keyCode;
		myShiftKey=e.shiftKey;
	} else if ( document.layers ) {
		myKeyCode=e.which;
		myShiftKey=( myKeyCode == 16 ) ? true : false;
	} else if ( document.getElementById ) {
		myKeyCode=e.which;
		myShiftKey=( myKeyCode == 16 ) ? true : false;
	}
	if ( ( myKeyCode >= 65 && myKeyCode <= 90 ) && !myShiftKey ) {
		document.getElementById("caps_lock").style.display = "";
	} else if ( ( myKeyCode >= 97 && myKeyCode <= 122 ) && myShiftKey ) {
		document.getElementById("caps_lock").style.display = "";
	} else {
		document.getElementById("caps_lock").style.display = "none";
	}
}
// 메뉴 페이지 이동
function goPage(url, kubun) {
	if (typeof(kubun) == "undefined") {
		location.href = g_recruit_url + url;
	} else {
		location.href = kubun + url;
	}
}

function printPage() {
	window.print();
}

function showNhideMenu(id) {
	$.each($('#header').find('li'), function() {
		var thisObj = $(this);
		if(thisObj.attr('useType') == 'menu') {
			var tmpId = thisObj.attr('menuName');
			hideMenu(tmpId);
		}
	});
	hideMenu('aff');
	showMenu(id);
}

function addClass(obj, value) {
	obj.className += " " + value;
}

function removeClass(obj, value) {
	obj.className = obj.className.replace(" " + value, "");
}

// 팝업창에서 오늘하루만 띄우기에 사용하는 함수.
function closeNoticeWindow(checkobj, cookie_name) {
	if (checkobj.checked) {
		setCookie(cookie_name, "checked", 1, "/");
	}
	window.close();
}

//쿠키 생성
function setCookie(name, value, expiredays, path, domain, secure) {
	var todayDate = new Date();
	todayDate.setDate( todayDate.getDate() + expiredays );

	var curCookie = name + "=" + escape(value) +
		((expiredays) ? "; expires=" + todayDate.toGMTString() : "") +
		((path) ? "; path=" + path : "") +
		((domain) ? "; domain=" + domain : "") +
		((secure) ? "; secure" : "");
	document.cookie = curCookie;
}

// 쿠키값 가져오기
function getCookie(name) {
	var dc = document.cookie;
	var prefix = name + "=";
	var begin = dc.indexOf("; " + prefix);
	if (begin == -1) {
		begin = dc.indexOf(prefix);
		if (begin != 0) return null;
	} else {
		begin += 2;
	}
	var end = document.cookie.indexOf(";", begin);
	if (end == -1) end = dc.length;
	return unescape(dc.substring(begin + prefix.length, end));
}

// 쿠키 삭제
function deleteCookie(name, path, domain) {
	if (getCookie(name)) {
		document.cookie = name + "=" +
			((path) ? "; path=" + path : "") +
			((domain) ? "; domain=" + domain : "") +
			"; expires=Thu, 01-Jan-70 00:00:01 GMT";
	}
}
/**
 * 폼 객체중 mask (날짜, 시간, 금액 등) 속성의 부여된 input 객체들의 포맷팅 일괄 제거
 * form submit 전에 호출하여 포맷팅정보들 제거한다.
 * @param formobject
 * @returns void
 * @example
 * $(function(){
 *    removeFormElementFmt($("#frmSearch"));
 *    removeFormElementFmt(document.frmSearch);
 * });
 */
function removeFormElementFmt(frm) {
	if (frm instanceof jQuery) {
		frm = frm[0];
	}

	for ( var i = 0; i < frm.elements.length; i++) {
		var tagName = frm.elements[i].tagName;
		var maskType = frm.elements[i].getAttribute("maskType");

		if (tagName == "INPUT") {
			switch (maskType) {
				case "time":
				case "date":
				case "dateYmd":
				case "dateYm":
				case "ctzno":
				case "postno":
				case "bizno":
				case "number":
				case "integer":
				case "money":
				frm.elements[i].value=frm.elements[i].value.removeFmt();
			}
		}
	}
}

/**
 * Ajax를 이용한 동적 코드 검색
 * @param 대상SelectObject
 * @param parameter
 * @param resultType
 * @param initial  all : - 전체 -, choice : - 선택 -, "" : 빈값
 * @param selectedValue 기본선택값정의
 * @example
 * <pre>
 * 1. select change이벤트에서 다음과 같이 코딩
 * $("#orgList").change(function(){
 *    var param = "";
 *    param += "searchId=${hris:encryptMsgAES("sample.searchCodeListOrgPosCustomer")}";
 *    param += "&org_cd=" + $(this).val();
 *    g_hc.codeSearch($("#posList"), param, "option", "all");
 * });
 *
 * 2. ibsheet의 결과를 받을 때
 * var data = g_hc.codeSearch(null, param, "ibsheet");
 * alert(data["ibsheetCode"]);    // or alert(data.ibsheetCode);
 * alert(data["ibsheetName"]);
 *
 * 3. json 형태로 결과를 받을때
 * var data = g_hc.codeSearch(null, param, "data");
 *  for (var i = 0; i < data.length; i++) {
 *      alert(data[i].cd);
 *  }
 *  </pre>
 */
function codeSearch(targetObj, param, resultType, initial, selectedValue) {
	var async = false;
	var aventailPatch = {src:""};
	var retObj = new Object();
	var targetObjDOM = null;
	var targetObjJquery = null;

	aventailPatch.src = "/common/codeSearchJson.nhn";
	$.ajax({
		type: "POST",
		url: aventailPatch.src,
		data: param,
		success: function(data, textStatus, xhr){
			// select 의 option 형태로 결과 셋팅
			if (resultType == "option") {
				var selectedIndex = 0;
				if (targetObj instanceof jQuery) {
					targetObjDOM = targetObj[0];
					targetObjJquery = targetObj;
				} else {
					targetObjDOM = targetObj;
					targetObjJquery = $("#" + targetObj.getAttribute("id"));
				}

				// option 초기화
				while (targetObjDOM.options.length > 0) {
					targetObjDOM.remove(0);
				}

				if (initial == "all") {
					targetObjDOM.options[0] = new Option("", "");
					selectedIndex++;
				} else if (initial == "choice") {
					targetObjDOM.options[0] = new Option("- 선택 -", "");
					selectedIndex++;
				} else if (initial == "empty") {
					targetObjDOM.options[0] = new Option(" ", "");
					selectedIndex++;
				}

				var curNum = targetObjDOM.options.length;
				for (var i = 0; i < (data.length); i++) {
					var cd = data[i].cd;
					var cdNm = data[i].cdNm;

					targetObjDOM.options[i + curNum] = new Option(cdNm, cd);

					if (typeof(data[i].att1) != "undefined") {
						targetObjDOM.options[i + curNum].setAttribute("att1", data[i].att1);
					}
					if (typeof(data[i].att2) != "undefined") {
						targetObjDOM.options[i + curNum].setAttribute("att2", data[i].att2);
					}
					if (typeof(data[i].att3) != "undefined") {
						targetObjDOM.options[i + curNum].setAttribute("att3", data[i].att3);
					}
					if (typeof(data[i].att4) != "undefined") {
						targetObjDOM.options[i + curNum].setAttribute("att4", data[i].att4);
					}
					if (typeof(data[i].att5) != "undefined") {
						targetObjDOM.options[i + curNum].setAttribute("att5", data[i].att5);
					}
					if (typeof(selectedValue) != "undefined") {
						if (selectedValue == cd) {
							targetObjDOM.selectedIndex = selectedIndex;
						}
					}
					selectedIndex++;
				}

				targetObjJquery.change();
			} else if (resultType == "data") {
				retObj = data;
			}
		},
		error: function(x, o, e) {
			alert("오류가 발생하였습니다");
			retObj = x;
		},
		dataType: "json",
		async: async
	});
	return retObj;
}


/*
 * radio element의 기본값 설정해주는 함수
 * @param inputName : radio 객체의 name
 * @param checkValue : 체크해야할 값
 */
function initRadioValue(inputName, checkedValue) {
	$("input[name='" + inputName + "']").each(function() {
		if (checkedValue == $(this).val()) {
			$(this).attr("checked", true);
		}
	});
}

/*
 * select element의 기본값 설정해주는 함수
 * @param selectName : select 객체의 name
 * @param selectValue : 선택해야할 값
 */
function initSelectValue(selectName, selectedValue) {
	var selObj = $("select[name='" + selectName + "']");
	for (var i = 0; i < selObj.get(0).options.length; i++) {
		if (selObj.get(0).options[i].value == selectedValue) {
			selObj.get(0).options[i].selected = true;
		}
	}
}

// 공지사항 이동
function searchNoticeType(noticeTypeCd) {
	$("#noticeSearchForm #noticeTypeCd").val(noticeTypeCd);
	$("#noticeSearchForm").submit();
}

////////////////////////////////////////////////////////////////////
//네이버 채용 개편 추가
////////////////////////////////////////////////////////////////////
function selectComboBoxData(ulObj) {
	ulObj.find("li").each(function(idx) {
		$(this).click(function() {
			var divObj = $(this).parent().parent();
			//var spanObj = divObj.prev().prev().find("span").eq(0);
			//spanObj.empty().html($(this).text());
			//spanObj.addClass("selected");
			$("select[name='" + divObj.attr("target") + "'] option:eq(" + idx + ")").attr("selected", "selected").change();
		});
	});
}

function selectedComboBoxText(comboObj) {
	var selectedText = $("#" + comboObj.attr("id") + " option:selected").text();
	var spanObj = comboObj.prev().find("span");
	spanObj.empty().html(selectedText);
	spanObj.addClass("selected");
}

function createComboBoxList(comboObj) {
	var lySrch = comboObj.parent().parent().parent().parent().hasClass("ly_srch");
	var srchInfo = comboObj.parent().parent().parent().hasClass("srch_info");
	
	comboObj.next(".slct_box_list").remove();
	comboObj.after("<div class='slct_box_list'><ul></ul></div>");
	var divObj = comboObj.next();
	divObj.css("width", comboObj.css("width"));
	divObj.attr("target", comboObj.attr("name"));
	
	comboObj.find("option").each(function() {
		var text = $(this).text();
		var value = $(this).val();
		var style = "";
		
		if (text == "" && value == "") {
			// layer와 page의 style이 다름
			if (lySrch) {
				style = "margin-top:-35px;";
			} else if (srchInfo) {
				style = "";
			} else {
				style = "margin-top:-20px;";
			}
		} else if (text != "" && value == "") {
			style = "margin-top:8px;";
		}
		divObj.children().append("<li style='" + style + "'><a href='#null'>" + text + "</a></li>");
	});
	
	if (divObj.children().children().size() < 8) {
		divObj.children().css("margin-bottom", "0px");
	}
	
	resetComboBox(comboObj);
}

function resetComboBox(comboObj) {
	var comboName = comboObj.attr("name");
	$("select[name='"+ comboName + "']").next(".slct_box_list").find("ul").each(function(){
		selectComboBoxData($(this));
	});
}

function getSelectboxCount(obj) {
	var count = 0;
	obj.each(function() {
		if ($(this).val() != "") {
			count++;
		}
	});
	return count;
}

function getToDay(fmt) {
	 var today = new Date();
	 return (fmt) ? today.toDateFmt() : today.toDateFmt().removeFmt();
}

function isMobileWeb() {
	var check = false;
	(function(a,b){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))check = true})(navigator.userAgent||navigator.vendor||window.opera);
	return check;
}

function getOSInfo() {
	var ua = navigator.userAgent;

	if(ua.indexOf("NT 6.0") != -1) return "Windows Vista/Server 2008";
	else if(ua.indexOf("NT 6.1") != -1) return "Windows 7";
	else if(ua.indexOf("NT 5.2") != -1) return "Windows Server 2003";
	else if(ua.indexOf("NT 5.1") != -1) return "Windows XP";
	else if(ua.indexOf("NT 5.0") != -1) return "Windows 2000";
	else if(ua.indexOf("NT") != -1) return "Windows NT";
	else if(ua.indexOf("9x 4.90") != -1) return "Windows Me";
	else if(ua.indexOf("98") != -1) return "Windows 98";
	else if(ua.indexOf("95") != -1) return "Windows 95";
	else if(ua.indexOf("Win16") != -1) return "Windows 3.x";
	else if(ua.indexOf("Windows") != -1) return "Windows";
	else if(ua.indexOf("Linux") != -1) return "Linux";
	else if(ua.indexOf("Macintosh") != -1) return "Macintosh";
	else if(ua.indexOf("Mac") != -1) return "Mac";
	else return "";
}

//비밀번호 체크 함수
// 영문 대/소문자, 숫자, 특수문자 조합
function checkPassword(pwd) {
	var regExp = /^.*(?=^.{8,20}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[~,!,@,#,$,%,^,&,*,(,),=,+,_,.,|]).*$/;
	
	if (!regExp.test(pwd)) {
		alert("비밀번호는 8~20자의 영문 대/소문자, 숫자, 특수문자를 혼합해서 사용해야 합니다.");
		return false;
	}
	
	return true;
}

// 
function openPrivacyPolicy() {
	var page_url = "";
	var param = "";
	var appl_win;

	param += ""
	
	page_url = "/global/privacyPolicyPopup";
	
	appl_win = open(page_url + param, "_privacy_policy","height=530,width=880,resizable=yes,scrollbars=yes");
	//checkPopupBlocker(appl_win, true);
}

function isUploadLimitFileSize(file, maxFileMB) {
	
	var fileMB = 200;
	if(typeof maxFileMB != 'undefined'){
		fileMB = parseInt(maxFileMB);
	}

	var maxFileSize = fileMB * 1024 * 1024    //200MB
	var fileSize = 0;

	try {
		// 파일 확장자 체크
		if (!isUploadFileExt(file)) {
			return true;
		}
		if (navigator.appName=="Microsoft Internet Explorer") {
			var osf = new ActiveXObject("Scripting.FileSystemObject");
			fileSize = osf.getFile(file.value).size;
		} else {
			fileSize = file.files[0].size;
		}
		
		if(fileSize > maxFileSize) {
			alert("첨부파일 사이즈는 " + fileMB + "MB 이내로 등록해주세요. (첨부한 파일 : " + parseInt(fileSize/1024/1024) + "MB)");
			$(file).val("");
			return true;
		}
	} catch(e) {
		return false;
	}
	return false;
}

function isUploadFileExt(file) {
	var extBlackList = ['bat', 'exe', 'cmd', 'com', 'lnk', 'pif', 'scr', 'vb', 'vbe', 'vbs', 'wsh', 'js','jar', 
	                    'asp', 'aspx', 'htm', 'html', 'asa', 'phtml', 'php', 'php3', 'php4', 'php5', 'inc', 
	                    'jsp', 'jspx', 'jsw', 'jsv', 'jspf', 'pl', 'pm', 'cgi', 'lib', 'cfm', 'cfml', 'cfc', 'dbm'];
	var ext = file.value.split(".").pop().toLowerCase();
	
	if ($.inArray(ext, extBlackList) > -1) {
		alert("첨부할 수 없는 파일입니다.\n관리자가 제한한 파일 형식은 첨부할 수 없습니다.");
		$(file).val("");
		return false;
	} 
	
	return true;
}