---
layout: docs
permalink: /docs/chap-13/
title: chap-13
---
<h1>
13. Procéder à la phase de test
</h1>
 
<p>
Préalablement au passage en production de la boutique, il est nécessaire de réaliser des tests pour s’assurer du bon fonctionnement entre le site marchand et la plateforme de paiement.
</p>
 
<p>
Ces tests doivent impérativement être réalisés avant de demander le passage en production. 
</p>
 <!-- tla1410335135439.xml -->
<h2>
13.1. Réaliser des tests de paiement
</h2>
 
<p>
Les demandes de paiement de test adressées via le formulaire HTTP POST doivent:
</p>
 
<p>
 
<ul>
 
 <li>
Contenir la donnée 
<b>vads_ctx_mode</b> valorisée à 
<b>TEST</b>. 
 </li>
 
 <li>
Utiliser 
<b>le certificat de test</b> précédemment récupéré pour le calcul de la signature. 
 </li>
 
</ul>
 
</p>
 
<p>
En phase de test, le marchand peut tester les configurations 3D Secure (si ce dernier est enrôlé 3DS et si l’option 3DS n’est pas désactivée).
</p>
 
<p>
Différents cas de paiements peuvent être simulés en utilisant les numéros de carte de test précisés sur la page de paiement.
</p>
 
<p>
Toutes les transactions réalisées en mode test sont consultables par les personnes habilitées à utiliser le Back Office à l’adresse suivante :
<table>
    
 <tr>
 
  <td>
<a href="https://secure.payzen.eu/vads-merchant/">https://secure.payzen.eu/vads-merchant/</a>
  </td>
 
 </tr>
   
</table>

</p>
 
<p>
Ces transactions sont consultables depuis le menu 
<b>Gestion &gt;Transaction de test</b> situé en haut à gauche du Back Office.
</p>
 <!-- tla1410339647667.xml -->
<h2>
13.2. Tester l&#x27;URL de notification instantanée (IPN)
</h2>
 
<p>
Vérifiez tout d&#x27;abord l&#x27;état de l&#x27;URL de notification instantanée (également appelée IPN) dans le Back Office.
</p>
 
<p>
Pour cela:
</p>
 
<p>
 
<ol>
 
 <li>
Effectuez un clic droit sur une transaction.
 </li>
 
 <li>
Sélectionnez 
<b>Afficher le détail de la transaction</b>.
 </li>
 
 <li>
Vérifiez le statut de l&#x27;URL de notification instantanée (IPN). 
 <ul>
 
  <li>
Dans le cas où le statut est 
<b>Envoyé</b>, cela signifie que vous avez correctement renseigné l&#x27;URL dans le Back Office. 
  </li>
 
  <li>
Dans le cas où le statut apparaît en 
<b>URL non définie</b>, cela signifie que vous n&#x27;avez pas renseigné l&#x27;URL dans le Back Office. 
  <ol>
 
   <li>
Vérifiez l&#x27;adresse de l&#x27;URL de notification instantanée saisie en mode TEST et PRODUCTION. 
   </li>
 
   <li>
Cliquez sur 
<b>Paramétrage</b> &gt; 
<b>Règles de notification</b>.
   </li>
 
   <li>
Renseignez l&#x27;URL de notification de paiement instantanée (URL de notification à la fin du paiement). 
   <p>
Ne saisissez pas une adresse en &quot;localhost&quot;. L&#x27;appel à cette l&#x27;URL se fait de serveur à serveur.
   </p>

   </li>
 
   <li>
Cliquez sur 
<b>Sauvegarder</b>.
   </li>
 
  </ol>

  </li>
 
 </ul>

 <ul>
 
  <li>
Dans le cas où le statut est 
<b>Echoué</b>, se reporter au chapitre 
<b>Traiter les erreurs</b>.
  </li>
 
 </ul>

 </li>
 
</ol>
 
</p>
 <!-- emm1405088970747.xml -->
