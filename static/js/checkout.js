
$(document).ready(function () {

    $('.paywithRazorpay').click(function (e) {
        e.preventDefault();
        var fname = $("[name='fname']").val();
        var lname = $("[name='lname']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var pincode = $("[name='pincode']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();
        // var totalPrice = parseFloat($('#totalPrice').text().trim().replace(/\D/g, ''));


        if (fname == "" || lname == "" || email == "" || phone == "" || address == "" || city == "" || state == "" || pincode == "" || country == "") {
            swal("Alert!", "All fields are mandatory", "error");
            return false;
        } else {
            // console.log("Total Price:", totalPrice);
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                success: function (response) {
                    // console.log(response)

                    var options = {
                        // "key": "{{ settings.RAZORPAY_KEY }}",
                        "key": "rzp_test_6rOUhn8C1ov0dx", // Enter the Key ID 
                        "amount": response.total_price * 100, // Default currency is INR. 
                        // "amount": 1 * 100, // Default currency is INR. 
                        "currency": "INR",
                        "name": "Pinto Furniture", // Your business name
                        "description": "Thank you for buying from us",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", 
                        "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
                        "handler": function (responseb) {
                            alert(responseb.razorpay_payment_id);
                            // window.location.href = '/orders';
                            data = {
                                "fname": fname,
                                "lname": lname,
                                "email": email,
                                "phone": phone,
                                "address": address,
                                "city": city,
                                "state": state,
                                "country": country,
                                "pincode": pincode,
                                "payment_mode": "Paid by Razorpay",
                                "payment_id": responseb.razorpay_payment_id,
                                csrfmiddlewaretoken: token
                            }
                            $.ajax({
                                method: "POST",
                                url: "/place-order",
                                data: data,
                                success: function (responsec) {
                                    swal("Congratulation!", responsec.status, "succes").then((value) => {
                                        window.location.href = '/about';
                                    });

                                }
                            });

                        },
                        "prefill": {
                            "name": fname + " " + lname,
                            "email": email,
                            "contact": phone
                        },

                        "theme": {
                            "color": "#3399cc"

                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();

                }
            });
        }
    });

});


