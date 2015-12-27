---
layout: docs
permalink: /docs/chap-8/
title: chap-8
---
<h1>
8. Utiliser des fonctions complémentaires
</h1>
 <!-- tla1406104794231.xml -->
<h2>
8.1. Définir le mode de remise en banque (automatique / manuel)
</h2>
  
<p>
Le marchand peut paramétrer dans le Back Office la manière dont sont envoyés les paiements à la banque (Menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; onglet 
<b>Configuration</b>) :
</p>
 
<p>
Définir le mode de remise en banque
</p>
<img src="/docs_img/tla1412755027294.image" alt="DefinirModeRemiseBanque"/> 
<p>
 
<ul>
 
 <li>

<b>Automatique</b> : aucune action nécessaire, les paiements sont remis en banque une fois le délai de remise atteint.
 </li>
 
 <li>

<b>Manuel</b> : le marchand doit impérativement valider chaque paiement depuis son Back Office pour qu’il soit remis en banque, et ceci, avant la date de remise souhaitée.
 <p>

 </p>

 <p>

<b>Toute transaction qui n’a pas été validée dans les délais impartis est considérée comme expirée et ne sera jamais remise en banque.</b>
 </p>
Par défaut, le Back Office est configuré pour remettre automatiquement en banque tous les paiements.
 <p>

 </p>
Le marchand peut surcharger cette configuration dans son formulaire de paiement. 
 <p>
Il devra implémenter les critères de son choix (état du stock, délai de réapprovisionnement, etc...) permettant de décider si la transaction doit être remise en banque automatiquement ou non.
 </p>

 </li>
 
</ul>
 
</p>
  
<ol>
 
 <li>
 
 <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez le champ 
<b>vads_validation_mode</b> pour configurer le mode de remise en banque de la transaction (manuel ou automatique).
 </p>
 
 <p>
Ce champ sera renvoyé dans la réponse avec la valeur transmise dans le formulaire.
 </p>
 
 <p>
 
 <table>
      
  <tr>
 
   <td>
Valeur
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b>Absent ou vide</b>
   </td>
 
   <td>
Prend la valeur définie dans le Back Office.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>0</b>
   </td>
 
   <td>
Remise en banque automatique.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>1</b>
   </td>
 
   <td>
Remise en banque manuelle.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre <a href="#TODO-emm1405088305497.xml">
<b>Calculer la signature</b></a>).
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>

<u>Exemple de formulaire de paiement avec définition du mode de remise en banque en mode SILENT:</u><code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;SILENT&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;4000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_card_number&quot; value=&quot;4970100000000000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
<p>

<u>Exemple de formulaire de paiement avec définition du mode de remise en banque en mode INTERACTIVE:</u><code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;4000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
<p>

</p>
 
<p>

<i>
<b>
<u>Remarque :</u></b></i>
</p>
 
<p>

<i>Les champs requis diffèrent selon le mode d’acquisition des informations du moyen de paiement (
<b>SILENT</b> ou 
<b>INTERACTIVE</b>).</i>
</p>
 
<p>

<i>Lorsque le champ 
<b>vads_action_mode</b> est valorisé à 
<b>SILENT</b>, les informations du moyen de paiement deviennent obligatoires.</i>
</p>
 
</p>
 <!-- tla1406107315964.xml -->
<h2>
8.2. Transmettre les données de l&#x27;acheteur
</h2>
  
<p>
Le marchand peut transmettre des informations concernant l’acheteur (adresse e-mail, civilité, numéro de téléphone etc…). Ces données constitueront les informations de facturation. 
</p>
 
<p>

</p>
 
<p>
Toutes les données qui seront transmises via le formulaire de paiement seront affichées dans le Back Office en consultant le détail de la transaction (onglet 
<b>Acheteur</b>).
</p>
  
<ol>
 
 <li>
 
 <p>

 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez les champs facultatifs ci-dessous en fonction de vos besoins.
 </p>
 
 <p>
Ces champs seront renvoyés dans la réponse avec la valeur transmise dans le formulaire.
 </p>
 
 <p>
 
 <table>
   
  <tr>
 
   <td>

   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 <p>

 </p>
 
 </li>
 
 <li>
 
 <p>

 </p>
 
 </li>
 
</ol>
 <!-- tla1406107961818.xml -->
<h2>
8.3. Transmettre les données de livraison
</h2>
  
<p>
Le marchand peut transmettre les données de livraison de l&#x27;acheteur (adresse, civilité, numéro de téléphone etc…). 
</p>
  
