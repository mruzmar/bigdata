function cargaPuntuaciones() {
	db = db.getSiblingDB('curso');

	db.puntuaciones.drop();

	var tiposEjercicios = [ "pregunta" , "ejercicio" , "tarea" , "examen" ];

	if ( version26Post() ) {
		var cargaMasiva = db.puntuaciones.initializeUnorderedBulkOp();
		for ( var i = 0 ; i < 500 ; i++ ) { 
			for (var j = 0 ; j < 4 ; j++ ) { 
				cargaMasiva.insert( { 
					idEstudiante : i + 1 , 
					tipo : tiposEjercicios[j] , 
					puntuacion : 100 * Math.random() 
				} ) 
			}
		};
		cargaMasiva.execute();
	}
	else {
		for ( var i = 0 ; i < 500 ; i++ ) { 
			for (var j = 0 ; j < 4 ; j++ ) { 
				db.puntuaciones.insert( { 
					idEstudiante : i + 1 , 
					tipo : tiposEjercicios[j] , 
					puntuacion : 100 * Math.random() 
				} ) 
			}
		};
	}
};

function version26Post() {
	var partesVersion = version().split( "." );
	return partesVersion[0] + partesVersion[1] >= 26;
};

cargaPuntuaciones();