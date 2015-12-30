---
layout: docs
permalink: /docs/chap-16/
title: chap-16
---
<h1>
16. Dictionnaire de données
</h1>
 
<p>
Le dictionnaire de données présente la liste complète des champs pouvant être utilisés dans le formulaire de paiement.
</p>
 
<p>
Il détaille tout d&#x27;abord les principales catégories (telles que les informations techniques, les informations sur la commande...). L&#x27;ensemble des champs appartenant à une catégorie sont présentés. 
</p>
 
<p>
Ces tableaux sont présentés de la manière suivante :
</p>
 
<p>
 

<ul>
 
<li>

<b>Nom du champ</b> : nom du paramètre, tel qu&#x27;il sera utilisé dans une requête HTTP.
</li>
 
<li>

<b>Format</b> : format des données, selon la codification suivante:
<table>
      
 <tr>
 
  <td>
Notation
  </td>
 
  <td>
Description
  </td>
 
 </tr>
   
 <tr>
 
  <td>
a
  </td>
 
  <td>
Caractères alphabétiques (de ‘A’ à ‘Z’ et de ‘a’ à ‘z’)
  </td>
 
 </tr>
 
 <tr>
 
  <td>
n
  </td>
 
  <td>
Caractères numériques
  </td>
 
 </tr>
 
 <tr>
 
  <td>
s
  </td>
 
  <td>
Caractères spéciaux
  </td>
 
 </tr>
 
 <tr>
 
  <td>
an
  </td>
 
  <td>
Caractères alphanumériques
  </td>
 
 </tr>
 
 <tr>
 
  <td>
ans
  </td>
 
  <td>
Caractères alphanumériques et spéciaux
  </td>
 
 </tr>
 
 <tr>
 
  <td>
3
  </td>
 
  <td>
Longueur fixe de 3 caractères
  </td>
 
 </tr>
 
 <tr>
 
  <td>
..12
  </td>
 
  <td>
Longueur variable jusqu’à 12 caractères
  </td>
 
 </tr>
   
</table>

</li>
 
<li>

<b>Description</b> : description du champ.
</li>

</ul>
 
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

</p>
 
<p>
Le dictionnaire de données présente ensuite le détail pour chacun des champs. Chaque champ est décrit de la manière suivante :
</p>
 
<p>
 

<ul>
 
<li>

<b>Description</b> : description du champ.
</li>
 
<li>

<b>Format</b> : format des données (voir tableau 
<b>Liste champs et formats</b> ci-dessus).
</li>
 
<li>

<b>Valeurs possibles</b> : valeurs attendues lorsque le champ doit être valorisé avec des valeurs spécifiques.
</li>
 
<li>

<b>Exemple</b> : exemple de codage correct des données. 
</li>
 
<li>

<b>Code erreur</b> : en cas d’erreur dans l’interfaçage entre le site marchand et la plateforme de paiement, cette dernière indiquera par un code numérique le paramètre fautif dans le champ 
<b>vads_extra_result</b>.
</li>
 
<li>

<b>Remarque</b> : information complémentaire, précision.
</li>
 
<li>

<b>Catégorie</b> : catégorie à laquelle est affilié le champ.
<p>

</p>

</li>
 
</ul>
 
</p>
 
<p>
Précisions sur les 
<b>codes erreur :</b>
</p>
 
<p>

<b>Code erreur</b> correspond au numéro de l’erreur lors de la soumission d’un formulaire de paiement incorrect. 
</p>
 

<ul>
 
<li>
 En mode test ce code sera affiché sur la page de paiement.
</li>
 
<li>
 En mode production un e-mail d’alerte sera envoyé en précisant le code erreur et le nom du paramètre incorrect.
</li>
 
</ul>
 
<p>

</p>
 
<p>

<b>
<u>Exemple</u> :</b>
<b> Erreur 09 correspond à une erreur sur le montant. Le montant envoyé ne respecte donc pas le format requis</b>
</p>
 <!-- tla1410350807080.xml -->
<h2>
16.1. Visualiser les paramètres classés par catégorie
</h2>
 
<p>
Référez-vous à la catégorie souhaitée pour obtenir la liste des paramètres sous-jacents.
</p>
 
<p>
 

<ul>
 
 <li>
<a href="#TODO-tla1410351589465.xml">Informations sur l&#x27;authentification 3DS</a>.
 </li>
 
 <li>
<a href="#TODO-tla1411025757958.xml">Informations sur l&#x27;abonnement</a>.
 </li>
 
 <li>
<a href="#TODO-tla1410534868650.xml">Informations sur l&#x27;acheteur</a>.
 </li>
 
 <li>
<a href="#TODO-tla1410533143029.xml">Informations sur le moyen de paiement</a>.
 </li>
 
 <li>
<a href="#TODO-tla1410525874342.xml">Informations sur la commande</a>.
 </li>
 
 <li>
<a href="#TODO-tla1410522989073.xml">Informations sur la livraison</a>.
 </li>
 
 <li>
<a href="#TODO-tla1411030317713.xml">Informations techniques</a>.
 </li>
 
 <li>
<a href="#TODO-tla1411031267607.xml">Informations sur la transaction</a>.
 </li>
 
 <li>
<a href="#TODO-tla1416328457246.xml">Informations sur les transactions de don</a>.
 </li>
 
 <li>
<a href="#TODO-tla1410518407791.xml">Personnalisation de la page de la page de paiement</a>.
 </li>
 
 <li>
<a href="#TODO-tla1410514133139.xml">Redirection automatique</a>.
 </li>
 
</ul>
 
</p>
 <!-- tla1411030317713.xml -->
 <h3>
16.1.1.  Informations techniques
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408640166705.xml">signature</a></b>
   </td>
 
   <td>
an40
   </td>
 
   <td>
Permet de vérifier l’intégrité des requêtes. 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1405002307652.xml">vads_action_mode</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Définit le mode d&#x27;acquisition des informations de la carte.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408607954033.xml">vads_contrib</a></b>
   </td>
 
   <td>
ans..128
   </td>
 
   <td>
Indique le nom de la contribution utilisée lors du paiement (Joomla, osCommerce...). 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408608221796.xml">vads_ctx_mode</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Mode de communication de la plateforme de paiement
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408624287246.xml">vads_extra_result</a></b>
   </td>
 
   <td>
n2
   </td>
 
   <td>
Code complémentaire de réponse. Sa signification dépend de la valeur renseignée dans 
<b>vads_result</b>.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408625090595.xml">vads_hash</a></b>
   </td>
 
   <td>
an64
   </td>
 
   <td>
 
   <p>
Clé unique renvoyée uniquement à l’URL de notification (IPN).
   </p>
 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408626371544.xml">vads_page_action</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Définit l&#x27;opération à réaliser.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1415014254111.xml">
<b>vads_payment_error</b></a>
   </td>
 
   <td>
n..3
   </td>
 
   <td>
Codes d&#x27;erreur sur un paiement refusé.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408628157713.xml">vads_result</a></b>
   </td>
 
   <td>
n2
   </td>
 
   <td>
Code retour général du résultat du paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408636137772.xml">vads_site_id</a></b>
   </td>
 
   <td>
n8
   </td>
 
   <td>
Identifiant du site.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408638807307.xml">
<b>vads_url_check</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
URL de la page à notifier à la fin du paiement. Surcharge la valeur saisie dans le paramétrage des règles de notification.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408638858037.xml">
<b>vads_url_check_src</b></a>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Ce paramètre définit l’origine de l’appel URL de notification (IPN Server).
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408639900969.xml">
<b>vads_version</b></a>
   </td>
 
   <td>
string
   </td>
 
   <td>
Version du protocole d’échange avec la plateforme de paiement.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1410525874342.xml -->
 <h3>
16.1.2.  Informations sur la commande
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408624169447.xml">vads_ext_info</a></b>
   </td>
 
   <td>
ans
   </td>
 
   <td>
Champs personnalisables permettant d&#x27;ajouter des données supplémentaires dans l&#x27;e-mail de confirmation envoyé au marchand et dans l&#x27;URL de notification.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1411125541878.xml">
<b>vads_nb_products</b></a>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Détail du panier. Nombre d’articles.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408626141983.xml">vads_order_id</a></b>
   </td>
 
   <td>
an..32
   </td>
 
   <td>
Numéro de commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408626234577.xml">vads_order_info</a></b>
   </td>
 
   <td>
an..255
   </td>
 
   <td>
Description de la commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408626308005.xml">vads_order_info2</a></b>
   </td>
 
   <td>
an..255
   </td>
 
   <td>
Description de la commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408626336653.xml">vads_order_info3</a></b>
   </td>
 
   <td>
an..255
   </td>
 
   <td>
Description de la commande.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1411126075812.xml">
<b>vads_product_amountN</b></a>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Détail du panier. Montant de l’article N
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1411125732485.xml">
<b>vads_product_labelN</b></a>
   </td>
 
   <td>
an..255
   </td>
 
   <td>
Détail du panier. Libellé de l’article N.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1411126555396.xml">
<b>vads_product_qtyN</b></a>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Détail du panier. Quantité d’article N.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1411126454471.xml">
<b>vads_product_refN</b></a>
   </td>
 
   <td>
an..64
   </td>
 
   <td>
Détail du panier. Référence de l’article N.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1411126340153.xml">
<b>vads_product_typeN</b></a>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Détail du panier. Type de l’article N.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1433941223778.xml">
<b>vads_product_vatN</b></a>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Détail du panier. Montant de la TVA de l&#x27;article N.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1410534868650.xml -->
 <h3>
16.1.3.  Informations sur l&#x27;acheteur
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408608603787.xml">vads_cust_address</a></b>
   </td>
 
   <td>
ans..255
   </td>
 
   <td>
Adresse postale.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408608675071.xml">vads_cust_address_number</a></b>
   </td>
 
   <td>
an..5
   </td>
 
   <td>
Numéro de rue.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408608769950.xml">vads_cust_cell_phone</a></b>
   </td>
 
   <td>
an..32
   </td>
 
   <td>
Numéro de téléphone mobile.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408614379476.xml">vads_cust_city</a></b>
   </td>
 
   <td>
an..128
   </td>
 
   <td>
Ville.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408614445899.xml">vads_cust_country</a></b>
   </td>
 
   <td>
a2
   </td>
 
   <td>
Code pays suivant la norme ISO 3166.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408614742379.xml">vads_cust_district</a></b>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
Quartier.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408614926108.xml">vads_cust_email</a></b>
   </td>
 
   <td>
ans..150
   </td>
 
   <td>
Adresse e-mail de l’acheteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408615025768.xml">vads_cust_first_name</a></b>
   </td>
 
   <td>
an..63
   </td>
 
   <td>
Prénom.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408615118352.xml">vads_cust_id</a></b>
   </td>
 
   <td>
an..63
   </td>
 
   <td>
Référence de l’acheteur sur le site marchand.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408615176997.xml">vads_cust_last_name</a></b>
   </td>
 
   <td>
an..63
   </td>
 
   <td>
Nom.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1423825610581.xml">
<b>vads_cust_legal_name</b></a>
   </td>
 
   <td>
an..100
   </td>
 
   <td>
Raison sociale de l&#x27;acheteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408615260331.xml">vads_cust_name</a>
   </td>
 
   <td>
an..127
   </td>
 
   <td>
Déprécié. 
   <p>
Utilisez 
<b>vads_cust_first_name</b> et 
<b>vads_cust_last_name</b>.
   </p>

   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1440084630860.xml">
<b>vads_cust_national_id</b></a>
   </td>
 
   <td>
ans..255
   </td>
 
   <td>
Identifiant national.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408615340066.xml">vads_cust_phone</a></b>
   </td>
 
   <td>
an..32
   </td>
 
   <td>
Numéro de téléphone.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408615396958.xml">vads_cust_state</a></b>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
Etat / Région.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408615475409.xml">vads_cust_status</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Statut (particulier / entreprise).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408615888267.xml">vads_cust_title</a></b>
   </td>
 
   <td>
an..63
   </td>
 
   <td>
Civilité de l’acheteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408616006014.xml">vads_cust_zip</a></b>
   </td>
 
   <td>
an..64
   </td>
 
   <td>
Code postal.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1410522989073.xml -->
 <h3>
16.1.4.  Informations sur la livraison
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408631826813.xml">vads_ship_to_city</a></b>
   </td>
 
   <td>
an..128
   </td>
 
   <td>
Ville.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408632458704.xml">vads_ship_to_country</a></b>
   </td>
 
   <td>
a2
   </td>
 
   <td>
Code pays suivant la norme ISO 3166.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408632679858.xml">vads_ship_to_delivery_company_name</a></b>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
Nom du transporteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408632864028.xml">vads_ship_to_district</a></b>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
Quartier.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408634336065.xml">vads_ship_to_first_name</a></b>
   </td>
 
   <td>
ans..63
   </td>
 
   <td>
Prénom.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408634522824.xml">vads_ship_to_last_name</a></b>
   </td>
 
   <td>
ans..63
   </td>
 
   <td>
Nom.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1423827002789.xml">
<b>vads_ship_to_legal_name</b></a>
   </td>
 
   <td>
an..100
   </td>
 
   <td>
Raison sociale de lieu de livraison.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408634587110.xml">vads_ship_to_name</a></b>
   </td>
 
   <td>
ans..63
   </td>
 
   <td>
Nom de l’acheteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408634698739.xml">vads_ship_to_phone_num</a></b>
   </td>
 
   <td>
ans..32
   </td>
 
   <td>
Numéro de téléphone.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408634757367.xml">vads_ship_to_speed</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Mode de livraison
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408635009448.xml">vads_ship_to_state</a></b>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
Etat / Région.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408634859538.xml">vads_ship_to_status</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Statut (particulier / entreprise).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408635091649.xml">vads_ship_to_street</a></b>
   </td>
 
   <td>
ans..255
   </td>
 
   <td>
Adresse postale.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408635487312.xml">vads_ship_to_street_number</a></b>
   </td>
 
   <td>
an..5
   </td>
 
   <td>
Numéro de rue.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408635139472.xml">vads_ship_to_street2</a></b>
   </td>
 
   <td>
ans..255
   </td>
 
   <td>
Deuxième ligne d’adresse.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408635578322.xml">vads_ship_to_type</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Type de livraison.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408635663652.xml">vads_ship_to_user_info</a></b>
   </td>
 
   <td>
ans..255
   </td>
 
   <td>
Informations acheteur (Identifant légal CPF/CNPJ).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408635725582.xml">vads_ship_to_zip</a></b>
   </td>
 
   <td>
an..64
   </td>
 
   <td>
Code postal.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1410533143029.xml -->
 <h3>
16.1.5.  Informations sur le moyen de paiement
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408550019475.xml">vads_bank_code</a></b>
   </td>
 
   <td>
n5
   </td>
 
   <td>
Code banque associé à la banque émettrice.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408550125294.xml">vads_bank_product</a></b>
   </td>
 
   <td>
an..3
   </td>
 
   <td>
Code produit de la carte utilisée pour le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408550840170.xml">vads_birth_day</a></b>
   </td>
 
   <td>
n..2
   </td>
 
   <td>
Jour de naissance du porteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408551247542.xml">vads_birth_month</a></b>
   </td>
 
   <td>
n..2
   </td>
 
   <td>
Mois de naissance du porteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408551527515.xml">vads_birth_year</a></b>
   </td>
 
   <td>
n4
   </td>
 
   <td>
Année de naissance du porteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408606602420.xml">vads_card_brand</a></b>
   </td>
 
   <td>
an..127
   </td>
 
   <td>
Type de carte utilisé pour le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408607272456.xml">vads_card_country</a></b>
   </td>
 
   <td>
ISO 3166
   </td>
 
   <td>
Code pays de la carte utilisée pour le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408607355172.xml">vads_card_number</a></b>
   </td>
 
   <td>
n..36
   </td>
 
   <td>
Numéro de carte masqué.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408616066204.xml">vads_cvv</a></b>
   </td>
 
   <td>
n..4
   </td>
 
   <td>
Code de sécurité de la carte à 3 ou 4 chiffres.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408624003656.xml">vads_expiry_month</a></b>
   </td>
 
   <td>
n..2
   </td>
 
   <td>
Mois d&#x27;expiration de la carte utilisée pour le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408624118504.xml">vads_expiry_year</a></b>
   </td>
 
   <td>
n4
   </td>
 
   <td>
Année d&#x27;expiration de la carte utilisée pour le paiement.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1411031267607.xml -->
 <h3>
16.1.6.  Informations sur la transaction
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408546768429.xml">vads_amount</a></b>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Montant de la transaction exprimé dans la plus petite unité de la devise (le centime pour l&#x27;euro) 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408547832760.xml">vads_auth_mode</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Spécifie de quelle manière est réalisée la demande d’autorisation. 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408547832760.xml">vads_auth_number</a></b>
   </td>
 
   <td>
an..6
   </td>
 
   <td>
Numéro d&#x27;autorisation retourné par le serveur bancaire.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408548356588.xml">vads_auth_result</a></b>
   </td>
 
   <td>
n2
   </td>
 
   <td>
Code retour de la demande d&#x27;autorisation retournée par la banque émettrice.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408604690440.xml">vads_capture_delay</a></b>
   </td>
 
   <td>
n..3
   </td>
 
   <td>
Délai en nombre de jours avant remise en banque.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1447857764792.xml">
<b>vads_change_rate</b></a>
   </td>
 
   <td>
string
   </td>
 
   <td>
Taux de change utilisé pour calculer le montant réél du paiement (paiement multi-devise).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408607837994.xml">vads_contract_used</a></b>
   </td>
 
   <td>
ans..250
   </td>
 
   <td>
Contrat commerçant utilisé.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408607561985.xml">vads_contracts</a></b>
   </td>
 
   <td>
RESEAU1=contrat1;
   <p>
RESEAU2=contrat2
   </p>

   </td>
 
   <td>
Contrat commerçant à utiliser.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1406044948454.xml">vads_currency</a></b>
   </td>
 
   <td>
n3
   </td>
 
   <td>
Code numérique de la monnaie à utiliser pour le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408616823195.xml">vads_effective_amount</a></b>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Montant du paiement exprimé dans la plus petite unité de la devise utilisée pour effectuer la remise en banque(le centime pour l&#x27;euro) 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408623011853.xml">vads_effective_creation_date</a></b>
   </td>
 
   <td>
n14
   </td>
 
   <td>
Date d&#x27;enregistrement de la transaction, dans le fuseau UTC (ou GMT+0) au format horaire 24h (AAAAMMJJHHMMSS).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408625891261.xml">vads_operation_type</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Permet de différencier une opération de débit ou de crédit (remboursement).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1406099131711.xml">vads_payment_cards </a></b>
   </td>
 
   <td>
type1;type2
   </td>
 
   <td>
Liste des moyens de paiement à proposer à l’acheteur.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408626891430.xml">vads_payment_certificate</a></b>
   </td>
 
   <td>
an40
   </td>
 
   <td>
Champ valorisé par la plateforme de paiement dans le cas où l’autorisation a été réalisée 
<b>avec succès</b>.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627002482.xml">vads_payment_config</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Type du paiement : comptant ou en plusieurs fois.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1415797825296.xml">vads_payment_option_code</a></b>
   </td>
 
   <td>
string
   </td>
 
   <td>
Permet de définir le code de l&#x27;option utilisée.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1424076095539.xml">
<b>vads_payment_seq</b></a>
   </td>
 
   <td>
json
   </td>
 
   <td>
Décrit la séquence d&#x27;un paiement fractionné.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627133271.xml">vads_payment_src</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Origine du paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1413811527238.xml">
<b>vads_risk_analyzer_result</b></a>
   </td>
 
   <td>
ans
   </td>
 
   <td>
Retourne le résultat de l&#x27;analyse de fraude effectué par un système externe (ClearSale, CyberSource,...).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1436276953870.xml">vads_risk_assessment_result</a></b>
   </td>
 
   <td>
ans
   </td>
 
   <td>
Retourne le résultat de l&#x27;analyse de gestion des risques avancée effectuée par la plateforme de paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1409751437465.xml">vads_risk_control</a></b>
   </td>
 
   <td>
contrôle1=resultat1;
   <p>
contrôle2=resultat2
   </p>

   </td>
 
   <td>
Résultat des contrôles associés à la fraude.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408631717602.xml">vads_sequence_number</a></b>
   </td>
 
   <td>
n
   </td>
 
   <td>
