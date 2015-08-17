(function($){

	$(document).ready(function(){

	$('#duenosi_set-group').hide();
	$('#duenono_set-group').hide();
	$('#panelsolar_set-group').hide();
	$('#contaminada_set-group').hide();
	$('#evidencia_set-group').hide();
	//$('.field-caso_si').hide();
	//$('.field-cuales_beneficios').hide();
	$('#fuentes_set-group').hide();
	//$('.field-monto').hide();
	//$('.field-pago').hide();
	//$('.field-recibe').hide();
	//$('.field-uso').hide();
	$('#respuestano41_set-group').hide();
	//$('.field-tipo_tratamiento').hide();

	//$('#organizacioncomunitaria_set-group table tr th:gt(0)').hide();
	//$('#prestamo_set-group table tr th:gt(0)').hide();
	//$('#otrasseguridad_set-group table tr th:gt(1)').hide();

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

	$('#id_tipoenergia_set-0-tipo_3').change(function(){
			var valor_tipo = $('#id_tipoenergia_set-0-tipo_3 ').val();
			if (valor_tipo === '4' ) {
				$('#panelsolar_set-group').show();
			}else{
				$('#panelsolar_set-group').hide();
			};
	});

	$('#id_calidadagua_set-0-calidad').change(function(){
			var valor_tipo = $('#id_calidadagua_set-0-calidad').val();
			if (valor_tipo === '3' ) {
				$('#contaminada_set-group').show();
				$('#evidencia_set-group').show();
			}else{
				$('#contaminada_set-group').hide();
				$('#evidencia_set-group').hide();
			};
	});

	$('#id_percibeingreso_set-0-si_no').change(function(){
			var valor_tipo = $('#id_percibeingreso_set-0-si_no').val();
			if (valor_tipo === '1' ) {
				$('#fuentes_set-group').show();
			}else{
				$('#fuentes_set-group').hide();
			};
		});

	$('#id_seguridadalimentaria_set-0-consumo_diario').change(function(){
			var valor_tipo = $('#id_seguridadalimentaria_set-0-consumo_diario').val();
			if (valor_tipo === '2' ) {
				$('#respuestano41_set-group').show();
			}else{
				$('#respuestano41_set-group').hide();
			};
		});

	});
})(jQuery || django.jQuery)
