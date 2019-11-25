![](https://md-kwadraat.nl/css/logo_met_text_transparant.png) 

>Technisch verslag: **Build Installer 3Di Modeller Interface**   
>Datum: 04-07-2019  
>Door:  
>>	*Marco Duiker* - MD-kwadraat

-------------------------------------------------


Toelichting
===========

Dit document beschrijft hoe een Windows installer gebouwd kan worden voor de 3Di Modeller Interface.

Uitgangspunten
==============

NSIS
-----

nsis 3 kan worden gedraaid met het commando:
 	
 	makensis3 makensis

Dit kan worden bereikt door een docker container te maken en een shell script in het pad. Bijvoorbeeld:

	#!/bin/bash
	CWD="$(pwd)"
	docker run -u "$UID" -w "$CWD" --net host -v /var/www:/var/www -v /home/marco:/home/marco -e PYTHONUNBUFFERED=0 makensis "$@"

Docker file is beschikbaar op: https://github.com/MarcoDuiker/dockered_nsis
	
QGIS
----

Er is een file tree beschikbaar als volgt:


`arbitraire root naam`

   - `QGIS` (`git clone https://github.com/qgis/QGIS.git`)
   - `3Di-additions`
   - `building_3Di_modeller_interface.mkd` (deze handleiding)
      
    
Bouwen
======

De juiste versie (laatste LTR) van QGIS uitchecken:

	cd QGIS
	git checkout final-3_4_x

En dan builden:

	cd 3Di-additions
	./create_qgis_nl_nsis.pl

De executable verschijnt in QGIS/ms-windows

**Let op**:

>Indien er nieuwe packages worden opgenomen bij een nieuwe QGIS LTR versie, of een nieuwe grass versie wordt opgenomen, dienen de pre-install en postinstall scripts in de volgende folders aangepast worden:

   - `3Di-additions/ms-windows/osgeo4w/unpacked-x86_64/etc/postinstall`
   - `3Di-additions/ms-windows/osgeo4w/unpacked-x86_64/etc/preremove`


Aanwijzingen
============

Het build script `create_qgis_nl_nsis.pl` download zelf steeds de nieuwste packages van de libraries van osgeo4w waar nodig. 

> De `QGIS` folder hoeft niet bij elke keer bouwen opnieuw gekloond te worden. Dit hoeft alleen als

   - Er een nieuwe QGIS LTR is verschenen
   - Er in 3Di-additions bestanden zijn verwijdert, die ook uit de uiteindelijke executable niet meer voor mogen komen

> Eventueel kan het verwijderen van alles wat in `3Di-additions` zit en niet in `QGIS` ook handmatig verwijdert worden.



Bij testen is het handig om de compressie uit te zetten die de executable in elkaar drukt. Bouwen gaat dan aanmerkelijk sneller.
Dit kan in regel 25 en 26 van `3Di-additions/ms-windows/3Di-installer.nsi` door de een uit en de ander aan te commentariëren mbv `;`.




