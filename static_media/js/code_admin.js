(function($){

	$(document).ready(function(){

	var respuesta_si = $('#id_dueno').val();

	
	$('#duenosi_set-group').hide();
	$('#duenono_set-group').hide();
		

	$('#id_dueno').change(function(){
			var valor_tipo = $('#id_dueno').val();
			if (valor_tipo === '1' ) {
				$('#duenosi_set-group').show();
				$('#duenono_set-group').hide();
			}else{
				$('#duenosi_set-group').hide();
				$('#duenono_set-group').show();
			};
		});
	
	});
})(jQuery || django.jQuery)