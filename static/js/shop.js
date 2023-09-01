$(document).ready(function () {
    $("#addtocart").on('click', function(){
        var vn = $(this);
        var qnt = $("#qunt").val();
        var pid = $("#pid").val();
        $.ajax({
            url : 'addcart',
            data : {'id':pid, 'qnt':qnt},
            dataType : 'json',
            beforeSend:function(){
                vn.attr('disabled', true)
            },
            success:function(res){
                $('.quntity').fadeIn();
				$('.quntity').html(res.totalitems);
                console.log(res.data);
                $("#addtocart")[0].reset();
            },
            error: function(res){
                alert('failed');
            }
        });
    });
});

$(document).ready(function () {
    $("#addtocart2").on('click', function(){
        var vn = $(this);
        var qnt = $("#qunt").val();
        var pid = $("#pid").val();
        alert("Your Product Added In Card");
        $.ajax({
            url : '../../addcart',
            data : {'id':pid, 'qnt':qnt},
            dataType : 'json',
            beforeSend:function(){
                vn.attr('disabled', true)
            },
            success:function(res){
                $('.quntity').fadeIn();
				$('.quntity').html(res.totalitems);
                console.log(res.data);
                $("#addtocart")[0].reset();
            }
        });
    });
});