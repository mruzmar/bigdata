function cargaPreferencias() {
	db = db.getSiblingDB('curso');

	db.gimnasioescritura.drop();

	var preferencias = [ "Aerobic" , "Aquagym" , "Baloncesto" , "Carrera en cinta", "Elíptica", "Musculación", "Natación", "Padel", "Spinning", "Tenis" ];
	var numeroPreferencias = preferencias.length;

	var cargaMasiva = db.gimnasioescritura.initializeOrderedBulkOp();
	for ( var i = 0 ; i < 500 ; i++ ) { 
		var preferenciasCliente = [];
		cargaMasiva.insert( { 
			idCliente : i + 1 , 
			fechaAlta : new Date() , 
			preferencias : preferenciasCliente 
		} );
		var numeroPrefenciasCliente = Math.floor( ( 5 * Math.random() ) + 1 );
		for ( var j = 0 ; j < numeroPrefenciasCliente ; j++ ) {
			var indicePreferencias = Math.floor( numeroPreferencias * Math.random() );
			cargaMasiva.find( 
				{ idCliente : i + 1 } 
			).update(
				{ $addToSet : { preferencias : preferencias[indicePreferencias] } } 
			)
		} 
	};
	cargaMasiva.execute();
};

cargaPreferencias();