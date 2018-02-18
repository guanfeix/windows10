
$(function(){
    total()
    $("#check_all").click(function(event) {
		state = $(this).prop("checked")
		$(":checkbox:not(#check_all)").prop("checked",state)
	});

	$(":checkbox:not(#check_all)").click(function(event){
			if($(this).prop("checked")){
				if($(":checked").length+1==$(":checkbox").length){
					$("#check_all").prop("checked",true)}}

			else{ $("#check_all").prop({checked: false})}
    });

    $(".add").click(function() {
            var val = $(this).siblings('#txt1').val();
            var $txt1 = $(this).siblings('#txt1');
            $txt1.val(parseInt(val)+1).blur();


        });

    $(".minus").click(function(event) {

            var val = $(this).siblings('#txt1').val();
            var $txt1 = $(this).siblings('#txt1');

            $txt1.val(parseInt(val)-1).blur();


        });

    $(".num_show").blur(function(){
        count = $(this).val();
        stocks = $(this).parents(".cart_list_td").find(".stocks").val()
        if(count<=0){
            alert("请输入正确的数量");
            $(this).val(1)
            $(this).focus();
            return;
        }else if(count>100){
            alert("单个用户最多购买100份");
            $(this).val(100)
            $(this).focus();
            return;
        }else if(count>=parseInt(stocks)){
            alert("库存不足");
            $(this).val(stocks)
            $(this).focus();
            return;
        }

        cart_id = $(this).parents(".cart_list_td").attr("id");
        $.get("/edit"+cart_id+"_"+count+"/",function(data){
            if(data.ok==0){
            total();
            }else{
                $(this).val(data.ok)
            }



        })


    });

    function total(){
            var total_count = 0
            var total_money =0
            $(".cart_list_td .col07").each(function(){
                var $price = parseFloat($(this).siblings('.col05').children("span").html()*100)/100
                var $txt1 = $(this).siblings('.col06').children().children('#txt1')
                var val = $txt1.val()
                var single_pay = (parseFloat($price)*100*parseFloat(val)*100)/10000

                total_money = (parseFloat(total_money*100) + single_pay*100)/100
                total_count += parseInt(val)

                $(this).children('#sum').html(single_pay.toFixed(2))

            })

            var $pay = $(".settlements .col03 em")
            var $count1 = $(".settlements .col03 b")
            var $count2 = $(".total_count em")

            $pay.html(total_money.toFixed(2))
            $count1.html(total_count)
            $count2.html(total_count)


        };

    function cart_del(cart_id){
        del=confirm("确认删除吗？")
        if(del){
             $.get("/delete"+cart_id+"/",function(data){
                if(data.ok==1){
                    $("ul").remove("#"+cart_id)
                    total()
                }

             })

        }

    };
});