<ol>
 
 <li>
 
 <p>

 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez les champs facultatifs ci-dessous en fonction de vos besoins.
 </p>
 
 <p>
Ces champs seront renvoyés dans la réponse avec la valeur transmise dans le formulaire.
 </p>
 
 <p>
 
 <table>
      
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b>vads_ship_to_status</b>
   </td>
 
   <td>
Statut (
<b>PRIVATE</b>: pour particulier / 
<b>COMPANY</b> pour une entreprise).
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_ship_to_name
   </td>
 
   <td>

<b>Déprécié</b>. Nom de l’acheteur. Utilisez 
<b>vads_ship_to_first_name</b> et 
<b>vads_ship_to_last_name</b>.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_first_name</b>
   </td>
 
   <td>
Prénom.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_last_name</b>
   </td>
 
   <td>
Nom.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_legal_name</b>
   </td>
 
   <td>
Raison sociale.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_phone_num</b>
   </td>
 
   <td>
Numéro de téléphone.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_street_number</b>
   </td>
 
   <td>
Numéro de rue.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_street</b>
   </td>
 
   <td>
Adresse postale.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_street2</b>
   </td>
 
   <td>
Deuxième ligne d’adresse.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_district</b>
   </td>
 
   <td>
Quartier.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_zip</b>
   </td>
 
   <td>
Code postal.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_city</b>
   </td>
 
   <td>
Ville.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_state</b>
   </td>
 
   <td>
Etat / Région.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_ship_to_country</b>
   </td>
 
   <td>
Code pays suivant la norme ISO 3166
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
 
 <li>
 
 <p>

 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>

</p>
 
<p>

<u>Exemple de formulaire de paiement avec informations sur la livraison</u><code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;4000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406108665877.xml -->
<h2>
8.4. Transmettre les données de la commande
</h2>
  
<p>
Le marchand peut indiquer dans son formulaire de paiement s’il souhaite transmettre les informations de la commande (numéro de la commande, description, contenu du panier etc…). 
</p>
 
<p>
Ces données seront affichées dans le Back Office en consultant le détail de la transaction (onglet 
<b>Panier</b>).
</p>
  
<ol>
 
 <li>
 
 <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b>Générer un formulaire de paiement</b> pour construire votre formulaire de paiement.
 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez les champs facultatifs ci-dessous en fonction de vos besoins. Ces champs seront renvoyés dans la réponse avec la valeur transmise dans le formulaire.
 </p>
 
 <p>
 
 <table>
      
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b>vads_order_id</b>
   </td>
 
   <td>
Numéro de commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_order_info</b>
   </td>
 
   <td>
Description de la commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_order_info2</b>
   </td>
 
   <td>
Description de la commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_order_info3</b>
   </td>
 
   <td>
Description de la commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_nb_products</b>
   </td>
 
   <td>
Nombre d’articles. 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_product_labelN</b>
   </td>
 
   <td>
Libellé de l’article. N correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_product_amountN</b>
   </td>
 
   <td>
Montant de l’article. N correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_product_typeN</b>
   </td>
 
   <td>
Type de l’article. N correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...). 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_product_refN</b>
   </td>
 
   <td>
Référence de l’article. N correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_product_qtyN</b>
   </td>
 
   <td>
Quantité d’article. N correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_product_vatN</b>
   </td>
 
   <td>
TVA de l&#x27;article. N correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_nb_products</b> avec le nombre d&#x27;articles contenu dans le panier.
 </p>
 
 <p>

<u>
<i>Remarque :</i></u>
 </p>
 
 <p>

<i>Ce champ est obligatoire pour que le panier soit pris en compte.</i>
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_product_amountN</b> avec le montant des différents articles contenus dans le panier dans l&#x27;unité la plus petite de la devise.
 </p>
 
 <p>
0 correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_product_typeN</b> avec la valeur correspondant au type de l&#x27;article.
 </p>
 
 <p>
0 correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
 </p>
 
 <p>
 
 <table>
   
  <tr>
 
   <td>

   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_product_labelN</b> avec le libellé de chacun des articles contenus dans le panier.
 </p>
 
 <p>
0 correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_product_qtyN</b> avec la quantité de chacun des articles contenus dans le panier.
 </p>
 
 <p>
0 correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_product_refN</b> avec la référence de chacun des articles contenus dans le panier.
 </p>
 
 <p>
