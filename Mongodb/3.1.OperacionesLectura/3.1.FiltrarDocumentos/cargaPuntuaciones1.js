function cargaPuntuaciones() {
	db = db.getSiblingDB('curso');//Trabajo sobre la base de datos curso

	db.puntuaciones.drop();//Elimino coleccion para empezar de cero

	var tiposEjercicios = [ "pregunta" , "ejercicio" , "tarea" , "examen" ];//Array

	for ( var i = 0 ; i < 500 ; i++ ) { 
		for (var j = 0 ; j < 4 ; j++ ) { 
			db.puntuaciones.insert( { 
				idEstudiante : i + 1 , 
				tipo : tiposEjercicios[j] , 
				puntuacion : 100 * Math.random() 
			} ) 
		}
	};
};

cargaPuntuaciones();