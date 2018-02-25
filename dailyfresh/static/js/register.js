$(function(){

    var error_name = false
	var error_pwd = false
	var error_cpwd = false
	var error_email = false
	var error_allow = false

    $("#register").click(function(){
		check_username()
		check_pwd()
		check_cpwd()
		check_email()

		console.log(error_pwd)
		document.title = error_name+error_pwd+error_cpwd+error_email+error_allow
		if(error_name== false && error_pwd== false && error_cpwd== false && error_email== false && error_allow==false){
            $("#reg_form").submit()
		}
		else{
			return false
		}
	});


	$("#user_name").blur(function(){
		check_username()
	})
	$("#user_name").focus(function(){
		$(this).next().hide()
	})
	$("#pwd").blur(function(){
		check_pwd()
	})
	$("#pwd").focus(function(){
		$(this).next().hide()
	})
	$("#cpwd").blur(function(){
		check_cpwd()
	})
	$("#cpwd").focus(function(){
		$(this).next().hide()
	})
	$("#email").blur(function(){
		check_email()
	})
	$("#email").focus(function(){
		$(this).next().hide()
	})



	$("#allow").click(function(event){
		if($(this).prop("checked")==true){
			error_allow = false
			$(".error_tip2").hide()
		}
		else{
			error_allow = true
			$(".error_tip2").html("请仔细阅读协议")
			$(".error_tip2").show()
		}
	});





	function check_email(){

		var val = $("#email").val()

		var re = /^\w+@\w+(\.com)$/

		if(val==""){
			$("#email").next().html("请输入邮箱");
			$("#email").next().show();
			error_email = true
			return
		}
		if(re.test(val)){
			error_email = false
		}
		else{
			$("#email").next().html("请使用正确的邮箱格式");
			$("#email").next().show();
			error_email = true
			return
		}

	}

//



	function check_cpwd(){
		var val1 = $("#pwd").val()
		var val2 = $("#cpwd").val()
		// alert(val2+"|"val1)
		if(val1!=val2){
			error_cpwd = true
			$("#cpwd").next().html("两次输入的密码应相等");
			$("#cpwd").next().show();
		}
		else{
		    error_cpwd = false
			$("#cpwd").next().hide();
		}
	}

	function check_pwd(){

		var val = $("#pwd").val()
		// 1.出现这样神奇的bug怎么不让人崩溃，如此不严谨的语言，万能的是过一会自己好了玄学

		var re = /^[\w@%&\!\#\$\*\^\.\?]{8,16}$/

		if(val==""){
			$("#pwd").next().html("请输入密码");
			$("#pwd").next().show();
			error_pwd = true
			return
		}
		// 2.不熟悉就多用几下无所谓的，只要你想到的时候知道去哪找就行了不做复读机，是internal
		if(re.test(val)){
			error_pwd = false
		}
		else{
			$("#pwd").next().html("密码应为8-16位字符");
			$("#pwd").next().show();
			error_pwd = true
			return

		}

	}

	//
	function check_username(){

		var val = $("#user_name").val()
		// 1.出现这样神奇的bug怎么不让人崩溃，如此不严谨的语言，万能的是过一会自己好了玄学

		var re = /^\w{5,15}$/

		if(val==""){
			$("#user_name").next().html("请输入用户名");
			$("#user_name").next().show();
			error_name = true
			return
		}
		// 2.不熟悉就多用几下无所谓的，只要你想到的时候知道去哪找就行了不做复读机，是internal
		if(re.test(val)){
			error_name = false
		}
		else{
			$("#user_name").next().html("用户名是使用alpha的5到15位字符");
			$("#user_name").next().show();
			error_name = true
			return

		}

	}





})