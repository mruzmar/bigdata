function cargaPuntuaciones3() {
	db = db.getSiblingDB('curso');

	db.puntuaciones3.drop();

	for ( var i = 0 ; i < 500 ; i++ ) { 
		puntuacionesEstudiante = [];
		puntuacionesEstudiante.push( { tipo : "preguntas" , puntuacion : 100 * Math.random() } );
		puntuacionesEstudiante.push( { tipo : "ejercicios" , puntuacion : 100 * Math.random() } );
		puntuacionesEstudiante.push( { tipo : "tareas" , puntuacion : 100 * Math.random() } );
		puntuacionesEstudiante.push( { tipo : "examen" , puntuacion : 100 * Math.random() } );
		db.puntuaciones3.insert( { 
			idEstudiante : i + 1 , 
			puntuaciones : puntuacionesEstudiante 
		} )
	};
	
};

cargaPuntuaciones3();