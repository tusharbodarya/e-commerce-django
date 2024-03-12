
let monthsList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Aug', 'Oct', 'Nov', 'Dec'];

$("#reviewForm").submit(function(e){
    e.preventDefault();
    let myDate = new Date();
    let date = myDate.getDate();
    let month = monthsList[myDate.getMonth()];
    let year = myDate.getFullYear().toString().substr(2,2);

    let today = `${date} ${month}, ${year}`;
    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),
        dataType: "json",
        success: function (data) {
            if(data.status == true){
                $("#review_message").html("Review Added Successfully.");
                $(".hide-review-form").hide();
                $(".hide-add-review-title").hide();

                let _html = '<div class="single-comment justify-content-between d-flex mb-30"><div class="user justify-content-between d-flex">';
                    _html += '<div class="thumb text-center">';
                    _html += '<img src="http://127.0.0.1:8000/static/assets/imgs/blog/author-2.png" alt="" />';
                    _html += '<a href="#" class="font-heading text-brand">'+ data.context.user +'</a>';
                    _html += '</div>';
                    _html += '<div class="desc">';
                    _html += '<div class="d-flex justify-content-between mb-10">';
                    _html += '<div class="d-flex align-items-center">';
                    _html += '<span class="font-xs text-muted">'+today+' </span>';
                    _html += '</div>';

                    for(let i=1; i <= data.context.rating; i++){
                        _html += '<i class="fas fa-star text-warning"></i>';
                    }

                    _html += '</div>';
                    _html += '<p class="mb-10">'+ data.context.review +'</p>';
                    _html += '</div>';
                    _html += '</div>';
                    _html += '</div> ';

                    $(".comment-list").prepend(_html);
                

            }
        },
        error: function () {
            alert('An error occurred while submitting Review');
        }
    })
})


// filter products

$(document).ready(function(){
    $(".filter-checkbox, #price-filter-btn").on("click",function(){

        let filter_object = {};

        let min_price = $("#max_price").attr("min");
        let max_price = $("#max_price").val();

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val();
            let filter_key = $(this).data("filter");
            // console.log("Fliter Key", filter_key);
            // console.log("Fliter Value", filter_value);
            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter='+ filter_key +']:checked')).map(function(element){
                return element.value
            });
        });
        console.log("filter obj",filter_object);
        $.ajax({
            url: '/filter-product',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("Sending data..");
            },
            success:function(response){
                // console.log("res ",response)
                $("#filtered-products-list").html(response.data)
            }
        })
    });

    $("#max_price").on("blur",function(){
        let min_price = $(this).attr("min");
        let max_price = $(this).attr("max");
        let current_price = $(this).val();

        if(current_price < parseInt(min_price) || current_price > parseInt(max_price)){
            min_price = Math.round(min_price * 100) / 100;
            max_price = Math.round(max_price * 100) / 100;
            alert("Price must between $"+ min_price + " and $"+ max_price);
            $(this).val(min_price)
            $("#range").val(min_price)
            $(this).focus()
            return false
        }
        console.log("current_price", current_price);
        console.log("min_price", min_price);
        console.log("max_price", max_price);
    })
});


// Add to cart functinality

$(".add-to-cart-btn").on("click",function(){
    let this_val = $(this)
    let _index = this_val.attr('data-index')
    let id = $(".product-id-"+_index).val();
    let title = $(".product-title-"+_index).val();
    let price = $(".product-price-"+_index).val();
    let quantity = $(".product-quantity-"+_index).val();
    let pid = $(".product-pid-"+_index).val();
    let image = $(".product-image-"+_index).val();

    $.ajax({
        url:"/add-to-cart",
        data:{
            'id':id,
            'pid':pid,
            'title':title,
            'image':image,
            'qty':quantity,
            'price':price
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("adding products to cart");
        },
        success: function(response){
            this_val.html("✓");
            console.log("added product into cart");
            $(".cart-items-count").text(response.totalcartitems)
        }
    })
})