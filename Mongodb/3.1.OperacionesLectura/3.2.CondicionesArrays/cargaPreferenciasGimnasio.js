function cargaPreferencias() {
	db = db.getSiblingDB('curso');

	db.gimnasio.drop();

	var preferencias = [ "Aerobic" , "Aquagym" , "Baloncesto" , "Carrera en cinta", "Elíptica", "Musculación", "Natación", "Padel", "Spinning", "Tenis" ];
	var numeroPreferencias = preferencias.length;
	
	
	for ( var i = 0 ; i < 500 ; i++ ) { 
		var preferenciasCliente = [];
		var numeroPrefenciasCliente = Math.floor( ( 5 * Math.random() ) + 1 );
		for ( var j = 0 ; j < numeroPrefenciasCliente ; j++ ) {
			var indicePreferencias = Math.floor( numeroPreferencias * Math.random() );
			preferenciasCliente.push( preferencias[indicePreferencias] );
		}
		db.gimnasio.insert( { 
			idCliente : i + 1 , 
			fechaAlta : new Date() , 
			preferencias : preferenciasCliente 
		} ) 
	};
	
};

cargaPreferencias();