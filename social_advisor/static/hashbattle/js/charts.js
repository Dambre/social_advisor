var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
};
var lineChartData = {
    labels: ["January", "February", "March", "April", "May", "June", "July", "January", "February", "March", "April", "May", "June", "July", ],
    datasets: [{
        label: "My First dataset",
        fillColor: "rgba(238,238,238,0.2)",
        strokeColor: "rgba(220,220,220,1)",
        pointColor: "#eee",
        pointStrokeColor: "rgba(200,200,200,1)",
        pointHighlightFill: "rgba(3,169,244,1)",
        pointHighlightStroke: "rgba(3,169,244,1)",
        data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), ]
    }]
};

var barChartData = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(220,220,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: [65, 59, 80, 81, 56, 55, 40]
        },
        {
            label: "My Second dataset",
            fillColor: "rgba(151,187,205,0.5)",
            strokeColor: "rgba(151,187,205,0.8)",
            highlightFill: "rgba(151,187,205,0.75)",
            highlightStroke: "rgba(151,187,205,1)",
            data: [28, 48, 40, 19, 86, 27, 90]
        }
    ]
};

window.onload = function() {


  $("#submit_to_review").click(function(){
    /*$('#field').each(function(){
      $(this).attr('readonly','readonly');
    });*/
    $("#chart-area").slideDown(function(){
      setTimeout(
        function() {
          var lineChartGraphic = document.getElementById('line-chart').getContext("2d");
          window.myLine = new Chart(lineChartGraphic).Line(lineChartData, {
          	showXLabels: 7,
            showScale: true,
            pointDot : true,
            responsive: true,
            maintainAspectRatio: false,
            tooltipFontSize: 14.5,
            percentageInnerCutout : 50,
            tooltipCaretSize: 0,
          });
        },
      500);
      setTimeout(
        function() {
        	var barChartGraphic = document.getElementById('bar-chart').getContext("2d");
        	window.myBar = new Chart(barChartGraphic).Bar(barChartData, {
				responsive: true ,
				maintainAspectRatio: false,
				scaleBeginAtZero : true,
				//String - Colour of the grid lines
				scaleGridLineColor : "rgba(0,0,0,.05)",
				//Number - Width of the grid lines
				scaleGridLineWidth : 1,
				//Boolean - Whether to show horizontal lines (except X axis)
				scaleShowHorizontalLines: true,
				//Boolean - Whether to show vertical lines (except Y axis)
				scaleShowVerticalLines: true,
				//Boolean - If there is a stroke on each bar
				barShowStroke : true,
				//Number - Pixel width of the bar stroke
				barStrokeWidth : 2,
				//Number - Spacing between each of the X value sets
				barValueSpacing : 5,
				//Number - Spacing between data sets within X values
				barDatasetSpacing : 1
        	});
        },
      500);
    }); 
  });

  

};