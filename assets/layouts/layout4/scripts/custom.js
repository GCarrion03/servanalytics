
/* Init */

$('#resultados_candidato_desagregado').hide();

/*Change menu color when selected*/

$(".srv-modelos li a").on("click", function() {
  $(".srv-modelos li").removeClass("active");
  $(".srv-modelos li a").removeClass("active");
  $(this).addClass("active");
  $(this).parent().addClass("active");
});

/*Ajax snippet to call content on the page*/

$('#modelo1').on('click', function(){
	
    // start page loading indicator
    App.startPageLoading();            
    $.ajax({
        type: "GET",
        cache: false,
        url: "index.html",
        dataType: "html",
        success: function (html) {
        	App.stopPageLoading();
//            $('#grafica1').html(html);
        	$('#grafica1').html('<iframe width="100%" height="1000" frameborder="0" scrolling="yes" id="modelo1" src="http://169.45.220.147/dashboard/"></iframe>'); 
            Layout.fixContentHeight(); // fix content height
            App.initAjax(); // initialize core stuff
        },
        error: function (xhr, ajaxOptions, thrownError) {
        	App.stopPageLoading();
            $('#grafica1').html('<h4>Could not load the requested content.</h4>');                   
        }
    });
});

$('#avance_candidato_1').on('click', function(){
	
    // start page loading indicator
    App.startPageLoading();            
    $.ajax({
        type: "GET",
        cache: false,
        url: "index.html",
        dataType: "html",
        success: function (html) {
        	App.stopPageLoading();
        	
			$('#resultados_candidatos_principales').hide();
			$('#resultados_candidatos_desagregados').hide();
			$('#resultados_candidato_desagregado').show();

        	$('#resultados_candidato_desagregado_contenido').html('<iframe width="100%" height="1000" frameborder="0" scrolling="yes" id="modelo1" src="http://169.45.220.147/DOdashboard/"></iframe>'); 
            Layout.fixContentHeight(); // fix content height
            App.initAjax(); // initialize core stuff
        },
        error: function (xhr, ajaxOptions, thrownError) {
        	App.stopPageLoading();
            $('#grafica1').html('<h4>Could not load the requested content.</h4>');                   
        }
    });
});

/*Acceptance Percentage*/

