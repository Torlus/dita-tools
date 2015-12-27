---
layout: docs
permalink: /docs/chap-12/
title: chap-12
---
<h1>
12. Traiter le retour à la boutique
</h1>
 
<p>
Par défaut, lorsque l&#x27;acheteur revient sur le site marchand, aucun paramètre n&#x27;est transmis par son navigateur.
</p>
 
<p>
Néanmoins si le champ 
<b>vads_return_mode</b> a été transmis dans le formulaire de paiement (voir chapitre 
<b>Gérer le retour vers le site marchand</b> 
</p>
 
<ul>
 <li>
soit en GET : données présentes dans l’url sous la forme : ?param1=valeur1&amp;param2=valeur2.
</li>
 <li>
soit en POST : données envoyées dans un formulaire POST.
</li>
 
</ul>
 
<p>

</p>
 
<p>
Les données transmises au navigateur sont les mêmes que lors des notifications (IPN).
</p>
 
<p>
Seuls les champs 
<b>vads_url_check_src</b> et 
<b>vads_hash</b> ne seront envoyés que dans la notification instantanée.
</p>
 
<p>

</p>
 
<p>
Vous pouvez vous référer au chapitre 
<b>Analyser le résultat du paiement</b> pour analyser ces données.
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<b>Remarque</b> : le retour à la boutique doit vous permettre uniquement d&#x27;afficher un contexte visuel à l&#x27;acheteur. N&#x27;utilisez pas les données reçues pour effectuer le traitement en base de données. 
</p>
 <!-- emm1405088934849.xml -->