Numéro de séquence de la transaction (numéro d&#x27;échéance).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408638544413.xml">vads_trans_date</a></b>
   </td>
 
   <td>
n14
   </td>
 
   <td>
 
   <p>
Date et heure, dans le fuseau UTC (ou GMT+0) au format horaire 24h (AAAAMMJJHHMMSS).
   </p>
 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408638607923.xml">vads_trans_id</a></b>
   </td>
 
   <td>
n6
   </td>
 
   <td>
Identifiant unique d&#x27;une transaction.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408638657026.xml">vads_trans_status</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Statut de la transaction.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1432730650747.xml">vads_trans_uuid</a></b>
   </td>
 
   <td>
ans32
   </td>
 
   <td>
Référence unique de la transaction générée par la plateforme de paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408639754479.xml">vads_validation_mode</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Mode de validation de la transaction.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408639995934.xml">vads_warranty_result</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>

   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1410351589465.xml -->
 <h3>
16.1.7.  Authentification 3DS
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408636944655.xml">vads_threeds_cavv</a></b>
   </td>
 
   <td>
ans..28
   </td>
 
   <td>

   <p>
Désigne la vérification de l’authentification du porteur par l’ACS.
   </p>
Il est valorisé par le serveur d’authentification 3DS (ACS) lorsque l’acheteur s’est correctement authentifié (vads_threeds_status vaut « Y » ou « A »).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408637038608.xml">vads_threeds_cavvAlgorithm</a></b>
   </td>
 
   <td>
n1
   </td>
 
   <td>
 
   <p>
Algorithme utilisé par l’ACS pour générer la valeur du cavv.
   </p>
 
   <p>
Il est valorisé par le serveur d’authentification 3DS (ACS) lorsque l’acheteur s’est correctement authentifié (vads_threeds_status vaut « Y » ou « A »).
   </p>
 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408637200153.xml">vads_threeds_eci</a></b>
   </td>
 
   <td>
n..2
   </td>
 
   <td>

   <p>
Désigne l’Indicateur de Commerce Electronique.
   </p>
Il est valorisé par le serveur d’authentification 3DS (ACS) lorsque l’acheteur s’est correctement authentifié (vads_threeds_status vaut « Y » ou « A »).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408637262343.xml">vads_threeds_enrolled</a></b>
   </td>
 
   <td>
a1
   </td>
 
   <td>

   <p>
Désigne le statut de l’enrôlement du porteur.
   </p>
Il est valorisé par les serveurs VISA et MASTERCARD (DS) durant le processus 3D Secure
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408637376020.xml">vads_threeds_exit_status</a></b>
   </td>
 
   <td>
n..2
   </td>
 
   <td>
 
   <p>
Désigne le statut final du processus 3D Secure.
   </p>
 
   <p>
Il est valorisé par la plateforme de paiement.
   </p>
 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408638075046.xml">vads_threeds_mpi</a></b>
   </td>
 
   <td>
n1
   </td>
 
   <td>
Active / désactive le processus 3DS lors d’un paiement e-commerce
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408638234029.xml">vads_threeds_sign_valid</a></b>
   </td>
 
   <td>
n1
   </td>
 
   <td>

   <p>
Désigne la validité de la signature du message PARes.
   </p>
Il est valorisé par la plateforme de paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408638341396.xml">vads_threeds_status</a></b>
   </td>
 
   <td>
a1
   </td>
 
   <td>
 
   <p>
Désigne le statut de l’authentification du porteur.
   </p>
 
   <p>
Il est valorisé par le serveur d’authentification 3DS (ACS) durant le processus 3D Secure.
   </p>
 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408638445416.xml">vads_threeds_xid</a></b>
   </td>
 
   <td>
ans..28
   </td>
 
   <td>

   <p>
Désigne la référence unique de la transaction 3DS.
   </p>
Il est valorisé par le serveur d’authentification (ACS) durant le processus 3D Secure.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1416328457246.xml -->
 <h3>
16.1.8.  Information sur les transactions de don
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1416319402112.xml">vads_ext_info_donation</a></b>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Montant du don exprimé dans la plus petite unité de la monnaie ou devise(le centime pour l&#x27;euro) 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1416320032761.xml">vads_ext_info_donation_contribution</a></b>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Montant en centimes de la contribution exprimé dans la plus petite unité de la monnaie ou devise (le centime pour l&#x27;euro) 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1416319856371.xml">vads_ext_info_donation_merchant</a></b>
   </td>
 
   <td>
n8
   </td>
 
   <td>
Identifiant de la boutique sur laquelle le don est effectué.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1416319586041.xml">vads_ext_info_donation_recipient</a></b>
   </td>
 
   <td>
n..20
   </td>
 
   <td>
Identifiant HelloAsso de l&#x27;association qui a reçu le don.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1416319785868.xml">vads_ext_info_donation_recipient_name</a></b>
   </td>
 
   <td>
string
   </td>
 
   <td>
Nom de l&#x27;association qui a reçu le don.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1416242779600.xml">vads_risk_primery_warranty</a></b>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Permet de surcharger la configuration du contrôle de risque 
<b>Contrôle du transfert de responsabilité de la transaction primaire</b>.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1410518407791.xml -->
 <h3>
16.1.9.  Personnalisation de la page de paiement
</h3>
 
 <p>

 </p>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>
<a href="#TODO-tla1406127047143.xml">
<b>vads_available_languages</b></a>
   </td>
 
   <td>
langue1;langue2;langue3
   </td>
 
   <td>
Permet de spécifier les langues disponibles sur la page de paiement sous forme de liste.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1406125864809.xml">
<b>vads_language</b></a>
   </td>
 
   <td>
a2
   </td>
 
   <td>
Définit la langue dans laquelle est affichée la page de paiement (norme ISO 639-1).
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408635796483.xml">
<b>vads_shop_name</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
Permet de définir le nom de la boutique qui apparait dans les e-mails de confirmation de paiement et sur le récapitulatif de la transaction.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408635865701.xml">
<b>vads_shop_url</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
Permet de surcharger l&#x27;URL de la boutique qui apparait sur la page de paiement et les e-mails de confirmation de paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408636286614.xml">
<b>vads_theme_config</b></a>
   </td>
 
   <td>
code1=valeur1;code2=valeur2
   </td>
 
   <td>
Permet de personnaliser certains éléments de la page de paiement.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1410514133139.xml -->
 <h3>
16.1.10.  Redirection vers le site marchand
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627821400.xml">vads_redirect_error_message</a></b>
   </td>
 
   <td>
ans..255
   </td>
 
   <td>
 
   <p>

<u>Redirection automatique</u> :
   </p>
 
   <p>
Message affiché sur la page de paiement avant redirection vers le site marchand dans le cas d&#x27;un paiement refusé / accepté.
   </p>
 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627924375.xml">vads_redirect_error_timeout</a></b>
   </td>
 
   <td>
n..3
   </td>
 
   <td>
 
   <p>

<u>Redirection automatique</u> :
   </p>
 
   <p>
Délai ( en secondes ) avant redirection vers le site marchand après un paiement refusé / accepté. 
   </p>
 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408627992082.xml">vads_redirect_success_message</a></b>
   </td>
 
   <td>
ans..255
   </td>
 
   <td>

   <p>

<u>Redirection automatique</u> :
   </p>
Spécifie le message à la fin d’un paiement accepté dans le cas d’une redirection automatique vers le site marchand.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1408628074901.xml">vads_redirect_success_timeout</a></b>
   </td>
 
   <td>
n..3
   </td>
 
   <td>

   <p>

<u>Redirection automatique</u> :
   </p>
Délai en secondes avant redirection vers le site marchand à la fin d’un paiement accepté. Sa valeur est comprise entre 0 et 600s.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1406116003851.xml">vads_return_mode</a></b>
   </td>
 
   <td>
GET/POST/
   <p>
NONE
   </p>

   </td>
 
   <td>
Permet de spécifier le mode de transmission des données aux URLs de retour vers le site marchand.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408638742584.xml">
<b>vads_url_cancel</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
URL où sera redirigé l’acheteur si celui-ci appuie sur &quot; annuler et retourner à la boutique &quot; avant d&#x27;avoir procédé au paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408638807307.xml">
<b>vads_url_check</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
URL de la page à notifier à la fin du paiement. Surcharge la valeur saisie dans le paramétrage des règles de notification.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408638858037.xml">
<b>vads_url_check_src</b></a>
   </td>
 
   <td>
string (enum)
   </td>
 
   <td>
Ce paramètre définit l&#x27;évènement déclencheur de la notification instantanée (aussi appelée IPN ou URL de notification).
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408639045339.xml">
<b>vads_url_error</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
URL où sera redirigé l’acheteur en cas d&#x27;erreur de traitement interne.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408639165197.xml">
<b>vads_url_refused</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
URL où sera redirigé l’acheteur en cas de refus 
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408639224559.xml">
<b>vads_url_return</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
URL par défaut où sera redirigé l&#x27;acheteur si celui-ci appuie sur &quot;retourner à la boutique&quot;.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1408639383258.xml">
<b>vads_url_success</b></a>
   </td>
 
   <td>
ans..127
   </td>
 
   <td>
URL où sera redirigé l’acheteur en cas de succès.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1411025757958.xml -->
 <h3>
16.1.11.  Informations sur l&#x27;abonnement
</h3>
 
 <p>
 
 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Format
   </td>
 
   <td>
Description
   </td>
 
  </tr>
   
  <tr>
 
   <td>
<a href="#TODO-tla1411481213747.xml">
<b>vads_identifier_status</b></a>
   </td>
 
   <td>
string
   </td>
 
   <td>
Statut de l&#x27;enregistrement du mandat.
   </td>
 
  </tr>
 
  <tr>
 
   <td>
<a href="#TODO-tla1447863204383.xml">
<b>vads_recurrence_number</b></a>
   </td>
 
   <td>
n
   </td>
 
   <td>
Numéro de l&#x27;échéance de l&#x27;abonnement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411481506331.xml">vads_recurrence_status</a></b>
   </td>
 
   <td>
string
   </td>
 
   <td>
Statut de la création d&#x27;une récurrence.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411026103849.xml">vads_sub_amount</a></b>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Montant des échéances de l’abonnement pour toutes les échéances, hormis celles éventuellement définies par 
<b>vads_sub_init_amount_number</b>
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411026347617.xml">vads_sub_currency</a></b>
   </td>
 
   <td>
n3
   </td>
 
   <td>
Code numérique de la monnaie à utiliser pour l’abonnement, selon la norme ISO 4217.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411026999130.xml">vads_sub_desc</a></b>
   </td>
 
   <td>
string
   </td>
 
   <td>
Règle de récurrence à appliquer suivant la spécification iCalendar RFC5545.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411025901698.xml">vads_sub_effect_date</a></b>
   </td>
 
   <td>
n8
   </td>
 
   <td>
Date d&#x27;effet de l&#x27;abonnement. 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411026602462.xml">vads_sub_init_amount</a></b>
   </td>
 
   <td>
n..12
   </td>
 
   <td>
Montant des échéances de l’abonnement pour les 
<u>premières échéances</u>. 
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411026836617.xml">vads_sub_init_amount_number</a></b>
   </td>
 
   <td>
n..3
   </td>
 
   <td>
Nombre d’échéances auxquelles il faudra appliquer le montant 
<b>vads_sub_init_amount</b>.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b><a href="#TODO-tla1411025356421.xml">vads_subscription</a></b>
   </td>
 
   <td>
ans..50
   </td>
 
   <td>
Identifiant de l&#x27;abonnement à créer.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 <!-- tla1408640166705.xml -->
<h2>
16.2. signature
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre obligatoire.
  <p>
Permet de vérifier l’intégrité des requêtes transmises. 
  </p>

  <p>
Sa valeur est calculée : 
  </p>

  <p>
 

  <ul>
 
   <li>
par le site marchand lors de la demande de paiement
   </li>
 
   <li>
par la plateforme de paiement lors de la réponse.
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an40
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>

<b>00 - signature</b> lorsque la valeur de ce champ est incorrecte. 
  <p>

<b>70-empty params</b> si le champ est absent ou si ce dernier est posté à vide.
  </p>

  <p>

  </p>

  <p>

<b>Erreurs fréquentes</b>:
  </p>

  <p>
 

  <ul>
 
   <li>
Les différents champs du formulaire n&#x27;ont pas été encodés en UTF-8. 
   </li>
 
   <li>
Le MODE (test ou production) ou le CERTIFICAT utilisé est incorrect. 
   </li>
 
   <li>
Retour à la ligne et/ou retour chariot postés dans le formulaire. 
   </li>
 
   <li>
Caractère guillemets [&quot;] posté dans le formulaire. 
   </li>
 
   <li>
La signature envoyée ne répond pas à la régle de calcul de signature. 
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1405002307652.xml -->
<h2>
16.3. vads_action_mode
</h2>
  
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Paramètre obligatoire.
  </p>
 
  <p>
Mode d’acquisition des informations de la carte. 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
47
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>

<b>INTERACTIVE</b>: saisie des informations de la carte sur la page de paiement.
  </p>
 
  <p>

<b>SILENT</b>: saisie des informations de la carte sur le site marchand (soumis à option commerciale délivrée par votre banque).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
  <!-- tla1408546768429.xml -->
<h2>
16.4. vads_amount
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Montant de la transaction exprimé dans la plus petite unité de la monnaie ou devise (le centime pour l&#x27;euro) 
  </p>
Exemple : pour une transaction de 10 euros
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
09
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408547056236.xml -->
<h2>
16.5. vads_auth_mode
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Spécifie de quelle manière est réalisée la demande d’autorisation. 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>

<b>FULL</b> : correspond à une autorisation du montant total de la transaction.
  </p>
 
  <p>
Valeur utilisée dans le cas d’un paiement comptant, si la durée séparant la date de remise demandée de la date du jour est strictement inférieure à la durée de validité de l&#x27;autorisation. 
  </p>
 
  <p>

<b>MARK</b> : correspond à une autorisation de 1 euro
  </p>
 
  <p>
Valeur utilisée dans le cas d&#x27;un paiement différé, si la durée séparant la date de remise demandée de la date du jour est strictement supérieure à la durée de validité de l&#x27;autorisation. 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408547832760.xml -->
<h2>
16.6. vads_auth_number
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Numéro d&#x27;autorisation retourné par le serveur bancaire, si disponible (sinon vide).
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..6
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408548356588.xml -->
<h2>
16.7. vads_auth_result
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Code retour de la demande d&#x27;autorisation retournée par la banque émettrice, si disponible.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>
 
  <table>
         
   <tr>
 
    <td>
Valeur
    </td>
 
    <td>
Description
    </td>
 
    <td>
Motif frauduleux
    </td>
 
    <td>
Valeur
    </td>
 
    <td>
Description
    </td>
 
    <td>
Motif frauduleux
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>00</b>
    </td>
 
    <td>
Transaction approuvée ou traitée avec succès.
    </td>
 
    <td>

    </td>
 
    <td>

<b>38</b>
    </td>
 
    <td>
Date de validité de la carte dépassée.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>02</b>
    </td>
 
    <td>
Contacter l’émetteur de carte.
    </td>
 
    <td>

    </td>
 
    <td>

<b>41</b>
    </td>
 
    <td>
Carte perdue.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>03</b>
    </td>
 
    <td>
Accepteur invalide.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>43</b>
    </td>
 
    <td>
Carte volée.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>04</b>
    </td>
 
    <td>
Conserver la carte.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>51</b>
    </td>
 
    <td>
Provision insuffisante ou crédit dépassé.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>05</b>
    </td>
 
    <td>
Ne pas honorer.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>54</b>
    </td>
 
    <td>
Date de validité de la carte dépassée.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>07</b>
    </td>
 
    <td>
Conserver la carte, conditions spéciales.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>55</b>
    </td>
 
    <td>
Code confidentiel erroné.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>08</b>
    </td>
 
    <td>
Approuver après identification.
    </td>
 
    <td>

    </td>
 
    <td>

<b>56</b>
    </td>
 
    <td>
Carte absente du fichier.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>12</b>
    </td>
 
    <td>
Transaction invalide.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>57</b>
    </td>
 
    <td>
Transaction non permise à ce porteur.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>13</b>
    </td>
 
    <td>
Montant invalide
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>58</b>
    </td>
 
    <td>
Transaction non permise à ce porteur.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>14</b>
    </td>
 
    <td>
Numéro de porteur invalide.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>59</b>
    </td>
 
    <td>
Suspicion de fraude.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>15</b>
    </td>
 
    <td>
Emetteur de carte inconnu.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>60</b>
    </td>
 
    <td>
L’accepteur de carte doit contacter l’acquéreur.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>17</b>
    </td>
 
    <td>
Annulation acheteur.
    </td>
 
    <td>

    </td>
 
    <td>

<b>61</b>
    </td>
 
    <td>
Montant de retrait hors limite.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>19</b>
    </td>
 
    <td>
Répéter la transaction ultérieurement.
    </td>
 
    <td>

    </td>
 
    <td>

<b>63</b>
    </td>
 
    <td>
Règles de sécurité non respectées.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>20</b>
    </td>
 
    <td>
Réponse erronée (erreur dans le domaine serveur).
    </td>
 
    <td>

    </td>
 
    <td>

<b>68</b>
    </td>
 
    <td>
Réponse non parvenue ou reçue trop tard.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>24</b>
    </td>
 
    <td>
Mise à jour de fichier non supportée
    </td>
 
    <td>

    </td>
 
    <td>

<b>75</b>
    </td>
 
    <td>
Nombre d’essais code confidentiel dépassé.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>25</b>
    </td>
 
    <td>
Impossible de localiser l’enregistrement dans le fichier.
    </td>
 
    <td>

    </td>
 
    <td>

<b>76</b>
    </td>
 
    <td>
Porteur déjà en opposition, ancien enregistrement conservé.
    </td>
 
    <td>
OUI
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>26</b>
    </td>
 
    <td>
Enregistrement dupliqué, ancien enregistrement remplacé.
    </td>
 
    <td>

    </td>
 
    <td>

<b>90</b>
    </td>
 
    <td>
Arrêt momentané du système.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>27</b>
    </td>
 
    <td>
Erreur en « edit » sur champ de liste à jour fichier.
    </td>
 
    <td>

    </td>
 
    <td>

<b>91</b>
    </td>
 
    <td>
Émetteur de cartes inaccessible.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>28</b>
    </td>
 
    <td>
Accès interdit au fichier.
    </td>
 
    <td>

    </td>
 
    <td>

<b>94</b>
    </td>
 
    <td>
Transaction dupliquée.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>29</b>
    </td>
 
    <td>
Mise à jour impossible.
    </td>
 
    <td>

    </td>
 
    <td>

<b>96</b>
    </td>
 
    <td>
Mauvais fonctionnement du système.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>30</b>
    </td>
 
    <td>
Erreur de format.
    </td>
 
    <td>

    </td>
 
    <td>

<b>97</b>
    </td>
 
    <td>
Échéance de la temporisation de surveillance globale.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>31</b>
    </td>
 
    <td>
Identifiant de l’organisme acquéreur inconnu.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>98</b>
    </td>
 
    <td>
Serveur indisponible routage réseau demandé à nouveau.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>33</b>
    </td>
 
    <td>
Date de validité de la carte dépassée.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

<b>99</b>
    </td>
 
    <td>
Incident domaine initiateur.
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>34</b>
    </td>
 
    <td>
Suspicion de fraude.
    </td>
 
    <td>
OUI
    </td>
 
    <td>

    </td>
 
    <td>

    </td>
 
    <td>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1406127047143.xml -->
<h2>
16.8. vads_available_languages
</h2>
  
<p>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Permet de spécifier les langues disponibles sur la page de paiement sous forme de liste. 
  </p>
 
  <p>
Chaque élément de la liste doit être séparé par un point-virgule « ; ».
  </p>
 
  <p>
Est matérialisé par l’affichage de drapeaux sur la page de paiement . 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
langue1;langue2;langue3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
71
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  <table>
      
   <tr>
 
    <td>
Langue
    </td>
 
    <td>
Valeur
    </td>
 
    <td>
Drapeau affiché par défaut
    </td>
 
   </tr>
   
   <tr>
 
    <td>
Allemand
    </td>
 
    <td>
de
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Anglais
    </td>
 
    <td>
en
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Chinois
    </td>
 
    <td>
zh
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Espagnol
    </td>
 
    <td>
es
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Français
    </td>
 
    <td>
fr
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Italien
    </td>
 
    <td>
it
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Japonais
    </td>
 
    <td>
ja
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Néerlandais
    </td>
 
    <td>
nl
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Polonais
    </td>
 
    <td>
pl
    </td>
 
    <td>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
Portugais
    </td>
 
    <td>
pt
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Russe
    </td>
 
    <td>
ru
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Suédois
    </td>
 
    <td>
sv
    </td>
 
    <td>
x
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Turc
    </td>
 
    <td>
tr
    </td>
 
    <td>
x
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
Exemple : pour afficher les drapeaux des langues français et anglais, il faut poster vads_available_languages=fr ;en
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Personnalisation de la page de paiement.
  </td>
 
 </tr>
   
</table>
 
</p>
  <!-- tla1408550019475.xml -->
<h2>
16.9. vads_bank_code
</h2>
  
<p>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Code banque associé à la banque émettrice. 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n5
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 
</p>
  <!-- tla1408550125294.xml -->
<h2>
16.10. vads_bank_product
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Code produit de la carte utilisée pour le paiement.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>
 
  <table>
     
   <tr>
 
    <td>

<b>VISA</b>
    </td>
 
    <td>

<b>Désignation</b>
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>A</b>
    </td>
 
    <td>
Visa Traditional
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>B</b>
    </td>
 
    <td>
Visa Traditional Rewards
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>C</b>
    </td>
 
    <td>
Visa Signature
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>D</b>
    </td>
 
    <td>
Visa Signature Preferred
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>E</b>
    </td>
 
    <td>
Proprietary ATM
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>F</b>
    </td>
 
    <td>
Visa Classic
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>G</b>
    </td>
 
    <td>
Visa Business
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>G1</b>
    </td>
 
    <td>
Visa Signature Business
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>G2</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>G3</b>
    </td>
 
    <td>
Visa Business Enhanced
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>H</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>I</b>
    </td>
 
    <td>
Visa Infinite
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>J</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>J1</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>J2</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>J3</b>
    </td>
 
    <td>
Visa Healthcare
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>J4</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>K</b>
    </td>
 
    <td>
Visa Corporate T&amp;E
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>K1</b>
    </td>
 
    <td>
Visa GSA Corporate T&amp;E
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>L</b>
    </td>
 
    <td>
Electron
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>N</b>
    </td>
 
    <td>
Visa Platinium
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>N1</b>
    </td>
 
    <td>
TBA
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>P</b>
    </td>
 
    <td>
Visa Gold
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>Q</b>
    </td>
 
    <td>
Private Label
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>Q1</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>R</b>
    </td>
 
    <td>
Proprietary
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S</b>
    </td>
 
    <td>
Visa Purchasing
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S1</b>
    </td>
 
    <td>
Visa Purchasing
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S2</b>
    </td>
 
    <td>
Visa Purchasing
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S3</b>
    </td>
 
    <td>
Visa Purchasing
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S4</b>
    </td>
 
    <td>
Government Services Loan
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S5</b>
    </td>
 
    <td>
Commercial Transport EBT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S6</b>
    </td>
 
    <td>
Business Loan
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>S7</b>
    </td>
 
    <td>
Visa Distribution
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>T</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>U</b>
    </td>
 
    <td>
Visa TravelMoney
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>V</b>
    </td>
 
    <td>
Visa VPay
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>W</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>X</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>Y</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>Z</b>
    </td>
 
    <td>
Reserved
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>

  </p>
 
  <p>
 
  <table>
     
   <tr>
 
    <td>
 
    <p>
MASTERCARD
    </p>
 
    </td>
 
    <td>

<b>Désignation</b>
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>MPN</b>
    </td>
 
    <td>
MASTERCARD PREPAID DEBIT STANDARD-INSURANCE
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPO</b>
    </td>
 
    <td>
MASTERCARD PREPAID DEBIT STANDARD-OTHER
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPP</b>
    </td>
 
    <td>
MASTERCARD PREPAID CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPR</b>
    </td>
 
    <td>
MASTERCARD PREPAID DEBIT STANDARD-TRAVEL
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPT</b>
    </td>
 
    <td>
MASTERCARD PREPAID DEBIT STANDARD-TEEN
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPV</b>
    </td>
 
    <td>
MASTERCARD PREPAID DEBIT STANDARD-VERNMENT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPW</b>
    </td>
 
    <td>
DEBIT MASTERCARD BUSINESS CARD PREPAID WORK B2B
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPX</b>
    </td>
 
    <td>
MASTERCARD PREPAID DEBIT STANDARD-FLEX BENEFIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPY</b>
    </td>
 
    <td>
MASTERCARD PREPAID DEB STANDARD-EMPLOYEE INCENTIVE
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MRG</b>
    </td>
 
    <td>
MASTERCARD PREPAID CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MRH</b>
    </td>
 
    <td>
MASTERCARD UNKNOWN PRODUCT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MRW</b>
    </td>
 
    <td>
PREPAID MASTERCARD BUSINESS CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MSG</b>
    </td>
 
    <td>
PREPAID MAESTRO CONSUMER RELOADABLE CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MSI</b>
    </td>
 
    <td>
MAESTRO CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MWB</b>
    </td>
 
    <td>
WORLD MASTERCARD FOR BUSINESS CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MWE</b>
    </td>
 
    <td>
WORLD ELITE MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>DLS</b>
    </td>
 
    <td>
DEBIT MASTERCARD CARD-DELAYED DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MCB</b>
    </td>
 
    <td>
MASTERCARD BUSINESSCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MCC</b>
    </td>
 
    <td>
MASTERCARD CREDIT CARD (MIXED BIN)
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MVOIR</b>
    </td>
 
    <td>
MASTERCARD FLEET CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MCG</b>
    </td>
 
    <td>
LD MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MCO</b>
    </td>
 
    <td>
MASTERCARD CORPORATE CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MCP</b>
    </td>
 
    <td>
MASTERCARD PURCHASING CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MCS</b>
    </td>
 
    <td>
STANDARD MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MCW</b>
    </td>
 
    <td>
WORLD MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MDG</b>
    </td>
 
    <td>
LD DEBIT MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MDH</b>
    </td>
 
    <td>
WORLD DEBIT EMBOSSED MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MDP</b>
    </td>
 
    <td>
PLATINUM DEBIT MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MDS</b>
    </td>
 
    <td>
DEBIT MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MIU</b>
    </td>
 
    <td>
DEBIT MASTERCARD UNEMBOSSED
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MNW</b>
    </td>
 
    <td>
MASTERCARD WORLD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MOC</b>
    </td>
 
    <td>
MASTERCARD UNKNOWN PRODUCT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPG</b>
    </td>
 
    <td>
DEBIT MASTERCARD STANDARD PREPAID-GENERAL SPEND
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPL</b>
    </td>
 
    <td>
PLATINUM MASTERCARD CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MPP</b>
    </td>
 
    <td>
MASTERCARD PREPAID CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MRG</b>
    </td>
 
    <td>
MASTERCARD PREPAID CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MRO</b>
    </td>
 
    <td>
MASTERCARD REWARDS ONLY
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MRW</b>
    </td>
 
    <td>
PREPAID MASTERCARD BUSINESS CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MSB</b>
    </td>
 
    <td>
MAESTRO SMALL BUSINESS CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MSI</b>
    </td>
 
    <td>
MAESTRO CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MSO</b>
    </td>
 
    <td>
MAESTRO PREPAID OTHER CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MSW</b>
    </td>
 
    <td>
PREPAID MAESTRO CORPORATE CARD
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>OLS</b>
    </td>
 
    <td>
MAESTRO-DELAYED DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>TCB</b>
    </td>
 
    <td>
MASTERCARD BUSINESS CARD-IMMEDIATE DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>TCC</b>
    </td>
 
    <td>
MASTERCARD (MIXED BIN)-IMMEDIATE DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>TCG</b>
    </td>
 
    <td>
LD MASTERCARD CARD-IMMEDIATE DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>TCS</b>
    </td>
 
    <td>
MASTERCARD STANDARD CARD-IMMEDIATE DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>TCW</b>
    </td>
 
    <td>
WORLD SIGNIA MASTERCARD CARD-IMMEDIATE DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>TNW</b>
    </td>
 
    <td>
MASTERCARD NEW WORLD-IMMEDIATE DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>TPL</b>
    </td>
 
    <td>
PLATINUM MASTERCARD-IMMEDIATE DEBIT
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>WBE</b>
    </td>
 
    <td>
MASTERCARD UNKNOWN PRODUCT
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
 
  <table>
     
   <tr>
 
    <td>

<b>CB</b>
    </td>
 
    <td>

<b>Désignation</b>
    </td>
 
   </tr>
   
   <tr>
 
    <td>
1
    </td>
 
    <td>
Carte nationale de retrait
    </td>
 
   </tr>
 
   <tr>
 
    <td>
2
    </td>
 
    <td>
Carte nationale de retrait et de paiement
    </td>
 
   </tr>
 
   <tr>
 
    <td>
3
    </td>
 
    <td>
Carte nationale de paiement
    </td>
 
   </tr>
 
   <tr>
 
    <td>
4
    </td>
 
    <td>
Carte nationale de paiement et de retrait à autorisation systématique
    </td>
 
   </tr>
 
   <tr>
 
    <td>
5
    </td>
 
    <td>
Carte nationale de paiement à autorisation systématique
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408550840170.xml -->
<h2>
16.11. vads_birth_day
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Jour de naissance du porteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
76
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408551247542.xml -->
<h2>
16.12. vads_birth_month
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Mois de naissance du porteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
76
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408551527515.xml -->
<h2>
16.13. vads_birth_year
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Année de naissance du porteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n4
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
78
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408604690440.xml -->
<h2>
16.14. vads_capture_delay
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Indique le délai en nombre de jours avant remise en banque. 
  <p>
Si ce paramètre n’est pas transmis, alors la valeur par défaut définie dans le Back Office sera utilisée. Cette dernière est paramétrable dans le Back Office par toutes les personnes dûment habilitées.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
06
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408606602420.xml -->
<h2>
16.15. vads_card_brand
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>

  <p>
Moyen de paiement utilisé, si disponible (vide sinon). 
  </p>
La valeur est issue des fichiers de plages de BIN.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
Se référer au paramètre <a href="#TODO-tla1406099131711.xml">
<b>vads_payment_cards</b></a>.
  </p>
 
  <p>
La valeur CB sera renvoyée pour les cartes CB cobrandées Visa ou Mastercard.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408607272456.xml -->
<h2>
16.16. vads_card_country
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>
Code pays de la carte utilisée pour le paiement à la norme ISO 3166.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ISO 3166
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408607355172.xml -->
<h2>
16.17. vads_card_number
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>

<u>Dans la demande de paiement</u>
  </p>
 
  <p>
Numéro de carte en clair (cas du paiement silencieux).
  </p>
 
  <p>

<u>Dans la réponse</u>
  </p>
 
  <p>
 

  <ul>
 
   <li>
Numéro de carte masqué. Contient les 6 premiers chiffres du numéro, suivi par “XXXXXX” et enfin les 4 derniers numéros. 
   </li>
 
   <li>
 
   <p>
IBAN et BIC utilisés pour le paiement, séparés par un « _ » dans le cas d’un paiement par prélèvement.
   </p>
 
   </li>
 
  </ul>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..36
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
40
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1447857764792.xml -->
<h2>
16.18. vads_change_rate
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Taux de change utilisé pour calculer le montant réél du paiement (lors d&#x27;un paiement multi-devise).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408607561985.xml -->
<h2>
16.19. vads_contracts
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Permet de spécifier, pour chaque réseau d’acceptation, le contrat commerçant à utiliser sous forme de liste. 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
RESEAU1=contrat1;RESEAU2=contrat2;RESEAU3=contrat3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
62
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
Les différents réseaux possibles sont:
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
ACCORD
    </td>
 
    <td>
réseau Banque Accord (cartes cadeau et privatives)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ACCORD_SANDBOX
    </td>
 
    <td>
réseau Banque Accord (cartes cadeau et privatives) - mode sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
AMEX
    </td>
 
    <td>
American Express
    </td>
 
   </tr>
 
   <tr>
 
    <td>
AURORE
    </td>
 
    <td>
réseau Cetelem Aurore (cartes Enseignes et carte Aurore universelle)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CB
    </td>
 
    <td>
réseau CB (Visa, Mastercard, CB, eCB, Maestro, Visa Electron)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CDGP
    </td>
 
    <td>
réseau CDGP (carte Privilège)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CERIDIAN
    </td>
 
    <td>
réseau Céridian (carte cadeau)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
COF3XCB
    </td>
 
    <td>
réseau 3xCB Cofinoga
    </td>
 
   </tr>
 
   <tr>
 
    <td>
COF3XCB_SB
    </td>
 
    <td>
réseau 3xCB Cofinoga - mode sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
COFINOGA
    </td>
 
    <td>
réseau Cofinoga (carte Be Smart et enseignes)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
E_CV
    </td>
 
    <td>
réseau ANCV
    </td>
 
   </tr>
 
   <tr>
 
    <td>
GATECONEX
    </td>
 
    <td>
réseau Gateconex (Visa, Mastercard, CB, Maestro, Visa Electron, Diners)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
GICC_MAESTRO
    </td>
 
    <td>
réseau GICC (carte maestro)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
GICC_MASTERCARD
    </td>
 
    <td>
réseau GICC (carte mastercard)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
GICC_VISA
    </td>
 
    <td>
réseau GICC (carte visa)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
GIROPAY
    </td>
 
    <td>
réseau Giropay
    </td>
 
   </tr>
 
   <tr>
 
    <td>
IDEAL
    </td>
 
    <td>
réseau IDEAL 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
JCB
    </td>
 
    <td>
réseau JCB
    </td>
 
   </tr>
 
   <tr>
 
    <td>
KLARNA
    </td>
 
    <td>
réseau Klarna
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ONEY
    </td>
 
    <td>
réseau Oney
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ONEY_SANDBOX
    </td>
 
    <td>
réseau Oney - mode sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
PAYPAL
    </td>
 
    <td>
réseau PayPal
    </td>
 
   </tr>
 
   <tr>
 
    <td>
PAYPAL_SB
    </td>
 
    <td>
réseau PayPal - mode sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
PAYSAFECARD
    </td>
 
    <td>
réseau paysafecard
    </td>
 
   </tr>
 
   <tr>
 
    <td>
POSTFINANCE
    </td>
 
    <td>
réseau Postfinance
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SEPA
    </td>
 
    <td>
réseau SEPA (SDD et SCT)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SOFORT
    </td>
 
    <td>
réseau Sofort
    </td>
 
   </tr>
 
   <tr>
 
    <td>
WIRECARD
    </td>
 
    <td>
réseau WIRECARD
    </td>
 
   </tr>
   
  </table>
 
  </p>

  <p>
 
  </p>

  <p>
 
  </p>

  <p>
 
  </p>

  <p>
 
  </p>

  <p>
 
  </p>

  <p>

  </p>

  <p>
Par exemple, si vous disposez d’un 2ème contrat VAD de numéro 12312312 dans votre banque, et que vous souhaitez enregistrer pour une commande donnée un paiement par carte bancaire (Visa, MasterCard ou CB) sur ce contrat, alors il faudra valoriser 
<b>vads_contracts</b> de la manière suivante :
  </p>

  <p>
 
  </p>

  <p>

<u>Exemple :</u>
  </p>

  <p>
vads_contracts=CB=12312312;AMEX=949400444000
  </p>

<b>
<u>Remarque </u>:</b> ce paramètre est facultatif et n’est utile que dans le cas 
<b>où vous avez plusieurs contrats VAD</b> sur le même réseau et si vous souhaitez 
<b>en changer dynamiquement en fonction du paiement.</b> Si ce paramètre n’est pas renseigné ou absent, alors le paiement sera enregistré sur votre contrat commerçant VAD par défaut.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408607837994.xml -->
<h2>
16.20. vads_contract_used
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Ce champ définit la valeur du contrat associé à la transaction. Il est valorisé par le contrat enregistré par défaut dans votre boutique ou prend la valeur du champ 
<b>vads_contracts</b> passé lors de la demande de paiement.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..250
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408607954033.xml -->
<h2>
16.21. vads_contrib
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Information complémentaire facultative destinée à indiquer le nom de la contribution utilisée lors du paiement (Joomla, osCommerce...). Si vous utilisez une implémentation propriétaire, ce champ peut accueillir votre numéro de version interne du module que vous avez développé par exemple.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..128
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
31
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408607954033.xml -->
<h2>
16.22. vads_contrib
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Information complémentaire facultative destinée à indiquer le nom de la contribution utilisée lors du paiement (Joomla, osCommerce...). Si vous utilisez une implémentation propriétaire, ce champ peut accueillir votre numéro de version interne du module que vous avez développé par exemple.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..128
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
31
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408608221796.xml -->
<h2>
16.23. vads_ctx_mode
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Paramètre obligatoire.
  </p>

  <p>
Définit le mode de sollicitation de la plateforme de paiement. 
  </p>

  <p>
Influe sur le choix du certificat à utiliser (certificat de test ou certificat de production) pour le calcul de la signature.
  </p>

  <p>
Le mode TEST est toujours disponible, même après la génération du certificat de production.
  </p>
Si vous créez un nouveau site marchand (ou disposez d’un environnement de recette), vous pourrez effectuer vos tests sans impacter le site actuellement en production.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
11
  <p>

<b>Erreurs fréquentes</b>:
  </p>

  <p>
 

  <ul>
 
   <li>
Le mode n&#x27;a pas été envoyé à la plateforme de paiement.
   </li>
 
   <li>
Ne pas coder PROD à la place de PRODUCTION
   </li>
 
   <li>
Ne pas coder la valeur en minuscules (test ou production). Ce champ attend exclusivement des valeurs en majuscules et sans abréviation.
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

<b>TEST</b>, 
<b>PRODUCTION</b>
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408608221796.xml -->
<h2>
16.24. vads_ctx_mode
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Paramètre obligatoire.
  </p>

  <p>
Définit le mode de sollicitation de la plateforme de paiement. 
  </p>

  <p>
Influe sur le choix du certificat à utiliser (certificat de test ou certificat de production) pour le calcul de la signature.
  </p>

  <p>
Le mode TEST est toujours disponible, même après la génération du certificat de production.
  </p>
Si vous créez un nouveau site marchand (ou disposez d’un environnement de recette), vous pourrez effectuer vos tests sans impacter le site actuellement en production.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
11
  <p>

<b>Erreurs fréquentes</b>:
  </p>

  <p>
 

  <ul>
 
   <li>
Le mode n&#x27;a pas été envoyé à la plateforme de paiement.
   </li>
 
   <li>
Ne pas coder PROD à la place de PRODUCTION
   </li>
 
   <li>
Ne pas coder la valeur en minuscules (test ou production). Ce champ attend exclusivement des valeurs en majuscules et sans abréviation.
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

<b>TEST</b>, 
<b>PRODUCTION</b>
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1406044948454.xml -->
<h2>
16.25. vads_currency
</h2>
  
<p>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Code numérique de la monnaie à utiliser pour le paiement, selon la norme ISO 4217 (code numérique).
  </p>
Pour utiliser une devise différente de l’euro (978), il est nécessaire de demander l’activation de l’option « multi devise ».
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
10
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  <table>
       
   <tr>
 
    <td>
Devise
    </td>
 
    <td>
Codification ISO 4217
    </td>
 
    <td>
Devise
    </td>
 
    <td>
Codification ISO 4217
    </td>
 
   </tr>
   
   <tr>
 
    <td>
Baht thailandais
    </td>
 
    <td>
764
    </td>
 
    <td>
Moroccan Dirham
    </td>
 
    <td>
504
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Couronne danoise
    </td>
 
    <td>
208
    </td>
 
    <td>
Nouveau dollar de Taïwan
    </td>
 
    <td>
901
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Couronne islandaise
    </td>
 
    <td>
352
    </td>
 
    <td>
Nouvelle Livre turque
    </td>
 
    <td>
949
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Couronne norvégienne
    </td>
 
    <td>
578
    </td>
 
    <td>
Kuwaiti Dinar
    </td>
 
    <td>
414
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Couronne suédoise
    </td>
 
    <td>
752
    </td>
 
    <td>
Dinar Tunisien 
    </td>
 
    <td>
788
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Couronne tchèque
    </td>
 
    <td>
203
    </td>
 
    <td>
Peso argentin
    </td>
 
    <td>
032
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Dollar australien
    </td>
 
    <td>
036
    </td>
 
    <td>
Peso mexicain
    </td>
 
    <td>
484
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Dollar canadien
    </td>
 
    <td>
124
    </td>
 
    <td>
Peso philippin
    </td>
 
    <td>
608
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Dollar de Hong Kong
    </td>
 
    <td>
344
    </td>
 
    <td>
Rand sud-africain
    </td>
 
    <td>
710
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Dollar de Singapour
    </td>
 
    <td>
702
    </td>
 
    <td>
Real de Brésil
    </td>
 
    <td>
986
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Dollar des États-Unis
    </td>
 
    <td>
840
    </td>
 
    <td>
Renminbi yuan chinois
    </td>
 
    <td>
156
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Dollar néo-zélandais
    </td>
 
    <td>
554
    </td>
 
    <td>
Ringgit malais
    </td>
 
    <td>
458
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Euro
    </td>
 
    <td>
978
    </td>
 
    <td>
Rouble russe
    </td>
 
    <td>
643
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Forint hongrois
    </td>
 
    <td>
348
    </td>
 
    <td>
Rupiah indonésienne
    </td>
 
    <td>
360
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Franc CFP
    </td>
 
    <td>
953
    </td>
 
    <td>
Won de Corée du Sud
    </td>
 
    <td>
410
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Franc suisse
    </td>
 
    <td>
756
    </td>
 
    <td>
Yen
    </td>
 
    <td>
392
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Indian rupee
    </td>
 
    <td>
356
    </td>
 
    <td>
Zloty polonais
    </td>
 
    <td>
985
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Livre sterling
    </td>
 
    <td>
826
    </td>
 
    <td>

    </td>
 
    <td>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
   
</table>
 
</p>
  <!-- tla1408608603787.xml -->
<h2>
16.26. vads_cust_address
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Adresse postale de l’acheteur.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..255
  <p>

<i>
<u>
<b>Remarque :</b></u></i> 
  </p>

  <p>

<u>
<i>Les caractères 
<b>&gt;</b> et 
<b>&lt;</b> ne sont pas autorisés.</i></u>
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
19
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Remarque</b>
  </td>
 
  <td>
Paramètre obligatoire pour 3xCB Cofinoga. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408608675071.xml -->
<h2>
16.27. vads_cust_address_number
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Numéro de rue de l’acheteur.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..5
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
112
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408608769950.xml -->
<h2>
16.28. vads_cust_cell_phone
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Numéro de téléphone mobile de l’acheteur.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..32
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
77
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408614379476.xml -->
<h2>
16.29. vads_cust_city
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Ville de l’acheteur.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..128
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
21
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Remarque</b>
  </td>
 
  <td>
Paramètre obligatoire pour 3xCB Cofinoga. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408614445899.xml -->
<h2>
16.30. vads_cust_country
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Permet de spécifier le code du pays de l’acheteur à la norme ISO 3166. 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
a2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
22
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemples de valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  <table>
     
   <tr>
 
    <td>
Pays
    </td>
 
    <td>
Code
    </td>
 
   </tr>
   
   <tr>
 
    <td>
BRESIL
    </td>
 
    <td>
BR
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CORSE
    </td>
 
    <td>
FR
    </td>
 
   </tr>
 
   <tr>
 
    <td>
FRANCE
    </td>
 
    <td>
FR
    </td>
 
   </tr>
 
   <tr>
 
    <td>
GUADELOUPE
    </td>
 
    <td>
GP
    </td>
 
   </tr>
 
   <tr>
 
    <td>
MARTINIQUE
    </td>
 
    <td>
MQ
    </td>
 
   </tr>
 
   <tr>
 
    <td>
NOUVELLE-CALÉDONIE
    </td>
 
    <td>
NC
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ST-PIERRE-ET-MIQUELON
    </td>
 
    <td>
PM
    </td>
 
   </tr>
 
   <tr>
 
    <td>
POLYNESIE FRANCAISE
    </td>
 
    <td>
PF
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Remarque</b>
  </td>
 
  <td>
Paramètre obligatoire pour 3xCB Cofinoga. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408614742379.xml -->
<h2>
16.31. vads_cust_district
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Quartier de l’acheteur. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
113
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408614926108.xml -->
<h2>
16.32. vads_cust_email
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Adresse e-mail de l’acheteur, 
<b>nécessaire si vous souhaitez que la plateforme de paiement envoie un e-mail à l’acheteur</b>.
  <p>
Pour que l&#x27;acheteur reçoive un e-mail, n&#x27;oubliez pas de poster ce paramètre dans le formulaire lorsque vous générez une demande de paiement.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..150
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
15
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615025768.xml -->
<h2>
16.33. vads_cust_first_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Prénom de l’acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
104
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Remarque</b>
  </td>
 
  <td>
Paramètre obligatoire pour 3xCB Cofinoga. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615118352.xml -->
<h2>
16.34. vads_cust_id
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Identifiant de l’acheteur chez le marchand.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
16
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615176997.xml -->
<h2>
16.35. vads_cust_last_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Nom de l’acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
105
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Remarque</b>
  </td>
 
  <td>
Paramètre obligatoire pour 3xCB Cofinoga. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1423825610581.xml -->
<h2>
16.36. vads_cust_legal_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Raison sociale de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..100
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
121
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615260331.xml -->
<h2>
16.37. vads_cust_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Nom de l’acheteur.
  <p>
Ce champ est déprécié. Il est remplacé par les champs 
<b>vads_cust_first_name</b> et 
<b>vads_cust_last_name</b>
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
18
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1440084630860.xml -->
<h2>
16.38. vads_cust_national_id
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Identifiant national. 
  <p>
Permet d&#x27;identifier de façon unique chaque citoyen au sein d&#x27;un pays.
  </p>

  <p>
Par exemple, au Brésil, ClearSale impose que ce champ soit valorisé avec le CPF/CNPJ (format numérique, de longueur comprise entre 11 et 20 digits).
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615340066.xml -->
<h2>
16.39. vads_cust_phone
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Numéro de téléphone de l’acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..32
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
23
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Remarque</b>
  </td>
 
  <td>
Paramètre obligatoire pour 3xCB Cofinoga. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615396958.xml -->
<h2>
16.40. vads_cust_state
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Etat/ Région de l’acheteur
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
88
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615475409.xml -->
<h2>
16.41. vads_cust_status
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Type d’acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
92
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

<b>PRIVATE</b>, 
<b>COMPANY</b>
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408615888267.xml -->
<h2>
16.42. vads_cust_title
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Civilité de l’acheteur (Exemple Mr, Mme, Melle).
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
17
  </td>
 
 </tr>
   
</table>
 <!-- tla1408616006014.xml -->
<h2>
16.43. vads_cust_zip
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Code postal de l’acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..64
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
20
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Remarque</b>
  </td>
 
  <td>
Paramètre obligatoire pour 3xCB Cofinoga. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408616066204.xml -->
<h2>
16.44. vads_cvv
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

<u>Dans la demande de paiement</u>
  <p>
Code de sécurité de la carte (cas du paiement silencieux).
  </p>

  <p>

<u>Dans la réponse</u>
  </p>

  <p>
Code de sécurité masqué.
  </p>

  <p>

  </p>

  <p>
Sa longueur peut varier entre 3 ou 4 chiffres en fonction du type de carte.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..4
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
43
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408616823195.xml -->
<h2>
16.45. vads_effective_amount
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ renvoyé dans la réponse.
  <p>
Montant du paiement dans la devise réellement utilisée pour effectuer la remise en banque.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemples</b>
  </td>
 
  <td>

<b>EXEMPLE POUR UNE BOUTIQUE OU LA REMISE EST EFFECTUÉE EN EURO</b>
  <p>

  </p>

<u>Paiement de 10 euros</u>
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408623011853.xml -->
<h2>
16.46. vads_effective_creation_date
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>
Date d&#x27;enregistrement de la transaction, dans le fuseau UTC (ou GMT+0) au format horaire 24h (AAAAMMJJHHMMSS).
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n14
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408624003656.xml -->
<h2>
16.47. vads_expiry_month
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Mois d’expiration de la carte utilisée pour le paiement.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
41
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408624118504.xml -->
<h2>
16.48. vads_expiry_year
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Année d’expiration de la carte utilisée pour le paiement.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n4
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
42
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur le moyen de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408624169447.xml -->
<h2>
16.49. vads_ext_info
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Permet d’ajouter un champ supplémentaire qui sera visible dans l&#x27;e-mail de confirmation de paiement à l’attention du marchand. 
  </p>

  <p>
Cette information sera visible dans le Back Office, dans le détail de la transaction (onglet 
<b>Extras</b>), et sera également retournée dans l&#x27;URL de notification. 
  </p>

  <p>
Le nom doit commencer par 
<b>vads_ext_info</b> pour être pris en compte.
  </p>
vads_ext_info_
<i>lenomduchamp</i>=valeur
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
91
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418032860506.xml -->
<h2>
16.50. vads_ext_info_bil_address_complement
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Permet de préciser un complément d&#x27;adresse pour la facturation.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..250
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418036120946.xml -->
<h2>
16.51. vads_ext_info_deadline
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Permet de préciser le délai de livraison en jour (N jours).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418033120031.xml -->
<h2>
16.52. vads_ext_info_bil_date_of_birth
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Permet de préciser sur la facture la date de naissance de l&#x27;acheteur.
  </p>
 
  <p>
Format : yyyy-mm-ddThh:mm:ss)
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
Datetime
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418032336492.xml -->
<h2>
16.53. vads_ext_info_bil_gender
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Permet de préciser sur la facture si l&#x27;acheteur est un homme ou une femme.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n1
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418037434548.xml -->
<h2>
16.54. vads_ext_info_fingerprint_id
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Identifiant unique de session.
  </p>
 
  <p>
 

  <ul>
 
   <li>
Soit cet identifiant de session est généré par la plateforme de paiement
   <p>
Dans ce cas, ce paramètre ne doit pas être renseigné.
   </p>

   </li>
 
   <li>
 
   <p>
Soit cet identifiant de session est généré par le site marchand
   </p>
 
   <p>
Dans ce cas, ce paramètre doit être renseigné avec la valeur de l’identifiant souhaité. Attention, il incombe au site marchand de s’assurer de l’unicité des identifiants. Toute demande d&#x27;enregistrement contenant un identifiant déjà existant, sera rejetée, et provoquera l’affichage d’un message d’erreur
   </p>
 
   </li>
 
  </ul>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string
  <p>
Codé sur 128 octets, peut être composé de majuscules ou de minuscules, chiffres ou tiret ([A-Z] [a-z], 0-9, _, -).
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418032955977.xml -->
<h2>
16.55. vads_ext_info_ship_address_complement
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Permet de préciser un complément d&#x27;adresse pour la livraison.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..250
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418033253071.xml -->
<h2>
16.56. vads_ext_info_ship_date_of_birth
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Permet de préciser pour la livraison la date de naissance de l&#x27;acheteur.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
Datetime
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1418032770788.xml -->
<h2>
16.57. vads_ext_info_ship_gender
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Spécifique au Brésil et à l&#x27;analyseur de fraude ClearSale.
  </p>
 
  <p>
Permet de préciser pour la livraison si l&#x27;acheteur est un homme ou une femme.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n1
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1416319402112.xml -->
<h2>
16.58. vads_ext_info_donation
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Paramètre renvoyé uniquement dans la notification instantanée (également appelée IPN) en cas de don.
  </p>
 
  <p>
Montant du don exprimé dans la plus petite unité de la monnaie ou devise (le centime pour l&#x27;Euro)
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Information sur les transactions de don.
  </td>
 
 </tr>
   
</table>
 <!-- tla1416319586041.xml -->
<h2>
16.59. vads_ext_info_donation_recipient 
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Paramètre renvoyé uniquement dans la notification instantanée (également appelée IPN) en cas de don.
  </p>
 
  <p>
Identifiant HelloAsso de l&#x27;association qui a reçu le don.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..20
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Information sur les transactions de don.
  </td>
 
 </tr>
   
</table>
 <!-- tla1416319785868.xml -->
<h2>
16.60. vads_ext_info_donation_recipient_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre renvoyé uniquement dans la notification instantanée (également appelée IPN) en cas de don.
  <p>
Nom de l&#x27;association qui a reçu le don.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Information sur les transactions de don.
  </td>
 
 </tr>
   
</table>
 <!-- tla1416319856371.xml -->
<h2>
16.61. vads_ext_info_donation_merchant 
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Paramètre renvoyé uniquement dans la notification instantanée (également appelée IPN) en cas de don.
  </p>
 
  <p>
Identifiant de la boutique sur laquelle le don est effectué.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n8
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Information sur les transactions de don.
  </td>
 
 </tr>
   
</table>
 <!-- tla1416320032761.xml -->
<h2>
16.62. vads_ext_info_donation_contribution
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Paramètre renvoyé uniquement dans la notification instantanée (également appelée IPN) en cas de don.
  </p>
 
  <p>
Montant en centimes du don exprimé dans la plus petite unité de la monnaie ou devise (le centime pour l&#x27;Euro)
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Information sur les transactions de don.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408624287246.xml -->
<h2>
16.63. vads_extra_result
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Code complémentaire de réponse. Sa signification dépend de la valeur renseignée dans 
<b>vads_result</b>.
  </p>
 
  <p>
 

  <ul>
 
   <li>
Lorsque 
<b>vads_result</b> vaut 30 (erreur de requête), alors 
<b>vads_extra_result</b> contient le code numérique du champ qui comporte une erreur de valorisation ou de format. Cette valeur peut être renseignée à 99 dans le cas d’une erreur inconnue dans la requête.
   <p>

<b>Exemple</b> : si 
<b>vads_extra_result</b> contient la valeur 09, cela signifie que le montant spécifié dans 
<b>vads_amount</b> est incorrect (par exemple, si le montant contient des décimales, car il n’aurait pas été converti préalablement en centimes).
   </p>

   </li>
 
  </ul>
 
  </p>
 
  <p>
 

  <ul>
 
   <li>
Lorsque 
<b>vads_result</b> vaut 05 (refusée) ou 00 (acceptée), alors 
<b>vads_extra_result</b> contient le code numérique du résultat des contrôles de risques. 
   </li>
 
  </ul>
 
  <table>
     
   <tr>
 
    <td>
vads_extra_result
    </td>
 
    <td>
Description
    </td>
 
   </tr>
   
   <tr>
 
    <td>
Vide
    </td>
 
    <td>
Pas de contrôle effectué.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
00
    </td>
 
    <td>
Tous les contrôles se sont déroulés avec succès.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
02
    </td>
 
    <td>
La carte a dépassé l’encours autorisé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
03
    </td>
 
    <td>
La carte appartient à la liste grise du marchand.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
04
    </td>
 
    <td>
Le pays d’émission de la carte appartient à la liste grise du marchand.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
05
    </td>
 
    <td>
L’adresse IP appartient à la liste grise du marchand.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
06
    </td>
 
    <td>
Le code bin appartient à la liste grise du marchand.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
07
    </td>
 
    <td>
Détection d’une e-carte bleue.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
08
    </td>
 
    <td>
Détection d’une carte commerciale nationale.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
09
    </td>
 
    <td>
Détection d’une carte commerciale étrangère.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
14
    </td>
 
    <td>
Détection d’une carte à autorisation systématique.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
20
    </td>
 
    <td>
Contrôle de cohérence : aucun pays ne correspond (pays IP, pays carte, pays de l’acheteur ).
    </td>
 
   </tr>
 
   <tr>
 
    <td>
30
    </td>
 
    <td>
Le pays de l’adresse IP appartient à la liste grise.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
99
    </td>
 
    <td>
Problème technique rencontré par le serveur lors du traitement d’un des contrôles locaux.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408625090595.xml -->
<h2>
16.64. vads_hash
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Clé unique renvoyée uniquement à l’URL de notification (IPN).
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an64
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408625202233.xml -->
<h2>
16.65. vads_identifier
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Identifiant unique (alias ou référence unique de mandat) associé à un moyen de paiement.
  <p>
 

  <ul>
 
   <li>
Soit cet identifiant est généré par la plateforme.
   <p>
Dans ce cas, ce paramètre ne doit pas être renseigné.
   </p>

   </li>
 
   <li>
 
   <p>
Soit cet identifiant est généré par le site marchand.
   </p>
 
   <p>
Dans ce cas, ce paramètre doit être renseigné avec la valeur de l’identifiant souhaité. 
<b>Attention, il incombe au site marchand de s’assurer de l’unicité des identifiants</b>. Toute demande d&#x27;enregistrement contenant un identifiant déjà existant, sera rejetée, et provoquera l’affichage d’un message d’erreur.
   </p>
 
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..50
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
30
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411481213747.xml -->
<h2>
16.66. vads_identifier_status
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Présent uniquement si l’action demandée correspond à la création ou à la mise à jour d&#x27;un:
  </p>
 
  <p>
 

  <ul>
 
   <li>
alias (abonnement)
   </li>
 
   <li>
RUM ou référence unique de mandat (SEPA)
   </li>
 
  </ul>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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

<b>CREATED</b>
    </td>
 
    <td>
 
    <p>
La demande d’autorisation a été acceptée.
    </p>
 
    <p>
L&#x27;alias ou RUM est créé avec succès.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>NOT_CREATED</b>
    </td>
 
    <td>
 
    <p>
La demande d’autorisation a été refusée. 
    </p>
 
    <p>
L&#x27;alias ou RUM n&#x27;est pas créé et n&#x27;apparaîtra pas dans le Back Office.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>UPDATED</b>
    </td>
 
    <td>
L&#x27;alias ou RUM est mis à jour avec succès.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>ABANDONED</b>
    </td>
 
    <td>
 
    <p>
Action abandonnée par l&#x27;acheteur (débiteur).
    </p>
 
    <p>
L&#x27;alias ou RUM n&#x27;est pas créé et n&#x27;apparaîtra pas dans le Back Office.
    </p>
 
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1412321830815.xml -->
<h2>
16.67. vads_insurance_amount
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Montant de l’assurance pour l’ensemble de la commande. 
  </p>
 
  <p>
Spécifique au moyen de paiement PayPal.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
110
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1406125864809.xml -->
<h2>
16.68. vads_language
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>

<u>Dans la demande de paiement :</u>
  </p>

  <p>
Définit la langue dans laquelle est affichée la page de paiement (norme ISO 639-1). 
  </p>

  <p>
Si le champ n’est pas envoyé ou s’il est valorisé à vide dans la demande de paiement, la page de paiement sera affichée dans la langue présentée par le navigateur de l’acheteur.
  </p>

  <p>

  </p>

  <p>

<u>Dans la réponse :</u>
  </p>

  <p>
Retourne la valeur spécifiée dans le formulaire si l’acheteur n’a pas changé la langue sur la page de paiement. 
  </p>
Retourne la langue sélectionnée par l’acheteur si celui-ci a changé de langue sur la page de paiement en sélectionnant un autre drapeau.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
a2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
12
  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>

  </p>
 
  <p>

  </p>
 
  <p>

  </p>
 
  <p>

  </p>
 
  <p>

  </p>
 
  <p>

  </p>
 
  <p>

  </p>
 
  <p>

  </p>
 
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  <table>
     
   <tr>
 
    <td>
Langue
    </td>
 
    <td>
Codification ISO 639-1
    </td>
 
   </tr>
   
   <tr>
 
    <td>
Allemand
    </td>
 
    <td>
de
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Anglais
    </td>
 
    <td>
en
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Chinois
    </td>
 
    <td>
zh
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Espagnol
    </td>
 
    <td>
es
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Français
    </td>
 
    <td>
fr
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Italien
    </td>
 
    <td>
it
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Japonais
    </td>
 
    <td>
ja
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Néerlandais
    </td>
 
    <td>
nl
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Polonais
    </td>
 
    <td>
pl
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Portugais
    </td>
 
    <td>
pt
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Russe
    </td>
 
    <td>
ru
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Suédois
    </td>
 
    <td>
sv
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Turc
    </td>
 
    <td>
tr
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Personnalisation de la page de paiement
  </td>
 
 </tr>
   
</table>
 <!-- tla1411125541878.xml -->
<h2>
16.69. vads_nb_products
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le nombre de produits contenu dans le panier
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408625891261.xml -->
<h2>
16.70. vads_operation_type
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Permet de différencier une opération de débit ou de crédit (remboursement).
  </p>

  <p>

<i>
<b>Remarque :</b></i>
  </p>

  <p>

<i>Le champ 
<b>vads_operation_type</b> n&#x27;est pas retourné dans la réponse lorsqu&#x27;un paiement est annulé ou abandonné.</i>
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

<b>DEBIT</b>,
<b> CREDIT</b>
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408626141983.xml -->
<h2>
16.71. vads_order_id
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Numéro de commande. Il est également inclu dans l&#x27;e-mail de confirmation de paiement adressé à l’acheteur. 
  </p>

<b>Champ au format alphanumérique. Seul le caractère spécial « - » est autorisé</b>.
  <p>
S&#x27;il contient un caractère spécial (&amp;, ;, @, etc...), la plateforme de paiement retourne une erreur.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..32
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
13
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408626234577.xml -->
<h2>
16.72. vads_order_info
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Descriptif de la commande.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
14
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408626308005.xml -->
<h2>
16.73. vads_oder_info2
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Descriptif de la commande.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
14
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408626336653.xml -->
<h2>
16.74. vads_order_info3
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Descriptif de la commande.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
14
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408626371544.xml -->
<h2>
16.75. vads_page_action
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre obligatoire.
  <p>
Définit l&#x27;opération à réaliser.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
46
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 

  <ul>
 
   <li>
PAYMENT
   </li>
 
   <li>
REGISTER
   </li>
 
   <li>
REGISTER_UPDATE
   </li>
 
   <li>
REGISTER_PAY
   </li>
 
   <li>
REGISTER_SUBSCRIBE
   </li>
 
   <li>
REGISTER_PAY_SUBSCRIBE
   </li>
 
   <li>
SUBSCRIBE
   </li>
 
   <li>
REGISTER_UPDATE_PAY
   </li>
 
   <li>
ASK_REGISTER_PAY
   </li>
 
  </ul>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1406099131711.xml -->
<h2>
16.76. vads_payment_cards
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Contient la liste des moyens de paiement à proposer à l’acheteur, séparés par des &quot; 
<b>;</b>&quot;. 
  </p>

  <p>
Si la liste ne contient qu&#x27;un moyen de paiement, la page de saisie des données de ce moyen de paiement sera directement présentée. Sinon la page de sélection des moyens de paiement sera présentée. 
  </p>
Si ce paramètre est vide (conseillé) alors les moyens de paiement éligibles (devises, contraintes techniques, etc) associés à la boutique seront proposés.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
type1;type2;type3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
08
  <p>
Le formulaire sera rejeté dans les cas suivants :
  </p>

  <p>
 

  <ul>
 
   <li>
la valeur transmise n&#x27;est pas présente dans la liste ci-dessous. 
   </li>
 
   <li>
TOUTES, ALL ne sont pas des valeurs acceptées. Pour proposer tous les moyens de paiement ce paramètre ne doit pas être posté ou être posté à vide. 
   </li>
 
   <li>
 
   <p>
la valeur transmise ne correspond pas au moyen de paiement disponible pour votre boutique.
   </p>
 
   </li>
 
   <li>
 
   <p>
Votre contrat e-commerce a été clôturé par votre établissement bancaire. Contactez le service client de votre plateforme de paiement.
   </p>
 
   </li>
 
   <li>
la valeur transmise n&#x27;est pas éligible dans le réseau associé.
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  </p>
 
  <p>
 
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
ACCORD_STORE
    </td>
 
    <td>
Carte de paiement Banque Accord 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ACCORD_STORE_SB
    </td>
 
    <td>
Carte de paiement Banque Accord - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ALINEA
    </td>
 
    <td>
Carte Privative Alinea
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ALINEA_CDX
    </td>
 
    <td>
Carte cadeau Alinea
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ALINEA_CDX_SB
    </td>
 
    <td>
Carte cadeau Alinea - SandBox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ALINEA_SB
    </td>
 
    <td>
Carte Privative Alinea - SandBox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
AMEX
    </td>
 
    <td>
American Express
    </td>
 
   </tr>
 
   <tr>
 
    <td>
AURORE-MULTI
    </td>
 
    <td>
Carte Aurore
    </td>
 
   </tr>
 
   <tr>
 
    <td>
BANCONTACT
    </td>
 
    <td>
Carte Maestro Bancontact Mistercash
    </td>
 
   </tr>
  
   <tr>
 
    <td>
BITCOIN
    </td>
 
    <td>
Paiement par monnaie virtuelle
    </td>
 
   </tr>
  
   <tr>
 
    <td>
BIZZBEE_CDX
    </td>
 
    <td>
Carte cadeau Bizzbee
    </td>
 
   </tr>
 
   <tr>
 
    <td>
BIZZBEE_CDX_SB
    </td>
 
    <td>
Carte cadeau Bizzbee - Sandbox 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
BRICE_CDX
    </td>
 
    <td>
Carte cadeau Brice
    </td>
 
   </tr>
 
   <tr>
 
    <td>
BRICE_CDX_SB
    </td>
 
    <td>
Carte cadeau Brice - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CB
    </td>
 
    <td>
CB
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CDGP
    </td>
 
    <td>
Carte Privilège
    </td>
 
   </tr>
 
   <tr>
 
    <td>
COF3XCB
    </td>
 
    <td>
3 fois CB Cofinoga
    </td>
 
   </tr>
 
   <tr>
 
    <td>
COF3XCB_SB
    </td>
 
    <td>
3 fois CB Cofinoga - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
COFINOGA
    </td>
 
    <td>
Carte Be Smart
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CORA_BLANCHE
    </td>
 
    <td>
Carte Cora Blanche
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CORA_PREM
    </td>
 
    <td>
Carte Cora Premium
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CORA_VISA
    </td>
 
    <td>
Carte Cora Visa
    </td>
 
   </tr>
 
   <tr>
 
    <td>
DINERS
    </td>
 
    <td>
Carte Diners Club
    </td>
 
   </tr>
 
   <tr>
 
    <td>
E-CARTEBLEUE
    </td>
 
    <td>
E-carte bleue
    </td>
 
   </tr>
 
   <tr>
 
    <td>
E_CV
    </td>
 
    <td>
E-chèque vacance
    </td>
 
   </tr>
  
   <tr>
 
    <td>
EDENRED
    </td>
 
    <td>
Carte &quot;Ticket Restaurant&quot;
    </td>
 
   </tr>
 
   <tr>
 
    <td>
GIROPAY
    </td>
 
    <td>
Virement bancaire
    </td>
 
   </tr>
 
   <tr>
 
    <td>
KLARNA
    </td>
 
    <td>
Paiement par facture
    </td>
 
   </tr>
  
   <tr>
 
    <td>
IDEAL
    </td>
 
    <td>
Virement bancaire
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ILLICADO
    </td>
 
    <td>
Carte cadeau Illicado
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ILLICADO_SB
    </td>
 
    <td>
Carte cadeau Illicado - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
JCB
    </td>
 
    <td>
Carte JCB
    </td>
 
   </tr>
 
   <tr>
 
    <td>
JOUECLUB_CDX
    </td>
 
    <td>
Carte cadeau Jouéclub
    </td>
 
   </tr>
 
   <tr>
 
    <td>
JOUECLUB_CDX_SB
    </td>
 
    <td>
Carte cadeau Jouéclub - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
JULES_CDX
    </td>
 
    <td>
Carte cadeau Jules
    </td>
 
   </tr>
 
   <tr>
 
    <td>
JULES_CDX_SB
    </td>
 
    <td>
Carte cadeau Jules - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
MAESTRO
    </td>
 
    <td>
Maestro
    </td>
 
   </tr>
 
   <tr>
 
    <td>
MASTERCARD
    </td>
 
    <td>
MasterCard
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ONEY
    </td>
 
    <td>
Paiement en 3/4 fois Oney FacilyPay
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ONEY_SANDBOX
    </td>
 
    <td>
Paiement en 3/4 fois Oney FacilyPay - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
PAYLIB
    </td>
 
    <td>
Paylib
    </td>
 
   </tr>
 
   <tr>
 
    <td>
PAYPAL
    </td>
 
    <td>
PayPal
    </td>
 
   </tr>
 
   <tr>
 
    <td>
PAYPAL_SB
    </td>
 
    <td>
PayPal - Sandbox
    </td>
 
   </tr>
 
   <tr>
 
    <td>
PAYSAFECARD
    </td>
 
    <td>
Carte prépayée Paysafecard
    </td>
 
   </tr>
 
   <tr>
 
    <td>
POSTFINANCE
    </td>
 
    <td>
PostFinance
    </td>
 
   </tr>
 
   <tr>
 
    <td>
POSTFINANCE_EFIN
    </td>
 
    <td>
PostFinance mode E-finance
    </td>
 
   </tr>
 
   <tr>
 
    <td>
RUPAY
    </td>
 
    <td>
Moyen de paiement Indien 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SCT
    </td>
 
    <td>
Virement SEPA
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SDD
    </td>
 
    <td>
Prélèvement SEPA
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SOFORT_BANKING
    </td>
 
    <td>
Sofort
    </td>
 
   </tr>
 
   <tr>
 
    <td>
TRUFFAUT_CDX
    </td>
 
    <td>
Carte cadeau Truffaut
    </td>
 
   </tr>
 
   <tr>
 
    <td>
VISA
    </td>
 
    <td>
Visa
    </td>
 
   </tr>
 
   <tr>
 
    <td>
VISA_ELECTRON
    </td>
 
    <td>
Visa Electron
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
 
  </p>
 
  <p>
 
  </p>
 
  <p>
 
  </p>
 
  <p>
 
  </p>
 
  <p>

  </p>
 
  <p>
 
  </p>
 
  </td>
 
 </tr>
   
</table>
 <!-- tla1408626891430.xml -->
<h2>
16.77. vads_payment_certificate
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>
Ce champ est valorisé par la plateforme de paiement dans le cas où l’autorisation a été réalisée 
<b>avec succès</b>.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an40
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408626891430.xml -->
<h2>
16.78. vads_payment_certificate
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>
Ce champ est valorisé par la plateforme de paiement dans le cas où l’autorisation a été réalisée 
<b>avec succès</b>.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an40
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627002482.xml -->
<h2>
16.79. vads_payment_config
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Désigne le type du paiement : comptant ou en plusieurs fois.
  </p>
 
  <p>
 

  <ul>
 
   <li>
Pour un paiement simple, la valeur doit être égale à 
<b>SINGLE</b>. 
   </li>
 
   <li>
Pour un paiement en plusieurs fois avec montants et dates fixes, la valeur doit être égale à 
<b>MULTI: </b>suivi par des paires clé=valeur séparées par des « 
<b>;</b> ». 
   <p>
Les paramètres sont les suivants : 
   </p>


   <ul>
 
    <li>
« 
<b>first</b> » indique le montant du premier paiement (exprimé dans la plus petite unité de la monnaie ou devise).
    </li>
 
    <li>
« 
<b>count</b> » indique le nombre total d&#x27;échéances.
    </li>
 
    <li>
« 
<b>period</b> » indique l’intervalle en nombre de jours entre 2 paiements.
    <p>
L&#x27;ordre des champs associés à MULTI est imposé. 
    </p>

    </li>
 
   </ul>

   </li>
 
   <li>
Pour un paiement en plusieurs fois, avec un échéancier personnalisé, la valeur doit être égale à 
<b>MULTI_EXT:</b> suivi par des paires date=montant séparées par des « 
<b>;</b> ». 
   <p>
Les dates ne doivent pas être dans le passé.
   </p>

   </li>
 
  </ul>
 
  </p>
 
  <p>
L’utilisation de la valeur MULTI_EXT nécessite la souscription de l’option 
<b>Paiement en plusieurs fois avancé</b>.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
07
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 

  <ul>
 
   <li>

<b>SINGLE</b>
   </li>
 
  </ul>
 

  <ul>
 
   <li>

<b>MULTI:first= montant_inital ;count= nbre_echeances ;period= intervalle_en_jours</b>
   </li>
 
   <li>

<b>MULTI_EXT:date1=montant1;date2=montant2;date3=montant3</b>
   </li>
 
  </ul>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemple 1</b>
  </td>
 
  <td>

  <p>

<b>MULTI</b> permet de définir un paiement en plusieurs fois. 
  </p>

  <p>
Le montant de chaque échéance correspond au montant total divisé par le nombre d&#x27;échéances. 
  </p>

  <p>
La valeur du premier montant peut être différente et spécifiée dans le paramètre 
<b>first</b>. 
  </p>

  <p>
En cas de reste différent de zéro, il sera reporté sur le montant de la dernière échéance.
  </p>

<u>Requête de paiement :</u>
  <p>
 

  <ul>
 
   <li>
vads_capture_delay=2
   </li>
 
   <li>
vads_currency=978
   </li>
 
   <li>
vads_amount=20000
   </li>
 
   <li>
vads_payment_config=MULTI:first=10000;count=4;period=30
   </li>
 
  </ul>
 
  </p>

  <p>

<u>Résultat :</u>
  </p>

  <p>
Un premier paiement de 100 euros
  </p>

  <p>
Un deuxième paiement de 33.33 euros
  </p>

  <p>
Un troisième paiement de 33.33 euros
  </p>

  <p>
Un quatrième et dernier paiement de 33.34 euros
  </p>

  <p>
Le total donne bien 200 euros
  </p>

  <p>
Cette instruction permet de créer immédiatement 4 paiements avec le même numéro de transaction mais un numéro d&#x27;échéance différent (vads_sequence_number).
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemple 2</b>
  </td>
 
  <td>
 
  <p>

<b>MULTI_EXT</b> permet de définir un échéancier personnalisé. Vous pourrez ainsi définir la date et le montant de chaque échéance. 
  </p>
 
  <p>

<u>Requête de paiement MULTI_EXT :</u>
  </p>
 
  <p>
 

  <ul>
 
   <li>
vads_currency=978
   </li>
 
   <li>
vads_amount=10000
   </li>
 
   <li>
vads_payment_config= MULTI_EXT
<b>:</b>20150601 =5000; 20150701 =2500; 20150808 =2500
   </li>
 
  </ul>
 
  </p>
 
  <p>

<u>Résultat :</u>
  </p>
 
  <p>
Le premier paiement aura lieu le 1er juin 2015 pour un montant de 50euros
  </p>
 
  <p>
Le second paiement aura lieu le 1er juillet 2015 pour un montant de 25euros
  </p>
 
  <p>
Le dernier paiement aura lieu le 8 août 2015 pour un montant de 25euros
  </p>
 
  <p>

<u>Remarque :</u>
  </p>
 
  <p>
La somme totale des montants doit être égale à la valeur du champ 
<b>vads_amount</b>. La date de la dernière échéance ne peut être supérieure à 12 mois par rapport à la date de soumission du formulaire. Si la date de la dernière échéance est supérieure à la date de validité de la carte, aucune échéance ne sera enregistrée et l’acheteur sera notifié par un message de ce problème.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627002482.xml -->
<h2>
16.80. vads_payment_config
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Désigne le type du paiement : comptant ou en plusieurs fois.
  </p>
 
  <p>
 

  <ul>
 
   <li>
Pour un paiement simple, la valeur doit être égale à 
<b>SINGLE</b>. 
   </li>
 
   <li>
Pour un paiement en plusieurs fois avec montants et dates fixes, la valeur doit être égale à 
<b>MULTI: </b>suivi par des paires clé=valeur séparées par des « 
<b>;</b> ». 
   <p>
Les paramètres sont les suivants : 
   </p>


   <ul>
 
    <li>
« 
<b>first</b> » indique le montant du premier paiement (exprimé dans la plus petite unité de la monnaie ou devise).
    </li>
 
    <li>
« 
<b>count</b> » indique le nombre total d&#x27;échéances.
    </li>
 
    <li>
« 
<b>period</b> » indique l’intervalle en nombre de jours entre 2 paiements.
    <p>
L&#x27;ordre des champs associés à MULTI est imposé. 
    </p>

    </li>
 
   </ul>

   </li>
 
   <li>
Pour un paiement en plusieurs fois, avec un échéancier personnalisé, la valeur doit être égale à 
<b>MULTI_EXT:</b> suivi par des paires date=montant séparées par des « 
<b>;</b> ». 
   <p>
Les dates ne doivent pas être dans le passé.
   </p>

   </li>
 
  </ul>
 
  </p>
 
  <p>
L’utilisation de la valeur MULTI_EXT nécessite la souscription de l’option 
<b>Paiement en plusieurs fois avancé</b>.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
07
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 

  <ul>
 
   <li>

<b>SINGLE</b>
   </li>
 
  </ul>
 

  <ul>
 
   <li>

<b>MULTI:first= montant_inital ;count= nbre_echeances ;period= intervalle_en_jours</b>
   </li>
 
   <li>

<b>MULTI_EXT:date1=montant1;date2=montant2;date3=montant3</b>
   </li>
 
  </ul>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemple 1</b>
  </td>
 
  <td>

  <p>

<b>MULTI</b> permet de définir un paiement en plusieurs fois. 
  </p>

  <p>
Le montant de chaque échéance correspond au montant total divisé par le nombre d&#x27;échéances. 
  </p>

  <p>
La valeur du premier montant peut être différente et spécifiée dans le paramètre 
<b>first</b>. 
  </p>

  <p>
En cas de reste différent de zéro, il sera reporté sur le montant de la dernière échéance.
  </p>

<u>Requête de paiement :</u>
  <p>
 

  <ul>
 
   <li>
vads_capture_delay=2
   </li>
 
   <li>
vads_currency=978
   </li>
 
   <li>
vads_amount=20000
   </li>
 
   <li>
vads_payment_config=MULTI:first=10000;count=4;period=30
   </li>
 
  </ul>
 
  </p>

  <p>

<u>Résultat :</u>
  </p>

  <p>
Un premier paiement de 100 euros
  </p>

  <p>
Un deuxième paiement de 33.33 euros
  </p>

  <p>
Un troisième paiement de 33.33 euros
  </p>

  <p>
Un quatrième et dernier paiement de 33.34 euros
  </p>

  <p>
Le total donne bien 200 euros
  </p>

  <p>
Cette instruction permet de créer immédiatement 4 paiements avec le même numéro de transaction mais un numéro d&#x27;échéance différent (vads_sequence_number).
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemple 2</b>
  </td>
 
  <td>
 
  <p>

<b>MULTI_EXT</b> permet de définir un échéancier personnalisé. Vous pourrez ainsi définir la date et le montant de chaque échéance. 
  </p>
 
  <p>

<u>Requête de paiement MULTI_EXT :</u>
  </p>
 
  <p>
 

  <ul>
 
   <li>
vads_currency=978
   </li>
 
   <li>
vads_amount=10000
   </li>
 
   <li>
vads_payment_config= MULTI_EXT
<b>:</b>20150601 =5000; 20150701 =2500; 20150808 =2500
   </li>
 
  </ul>
 
  </p>
 
  <p>

<u>Résultat :</u>
  </p>
 
  <p>
Le premier paiement aura lieu le 1er juin 2015 pour un montant de 50euros
  </p>
 
  <p>
Le second paiement aura lieu le 1er juillet 2015 pour un montant de 25euros
  </p>
 
  <p>
Le dernier paiement aura lieu le 8 août 2015 pour un montant de 25euros
  </p>
 
  <p>

<u>Remarque :</u>
  </p>
 
  <p>
La somme totale des montants doit être égale à la valeur du champ 
<b>vads_amount</b>. La date de la dernière échéance ne peut être supérieure à 12 mois par rapport à la date de soumission du formulaire. Si la date de la dernière échéance est supérieure à la date de validité de la carte, aucune échéance ne sera enregistrée et l’acheteur sera notifié par un message de ce problème.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1415014254111.xml -->
<h2>
16.81. vads_payment_error
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Codes d&#x27;erreurs pouvant apparaître lors d&#x27;un paiement refusé.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>
 
  <table>
       
   <tr>
 
    <td>
Code d&#x27;erreur
    </td>
 
    <td>
Message d&#x27;erreur
    </td>
 
    <td>
Code d&#x27;erreur
    </td>
 
    <td>
Message d&#x27;erreur
    </td>
 
   </tr>
   
   <tr>
 
    <td>
1
    </td>
 
    <td>
La transaction n&#x27;a pas été trouvée.
    </td>
 
    <td>
72
    </td>
 
    <td>
 
    <p>
Refus d&#x27;autorisation par Cofinoga.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
2
    </td>
 
    <td>
La transaction n&#x27;a pas été trouvée.
    </td>
 
    <td>
73
    </td>
 
    <td>
 
    <p>
Refus de l&#x27;autorisation à 1 euro
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
3
    </td>
 
    <td>
Cette action n&#x27;est pas autorisée sur une transaction ayant ce statut {0}. 
    </td>
 
    <td>
74
    </td>
 
    <td>
 
    <p>
Configuration de paiement invalide.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
4
    </td>
 
    <td>
Cette transaction n&#x27;est pas autorisée dans ce contexte. 
    </td>
 
    <td>
75
    </td>
 
    <td>
L&#x27;opération a été refusée par PayPal.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
5
    </td>
 
    <td>
La transaction existe déjà. 
    </td>
 
    <td>
76
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
6
    </td>
 
    <td>
Montant de transaction invalide. 
    </td>
 
    <td>
77
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
7
    </td>
 
    <td>
Cette action n&#x27;est plus possible pour une transaction créée à cette date. 
    </td>
 
    <td>
78
    </td>
 
    <td>
 
    <p>
Identifiant de transaction non défini.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
8
    </td>
 
    <td>
La date d&#x27;expiration de la carte ne permet pas cette action. 
    </td>
 
    <td>
79
    </td>
 
    <td>
 
    <p>
Identifiant de transaction déjà utilisé.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
9
    </td>
 
    <td>
CVV obligatoire pour la carte. 
    </td>
 
    <td>
80
    </td>
 
    <td>
 
    <p>
Identifiant de transaction expiré.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
10
    </td>
 
    <td>
Le montant de remboursement est supérieur au montant initial. 
    </td>
 
    <td>
81
    </td>
 
    <td>
Contenu du thème config invalide.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
11
    </td>
 
    <td>
La somme des remboursements effectués est supérieure au montant initial. 
    </td>
 
    <td>
82
    </td>
 
    <td>
 
    <p>
Le remboursement n&#x27;est pas autorisé.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
12
    </td>
 
    <td>
La duplication d&#x27;un crédit (remboursement) n&#x27;est pas autorisée. 
    </td>
 
    <td>
83
    </td>
 
    <td>
 
    <p>
Montant de transaction en dehors des valeurs permises.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
13
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande. 
    </td>
 
    <td>
84
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
14
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </td>
 
    <td>
85
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
15
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande. 
    </td>
 
    <td>
86
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
16
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande. 
    </td>
 
    <td>
87
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
17
    </td>
 
    <td>
Le téléparamétrage du contrat Aurore a échoué. 
    </td>
 
    <td>
88
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
18
    </td>
 
    <td>
L&#x27;analyse de la réponse Cetelem a échoué. 
    </td>
 
    <td>
89
    </td>
 
    <td>
 
    <p>
La modification n&#x27;est pas autorisée.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
19
    </td>
 
    <td>
Devise inconnue.
    </td>
 
    <td>
90
    </td>
 
    <td>
 
    <p>
Une erreur est apparue lors du remboursement de cette transaction.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
20
    </td>
 
    <td>
Type de carte invalide.
    </td>
 
    <td>
91
    </td>
 
    <td>
Aucune option de paiement activée pour ce contrat.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
21
    </td>
 
    <td>
Aucun contrat trouvé pour ce paiement. Veuillez modifier les données ou contacter votre gestionnaire en cas d&#x27;échecs répétés. 
    </td>
 
    <td>
92
    </td>
 
    <td>
Une erreur est survenue lors du calcul du canal de paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
22
    </td>
 
    <td>
Boutique non trouvée. 
    </td>
 
    <td>
93
    </td>
 
    <td>
Une erreur est survenue lors du retour de l&#x27;acheteur sur la page de finalisation de paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
23
    </td>
 
    <td>
Contrat ambigüe
    </td>
 
    <td>
94
    </td>
 
    <td>
Une erreur technique est survenue.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
24
    </td>
 
    <td>
Contrat invalide
    </td>
 
    <td>
95
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
25
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande. 
    </td>
 
    <td>
96
    </td>
 
    <td>
 
    <p>
Une erreur est apparue lors de la remise de cette transaction.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
26
    </td>
 
    <td>
Numéro de carte invalide
    </td>
 
    <td>
97
    </td>
 
    <td>
Date de remise trop éloignée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
27
    </td>
 
    <td>
Numéro de carte invalide
    </td>
 
    <td>
98
    </td>
 
    <td>
Date de transaction invalide. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
28
    </td>
 
    <td>
Numéro de carte invalide
    </td>
 
    <td>
99
    </td>
 
    <td>
Une erreur est survenue lors du calcul de l&#x27;origine du paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
29
    </td>
 
    <td>
Numéro de carte invalide
    </td>
 
    <td>
100
    </td>
 
    <td>
Contrôle carte commerciale en échec.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
30
    </td>
 
    <td>
Numéro de carte invalide (Luhn)
    </td>
 
    <td>
101
    </td>
 
    <td>
 
    <p>
Refusé car première échéance refusée.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
31
    </td>
 
    <td>
Numéro de carte invalide (longueur)
    </td>
 
    <td>
102
    </td>
 
    <td>
 
    <p>
L&#x27;opération a été refusée par Buyster.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
32
    </td>
 
    <td>
Numéro de carte invalide (non trouvé)
    </td>
 
    <td>
103
    </td>
 
    <td>
 
    <p>
Le statut de la transaction n&#x27;a pas pu être synchronisé avec le système externe
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
33
    </td>
 
    <td>
Numéro de carte invalide (non trouvé)
    </td>
 
    <td>
104
    </td>
 
    <td>
Une erreur est apparue lors de la remise de cette transaction.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
34
    </td>
 
    <td>
Contrôle carte à autorisation systématique en échec. 
    </td>
 
    <td>
105
    </td>
 
    <td>
 
    <p>
Une erreur de sécurité est apparue lors du processus 3DS de cette transaction.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
35
    </td>
 
    <td>
Contrôle e-Carte Bleue en échec. 
    </td>
 
    <td>
106
    </td>
 
    <td>
Devise non supportée pour ce contrat et/ou cette boutique.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
36
    </td>
 
    <td>
Le contrôle des risques a provoqué le refus de la transaction. 
    </td>
 
    <td>
107
    </td>
 
    <td>
La carte associée à l&#x27;alias n&#x27;est plus valide.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
37
    </td>
 
    <td>
Interruption non gérée lors du processus de paiement.
    </td>
 
    <td>
108
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
38
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
    <td>
109
    </td>
 
    <td>
Délai d&#x27;attente dépassé lors de la redirection de l&#x27;acheteur.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
39
    </td>
 
    <td>
 
    <p>
Refus 3D Secure pour la transaction.
    </p>
 
    </td>
 
    <td>
110
    </td>
 
    <td>
Carte de paiement non supportée par le contrat.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
40
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
    <td>
111
    </td>
 
    <td>
Refus des transactions sans transfert de responsabilité.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
41
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
    <td>
112
    </td>
 
    <td>
L&#x27;annulation n&#x27;est pas autorisée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
42
    </td>
 
    <td>
 
    <p>
Une erreur interne est survenue lors de la consultation du numéro de carte.
    </p>
 
    </td>
 
    <td>
113
    </td>
 
    <td>
 
    <p>
La duplication n&#x27;est pas autorisée.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
43
    </td>
 
    <td>
 
    <p>
Une erreur interne est survenue lors de la consultation du numéro de carte.
    </p>
 
    </td>
 
    <td>
114
    </td>
 
    <td>
 
    <p>
Le forçage n&#x27;est pas autorisé.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
44
    </td>
 
    <td>
 
    <p>
Il n&#x27;est pas possible de forcer une autorisation à 1 euro
    </p>
 
    </td>
 
    <td>
115
    </td>
 
    <td>
Le remboursement n&#x27;est pas autorisé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
45
    </td>
 
    <td>
 
    <p>
Devise invalide pour la modification.
    </p>
 
    </td>
 
    <td>
116
    </td>
 
    <td>
Paiement manuel non autorisé pour cette carte.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
46
    </td>
 
    <td>
Le montant est supérieur au montant autorisé.
    </td>
 
    <td>
118
    </td>
 
    <td>
 
    <p>
Paiement manuel en plusieurs fois non autorisé pour cette carte.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
47
    </td>
 
    <td>
 
    <p>
La date de présentation souhaitée est postérieure à la date de validité de l&#x27;autorisation.
    </p>
 
    </td>
 
    <td>
119
    </td>
 
    <td>
La date soumise est invalide.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
48
    </td>
 
    <td>
 
    <p>
La modification requise est invalide.
    </p>
 
    </td>
 
    <td>
120
    </td>
 
    <td>
 
    <p>
L&#x27;option de paiement de la transaction initiale n&#x27;est pas applicable.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
49
    </td>
 
    <td>
 
    <p>
Définition du paiement multiple invalide.
    </p>
 
    </td>
 
    <td>
124
    </td>
 
    <td>
Carte inactive.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
50
    </td>
 
    <td>
 
    <p>
Boutique inconnue.
    </p>
 
    </td>
 
    <td>
125
    </td>
 
    <td>
Paiement refusé par l&#x27;acquéreur.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
51
    </td>
 
    <td>
 
    <p>
Cours inconnu.
    </p>
 
    </td>
 
    <td>
126
    </td>
 
    <td>
Cette action n&#x27;est pas possible car la séquence de paiement n&#x27;est pas terminée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
52
    </td>
 
    <td>
 
    <p>
Le contrat est clos depuis le {0}.
    </p>
 
    </td>
 
    <td>
132
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
53
    </td>
 
    <td>
 
    <p>
La boutique {0} est close depuis le {1}.
    </p>
 
    </td>
 
    <td>
135
    </td>
 
    <td>
L&#x27;intégration de la page de paiement dans une iframe n&#x27;est pas autorisée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
54
    </td>
 
    <td>
Paramètre rejeté pouvant contenir des données sensibles {0}.
    </td>
 
    <td>
136
    </td>
 
    <td>
 
    <p>
Refus des transactions dérivées, sans transfert de responsabilité sur la transaction primaire.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
55
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
    <td>
137
    </td>
 
    <td>
La transaction est un doublon.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
57
    </td>
 
    <td>
 
    <p>
Erreur lors de la récupération de l&#x27;alias.
    </p>
 
    </td>
 
    <td>
138
    </td>
 
    <td>
Le remboursement partiel n&#x27;est pas possible sur cette transaction.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
58
    </td>
 
    <td>
Le statut de l&#x27;alias n&#x27;est pas compatible avec cette opération
    </td>
 
    <td>
139
    </td>
 
    <td>
Remboursement refusé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
59
    </td>
 
    <td>
 
    <p>
Erreur lors de la récupération de l&#x27;alias.
    </p>
 
    </td>
 
    <td>
141
    </td>
 
    <td>
L&#x27;analyseur de risque a rejeté cette transaction.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
60
    </td>
 
    <td>
 
    <p>
Alias existant.
    </p>
 
    </td>
 
    <td>
142
    </td>
 
    <td>
 
    <p>
Le type de carte utilisé n&#x27;est pas valide pour le mode de paiement demandé.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
61
    </td>
 
    <td>
Alias invalide
    </td>
 
    <td>
143
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
62
    </td>
 
    <td>
 
    <p>
Création d&#x27;un alias refusée.
    </p>
 
    </td>
 
    <td>
144
    </td>
 
    <td>
Une transaction en mode production a été marquée en mode test chez l&#x27;acquéreur.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
63
    </td>
 
    <td>
 
    <p>
Abonnement déjà existant.
    </p>
 
    </td>
 
    <td>
145
    </td>
 
    <td>
 
    <p>
Une transaction en mode test a été marquée en mode production chez l&#x27;acquéreur.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
64
    </td>
 
    <td>
Cet abonnement est déjà résilié.
    </td>
 
    <td>
146
    </td>
 
    <td>
Code sms invalide.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
65
    </td>
 
    <td>
 
    <p>
Cet abonnement est invalide.
    </p>
 
    </td>
 
    <td>
147
    </td>
 
    <td>
Le module de gestion de fraudes a demandé le refus de cette transaction.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
66
    </td>
 
    <td>
 
    <p>
La règle de récurrence n&#x27;est pas valide.
    </p>
 
    </td>
 
    <td>
148
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande. La transaction n&#x27;a pas été créée.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
67
    </td>
 
    <td>
Création de l&#x27;abonnement refusée.
    </td>
 
    <td>
149
    </td>
 
    <td>
La durée de la session de paiement a expiré (cas de l&#x27;acheteur qui est redirigé vers l&#x27;ACS et qui ne finalise pas l&#x27;authentification 3D Secure).
    </td>
 
   </tr>
 
   <tr>
 
    <td>
69
    </td>
 
    <td>
 
    <p>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande.
    </p>
 
    </td>
 
    <td>
150
    </td>
 
    <td>
Suite à un incident technique, nous ne sommes pas en mesure de traiter votre demande. La transaction n&#x27;a pas été créée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
70
    </td>
 
    <td>
Code pays invalide.
    </td>
 
    <td>

    </td>
 
    <td>
 
    <p>

    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
71
    </td>
 
    <td>
Paramètre du service web invalide.
    </td>
 
    <td>

    </td>
 
    <td>
 
    <p>

    </p>
 
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1415797825296.xml -->
<h2>
16.82. vads_payment_option_code
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le code de l&#x27;option utilisée.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
103
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1424076095539.xml -->
<h2>
16.83. vads_payment_seq
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Détails des transactions réalisées.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
json 
  <p>

<b>vads_payment_seq</b> (format json) décrit la séquence de paiement fractionné. Il contient les éléments :
  </p>

  <p>
 

  <ul>
 
   <li>

<b>&quot;trans_id&quot;</b> : identifiant de la transaction global à la séquence de paiement.
   </li>
 
   <li>

<b>&quot;transaction&quot;</b> : tableau des transactions de la séquence. Il contient les éléments suivants :
   </li>
 
  </ul>
 
  </p>

  <p>
 
  <table>
      
   <tr>
 
    <td>
Nom du paramètre
    </td>
 
    <td>
Description
    </td>
 
   </tr>
   
   <tr>
 
    <td>
amount
    </td>
 
    <td>
Montant de la séquence de paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
operation_type
    </td>
 
    <td>
Opération de débit.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
auth_number
    </td>
 
    <td>
Numéro d&#x27;autorisation retourné par le serveur bancaire, si disponible (sinon vide).
    <p>
Ce paramètre est retourné vide pour un paiement par e-Chèque-Vacances. En effet, le serveur de titres de l&#x27;ANCV ne le fourni pas.
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
capture_delay
    </td>
 
    <td>
Délai avant remise (en jours).
    <p>
 

    <ul>
 
     <li>
Pour un paiement par e-Chèques-Vacances, ce paramètre est valorisé à 
<b>0</b>. En effet, les e-Chèques-Vacances sont validés en temps réel.
     </li>
 
     <li>
Pour un paiement par carte bancaire, la valeur de ce paramètre tient compte du délai en nombre de jours avant la remise en banque. Si ce paramètre n&#x27;est pas transmis dans le formulaire de paiement, la valeur par défaut définie dans le Back Office sera utilisée.
     </li>
 
    </ul>
 
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
card_brand
    </td>
 
    <td>
Moyen de paiement utilisé.
    <p>
 

    <ul>
 
     <li>
Pour un paiement par e-Chèques-Vacances, ce paramètre est valorisé à 
<b>E_CV</b>.
     </li>
 
     <li>
Pour un paiement par carte bancaire (exemple CB ou cartes CB cobrandées Visa ou Mastercard), ce paramètre est valorisé à 
<b>CB</b>.
     </li>
 
    </ul>
 
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
card_number
    </td>
 
    <td>
Numéro du moyen de paiement.
    <p>
 

    <ul>
 
     <li>
Pour un paiement par e-Chèques-Vacances, ce paramètre est valorisé en concaténant le numéro de chèque - numéro organisme - année d&#x27;émission en les séparant avec le caractère &quot;-&quot;.
     </li>
 
     <li>
Pour un paiement par carte bancaire, le numéro est masqué.
     </li>
 
    </ul>
 
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
expiry_month
    </td>
 
    <td>
Mois d&#x27;expiration de la carte bancaire.
    <p>
Paramètre absent pour le paiement par e-Chèque-Vacances.
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
expiry_year
    </td>
 
    <td>
Année d&#x27;expiration de la carte bancaire.
    <p>
Paramètre absent pour le paiement par e-Chèque-Vacances.
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
payment_certificate
    </td>
 
    <td>
Certificat de paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
presentation_date
    </td>
 
    <td>
 
    <p>
 

    <ul>
 
     <li>
Pour un paiement par carte bancaire, ce paramètre correspond à la date de remise en banque souhaitée (au format ISO 8601).
     </li>
 
    </ul>
 
    </p>
 

    <ul>
 
     <li>
Pour un paiement par e-Chèques-Vacances, ce paramètre correspond à la date du jour de la commande. En effet, les e-Chèques-Vacances sont validés en temps réel auprès du serveur de titres de l&#x27;ANCV.
     </li>
 
    </ul>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
trans_id
    </td>
 
    <td>
Numéro de transaction.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ext_trans_id
    </td>
 
    <td>
Paramètre absent pour le paiement par carte bancaire.
    <p>
Pour un paiement par e-Chèques-Vacances, ce paramètre est un identifiant technique généré par la plateforme de paiement (référence de transaction).
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
sequence_number
    </td>
 
    <td>
Numéro de séquence.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
trans_status
    </td>
 
    <td>
Statut de la transaction.
    </td>
 
   </tr>
   
  </table>
 
  </p>

  <p>

<u>Remarque</u> : les transactions annulées sont également présentes dans le tableau (information donnée dans le paramètre JSON trans_status).
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627133271.xml -->
<h2>
16.84. vads_payment_src
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir l’origine du paiement.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
60
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
EC
    </td>
 
    <td>
E-commerce : paiement réalisé depuis la page de paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
MOTO
    </td>
 
    <td>
MAIL OR TELEPHONE ORDER : paiement effectué par un opérateur suite à une commande par téléphone ou e-mail.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CC
    </td>
 
    <td>
Call center : paiement effectué via un centre d’appel.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
OTHER
    </td>
 
    <td>
Autre : paiement réalisé depuis une autre source comme le Back Office exemple.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627517688.xml -->
<h2>
16.85. vads_pays_ip
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>
Code pays de l’adresse IP de l’acheteur à la norme ISO 3166.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
a2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411642615770.xml -->
<h2>
16.86. vads_presentation_date
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
 

  <ul>
 
   <li>
Date de remise en banque demandée.
   <p>
ou
   </p>

   </li>
 
   <li>
Date de l&#x27;échéance demandée dans le cadre d&#x27;un prélèvement SEPA.
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n14
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411126075812.xml -->
<h2>
16.87. vads_product_amountN
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le montant des différents articles contenus dans le panier.
  <p>
N correspond à l&#x27;indice de l&#x27;article. (0 pour le premier, 1 pour le deuxième etc...)
  </p>

  <p>
Le montant sera exprimé dans l&#x27;unité la plus petite de la devise. Le centime pour l&#x27;euro.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
102
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411125732485.xml -->
<h2>
16.88. vads_product_labelN
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le libéllé de chacun des articles contenus dans le panier.
  <p>
N correspond à l&#x27;indice de l&#x27;article. (0 pour le premier, 1 pour le deuxième etc...)
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..255
  <p>

<u>
<i>
<b>Remarque : </b></i></u>
  </p>

  <p>

<i>Veillez à ne pas utiliser des caractères autres que alphabétiques et numériques (les espaces ne sont pas autorisés par exemple) et de respecter la RegEx 
<b>^[a-zA-Z0-9]{1,255}$</b> .</i>
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
97
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411126555396.xml -->
<h2>
16.89. vads_product_qtyN
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir la quantité de chacun des articles contenus dans le panier.
  <p>
N correspond à l&#x27;indice de l&#x27;article. (0 pour le premier, 1 pour le deuxième etc...)
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
101
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411126454471.xml -->
<h2>
16.90. vads_product_refN
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir une référence pour chacun des articles contenus dans le panier.
  <p>
N correspond à l&#x27;indice de l&#x27;article. (0 pour le premier, 1 pour le deuxième etc...)
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..64
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
100
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411126340153.xml -->
<h2>
16.91. vads_product_typeN
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le type de l&#x27;article contenu dans le panier.
  <p>
N correspond à l&#x27;indice de l&#x27;article. (0 pour le premier, 1 pour le deuxième etc...)
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
98
  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>

<b>Valeurs possibles</b>
  </p>
 
  </td>
 
  <td>
 
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
FOOD_AND_GROCERY
    </td>
 
    <td>
Produits alimentaires et d&#x27;épicerie
    </td>
 
   </tr>
 
   <tr>
 
    <td>
AUTOMOTIVE
    </td>
 
    <td>
Automobile / Moto
    </td>
 
   </tr>
 
   <tr>
 
    <td>
ENTERTAINMENT
    </td>
 
    <td>
Divertissement / Culture
    </td>
 
   </tr>
 
   <tr>
 
    <td>
HOME_AND_GARDEN
    </td>
 
    <td>
Maison et jardin
    </td>
 
   </tr>
 
   <tr>
 
    <td>
HOME_APPLIANCE
    </td>
 
    <td>
Equipement de la maison
    </td>
 
   </tr>
 
   <tr>
 
    <td>
AUCTION_AND_GROUP_BUYING
    </td>
 
    <td>
Ventes aux enchères et achats groupés
    </td>
 
   </tr>
 
   <tr>
 
    <td>
FLOWERS_AND_GIFTS|
    </td>
 
    <td>
Fleurs et cadeaux
    </td>
 
   </tr>
 
   <tr>
 
    <td>
COMPUTER_AND_SOFTWARE
    </td>
 
    <td>
Ordinateurs et logiciels
    </td>
 
   </tr>
 
   <tr>
 
    <td>
HEALTH_AND_BEAUTY
    </td>
 
    <td>
Santé et beauté
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SERVICE_FOR_INDIVIDUAL
    </td>
 
    <td>
Services à la personne
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SERVICE_FOR_BUSINESS
    </td>
 
    <td>
Services aux entreprises
    </td>
 
   </tr>
 
   <tr>
 
    <td>
SPORTS
    </td>
 
    <td>
Sports
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CLOTHING_AND_ACCESSORIES
    </td>
 
    <td>
Vêtements et accessoires
    </td>
 
   </tr>
 
   <tr>
 
    <td>
TRAVEL
    </td>
 
    <td>
Voyage
    </td>
 
   </tr>
 
   <tr>
 
    <td>
HOME_AUDIO_PHOTO_VIDEO
    </td>
 
    <td>
Son, image et vidéo
    </td>
 
   </tr>
 
   <tr>
 
    <td>
TELEPHONY
    </td>
 
    <td>
Téléphonie
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1433941223778.xml -->
<h2>
16.92. vads_product_vatN
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le montant de la taxe pour chacun des articles contenu dans le panier.
  <p>
N correspond à l&#x27;indice de l&#x27;article. (0 pour le premier, 1 pour le deuxième etc...)
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
 
  <p>
n..12 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
203
  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>

<b>Valeurs possibles</b>
  </p>
 
  </td>
 
  <td>
 

  <ul>
 
   <li>

<b>Un entier sans décimal</b> 
   <p>
Pour exprimer un montant en centime appliqué sur le produit concerné. 
   </p>

   <p>
Exemple en euros
   </p>

   </li>
 
  </ul>
 
  <p>
 

  <ul>
 
   <li>

<b>Un entier avec décimal inférieur à 100</b>
   <p>
Pour exprimer un pourcentage appliqué sur le montant du produit concerné avec maximum 4 chiffres après la virgule. 
   </p>

   <p>
Exemples : 20.0 ou 19.6532 
   </p>

   <p>

<i>
<u>Remarques : </u></i>

   <ul>
 
    <li>

<i>La décimale est obligatoire pour exprimer un pourcentage</i>.
    </li>
 
    <li>

<i>La décimale est marquée par le caractère &quot;
<b>.</b>&quot;</i>.
    </li>
 
   </ul>

   </p>

   </li>
 
  </ul>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1447863204383.xml -->
<h2>
16.93. vads_recurrence_number
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>
Numéro de l&#x27;échéance de l&#x27;abonnement.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411481506331.xml -->
<h2>
16.94. vads_recurrence_status
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Statut de l&#x27;abonnement.
  </p>
 
  <p>
Présent uniquement si l’action demandée correspond à la création d&#x27;un abonnement (REGISTER_SUBSCRIBE, SUBSCRIBE, REGISTER_PAY_SUBSCRIBE).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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

<b>CREATED</b>
    </td>
 
    <td>

    <p>
L’abonnement a été créé avec succès.
    </p>
Le détail de l’abonnement est visible dans le Back Office. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>NOT_CREATED</b>
    </td>
 
    <td>
L’abonnement n’a pas été créé et n’est pas visible dans le Back Office.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>ABANDONED</b>
    </td>
 
    <td>

    <p>
La demande de création de l’abonnement a été abandonnée par l’acheteur (débiteur). 
    </p>
L’abonnement n’a pas été créé et n’est pas visible dans le Back Office. 
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627821400.xml -->
<h2>
16.95. vads_redirect_error_message
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de spécifier le message en cas de paiement refusé dans le cas d’une redirection automatique vers le site marchand.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
37
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627821400.xml -->
<h2>
16.96. vads_redirect_error_message
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de spécifier le message en cas de paiement refusé dans le cas d’une redirection automatique vers le site marchand.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
37
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627924375.xml -->
<h2>
16.97. vads_redirect_error_timeout
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir un délai en secondes avant redirection automatique vers le site marchand à la fin d’un paiement refusé. 
  <p>
Sa valeur est comprise entre 
<b>0</b> et 
<b>600</b>s. 
  </p>

  <p>
Passé ce délai, l&#x27;acheteur sera dirigé vers l&#x27;URL renseignée dans le champ 
<b>
<b>vads_url_refusal</b></b>. Si ce champ n&#x27;est pas renseigné, l&#x27;acheteur sera redirigé sur l&#x27;URL de retour renseignée dans le champ 
<b>vads_url_return</b> ou sur l’URL de retour renseignée dans le Back Office. Si l&#x27;URL de retour n&#x27;est pas définie, il sera redirigé sur vers l’URL de la boutique.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
36
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408627992082.xml -->
<h2>
16.98. vads_redirect_success_message
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de spécifier le message à la fin d’un paiement accepté dans le cas d’une redirection automatique vers le site marchand.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
35
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408628074901.xml -->
<h2>
16.99. vads_redirect_success_timeout
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir un délai en secondes avant redirection automatique vers le site marchand à la fin d’un paiement accepté. 
  <p>
Sa valeur est comprise entre 0 et 600s.
  </p>
Passé ce délai, l&#x27;acheteur sera dirigé vers l&#x27;URL renseignée dans le champ 
<b>
<b>vads_url_success</b></b>. Si ce champ n&#x27;est pas renseigné, l&#x27;acheteur sera redirigé sur l&#x27;URL de retour renseignée dans le champ 
<b>vads_url_return</b> ou sur l’URL de retour renseignée dans le Back Office. Si l&#x27;URL de retour n&#x27;est pas définie, il sera redirigé sur vers l’URL de la boutique.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
34
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408628157713.xml -->
<h2>
16.100. vads_result
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Code retour de l&#x27;action demandée.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
00
    </td>
 
    <td>
Action réalisée avec succès.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
02
    </td>
 
    <td>
Le marchand doit contacter la banque du porteur. Déprécié.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
05
    </td>
 
    <td>
Action refusée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
17
    </td>
 
    <td>
Annulation de l&#x27;acheteur
    </td>
 
   </tr>
 
   <tr>
 
    <td>
30
    </td>
 
    <td>
Erreur de format de la requête. A mettre en rapport avec la valorisation du champ vads_extra_result.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
96
    </td>
 
    <td>
Erreur technique.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1406116003851.xml -->
<h2>
16.101. vads_return_mode
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de spécifier la méthode de transmission des données utilisée lors du retour vers le site marchand.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
48
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  <table>
      
   <tr>
 
    <td>
Nom du champ
    </td>
 
    <td>
Valeur
    </td>
 
    <td>
Description
    </td>
 
   </tr>
   
   <tr>
 
    <td>
vads_return_mode
    </td>
 
    <td>
absent, vide ou 
<b>NONE</b>
    </td>
 
    <td>
Aucun paramètre ne sera passé à l’URL de retour vers le site marchand.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>GET</b>
    </td>
 
    <td>
Les champs de retour seront transmis à l’URL de retour sous la forme d’un formulaire HTTP GET (dans la « query string »).
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>POST</b>
    </td>
 
    <td>

    <p>
Les champs de retour seront transmis à l’URL de retour sous la forme d’un formulaire HTTP POST.
    </p>
Si le retour boutique se fait sur un environnement
<b> non https </b>alors le navigateur affichera un pop-up de sécurité à l’acheteur.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1413811527238.xml -->
<h2>
16.102. vads_risk_analyzis_result
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Retourne le résultat de l&#x27;analyse de fraude effectuée par un système externe (ClearSale, CyberSource,...).
  </p>

  <p>
Renvoyé dans l&#x27;URL de notification instantanée (également appelée IPN) et dans les paramètres de retour.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>
 
  <table>
      
   <tr>
 
    <td>
Valeurs communes à tous les analyseurs de risques
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>INVALID_CREDENCIAL</b>
    </td>
 
    <td>
Problème de paramétrage du contrat d’analyse de risques.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>COMUNICATION_PROBLEM</b>
    </td>
 
    <td>
Impossible de communiquer avec l’analyseur de risques.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>DATA_PROCESSING_PROBLEM</b>
    </td>
 
    <td>
Problème lors du traitement de l’envoi ou de la réponse d’analyse de risques.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MISSING_MANDATORY_ORDER_INFO</b>
    </td>
 
    <td>
 
    <p>
Des données relatives à la commande sont manquantes.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MISSING_MANDATORY_SHIPPING_INFO </b>
    </td>
 
    <td>
 
    <p>
Des données relatives à la livraison sont manquantes.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MISSING_MANDATORY_SHIPPING_ADDRESS_INFO</b>
    </td>
 
    <td>
 
    <p>
Des données relatives à l’adresse de livraison sont manquantes.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MISSING_MANDATORY_BILLING_INFO</b>
    </td>
 
    <td>
Des données relatives à la facturation sont manquantes. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
 
    <p>

<b>MISSING_MANDATORY_BILLING_ADDRESS_INFO</b>
    </p>
 
    </td>
 
    <td>
Des données relatives à l’adresse de facturation sont manquantes
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MISSING_MANDATORY_CARD_INFO</b>
    </td>
 
    <td>
 
    <p>
Des données concernant le moyen de paiement sont manquantes.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MISSING_MANDATORY_CUSTOMER_INFO</b>
    </td>
 
    <td>
 
    <p>
Des données concernant l’acheteur sont manquantes.
    </p>
 
    </td>
 
   </tr>
   
  </table>
 
  <table>
       
   <tr>
 
    <td>
ClearSale
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>APA</b>
    </td>
 
    <td>

<b>Automatically approved</b>
    </td>
 
    <td>
La transaction est automatiquement approuvée selon les paramètres définis.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>APM</b>
    </td>
 
    <td>

<b>Manually approved - order manually approved by analyst&#x27;s decision</b>
    </td>
 
    <td>
La transaction est manuellement approuvée par un analyste. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>RPM</b>
    </td>
 
    <td>

<b>Reproved with no suspect</b>
    </td>
 
    <td>
La commande est refusée en raison du manque d&#x27;informations sur l&#x27;acheteur en accord avec la politique appliquée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>AMA</b>
    </td>
 
    <td>

<b>Waiting for manual analysis - order is in a queue waiting for analysis</b>
    </td>
 
    <td>
En attente d&#x27;analyse manuelle. La commande est dans une file d&#x27;attente pour analyse.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>ERR</b>
    </td>
 
    <td>

<b>Error</b>
    </td>
 
    <td>
Erreur
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>NVO</b>
    </td>
 
    <td>

<b>New order - order waiting for score</b>
    </td>
 
    <td>
Nouvelle commande. En attente de traitement et de classification.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>SUS</b>
    </td>
 
    <td>

<b>Suspended order - order suspended by fraud suspicion</b>
    </td>
 
    <td>
Commande suspendue manuellement. La commande est suspendue pour suspicion de fraude.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CAN</b>
    </td>
 
    <td>
 
    <p>

<b>Canceled - order canceled by user</b>
    </p>
 
    </td>
 
    <td>
Commande annulée. La commande est annulée par l&#x27;acheteur.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>FRD</b>
    </td>
 
    <td>

<b>Order confirmed as a fraud</b>
    </td>
 
    <td>
Fraude confirmée avec l&#x27;opérateur de la carte de crédit ou du titulaire de la carte.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>RPA</b>
    </td>
 
    <td>

<b>Automatically reproved based on parameters within risk analyzer</b>
    </td>
 
    <td>
Commande refusée automatiquement. La commande est refusée en application des paramètres de l&#x27;analyseur de fraude externe. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>RPP</b>
    </td>
 
    <td>

<b>Automatically reproved based customer or ClearSale policy</b>
    </td>
 
    <td>
Commande refusée automatiquement. La commande est refusée en application de la politique client ou ClearSale.
    </td>
 
   </tr>
   
  </table>
 
  <table>
       
   <tr>
 
    <td>
CyberSource
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>100</b>
    </td>
 
    <td>

<b>SUCCESS</b>
    </td>
 
    <td>
La transaction s&#x27;est effectuée avec succès.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>101</b>
    </td>
 
    <td>

<b>MISSING_FIELDS</b>
    </td>
 
    <td>
La transaction est refusée. Un ou plusieurs champs sont manquants. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>102</b>
    </td>
 
    <td>

<b>INVALID_FIELDS</b>
    </td>
 
    <td>
La transaction est refusée. Un ou plusieurs champs contient des données invalides.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>150</b>
    </td>
 
    <td>

<b>ERROR_GENERAL_SYSTEM_FAILURE</b>
    </td>
 
    <td>
Erreur.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>151</b>
    </td>
 
    <td>

<b>SERVER_TIME_OUT</b>
    </td>
 
    <td>
Erreur. La requête a été reçue mais le délai a été dépassé. Cette erreur n&#x27;inclue pas les dépassements de délais entre le client et le serveur. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>152</b>
    </td>
 
    <td>

<b>SERVICE_TIME_OUT</b>
    </td>
 
    <td>
Erreur. La requête a été reçue mais un service n&#x27;a pas terminé à temps.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>202</b>
    </td>
 
    <td>

<b>CARD_EXPIRED</b>
    </td>
 
    <td>
Refusée. Carte expirée. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>231</b>
    </td>
 
    <td>
 
    <p>

<b>ACCOUNT_NUMBER_INVALID</b>
    </p>
 
    </td>
 
    <td>
Refusée. Numéro de compte invalide.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>234</b>
    </td>
 
    <td>

<b>ACCOUNT_PROBLEM</b>
    </td>
 
    <td>
Refusé. Un problème est survenu avec la configuration CyberSource du marchand.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>400</b>
    </td>
 
    <td>

<b>FRAUD_SCORE_TOO_HIGH</b>
    </td>
 
    <td>
Refusée. Le score de la fraude dépasse le seuil de tolérance.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>480</b>
    </td>
 
    <td>

<b>SUCCESS_TO_REVIEW</b>
    </td>
 
    <td>
La commande est marquée afin d&#x27;être examinée par le Decision Manager.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>481</b>
    </td>
 
    <td>

<b>SUCCESS_TO_REJECT</b>
    </td>
 
    <td>
La commande a été rejetée par le Decision Manager.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1436276953870.xml -->
<h2>
16.103. vads_risk_assessment_result
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Retourne le résultat de l&#x27;analyse de gestion des risques avancée effectuée par la plateforme de paiement.
  </p>

  <p>
Renvoyé dans l&#x27;URL de notification instantanée (également appelée IPN) et dans les paramètres de retour.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>
 
  <p>
 
  <table>
      
   <tr>
 
    <td>
Valeurs
    </td>
 
    <td>
Description
    </td>
 
   </tr>
   
   <tr>
 
    <td>
ENABLE_3DS
    </td>
 
    <td>
3D Secure activé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
DISABLE_3DS
    </td>
 
    <td>
3D Secure désactivé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
MANUAL_VALIDATION
    </td>
 
    <td>
La transaction est créée en validation manuelle.
    <p>
La remise du paiement est bloquée temporairement pour permettre au marchand de procéder à toutes les vérifications souhaitées.
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
REFUSE
    </td>
 
    <td>
La transaction est refusée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
RUN_RISK_ANALYSIS
    </td>
 
    <td>
Appel à un analyseur de risques externes sous condition que le marchand possède un contrat.
    <p>
Se référer à la description du champ 
<b>vads_risk_analysis_result</b> pour identifier la liste des valeurs possibles et leur description.
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>
INFORM
    </td>
 
    <td>
Une alerte est remontée. 
    <p>
Le marchand est averti qu’un risque est identifié.
    </p>

    <p>
Le marchand est informé via une ou plusieurs des règles du centre de notification (URL de notification, e-mail ou SMS).
    </p>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1409751437465.xml -->
<h2>
16.104. vads_risk_control
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Permet de définir le résultat du contrôle des risques.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
contrôle1=resultat1;contrôle2=resultat2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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

<b>CARD_FRAUD </b>
    </td>
 
    <td>
Contrôle la présence du numéro de carte de l&#x27;acheteur dans la liste grise de cartes.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>SUSPECT_COUNTRY</b>
    </td>
 
    <td>
Contrôle la présence du pays émetteur de la carte de l&#x27;acheteur dans la liste de pays interdits.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>IP_FRAUD</b> 
    </td>
 
    <td>
Contrôle la présence de l&#x27;adresse IP de l&#x27;acheteur dans la liste grise d&#x27;IP.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CREDIT_LIMIT </b>
    </td>
 
    <td>
Contrôle la fréquence et les montants d&#x27;achat d&#x27;un même numéro de carte, ou le montant maximum d&#x27;une commande.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>BIN_FRAUD</b>
    </td>
 
    <td>
Contrôle la présence du code BIN de la carte de l&#x27;acheteur dans la liste grise de codes BIN.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>ECB</b>
    </td>
 
    <td>
Contrôle si la carte de l&#x27;acheteur est de type e-carte bleue.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CARD_COMMERCIAL </b>
    </td>
 
    <td>
Contrôle si la carte de l&#x27;acheteur est une carte commerciale.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>SYSTEMATIC_AUTO</b>
    </td>
 
    <td>
Contrôle si la carte de l&#x27;acheteur est une carte à autorisation systématique.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>INCONSISTENT_COUNTRIES</b>
    </td>
 
    <td>
Contrôle si le pays de l&#x27;adresse IP, le pays émétteur de la carte de paiement, et le pays de l&#x27;adresse de l&#x27;acheteur sont cohérents entre eux.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>NON_WARRANTY_PAYMENT</b>
    </td>
 
    <td>
Contrôle le transfert de responsabilité de la transaction.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>SUSPECT_IP_COUNTRY</b>
    </td>
 
    <td>
Contrôle la présence du pays de l&#x27;acheteur, identifié par son adresse IP, dans la liste de pays interdits.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
Les différentes valeurs possibles pour ‘
<b>résultat’</b> sont :
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

<b>OK</b>
    </td>
 
    <td>
OK
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>WARNING</b>
    </td>
 
    <td>
Contrôle informatif échoué
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>ERROR</b>
    </td>
 
    <td>
Contrôle bloquant échoué
    </td>
 
   </tr>
   
  </table>

  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1416242779600.xml -->
<h2>
16.105. vads_risk_primary_warranty
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Spécifique au don (ou transaction secondaire).
  <p>

  </p>

  <p>
Permet de surcharger la configuration du contrôle de risque 
<b>Contrôle du transfert de responsabilité de la transaction primaire</b>. 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
117
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

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
DEFAULT ou vide
    </td>
 
    <td>
Valeur par défaut. Utilisation de la configuration de la boutique cible.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
IGNORE
    </td>
 
    <td>
Ignore la valeur du transfert de responsabilité de la transaction primaire avant de créer la transaction secondaire.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
CHECK
    </td>
 
    <td>
Force le contrôle du transfert de responsabilité de la transaction primaire avant de créer la transaction secondaire.
    </td>
 
   </tr>
   
  </table>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Information sur les transactions de don
  </td>
 
 </tr>
   
</table>
 <!-- tla1408631717602.xml -->
<h2>
16.106. vads_sequence_number
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Champ retourné dans la réponse.
  </p>

  <p>
Contient le numéro de séquence de la transaction.
  </p>

  <p>
Ce champ est toujours valorisé à 1 dans le cas d’un paiement comptant (vads_payment_config=SINGLE).
  </p>
Pour un paiement en plusieurs fois, ce champ prendra la valeur 1 pour la première échéance, la valeur 2 pour deuxième échéance, la valeur 3 pour la troisième échéance etc.
  <p>

  </p>

  <p>

<i>
<b>Remarque :</b></i>
  </p>

  <p>

<i>Le champ 
<b>vads_sequence_number</b> n&#x27;est pas retourné dans la réponse lorsqu&#x27;un paiement est annulé ou abandonné.</i>
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408631826813.xml -->
<h2>
16.107. vads_ship_to_city
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir la ville de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..128
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
83
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408632458704.xml -->
<h2>
16.108. vads_ship_to_country
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le code pays de l’acheteur à la norme ISO 3166.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
a2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
86
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemples de valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  <table>
   
   <tr>
 
    <td>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408632679858.xml -->
<h2>
16.109. vads_ship_to_delivery_company_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le nom du transporteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
96
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408632864028.xml -->
<h2>
16.110. vads_ship_to_district
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le quartier.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
115
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408634336065.xml -->
<h2>
16.111. vads_ship_to_first_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le prénom de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
106
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408634522824.xml -->
<h2>
16.112. vads_ship_to_last_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le nom de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
107
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1423827002789.xml -->
<h2>
16.113. vads_ship_to_legal_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Raison sociale de lieu de livraison.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..100
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
125
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1423827002789.xml -->
<h2>
16.114. vads_ship_to_legal_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Raison sociale de lieu de livraison.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..100
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
125
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408634587110.xml -->
<h2>
16.115. vads_ship_to_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le nom de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
80
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408634698739.xml -->
<h2>
16.116. vads_ship_to_phone_num
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le numéro de téléphone de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..32
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
87
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408634757367.xml -->
<h2>
16.117. vads_ship_to_speed
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le mode de livraison.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
95
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

<b>STANDARD</b>, 
<b>EXPRESS</b>
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408634859538.xml -->
<h2>
16.118. vads_ship_to_status
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le type d&#x27;adresse de livraison.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
93
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>

<b>PRIVATE</b>, 
<b>COMPANY</b>
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635009448.xml -->
<h2>
16.119. vads_ship_to_state
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir l&#x27;état de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
84
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635091649.xml -->
<h2>
16.120. vads_ship_to_street
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir l&#x27;adresse de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
81
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635091649.xml -->
<h2>
16.121. vads_ship_to_street
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir l&#x27;adresse de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
81
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635139472.xml -->
<h2>
16.122. vads_ship_to_street2
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir la deuxième ligne d&#x27;adresse de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
82
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635487312.xml -->
<h2>
16.123. vads_ship_to_street_number
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le numéro de rue.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..5
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
114
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635578322.xml -->
<h2>
16.124. vads_ship_to_type
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le type de livraison.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
94
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 

  <ul>
 
   <li>

<b>RECLAIM_IN_SHOP</b> pour le retrait de la marchandise en magasin.
   </li>
 
   <li>

<b>RELAY_POINT</b> pour l&#x27;utilisation d&#x27;un réseau de points de retrait tiers (Kiala, Alveol, etc).
   </li>
 
   <li>

<b>RECLAIM_IN_STATION</b> pour le retrait dans un aéroport, une garde ou une agence de voyage.
   </li>
 
   <li>

<b>PACKAGE_DELIVERY_COMPANY</b> pour la livraison par transporteur (Colissimo, UPS, etc).
   </li>
 
   <li>

<b>ETICKET</b> pour l&#x27;émission d&#x27;un billet électronique, téléchargement.
   </li>
 
  </ul>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635663652.xml -->
<h2>
16.125. vads_ship_to_user_info
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Information sur l’utilisateur à l’origine du paiement.
  <p>

  </p>

  <p>
Ce paramètre sera renvoyé dans la réponse avec la valeur transmise dans la requête.
  </p>

  <p>

<b>
<i>Remarque :</i></b> 
  </p>

  <p>

<i>Pour des raisons de rétrocompatibilité, il est possible d&#x27;utiliser ce champ pour valoriser le CPF/CNPJ (Identifiant légal, au format numérique, de longueur comprise entre 11 et 20 digits) imposé par le module de gestion de fraude ClearSale. Cependant, le CPF/CNPJ peut être valorisé dans le champ 
<b>vads_cust_national_id</b>.</i>
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
116
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635725582.xml -->
<h2>
16.126. vads_ship_to_zip
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le code postal de l&#x27;acheteur.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
an..64
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
85
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la livraison.
  </td>
 
 </tr>
   
</table>
 <!-- tla1412321271132.xml -->
<h2>
16.127. vads_shipping_amount
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Permet de définir le montant des frais de livraison pour l’ensemble de la commande.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
109
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635796483.xml -->
<h2>
16.128. vads_shop_name
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Permet de définir le nom de la boutique qui apparait dans les e-mails de confirmation de paiement.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
72
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Personnalisation de la page de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408635865701.xml -->
<h2>
16.129. vads_shop_url
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
URL de la boutique qui apparait sur la page de paiement et les e-mails de confirmation de paiement.
  <p>
Ce paramètre permet de surcharger la valeur par défaut de votre boutique.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
73
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Personnalisation de la page de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408636137772.xml -->
<h2>
16.130. vads_site_id
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Paramètre obligatoire.
  </p>

  <p>
Valeur générée lors de l&#x27;inscription à la plateforme de paiement.
  </p>
Sa valeur est consultable sur l’interface du Back Office dans le menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; 
<b>Certificats</b> par toutes les personnes habilitées.
  <p>

  </p>

  <p>
Dans le cas d&#x27;une valeur incorrecte, lors du paiement, l&#x27;acheteur obtient un message d&#x27;erreur sur son navigateur.
  </p>

  <p>
Le paiement est alors impossible et la transaction est définitivement interrompue.
  </p>

  <p>
Un e-mail d&#x27;alerte est alors envoyé au contact administratif de la boutique. Il contient le formulaire que la plateforme n&#x27;a pas pu traiter avec la valeur de la signature. 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n8
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
02
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411025356421.xml -->
<h2>
16.131. vads_subscription
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre facultatif utilisé dans le cas de la création d&#x27;un abonnement. Il désigne l&#x27;identifiant de l&#x27;abonnement à créer.
  <p>
Deux options sont possibles : 
  </p>

  <p>
 

  <ul>
 
   <li>
Soit la gestion de ces identifiants est déléguée à la plateforme.
   <p>
Dans ce cas, ce paramètre ne doit pas être renseigné.
   </p>

   <p>
En cas de succès de la création de l’abonnement, la réponse contiendra la valeur générée par la plateforme. 
   </p>

   </li>
 
   <li>
 
   <p>
Soit la gestion de ces identifiants est faite par le site marchand.
   </p>
 
   <p>
Dans ce cas, ce paramètre doit être renseigné avec la valeur de l’identifiant d’abonnement souhaité. 
<b>Attention, il incombe au site marchand de s’assurer de l’unicité des identifiants d’abonnement</b>. Toute demande de souscription à un abonnement contenant un identifiant d’abonnement déjà existant, sera rejetée, et provoquera l’affichage d’un message d’erreur.
   </p>
 
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..50
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
63
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411026103849.xml -->
<h2>
16.132. vads_sub_amount
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre obligatoire utilisé dans le cas de la création d&#x27;un abonnement. 
  <p>
Il fait référence au montant des échéances de l’abonnement pour toutes les échéances, hormis celles éventuellement définies par 
<b>vads_sub_init_amount_number</b>.
  </p>

  <p>
La valeur doit être exprimée dans la plus petite unité monétaire (le centime pour l&#x27;Euro).
  </p>

  <p>
Exemple : pour un montant de 10 euros et 28 centimes, la valeur du paramètre est 1028.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
65
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411026347617.xml -->
<h2>
16.133. vads_sub_currency
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre obligatoire utilisé dans le cas de la création d&#x27;un abonnement. 
  <p>
Il indique la monnaie à utiliser pour l’abonnement, selon la norme ISO 4217. 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Exemples de valeurs possibles</b>
  </td>
 
  <td>
Les devises possibles sont les suivantes :
  <p>
 
  <table>
   
   <tr>
 
    <td>

    </td>
 
   </tr>
   
  </table>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
67
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411026999130.xml -->
<h2>
16.134. vads_sub_desc
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre obligatoire utilisé dans le cas de la création d&#x27;un abonnement. 
  <p>
Il définit la règle de l’abonnement à appliquer.
  </p>

  <p>
La valeur attendue dans ce paramètre est une chaîne de caractères suivant la spécification 
<b>iCalendar</b>, ou Internet Calendar, décrite dans la RFC5545 (voir http://tools.ietf.org/html/rfc5545).
  </p>

  <p>
Cette spécification permet entre autre de définir des règles complexes d’abonnement, via la propriété 
<b>RRULE</b>. 
  </p>

  <p>
Pour des raisons techniques, il n’est pas possible de définir des périodes d’abonnement inférieures à une journée. 
  </p>

  <p>
Les mots clés &quot;SECONDLY&quot; / &quot;MINUTELY&quot; / &quot;HOURLY&quot; ne sont donc pas pris en compte. 
  </p>

  <p>

  </p>

  <p>
Exemples : 

  <ul>
 
   <li>
 
   <p>
Pour définir des échéances de paiement ayant lieu le dernier jour de chaque mois, pendant 12 mois, la règle s’écrit : 
   </p>
 
   <p>

<b>RRULE:FREQ=MONTHLY;BYMONTHDAY=28,29,30,31;BYSETPOS=-1;COUNT=12</b> 
   </p>
 
   <p>
Cette règle signifie que si le mois courant ne contient pas de 31, alors le moteur prendra en compte le 30. Si le 30 n’existe pas, alors il prendra en compte le 29 et ainsi de suite jusqu’au 28.
   </p>
 
   <p>
Une autre version de cette règle : 
<b>RRULE:FREQ=MONTHLY;COUNT=5;BYMONTHDAY=-1</b>
   </p>
 
   <p>

   </p>
 
   </li>
 
   <li>
Pour définir des échéances de paiement ayant lieu le 10 de chaque mois, pendant 12 mois, alors la règle d’abonnement s’écrit de la manière suivante : 
<b>RRULE:FREQ=MONTHLY;COUNT=12;BYMONTHDAY=10</b> 
   <p>

   </p>

   </li>
 
   <li>
Pour définir des échéances de paiement ayant lieu chaque trimestre, jusqu’au 31/12/2016 : 
<b>RRULE:FREQ=YEARLY;BYMONTHDAY=1;BYMONTH=1,4,7,10;UNTIL=20161231</b> 
   <p>
Les échéances auront lieu chaque 1er de janvier, avril, juillet et octobre. Leur nombre total dépend de la date d’effet de l’abonnement (voir paramètre 
<b><a href="#TODO-tla1411025901698.xml">vads_sub_effect_date</a></b>). 
   </p>

   <p>

   </p>

   <p>
Pour plus de détails et d&#x27;exemples vous pouvez consulter le site <a href="#TODO-http://recurrance.sourceforge.net/">http://recurrance.sourceforge.net/</a>.
   </p>

   </li>
 
  </ul>

  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
64
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411025901698.xml -->
<h2>
16.135. vads_sub_effect_date
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre obligatoire utilisé dans la création d&#x27;un abonnement qui permet de définir une date d&#x27;effet de l&#x27;abonnement.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n8
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
69
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411026602462.xml -->
<h2>
16.136. vads_sub_init_amount
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre facultatif utilisé lors de la création d&#x27;un abonnement. Représente le montant des échéances de l’abonnement pour les 
<u>premières échéances</u>. 
  <p>
Le nombre de ces premières échéances est défini par le paramètre 
<b><a href="#TODO-tla1411026836617.xml">vads_sub_init_amount_number</a></b>. 
  </p>

  <p>
Ce montant est exprimé dans la devise définie par le paramètre 
<b><a href="#TODO-tla1411026347617.xml">vads_sub_currency</a></b> et est 
<u>exprimé en son unité indivisible</u> (le centime pour l&#x27;Euro).
  </p>

  <p>
Exemple : pour un montant de 10 euros et 28 centimes, la valeur du paramètre est 1028.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
66
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1411026836617.xml -->
<h2>
16.137. vads_sub_init_amount_number
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre facultatif utilisé dans le cas de la création d&#x27;un abonnement. Représente le nombre d’échéances auxquelles il faudra appliquer le montant 
<b>vads_sub_init_amount</b>. 
  <p>
Une fois ce nombre d’échéances dépassé, c’est le montant 
<b>vads_sub_amount</b> qui sera utilisé.
  </p>

  <p>

<b>Exemple</b> : pour définir un abonnement dont les 3 premières échéances sont à 25 euros
  </p>

  <p>
 

  <ul>
 
   <li>
vads_sub_currency = 978
   </li>
 
   <li>
vads_sub_init_amount_number = 3 
   </li>
 
   <li>
vads_sub_init_amount = 2500 
   </li>
 
   <li>
vads_sub_amount = 3000
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..3
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
68
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;abonnement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1412321592265.xml -->
<h2>
16.138. vads_tax_amount
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre qui permet de définir le montant des taxes pour l’ensemble de la commande.
  <p>
La valeur doit être exprimée dans la plus petite unité monétaire (le centime pour l&#x27;Euro).
  </p>

  <p>
Spécifique au moyen de paiement PayPal.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..12
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
108
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la commande.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408636286614.xml -->
<h2>
16.139. vads_theme_config
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Permet de personnaliser certains éléments de la page de paiement : logos, bandeaux et certains messages (Certaines fonctionnalités sont 
<b>soumises à option commerciale</b>). 
  </p>

  <p>
Ce paramètre contient une liste de mots-clés (codes) associés à des éléments des pages de paiement (libellés, images), auxquels on associe une valeur. 
  </p>

  <p>

  </p>

  <p>

<u>Exemple</u>:
  </p>

  <p>
vads_theme_config=
  </p>

  <p>
SUCCESS_FOOTER_MSG_RETURN=Retour au site;CANCEL_FOOTER_MSG_RETURN=Annuler et retourner au site
  </p>

  <p>

  </p>
Les fonctionnalités de base sont décrites au chapitre 
<b>Personnaliser la page de paiement</b> du 
<b>Guide d&#x27;implémentation du formulaire de paiement</b>.
  <p>
Les fonctionnalités avancées (soumises à option) sont décrites dans le guide 
<b>Personnalisation avancée de la page de paiement</b>. 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
Code1=Valeur1;Code2=Valeur2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
32
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
  <p>
 
  <table>
     
   <tr>
 
    <td>
Code
    </td>
 
    <td>
Description
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>SUCCESS_FOOTER_MSG_RETURN</b>
    </td>
 
    <td>
Libellé remplaçant « Retour à la boutique » lors d’un paiement réalisé avec succès.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CANCEL_FOOTER_MSG_RETURN</b>
    </td>
 
    <td>
Libellé remplaçant « Annuler et retourner à la boutique » pendant les phases de sélection puis de saisie de carte, et en cas d’échec du paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>SECURE_ MESSAGE</b>
    </td>
 
    <td>
 
    <p>
Valeur par défaut : 
<i>L&#x27;adresse de ce site de paiement préfixée par https indique que vous êtes sur un site sécurisé et que vous pouvez régler votre achat en toute tranquillité</i>.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>SECURE_MESSAGE_REGISTER</b>
    </td>
 
    <td>
 
    <p>
Valeur par défaut : 
<i>L&#x27;adresse de ce site de paiement préfixée par https indique que vous êtes sur un site sécurisé et que vous pouvez renseigner vos coordonnées bancaires en toute tranquillité</i>
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>SITE_ID_LABEL</b>
    </td>
 
    <td>
 
    <p>
Valeur par défaut : 
<i>Identifiant du marchand</i>
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CSS_FOR_PAYMENT</b>
    <p>

<b>CSS_FOR_PAYMENT_MOBILE</b>
    </p>

    <p>

<b>HEADER_FOR_MAIL</b>
    </p>

    <p>

<b>FOOTER_FOR_MAIL</b>
    </p>

    <p>

<b>SHOP_LOGO</b>
    </p>

    </td>
 
    <td>
Voir guide 
<b>Personnalisation avancée de la page de paiement</b>.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CTRL_RISK_CARD_NOT_ACCEPTED</b>
    </td>
 
    <td>
Valeur par défaut : 
<i>Votre demande de paiement a été refusée par votre établissement bancaire.</i>
    <p>
Ce message est conditionné par le retour du service de contrôle de risque.
    </p>

    <p>
Le contrat doit supporter tous les types de cartes incluses dans le contrat, et non le sous-ensemble que le marchand veut accepter.
    </p>

    <p>
Permet de surcharger le libellé de refus lorsqu&#x27;une e-carte bleue est utilisée alors qu&#x27;elle n&#x27;est pas acceptée dans le contrôle de risque.
    </p>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Personnalisation de la page de paiement.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408636944655.xml -->
<h2>
16.140. vads_threeds_cavv
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Désigne la vérification de l’authentification du porteur par l’ACS. Il est valorisé par le serveur d’authentification 3DS (ACS) lorsque l’acheteur s’est correctement authentifié (vads_threeds_status vaut « Y » ou « A »).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..28
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
52
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408637038608.xml -->
<h2>
16.141. vads_threeds_cavvAlgorithm
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Algorithme utilisé par l’ACS pour générer la valeur du cavv.
  </p>
 
  <p>
Il est valorisé par le serveur d’authentification 3DS (ACS) lorsque l’acheteur s’est correctement authentifié (vads_threeds_status vaut « Y » ou « A »).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n1
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
55
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
0
    </td>
 
    <td>
HMAC
    </td>
 
   </tr>
 
   <tr>
 
    <td>
1
    </td>
 
    <td>
CVV
    </td>
 
   </tr>
 
   <tr>
 
    <td>
2
    </td>
 
    <td>
CVV_ATN
    </td>
 
   </tr>
 
   <tr>
 
    <td>
3
    </td>
 
    <td>
MasterCard SPA
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408637200153.xml -->
<h2>
16.142. vads_threeds_eci
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Désigne l’Indicateur de Commerce Electronique.
  </p>
Il est valorisé par le serveur d’authentification 3DS (ACS) lorsque l’acheteur s’est correctement authentifié (vads_threeds_status vaut « Y » ou « A »).
  <p>
 
  <table>
        
   <tr>
 
    <td>

    </td>
 
    <td>

<b>status</b> = 
<b>Y</b> 
    </td>
 
    <td>

<b>status</b> = 
<b>A</b> 
    </td>
 
    <td>

<b>status</b> = 
<b>U</b> 
    </td>
 
    <td>

<b>status</b> = 
<b>N</b> 
    </td>
 
   </tr>
   
   <tr>
 
    <td>

<b>VISA</b>
    </td>
 
    <td>
 5
    </td>
 
    <td>
6
    </td>
 
    <td>
7
    </td>
 
    <td>
-
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MasterCard</b>
    </td>
 
    <td>
 02
    </td>
 
    <td>
01
    </td>
 
    <td>
-
    </td>
 
    <td>
-
    </td>
 
   </tr>
   
  </table>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
53
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408637262343.xml -->
<h2>
16.143. vads_threeds_enrolled
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Désigne le statut de l’enrôlement du porteur. Il est valorisé par les serveurs VISA et MASTERCARD (DS) durant le processus 3D Secure.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
a1
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
51
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
Y
    </td>
 
    <td>
Porteur enrôlé, authentification 3DS possible.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
N
    </td>
 
    <td>
Porteur non enrôlé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
U
    </td>
 
    <td>
Impossible de vérifier le statut d’enrôlement.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408637376020.xml -->
<h2>
16.144. vads_threeds_exit_status
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Statut final du processus 3D Secure.
  </p>

  <p>
Il est valorisé par la plateforme de paiement.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n..2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
0
    </td>
 
    <td>
Statut initial
    </td>
 
   </tr>
 
   <tr>
 
    <td>
1
    </td>
 
    <td>
Statut non applicable (global, raison non détaillée)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
2
    </td>
 
    <td>
Statut non applicable (integrator disabled)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
3
    </td>
 
    <td>
Paiement non e-commerce
    </td>
 
   </tr>
 
   <tr>
 
    <td>
4
    </td>
 
    <td>
Paiement sans 3DS (paiement par alias, PayPal, Cetelem, etc.)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
5
    </td>
 
    <td>
Marchand non enrôlé, pas de 3DS
    </td>
 
   </tr>
 
   <tr>
 
    <td>
6
    </td>
 
    <td>
Erreur technique lors du processus 3DS, pas de 3DS
    </td>
 
   </tr>
 
   <tr>
 
    <td>
7
    </td>
 
    <td>

<b>Porteur non enrôlé, pas de 3DS</b>
    </td>
 
   </tr>
 
   <tr>
 
    <td>
8
    </td>
 
    <td>
Signature invalide
    </td>
 
   </tr>
 
   <tr>
 
    <td>
9
    </td>
 
    <td>
Problème venant de l&#x27;ACS
    </td>
 
   </tr>
 
   <tr>
 
    <td>
10
    </td>
 
    <td>

<b>Le processus 3DS s&#x27;est déroulé correctement</b>
    </td>
 
   </tr>
 
   <tr>
 
    <td>
11
    </td>
 
    <td>
Le processus 3DS a été fait par l&#x27;intégrateur
    </td>
 
   </tr>
 
   <tr>
 
    <td>
12
    </td>
 
    <td>
Problème venant du DS
    </td>
 
   </tr>
 
   <tr>
 
    <td>
13
    </td>
 
    <td>
Délai dépassé (timeout) lors d&#x27;une connexion au DS
    </td>
 
   </tr>
 
   <tr>
 
    <td>
15
    </td>
 
    <td>
Canal de paiement pour lequel 3DS n&#x27;est pas disponible (paiements par fichier...)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
16
    </td>
 
    <td>
Type carte et réseau elligible au 3DS, mais pas de &quot;brand&quot; associée à la carte (CB pure)
    </td>
 
   </tr>
 
   <tr>
 
    <td>
98
    </td>
 
    <td>
L&#x27;initialisation du processus 3DS est OK
    </td>
 
   </tr>
 
   <tr>
 
    <td>
99
    </td>
 
    <td>
Statut inconnu
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
* Ces statuts concernent les paiements pour lesquels 3DS a eu lieu mais sans saisie de carte (par alias).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638075046.xml -->
<h2>
16.145. vads_threeds_mpi
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Active / désactive le processus 3DS lors d’un paiement e-commerce.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n1
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
50
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
absent ou vide
    </td>
 
    <td>
 
    <p>
Authentification 3DS gérée par la plateforme de paiement (configuration du marchand).
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
0
    </td>
 
    <td>
 
    <p>
Authentification 3DS gérée par la plateforme de paiement (configuration du marchand).
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>
1
    </td>
 
    <td>

    <p>
Authentification 3DS intégralement gérée par le marchand à condition que vads_card_number soit valorisé (saisie des données cartes chez le marchand).
    </p>
Les données résultantes de l’authentification 3D Secure effectuée par le MPI du marchand doivent alors être transmises dans les champs du formulaire prévus à cet effet (vads_threeds_enrolled, vads_threeds_cavv, vads_threeds_eci, vads_threeds_xid, vads_threeds_ cavvAlgorithm, vads_threeds_status).
    </td>
 
   </tr>
 
   <tr>
 
    <td>
2
    </td>
 
    <td>
 
    <p>
Authentification 3DS désactivée pour la transaction, quelle que soit la configuration habituelle du marchand.
    </p>
 
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638234029.xml -->
<h2>
16.146. vads_threeds_sign_valid
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Désigne la validité de la signature du message PARes. Il est valorisé par la plateforme de paiement.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n1
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
vide
    </td>
 
    <td>
Pas de 3DS.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
0
    </td>
 
    <td>
signature incorrecte.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
1
    </td>
 
    <td>
signature correcte.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638341396.xml -->
<h2>
16.147. vads_threeds_status
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Désigne le statut de l’authentification du porteur. Il est valorisé par le serveur d’authentification 3DS (ACS) durant le processus 3D Secure.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
a1
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code d&#x27;erreur</b>
  </td>
 
  <td>
56
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
Y
    </td>
 
    <td>
Authentification réussie.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
N
    </td>
 
    <td>
Erreur d’authentification.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
U
    </td>
 
    <td>
Authentification impossible.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
A
    </td>
 
    <td>
Essai d’authentification.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638445416.xml -->
<h2>
16.148. vads_threeds_xid
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Désigne la référence unique de la transaction 3DS.
  </p>
Il est valorisé par le serveur d’authentification (ACS) durant le processus 3D Secure.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..28
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
54
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Authentification 3DS.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638544413.xml -->
<h2>
16.149. vads_trans_date
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Paramètre obligatoire. 
  </p>

  <p>
Correspond à l’horodatage au format AAAAMMJJHHMMSS.
  </p>

  <p>

<b>L’horodatage doit nécessairement correspondre à la date et heure courants, dans le fuseau GMT+0 (ou UTC) au format horaire 24h.</b>
  </p>

<b>Remarque : </b>Si vous utilisez les Webservices, la variable vads_trans_date correspond au champ 
<b>transmissionDate</b>. Nous vous conseillons donc d’enregistrer cette valeur en base afin de valoriser correctement le champ transmissionDate lors de vos appels via les Webservices.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n14
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
04
  <p>

<b>Erreurs fréquentes</b>:
  </p>

  <p>
 

  <ul>
 
   <li>
La date n&#x27;est pas envoyée sous le format AAAAMMJJHHMMSS (année, mois, jour, heure, minute, seconde).
   </li>
 
   <li>
La date n&#x27;est pas basée sur le fuseau horaire UTC (temps universel coordonné).
   <p>
Pensez à utiliser des fonctions date dans votre langage de programmation générant une heure UTC (gmdate en PHP par exemple)
   </p>

   </li>
 
   <li>
L&#x27;heure doit être calculée sur 24h et non sur 12h.
   </li>
 
   <li>
L&#x27;acheteur a attendu trop longtemps avant de cliquer sur le bouton 
<b>Payer</b>.
   </li>
 
   <li>
L&#x27;acheteur a utilisé l&#x27;historique de son navigateur.
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638607923.xml -->
<h2>
16.150. vads_trans_id
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Paramètre obligatoire.
  </p>
 
  <p>
Il est constitué de 6 caractères numériques et doit être unique pour chaque transaction pour une boutique donnée sur la journée. 
  </p>
 
  <p>
Il est à la charge du site marchand de garantir cette unicité sur la journée. Il doit être compris entre 000000 et 899999. 
  </p>
 
  <p>
La tranche 900000 et 999999 est reservée aux remboursements et aux opérations effectuées depuis le Back Office.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
n6
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
03
  <p>

<b>Erreurs fréquentes</b>:
  </p>

  <p>
Le formulaire est rejeté:

  <ul>
 
   <li>
si la valeur transmise est inférieure à 6 chiffres
   </li>
 
   <li>
si la valeur est nulle
   </li>
 
   <li>
si le champ est absent
   </li>
 
   <li>
si un numéro de transaction identique a déjà été envoyé le même jour.
   <p>
Si l&#x27;acheteur clique sur le bouton « Annuler et retourner à la boutique », le numéro de transaction devra être différent pour la prochaine tentative car celui-ci est considéré comme déjà utilisé. 
   <p>
Dans le cas contraire, le message « La transaction a été annulée » sera affiché.
   </p>

   </p>

   </li>
 
  </ul>

  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638657026.xml -->
<h2>
16.151. vads_trans_status
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Champ retourné dans la réponse.
  </p>
 
  <p>
Permet de définir le statut de la transaction. 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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

<b>ABANDONED</b>
    </td>
 
    <td>

<b>Abandonné</b>
    <p>
Le paiement a été abandonné par l’acheteur. 
    </p>

    <p>
La transaction n’est pas créée et 
<b>n’est donc pas visible dans le Back Office.</b>
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>AUTHORISED </b>
    </td>
 
    <td>

    <p>

<b>En attente de remise</b>
    </p>
La transaction est acceptée et sera remise en banque automatiquement à la date prévue.
    <p>

    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>AUTHORISED_TO_VALIDATE </b>
    </td>
 
    <td>
 
    <p>

<b>A valider</b>
    </p>
 
    <p>
La transaction, créée en validation manuelle, est autorisée. Le marchand doit valider manuellement la transaction afin qu&#x27;elle soit remise en banque.
    </p>
 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CANCELED</b>
    </td>
 
    <td>

    <p>

<b>Annulée</b>
    </p>
La transaction est annulée par le marchand.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>CAPTURED</b>
    </td>
 
    <td>

    <p>

<b>Remisée</b>
    </p>
La transaction est remise en banque.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>EXPIRED</b>
    </td>
 
    <td>

    <p>

<b>Expirée</b>
    </p>
 La date de remise est atteinte et le marchand n’a pas validé la transaction.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>REFUSED</b>
    </td>
 
    <td>

    <p>

<b>Refusée</b>
    </p>
La transaction est refusée.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>WAITING_AUTHORISATION</b>
    </td>
 
    <td>

<b>En attente d’autorisation</b>
    <p>
Le délai de remise en banque est supérieur à la durée de validité de l&#x27;autorisation .
    </p>

    <p>
Une autorisation d’un euro
    </p>
La demande d’autorisation sera déclenchée automatiquement à J-1 avant la date de remise en banque. Le paiement pourra être accepté ou refusé. La remise en banque est automatique. 
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>WAITING_AUTHORISATION_TO</b>
    <p>

<b>_VALIDATE</b>
    </p>

    </td>
 
    <td>

    <p>

<b>A valider et autoriser </b>
    </p>

    <p>
Le délai de remise en banque est supérieur à la durée de validité de l&#x27;autorisation .
    </p>
Une autorisation d’un euro
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>UNDER_VERIFICATION</b>
    </td>
 
    <td>

<b>Spécifique à PayPal</b> 
    <p>

<b>En attente de vérification par PayPal</b>
    </p>

    <p>
PayPal retient la transaction pour suspicion de fraude . Le paiement est alors dans l’onglet 
<b>Paiement en cours</b>.
    </p>

    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>NOT_CREATED</b>
    </td>
 
    <td>

    <p>

<b>Transaction non créée</b>
    </p>
La transaction n&#x27;est pas créée et n&#x27;est pas visible dans le Back Office.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>INITIAL</b> 
    </td>
 
    <td>

<b>En attente</b>
    <p>
Ce statut est spécifique à tous les moyens de paiement nécessitant une intégration par formulaire de paiement en redirection, notamment 
<b>SOFORT BANKING</b> et 
<b>3xCB COFINOGA</b>.
    </p>

    <p>
Ce statut est retourné lorsque :

    <ul>
 
     <li>
aucune réponse n&#x27;est renvoyée par l&#x27;acquéreur
     <p>
ou
     </p>

     </li>
 
     <li>
 
     <p>
le délai de réponse de la part de l&#x27;acquéreur est supéreieur à la durée de session du paiement sur la plateforme de paiement. 
     </p>
 
     <p>
Ce statut est temporaire. Le statut définitif sera affiché dans le Back Office aussitôt la synchronisation réalisée.
     </p>
 
     </li>
 
    </ul>

    </p>

    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1432730650747.xml -->
<h2>
16.152. vads_trans_uuid
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
Référence unique de la transaction générée par la plateforme de paiement suite à la création d&#x27;une transaction de paiement.
  </p>
 
  <p>
Offre une garantie d&#x27;unicité pour chaque transaction.
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans32
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638742584.xml -->
<h2>
16.153. vads_url_cancel
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
URL où sera redirigé l’acheteur si celui-ci appuie sur 
<b>Annuler et retourner à la boutique</b> avant d&#x27;avoir procédé au paiement.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
27
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638807307.xml -->
<h2>
16.154. vads_url_check
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
URL de la page à notifier à la fin du paiement. Surcharge la valeur saisie dans le paramétrage des règles de notification.
  <p>

<i>Remarque</i>
  </p>

  <p>

<i>Ce champ doit être utilisé de manière exceptionelle car :</i>
  </p>

  <p>
 

  <ul>
 
   <li>

<i>cette URL ne sera utilisée que dans l&#x27;appel de l&#x27;URL de notification de paiement (IPN) immédiat,</i>
   </li>
 
   <li>

<i>la valeur surchargée ne sera pas utilisée s&#x27;il y a un re-jeu automatique. </i>
   <p>
Incompatible avec l&#x27;exécution, depuis le Back Office, de la requête envoyée à l’url de notification instantanée. L’URL appelée sera celle configurée dans la règle de notification (voir chapitre 
<b>Paramétrer les notifications</b>
   </p>

   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
33
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408638858037.xml -->
<h2>
16.155. vads_url_check_src
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Ce paramètre définit l’origine de la notification (également appelée IPN).
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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

<b>PAY</b>
    </td>
 
    <td>
Création d’un paiement par formulaire.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>BO</b>
    </td>
 
    <td>
Exécution de l’URL de notification depuis le Back Office.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>BATCH_AUTO</b>
    </td>
 
    <td>
Demande d’autorisation sur un paiement qui était en attente d’autorisation.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>REC</b>
    </td>
 
    <td>
Paiement résultant d&#x27;un abonnement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>MERCH_BO</b>
    </td>
 
    <td>
Opération réalisée depuis le Back Office.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>RETRY</b>
    </td>
 
    <td>
Rejeu automatique de l’URL de notification.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639045339.xml -->
<h2>
16.156. vads_url_error
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
URL où sera redirigé l’acheteur en cas d&#x27;erreur de traitement interne.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
29
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639045339.xml -->
<h2>
16.157. vads_url_error
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
URL où sera redirigé l’acheteur en cas d&#x27;erreur de traitement interne.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
29
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639119392.xml -->
<h2>
16.158. vads_url_referral
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

<b>Champ déprécié</b>. Utilisez 
<b>vads_url_refused</b>.
  <p>
URL où sera redirigé l’acheteur en cas de refus d’autorisation (code 02 
<b>Contacter l’émetteur de la carte</b>) après appui sur 
<b>Retourner à la boutique</b>.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
26
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639165197.xml -->
<h2>
16.159. vads_url_refused
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
URL où sera redirigé l’acheteur en cas de refus, après appui du bouton 
<b>Retourner à la boutique</b>.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
25
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639224559.xml -->
<h2>
16.160. vads_url_return
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
 
  <p>
URL où sera redirigé par défaut l’acheteur après un appui sur le bouton 
<b>Retourner à la boutique</b>, si les URL 
<b>vads_url_error</b>, 
<b>vads_url_refused</b>, 
<b>vads_url_success</b> ou 
<b>vads_url_cancel</b> ne sont pas renseignées.
  </p>
 
  <p>
Si ce champ n’est pas transmis, la configuration du Back Office sera prise en compte. 
  </p>
 
  <p>
Il est possible de configurer des URL de retour, en mode TEST et en mode PRODUCTION. Ces champs sont nommés 
<b>URL de retour de la boutique en mode test</b> et 
<b>URL de retour de la boutique en mode production</b>, et sont accessibles depuis le menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; onglet 
<b>Configuration</b>.
  </p>
 
  <p>
Si aucune URL n’est définie dans le Back Office ou dans le formulaire, alors le bouton 
<b>Retourner à la boutique</b> redirigera l&#x27;acheteur vers l’URL du site marchand (champ 
<b>URL</b> dans la configuration de la boutique).
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
28
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639383258.xml -->
<h2>
16.161. vads_url_success
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
URL où sera redirigé l’acheteur en cas de succès du paiement, après appui du bouton 
<b>Retourner à la boutique</b>.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..127
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
24
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Redirection vers le site marchand.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639681161.xml -->
<h2>
16.162. vads_user_info
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>

  <p>
Information sur l’utilisateur à l’origine du paiement.
  </p>

  <p>
Dans le cas d’un paiement par formulaire, ce paramètre sera renvoyé dans la réponse avec la valeur transmise dans la requête.
  </p>
Dans le cas d’un paiement manuel depuis le Back Office, ce champ sera valorisé avec le compte utilisateur (login) qui a réalisé le paiement.
  <p>

<b>
<i>Remarque :</i></b>
  </p>

  <p>

<i>Pour des raisons de rétrocompatibilité, il est possible d&#x27;utiliser ce champ pour valoriser le CPF/CNPJ (Identifiant légal, au format numérique, de longueur comprise entre 11 et 20 digits) imposé par le module de gestion de fraude ClearSale. Cependant, le CPF/CNPJ peut être valorisé dans le champ 
<b>vads_cust_national_id</b>.</i>
  </p>

  <p>

  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
ans..255
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
61
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur l&#x27;acheteur.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639754479.xml -->
<h2>
16.163. vads_validation_mode
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Précise le mode de validation de la transaction. 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
05
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
Configuration par défaut de la boutique retenue (paramétrable dans le Back Office).
    </td>
 
   </tr>
 
   <tr>
 
    <td>
0
    </td>
 
    <td>
Validation automatique par la plateforme de paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
1
    </td>
 
    <td>
Validation manuelle par le marchand.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639900969.xml -->
<h2>
16.164. vads_version
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Paramètre obligatoire. 
  <p>
Version du protocole d’échange avec la plateforme de paiement.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Code erreur</b>
  </td>
 
  <td>
01
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Valeur possible</b>
  </td>
 
  <td>
V2
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations techniques.
  </td>
 
 </tr>
   
</table>
 <!-- tla1408639995934.xml -->
<h2>
16.165. vads_warranty_result
</h2>
 
<table>
     
 <tr>
 
  <td>

<b>Description</b>
  </td>
 
  <td>
Champ retourné dans la réponse.
  <p>
Indique la garantie du paiement dans le cas d’un paiement accepté.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Format</b>
  </td>
 
  <td>
string (enum)
  </td>
 
 </tr>
 
 <tr>
 
  <td>

  <p>

  </p>

<b>Valeurs possibles</b>
  </td>
 
  <td>
 
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
YES
    </td>
 
    <td>
Le paiement est garanti.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
NO
    </td>
 
    <td>
Le paiement n’est pas garanti.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
UNKNOW
    </td>
 
    <td>
Suite à une erreur technique, le paiement ne peut pas être garanti.
    </td>
 
   </tr>
 
   <tr>
 
    <td>
Non valorisé
    </td>
 
    <td>
Garantie de paiement non applicable.
    </td>
 
   </tr>
   
  </table>
 
  </p>
 
  <p>
 
  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>Catégorie</b>
  </td>
 
  <td>
Informations sur la transaction.
  </td>
 
 </tr>
   
</table>
 