$(window).load(function(){
    
    // Initialia


    $('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: true, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: true, // Displays dropdown below the button
      alignment: 'left' // Displays dropdown with edge aligned to the left of button
    });


	// Getting user input from review text area via ajax


	$("#review-post").submit(function(){
    	$(".preloader").show();
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: { 
            	csrfmiddlewaretoken: '{{ csrf_token }}',
            	user_input: $('textarea#user_input_to_analyze').val()
        	},
        	success: function(response){
                	$(".preloader").hide();
                	console.log("ajax success, user input: " +response);   
                },
            error: function(response){
	            $(".preloader").hide();	
	            console.log("ajax failed, user input: " +response);
            }   
        });
        return false;
   });

  // Preventing submiting user input to analyze while there is no user input in form

  $('#submit_to_review').attr('disabled',true);
    $('#user_input_to_analyze').keyup(function(){
        if($(this).val().length !=0)
            $('#submit_to_review').attr('disabled', false);            
        else
            $('#submit_to_review').attr('disabled',true);
    });
});
