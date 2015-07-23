$('document').ready(function(){

	/*CAMPOS NUMÉRICOS*/
	$('input[type="number"]').numeric();
	
	/*VALIDACION CARACTERES ESPECIALES*/
	function caracteresEspeciales(valInput, name){
 		var regex = /[\$\%\&\(\)\=\¿\?\*\^\{\}\_\-\"\'\<\>]/g;

 		if(regex.test(valInput)){
 			$('#formBuscar input[name="'+name+'"] ~ .msgError').text("* Campo erroneo");
			$('#formBuscar input[name="'+name+'"]').css('box-shadow','0px 0px 5px red');
			$('#formBuscar input[name="'+name+'"] ~ .msgError').animate({
				opacity: 1
			}, 
			1000);
 		}else{
 			$('#formBuscar input[name="'+name+'"]').css('box-shadow','0px 0px 0px red');
			$('#formBuscar input[name="'+name+'"] ~ .msgError').animate({
				opacity: 0
			}, 
			1000,
			function(){$('#formBuscar input[name="'+name+'"] ~ .msgError').text("");}
			);
 		}

	}

	/*EVENTO PARA COMPROBAR CAMPO*/
	$('#formBuscar input').blur(function(){
		var valInput = $(this).val();
		var name = $(this).attr("name");

		if(valInput != ''){
			caracteresEspeciales(valInput, name);
		}
		
	});

	$('.boton_formulario').click(function(){
		var error = $('.msgError').text();

		if(error == ''){
			$(this).submit();
		}else{
			return false;
		}
	});
});