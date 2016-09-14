$(window).load(function(){
	profilePushFromTop();
	$( window ).resize(profilePushFromTop);
	$("#profile-back-button").click(function(){
		$('.button-collapse').sideNav('hide');
	});
});

profilePushFromTop = function(){
	var pushFromTop = $(".profile-background-wrapper").outerHeight();
	$(".profile-image-wrapper").css("top", pushFromTop - 64);
};



/*

Todo 
if scrolltop > x

stickyheader.show()
stickyheader.addClass(flexcontainer)

else

stickyheader.hide()
stickyheader.removeClass(flexcontainer)

$("#slide-out").on("scroll", function(){
    var position = $("#slide-out").scrollTop();
    console.log(position);
    if (position > 48){
        $("#profile-sticky-header").slideDown();
    }
    else {
        $("#profile-sticky-header").slideUp(); 
    }

});
*/