0 correspond à l&#x27;indice de l&#x27;article (0 pour le premier, 1 pour le second...).
 </p>
 
 </li>
 
</ol>
 <!-- tla1406109053093.xml -->
<h2>
8.5. Activer / Désactiver 3D Secure
</h2>
  
<p>
Cette fonctionnalité nécessite la souscription de l’option 
<b>3D Secure sélectif</b>.
</p>
 
<p>
Le marchand peut indiquer dans son formulaire de paiement s’il souhaite activer ou désactiver le processus 3D Secure.
</p>
 
<p>
Le marchand devra implémenter les critères de son choix (montant, pays, département de livraison etc..) permettant de décider si la transaction doit être soumise au 3DS ou non.
</p>
  
<ol>
 
 <li>
 
 <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez le champ 
<b>vads_threeds_mpi</b> pour activer ou désactiver 3D Secure.
 </p>
 
 <p>
 
 <table>
   
  <tr>
 
   <td>

   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre <a href="#TODO-emm1405088305497.xml">
<b>Calculer la signature</b></a>).
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>

<u>Exemple d&#x27;activation du 3DS en fonction du montant</u>:<code><pre>
if (vads_amount &lt; 300 euro
</pre></code>

</p>
 
<p>

<u>Exemple d&#x27;activation du 3DS en fonction du département</u>:<code><pre>
if (vads_cust_zip = 92 ) or (vads_cust_zip = 93 ){ 
	then vads_threeds_mpi = 0 // 3DS enabled 
	else vads_threeds_mpi = 2 // 3DS disabled
}
</pre></code>

</p>
 
<p>

<u>Exemple de formulaire de paiement avec le 3DS désactivé</u>:<code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;4000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406109756086.xml -->
<h2>
8.6. Définir le contrat commerçant
</h2>
 Le marchand peut spécifier dans son formulaire de paiement la valeur du contrat commerçant à utiliser.
<p>
Cette fonctionnalité n&#x27;est utile que si vous possédez plusieurs contrats sur un même réseau d’acceptation. 
</p>

<p>

</p>
 
<ol>
 
 <li>
 
 <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez le champ facultatif 
<b>vads_contracts</b> pour définir le contrat commençant utilisé.
 </p>
 
 <p>
Exemple :
 </p>
 
 <p>
 
 <table>
     
  <tr>
 
   <td>
Valeur
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>
Absent ou vide
   </td>
 
   <td>
Utilisation du contrat tel que défini par l&#x27;ordre de priorité dans le Back Office (Menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; onglet 
<b>Contrats</b>).
   </td>
 
  </tr>
 
  <tr>
 
   <td>
CB=12312312 
   </td>
 
   <td>
Réseau CB 
   </td>
 
  </tr>
   
 </table>
 
 <p>
Pour définir une liste de contrats, séparez les valeurs par un point-virgule « ; ».
 </p>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre <a href="#TODO-emm1405088305497.xml">
<b>Calculer la signature</b></a>).
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>

<u>Exemple</u>:
</p>
 
<p>
Vous disposez de:
</p>
 
<p>
 
<ul>
 
 <li>
deux contrats CB
 </li>
 
 <li>
deux contrats AMEX : 949400444000 et 949400444001
 </li>
 
</ul>
 
</p>
 
<p>
Pour spécifier le contrat à utiliser pour ces deux réseaux, 
<b>vads_contracts</b> devra être valorisé de la manière suivante : vads_contracts=CB
</p>
 
<p>

<u>Exemple de formulaire de paiement définissant le contrat commerçant utilisé</u>:<code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;4000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;

<b>&lt;input type=&quot;hidden&quot; name=&quot;vads_contracts&quot; value=&quot;CB=1231231;AMEX=949400444000&quot;</b>
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406110492095.xml -->
<h2>
8.7. Gérer le retour vers le site marchand
</h2>
 
<p>
A la fin du paiement, l’acheteur a la possibilité de revenir sur le site marchand sur une page appelée 
<b>URL de retour</b>. 
</p>
 
<p>
A ne pas confondre avec l’
<b>URL de notification instantanée (également appelée IPN)</b> (voir chapitre 
<b><a href="#TODO-emm1405084980499.xml">Gérer le dialogue vers le site marchand</a></b>). 
</p>
 <!-- tla1406110787965.xml -->
 <h3>
8.7.1.  Définir les URL de retour
</h3>
  
 <p>
