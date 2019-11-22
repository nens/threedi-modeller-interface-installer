![](https://md-kwadraat.nl/css/logo_met_text_transparant.png) 

>Technisch verslag: **Build Installer 3Di Modeller Interface**   
>Datum: 17-07-2019  
>Door:  
>>	*Marco Duiker* - MD-kwadraat

-------------------------------------------------


Nog te doen door N&S
====================

   - Licensie voor 3Di Modeller Interface opnemen in `3Di-additions/create_qgis_nl_nsis.pl`
   - Icoontjes in `.ico` formaat van 3Di bevatten niet overal de juiste stack aan afmetingen, waardoor ze niet overal verschijnen waar het moet.   
     Vergelijk daarvoor alle `.ico` bestanden in de folder `3Di-additions/ms-windows` met de overeenkomstige `.ico` bestanden in `QGIS/ms-windows`.
   - De titel in de titelbalk van QGIS wordt gezet door het default project. Als dit er niet is, dan komt dus QGIS prominent naar voren ipv 3Di. Het verdient aanbeveling om een standaard QGIS project in het profiel op te nemen om dit te voorkomen.
   

Opmerkingen
===========

   - Het profiel zoals dat nu in de file tree zit is aangepast tov de aangeleverde. Met een diff zijn de wijzigingen wel te vinden.
   - De eerste keer opstarten duurt heeeeeel lang ivm installeren dependencies.



