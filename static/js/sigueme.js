$('document').ready(function(){

	if($('#follow_me').text() === "Dejar de seguir") {
		$("#follow_me").animate({
	  		backgroundColor: "red"
	  	},0);
	}
	
	$('#follow_me').click(function(e){

	var titulo = $('#activity_title').text();
	
	var url = "/detalle/"+titulo+"/";
	var datos = $('#formDetalle').serialize();
	var textoBoton = $(this).text();
	if (textoBoton == "¡Sígueme!") {
		var action = "follow";
	}
	else {
		var action = "unfollow";
	}

	datos+="&action="+action;
	$.ajax({
	  method: "POST",
	  url: url,
	  data: datos,
	  success: function(data){
	  	if(data.message == true){
	  		if(data.siguiendo == true){
	  			$("#follow_me").animate({
	  				backgroundColor: "red"
	  			},500);
	  			$("#follow_me").text("Dejar de seguir");
	  		}else{
	  			$("#follow_me").animate({
	  				backgroundColor: "#2E6EA5"
	  			},500);
	  			$("#follow_me").text("¡Sígueme!");
	  		}
	  	}
	  	else{
	  		alertify.set('notifier','position','top-right');
			alertify.error('Se ha producido un error');
	  	}
	  }
	});

		return false;

	});
	
});