Dans le formulaire de paiement, le marchand peut surcharger la configuration du Back Office. Pour cela il peut:
 </p>
 
 <p>
 
 <ul>
 
  <li>
Utiliser 4 URL différentes en fonction du résultat du paiement:
  <ul>
 
   <li>
Paiement accepté.
   </li>
 
   <li>
Paiement refusé.
   </li>
 
   <li>
Paiement abandonné.
   </li>
 
   <li>
Paiement en erreur.
   </li>
 
  </ul>

  </li>
 
  <li>
Utiliser une seule URL quel que soit le résultat du paiement.
  </li>
 
 </ul>
 
 </p>
 <!-- tla1406112125569.xml -->
  <h4>
8.7.1.1.   Définir les URL de retour en fonction du résultat du paiement
</h4>
  
  <p>

  </p>
  
  <ol>
 
   <li>
 
   <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
   </p>
 
   </li>
 
   <li>
 
   <p>
Utilisez les champs facultatifs présentés dans le tableau ci-dessous pour concevoir le formulaire de paiement adapté à vos besoins.
   </p>
 
   <p>
Si aucune URL n’est valorisée dans le formulaire, la valeur configurée dans le Back Office sera prise en compte.
   </p>
 
   <p>
 
   <table>
     
    <tr>
 
     <td>
Nom du champ
     </td>
 
     <td>
Descrition
     </td>
 
    </tr>
   
    <tr>
 
     <td>

<b><a href="#TODO-tla1408639383258.xml">vads_url_success</a></b>
     </td>
 
     <td>
URL où sera redirigé l’acheteur, en cas de succès du paiement, après appui sur &quot;retourner à la boutique&quot;.
     </td>
 
    </tr>
 
    <tr>
 
     <td>

<b><a href="#TODO-tla1408639165197.xml">vads_url_refused</a></b>
     </td>
 
     <td>
URL où sera redirigé l’acheteur, en cas de refus du paiement, après appui sur &quot;retourner à la boutique&quot;.
     </td>
 
    </tr>
 
    <tr>
 
     <td>

<b><a href="#TODO-tla1408638742584.xml">vads_url_cancel</a></b>
     </td>
 
     <td>
URL où sera redirigé l’acheteur après appui sur &quot;annuler et retourner à la boutique&quot; avant d&#x27;avoir procédé au paiement.
     </td>
 
    </tr>
 
    <tr>
 
     <td>

<b><a href="#TODO-tla1408639045339.xml">vads_url_error</a></b>
     </td>
 
     <td>
URL où sera redirigé l’acheteur en cas d&#x27;erreur de traitement par la plateforme de paiement.
     </td>
 
    </tr>
   
   </table>
 
   </p>
 
   </li>
 
   <li>
 
   <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
   </p>
 
   </li>
 
  </ol>
 
  <p>
 
  <p>

<u>Exemple de formulaire de paiement avec définition d&#x27;URL de retour en fonction du résultat du paiement:</u>  <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
  </pre></code>

  </p>
 
  </p>
 <!-- tla1406112532368.xml -->
  <h4>
8.7.1.2.   Définir une URL de retour unique quelque soit le résultat du paiement
</h4>
  
  <p>

  </p>
  
  <ol>
 
   <li>
 
   <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
   </p>
 
   </li>
 
   <li>
 
   <p>
Utilisez le champ facultatif <a href="#TODO-tla1408639224559.xml">
<b>vads_url_return</b></a> pour définir l’url de redirection à la fin du paiement.
   </p>
 
   <p>
Si aucune URL n’est valorisée dans le formulaire, la valeur configurée dans le Back Office sera prise en compte. 
   </p>
 
   </li>
 
   <li>
 
   <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
   </p>
 
   </li>
 
  </ol>
 
  <p>
 
  <p>

<u>Exemple de formulaire de paiement avec une URL de retour unique quelque soit le résultat du paiement</u>:  <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
  </pre></code>

  </p>
 
  </p>
 <!-- tla1406115871410.xml -->
 <h3>
8.7.2.  Définir la méthode de réception des données
</h3>
  
 <p>
Par défaut, le site marchand ne reçoit aucun paramètre.
 </p>
 
 <p>
Pour récupérer des informations sur la page de retour (tracking, statistiques, personnalisation des messages à destination de l’acheteur, etc..), le marchand peut surcharger cette configuration dans son formulaire de paiement.
 </p>
  
 <ol>
 
  <li>
 
  <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
  </p>
 
  </li>
 
  <li>
 
  <p>
