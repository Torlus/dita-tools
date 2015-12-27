---
layout: docs
permalink: /docs/chap-14/
title: chap-14
---
<h1>
14. Activer la boutique en mode production
</h1>
 
<p>
Ce chapitre vous détaille de quelle manière vous pouvez :
</p>
 
<ul>
 
<li>
Générer le certificat de production.
</li>
 
<li>
Basculer votre site marchand en production.
</li>
 
<li>
Réaliser un premier paiement en production.
</li>
 
<li>
Régénérer le certificat de production (en cas de problème).
</li>
 
</ul>
 <!-- emm1405089000731.xml -->
<h2>
14.1. Générer le certificat de production
</h2>
 
<p>
Vous pouvez générer le certificat de production depuis le menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; Onglet 
<b>Certificats</b> &gt; bouton 
<b>Générer le certificat de production</b>.
</p>
 
<p>
Une fois le certificat de production généré, sa valeur apparaît sous l&#x27;onglet 
<b>Certificats</b>.
</p>
 
<p>
Un e-mail est envoyé à l&#x27;interlocuteur en charge du dossier (responsable administratif de la société) pour lui confirmer la génération du certificat de production.
</p>
 <!-- emm1405089022352.xml -->
<h2>
14.2. Basculer le site marchand en production
</h2>
 
<p>
 
<ol>
 
 <li>
Valorisez le champ 
<b>vads_ctx_mode</b> à 
<b>PRODUCTION</b>.
 </li>
 
 <li>
Modifiez la valeur du certificat de test avec la valeur de votre certificat de production pour calculer la signature.
 <p>
Vous trouverez cette valeur depuis le menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; Onglet 
<b>Certificats</b>.
 </p>

 </li>
 
 <li>
Renseignez correctement l&#x27;URL de notification de paiement instantanée (URL server à la fin du paiement) en mode PRODUCTION depuis le menu 
<b>Paramétrage</b> &gt; 
<b>Règles de notification</b>.
 </li>
 
</ol>
 
</p>
 <!-- emm1405089047266.xml -->
<h2>
14.3. Réaliser un premier paiement de production
</h2>
 
<p>
Nous vous conseillons de vérifier les deux points suivants :
</p>
 
<p>
 
<ul>
 
 <li>
Le bon fonctionnement en environnement de production de bout-en-bout. 
 <p>
Pour ce faire, effectuez une transaction réelle.
 </p>

 <p>
Cette transaction pourra être annulée par la suite depuis le Back Office via le menu 
<b>Gestion</b> &gt; 
<b>Transaction</b> &gt; onglet 
<b>Paiements en cours</b>. Cette transaction ne sera donc pas remise en banque.
 </p>

 </li>
 
</ul>
 
</p>
 
<p>
 
<ul>
 
 <li>
Le bon fonctionnement de l&#x27;URL de notification de paiement instantanée (Url de notification à la fin du paiement) renseignée dans le Back Office. 
 <p>
Pour ce faire, ne cliquez pas sur le bouton 
<b>Retour à la boutique</b> après un paiement. 
 </p>

 <p>
Affichez le détail de la transaction dans le Back Office et vérifiez que le statut de l&#x27;URL de notification instantanée (Statut URL de notification) est bien 
<b>Envoyé.</b>
 </p>

 </li>
 
</ul>
 
</p>
 <!-- tla1408545933061.xml -->
<h2>
14.4. Regénérer le certificat de production
</h2>
 En cas de perte ou de corruption du certificat de production, le marchand a la possibilité de générer un nouveau certificat depuis son Back Office. Pour cela: 
<ol>
 
 <li>
 
 <p>
Dans le Back Office, sélectionnez 
<b>Paramétrage &gt; Boutique &gt; </b>onglet 
<b>Certificats.</b>
 </p>
 
 </li>
 
 <li>
 
 <p>
Cliquez sur 
<b>Générer à nouveau</b>.
 </p>
 
 </li>
 
</ol>
 <!-- tla1408546168107.xml -->
