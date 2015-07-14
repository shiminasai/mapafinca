(function($){

	$(document).ready(function(){

	var respuesta_si = $('#id_dueno').val();
	var respuesta_16 = $('#id_calidadagua_set-0-calidad').val();

	
	$('#duenosi_set-group').hide();
	$('#duenono_set-group').hide();
	$('#contaminada_set-group').hide();
	$('#evidencia_set-group').hide();
	$('.field-caso_si').hide();
	$('.field-cuales_beneficios').hide();
	$('#fuentes_set-group').hide();
	$('.field-monto').hide();
	$('.field-pago').hide();
	$('.field-recibe').hide();
	//$('.field-uso').hide();
	$('#respuestano41_set-group').hide();
	$('.field-tipo_tratamiento').hide();

	$('#organizacioncomunitaria_set-group table tr th:gt(0)').hide();
	$('#prestamo_set-group table tr th:gt(0)').hide();
	$('#otrasseguridad_set-group table tr th:gt(1)').hide();

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