Utilisez le champ facultatif 
<b>vads_return_mode</b> pour indiquer la méthode de transmission des données vers le site marchand.
  </p>
 
  <p>
 
  <table>
     
   <tr>
 
    <td>
Valeur
    </td>
 
    <td>
Description
    </td>
 
   </tr>
   
   <tr>
 
    <td>
Absent, vide ou 
<b>NONE</b>
    </td>
 
    <td>
Aucune donnée n&#x27;est passée à l’URL de retour.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>GET</b>
    </td>
 
    <td>
Les données sont transmises dans l’URL de la page de retour
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>POST</b>
    </td>
 
    <td>
Les données sont transmises à la page de retour sous la forme d’un formulaire HTTP 
<b>POST</b>.
    </td>
 
   </tr>
   
  </table>
 
  <p>
La méthode 
<b>GET</b> permet d&#x27;éviter l’affichage d’un message d&#x27;avertissement lorsque le retour se fait sur un environnement
<b> non sécurisé (http).</b>
  </p>
<img src="/docs_img/tla1406116471544.image" alt="MessageHTTPPOST"/> 
  </p>
 
  </li>
 
  <li>
 
  <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_ </b>(voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
  </p>
 
  </li>
 
 </ol>
 
 <p>
 
 <p>

<u>Exemple de formulaire de paiement avec définition du mode de transmission des données</u>: <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
 </pre></code>

 </p>
 
 </p>
 <!-- tla1406117141853.xml -->
<h2>
8.8. Activer le retour automatique vers le site marchand
</h2>
  
<p>
Le marchand peut indiquer dans son formulaire s’il souhaite rediriger automatiquement l’acheteur vers le site marchand à la fin du paiement.
</p>
 
<p>
Si vous utilisez un code de tracking (Google AnalyticsTM ou autre) sur votre site, vous devez implémenter cette fonctionnalité.
</p>
  
<ol>
 
 <li>
 
 <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez les champs facultatifs ci-dessous en fonction de vos besoins. 
 </p>
 
 <p>
 
 <table>
      
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408628074901.xml">vads_redirect_success_timeout</a></b>
   </td>
 
   <td>

   <p>
 Définit le délai d’attente avant redirection après un paiement réussi. 
   </p>
Ce délai est exprimé en seconde et doit être compris entre 0 et 300 secondes.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627992082.xml">vads_redirect_success_message</a></b>
   </td>
 
   <td>
Définit le message d’attente avant la redirection après un paiement réussi.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627924375.xml">vads_redirect_error_timeout</a></b>
   </td>
 
   <td>

   <p>
Définit le délai d’attente avant redirection après un paiement refusé. 
   </p>
Ce délai est exprimé en seconde et doit être compris entre 0 et 300 secondes.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627821400.xml">vads_redirect_error_message</a></b>
   </td>
 
   <td>
Définit le message d’attente avant la redirection après un paiement refusé.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_return_mode</b> à 
<b>GET</b> .
 </p>
 
 </li>
 
 <li>
 
 <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_ </b>(voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b> ).
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>

<u>Exemple de formulaire de paiement</u>:<code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406117692857.xml -->
<h2>
8.9. Personnaliser la page de paiement
</h2>
 
<p>
Vous pouvez personnaliser certains éléments de la page de paiement:
</p>
 
<p>
 
<ul>
 
 <li>
les moyens de paiement proposés au moment du paiement,
 </li>
 
 <li>
la langue dans laquelle seront affichées les pages de paiement,
 </li>
 
 <li>
les langues proposées à l’acheteur sur les pages de paiement (drapeaux),
 </li>
 
 <li>
le nom et l’url de la boutique,
 </li>
 
 <li>
le libellé du bouton 
<b>Retourner à la boutique</b>.
 </li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>
En souscrivant à l&#x27;option 
<b>personnalisation avancée</b>, vous pourrez modifier la page de paiement afin de la rendre visuellement proche de votre site marchand. Ceci aura pour effet de conforter l’acheteur et d’instaurer une confiance lors de la redirection pour procéder au paiement. Référez-vous au &quot;manuel utilisateur de la personnalisation avancée&quot; disponible sur le site documentaire <a href="https://www.payzen.eu/support/integration-payzen/">https://www.payzen.eu/support/integration-payzen/</a>.
</p>
 <!-- tla1406118103194.xml -->
 <h3>
8.9.1.  Gérer les moyens de paiement proposés à l&#x27;acheteur
</h3>
  
 <p>
Il est possible de personnaliser les moyens de paiement que vous souhaitez proposer à l’acheteur.
 </p>
  
 <ol>
 
  <li>
 
  <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
  </p>
 
  </li>
 
  <li>
 
  <p>
Valorisez le champ 
<b>vads_payment_cards</b> en utilisant le tableau ci-dessous
  </p>
 
  <ul>
 
   <li>
avec 
<u>une</u> seule valeur si vous ne souhaitez pas afficher la page de sélection des moyens de paiement.
   </li>
 
   <li>
avec une liste de valeurs séparées par un &quot;;&quot; pour afficher la page de sélection des moyens de paiements.
   </li>
 
  </ul>
 
  <p>
 
  <table>
    
   <tr>
 
    <td>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </li>
 
  <li>
 
  <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_ </b>(voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b> ).
  </p>
 
  </li>
 
 </ol>
 
 <p>
 
 <p>

<u>Exemple de formulaire de paiement avec liste de choix de moyens de paiement</u>: <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;30000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
 </pre></code>

 </p>
 
 </p>
 <!-- tla1406125668071.xml -->
 <h3>
8.9.2.  Modifier la langue
</h3>
  
 <p>
Vous pouvez personnaliser la langue utilisée sur les pages de paiement. 
 </p>
  
 <ol>
 
  <li>
 
  <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
  </p>
 
  </li>
 
  <li>
 
  <p>
Valorisez le champ 
<b>vads_language</b> avec une des valeurs présentes dans le tableau ci-dessous.
  </p>
 
  <p>
 
  <table>
   
   <tr>
 
    <td>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
 
  <ul>
 
   <li>
Si la valeur du champ 
<b>vads_language</b> est erronée, le formulaire sera rejeté.
   </li>
 
   <li>
Si le champ n’est pas envoyé ou s’il est valorisé à vide, la page de paiement sera affichée dans la langue du navigateur de l’acheteur.
   </li>
 
   <li>
L’acheteur pourra à tout moment changer de langue en cliquant sur les drapeaux présents en bas de la page de paiement.
   </li>
 
  </ul>
 
  </p>
 
  </li>
 
  <li>
 
  <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b>(voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
  </p>
 
  </li>
 
 </ol>
 
 <p>
 
 <p>

<u>Exemple de formulaire de paiement avec liste de choix de langues:</u> <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
 </pre></code>

 </p>
 
 </p>
 <!-- tla1406126865107.xml -->
 <h3>
8.9.3.  Modifier les langues proposées à l&#x27;acheteur
</h3>
  
 <p>
Vous pouvez personnaliser la liste des langues proposées à l’acheteur.
 </p>
 
 <p>
La dernière langue sélectionnée par l&#x27;acheteur sera la langue par défaut de l&#x27;e-mail de confirmation de paiement à destination de l&#x27;acheteur.
 </p>
  
 <ol>
 
  <li>
 
  <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
  </p>
 
  </li>
 
  <li>
 
  <p>
Valorisez le champ 
<b>vads_available_languages</b> en utilisant le tableau ci-dessous:
  </p>
 
  <ul>
 
   <li>
 
   <p>
avec 
<u>une</u> seule valeur si vous ne souhaitez pas que l’acheteur change de langue.
   </p>
 
   </li>
 
   <li>
 
   <p>

<b>avec une liste de valeurs séparées par un « ; »</b> pour lister les langues disponibles.
   </p>
 
   </li>
 
  </ul>
 
  <p>
 
  <table>
   
   <tr>
 
    <td>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
Si la valeur du champ 
<b>vads_available_languages</b> est erronée, le formulaire sera rejeté.
  </p>
 
  </li>
 
  <li>
 
  <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b>(voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
  </p>
 
  </li>
 
 </ol>
 
 <p>
 
 <p>

<u>Exemple de formulaire de paiement avec liste de choix de langues</u>: <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_available_languages&quot; value=&quot;fr;en&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
 </pre></code>

 </p>
 
 </p>
 <!-- tla1406129461393.xml -->
 <h3>
8.9.4.  Modifier le nom et l&#x27;URL de la boutique
</h3>
  
 <p>
Si vous possédez deux noms de domaines, vous pouvez modifier le nom et l’URL de la boutique pour faire apparaître le nom du domaine.
 </p>
  
 <ol>
 
  <li>
 
  <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
  </p>
 
  </li>
 
  <li>
 
  <p>
Utilisez le champ 
<b>vads_shop_name</b> pour surcharger le nom de la boutique affiché sur la page de paiement.
  </p>
 
  <p>
Cette valeur sera reprise sur le ticket de transaction ainsi que dans l&#x27;e-mail de confirmation.
  </p>
 
  </li>
 
  <li>
 
  <p>
Utilisez le champ 
<b>vads_shop_url</b> pour modifier l’URL de la boutique affichée sur les pages de paiement. 
  </p>
 
  <p>
Cette valeur sera reprise dans l&#x27; e-mail de confirmation.
  </p>
 
  <p>
Si la valeur du champ 
<b>vads_shop_url</b> est erronée, le formulaire ne sera pas rejeté. Cependant, sa valeur est utilisée pour le 3D Secure. Le paiement pourra être refusé si l’URL n’est pas valide.
  </p>
 
  </li>
 
  <li>
 
  <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
  </p>
 
  </li>
 
 </ol>
 
 <p>
 
 <p>

<u>Exemple de formulaire de paiement avec modification du nom et de l&#x27;URL de la boutique:</u> <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
 </pre></code>

 </p>
 
 </p>
 <!-- tla1406129791136.xml -->
 <h3>
8.9.5.  Modifier le libellé du bouton &quot;Retourner à la boutique&quot;
</h3>
  
 <p>
Vous pouvez personnaliser le texte 
<b>«</b> 
<b>Retourner à la boutique »</b>.
 </p>
  
 <ol>
 
  <li>
 
  <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
  </p>
 
  </li>
 
  <li>
 
  <p>
Utilisez le champ 
<b>vads_theme_config</b> pour modifier le libellé des boutons « Retourner à la boutique ».
  </p>
 
  </li>
 
  <li>
 
  <p>
Utilisez le mot-clé 
<b>SUCCESS_FOOTER_MSG_RETURN</b> pour modifier le libellé du bouton « Retour à la boutique » affiché en cas de paiement accepté.
  </p>
 
  </li>
 
  <li>
 
  <p>
Utilisez le mot-clé 
<b>CANCEL_FOOTER_MSG_RETURN</b> pour modifier le libellé du bouton « Annuler et retourner à la boutique » affiché sur les différentes pages de paiement.
  </p>
 
  </li>
 
  <li>
 
  <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
  </p>
 
  </li>
 
 </ol>
 
 <p>
 
 <p>
En souscrivant à l&#x27;option 
<b>personnalisation avancée</b>, vous pourrez modifier des libéllés (exemple : boutique) affichés sur la page de paiement. Référez-vous au &quot;manuel utilisateur de la personnalisation avancée&quot; disponible sur le site documentaire <a href="https://www.payzen.eu/support/integration-payzen/">https://www.payzen.eu/support/integration-payzen/</a>.
 </p>
 
 <p>

<u>Exemple de formulaire de paiement qui modifie le libellé du bouton &quot;Retourner à la boutique&quot;:</u> <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;4000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
 </pre></code>

 </p>
 
 </p>
 <!-- tla1406130055504.xml -->
<h2>
8.10. Surcharger l&#x27;URL de notification  instantanée (IPN)
</h2>
  
<p>
Vous pouvez surcharger l’url de notification instantanée (également appelée IPN) dans le formulaire dans le cas où vous utilisez une seule boutique pour différents canaux de ventes, différentes typologies de paiement, différentes langues etc….
</p>
 
<p>

</p>
 
<p>
Cette fonctionnalité est incompatible avec l&#x27;exécution, depuis le Back Office, de la requête envoyée à l’url de notification instantanée. L’URL appelée sera celle configurée dans la règle de notification (voir chapitre 
<b><a href="#TODO-emm1405085350214.xml">Paramétrer les notifications</a></b>.
</p>
  
<ol>
 
 <li>
 
 <p>
Utilisez l’ensemble des champs nécessaires à votre cas d’utilisation (voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) pour construire votre formulaire de paiement.
 </p>
 
 </li>
 
 <li>
 
 <p>
Utilisez le champ 
<b>vads_url_check</b> pour surcharger l’URL de la page à notifier. 
 </p>
 
 <p>
Si la valeur du champ 
<b>vads_url_check</b> est erronée, le formulaire sera rejeté.
 </p>
 
 </li>
 
 <li>
 
 <p>
Calculez la valeur du champ 
<b>signature</b> en utilisant l’ensemble des champs de votre formulaire, dont le nom commence par 
<b>vads_</b> (voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>

<u>Exemple de formulaire de paiement qui surcharge l&#x27;URL de notification instantanée</u>:<code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406100007665.xml -->
<h2>
8.11. Créer un paiement sans redirection vers la page de paiement
</h2>
 
<p>
Cette fonctionnalité nécessite la souscription de l’option 
<b>Acquisition des données bancaires</b>.
</p>
Dans ce mode, l’acquisition des données bancaires se fera sur le site du marchand.
<p>

</p>

<p>
Cette fonctionnalité :
</p>

<p>
 
<ul>
 
 <li>
est disponible si votre banque autorise la saisie des informations bancaires sur le site marchand.
 </li>
 
 <li>
requiert au minimum l’utilisation d’un certificat SSL sur le site marchand.
 </li>
 
 <li>
ne permet pas de réaliser un paiement avec l&#x27;authentification 3D Secure. 
 </li>
 
</ul>
 
</p>
 
<p>
Cette fonctionnalité ne fonctionne pas pour les paiements avec redirection, tels que :
<ul>
 
 <li>
PayPal, PayPal sandbox
 </li>
 
 <li>
Oney,
 </li>
 
 <li>
V.me by Visa,
 </li>
 
</ul>

</p>
  
<ol>
 
 <li>
 
 <p>
Utilisez les champs présentés ci-dessous pour construire votre formulaire de paiement.
 </p>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Description
   </td>
 
   <td>
Valeur
   </td>
 
  </tr>
   
  <tr>
 
   <td>
vads_site_id
   </td>
 
   <td>
Identifiant de la boutique
   </td>
 
   <td>
Ex : 12345678
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_ctx_mode
   </td>
 
   <td>
Mode de fonctionnement
   </td>
 
   <td>

<b>TEST</b> ou 
<b>PRODUCTION</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_trans_id
   </td>
 
   <td>
Numéro de la transaction 
   </td>
 
   <td>
Ex : 123456
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_trans_date
   </td>
 
   <td>
Date et heure UTC du formulaire de paiement
   </td>
 
   <td>
Ex : 20140129130025
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_amount
   </td>
 
   <td>
Montant du paiement (dans sa plus petite unité monétaire)
   </td>
 
   <td>
Ex : 3000 pour 30 euros
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_currency
   </td>
 
   <td>
Code de la devise utilisée pour le paiement
   </td>
 
   <td>
Ex : 978 pour euro
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_action_mode
   </td>
 
   <td>
Mode d’acquisition des données de la carte
   </td>
 
   <td>

<b>SILENT</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_page_action
   </td>
 
   <td>
Action à réaliser
   </td>
 
   <td>

<b>PAYMENT</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_version
   </td>
 
   <td>
Version du protocole d’échange 
   </td>
 
   <td>

<b>V2</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_payment_config
   </td>
 
   <td>
Type de paiement
   </td>
 
   <td>

<b>SINGLE</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_capture_delay
   </td>
 
   <td>
Délai avant remise en banque
   </td>
 
   <td>

<b>0 </b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_payment_cards
   </td>
 
   <td>
Réseau de la carte
   </td>
 
   <td>

<b>Ex : VISA</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_card_number
   </td>
 
   <td>
Numéro de la carte utilisée pour le paiement
   </td>
 
   <td>

<b>Ex : 4970100000000000</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_cvv
   </td>
 
   <td>
Cryptogramme visuel 
   </td>
 
   <td>

<b>Ex : 123</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_expiry_month
   </td>
 
   <td>
Mois d’expiration de la carte 
   </td>
 
   <td>

<b>Ex : 2</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>
vads_expiry_year
   </td>
 
   <td>
Année d’expiration 
   </td>
 
   <td>

<b>Ex : 2023</b>
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez les champs 
<b>vads_payment_config</b> et 
<b>vads_capture_delay</b> en fonction de votre besoin.
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_action_mode</b> à 
<b>SILENT</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Valorisez le champ 
<b>vads_currency</b> avec le code de la devise souhaitée en utilisant <a href="#TODO-tla1406044948454.xml">le tableau des devises</a> (exemple: 978 pour l&#x27;euro;
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>

</p>
 
<p>

<u>Exemple de formulaire de paiement sans redirection vers la page de paiement</u> : <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;

<b>&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;SILENT&quot; /&gt;</b>
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;4000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;

<b>&lt;input type=&quot;hidden&quot; name=&quot;vads_card_number&quot; value=&quot;4970100000000000&quot; /&gt;</b>
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- emm1405088305497.xml -->
