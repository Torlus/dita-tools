---
layout: docs
permalink: /docs/chap-7/
title: chap-7
---
<h1>
7. Générer un formulaire de paiement
</h1>
 
<p>
Pour générer une demande de paiement, vous devez construire un formulaire html comme suit :<code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
	&lt;input type=&quot;hidden&quot; name=&quot;parametre1&quot; value=&quot;valeur1&quot; /&gt;
	&lt;input type=&quot;hidden&quot; name=&quot;parametre2&quot; value=&quot;valeur2&quot; /&gt;
	&lt;input type=&quot;hidden&quot; name=&quot;parametre3&quot; value=&quot;valeur3&quot; /&gt;
	&lt;input type=&quot;hidden&quot; name=&quot;signature&quot; value=&quot;signature&quot;/&gt;
	&lt;input type=&quot;submit&quot; name=&quot;payer&quot; value=&quot;Payer&quot;/&gt;
&lt;/form&gt;
</pre></code>

</p>
 
<p>

</p>
 
<p>
Il contient:
</p>
 
<p>

</p>
 
<p>

<u>Les éléments techniques suivants : </u>
</p>
 
<p>
 
<ul>
 <li>
Les balises <code><pre>
&lt;form&gt;
</pre></code>
 et
						<code><pre>
&lt;/form&gt;
</pre></code>
 qui permettent de créer un
					formulaire HTML.
</li>
 <li>
L’attribut <code><pre>
method=&quot;POST&quot;
</pre></code>
 qui
					spécifie la méthode utilisée pour envoyer les données.
</li>
 <li>
L’attribut <code><pre>
action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;
</pre></code>
 qui spécifie où envoyer les données
					du formulaire.
</li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>

<u>Les données du formulaire :</u>
</p>
 
<p>
 
<ul>
 <li>
L’identifiant de la boutique,
</li>
 <li>
Les caractéristiques du paiement en fonction du cas d’utilisation(voir chapitres suivants),
</li>
 <li>
Les informations complémentaires en fonction de vos besoins (voir chapitre 
<b>Utiliser des fonctions complémentaires</b> ),
</li>
 <li>
La signature qui assure l&#x27;intégrité du formulaire (voir chapitre 
<b>Calculer la signature</b>).
</li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>
Ces données sont ajoutées au formulaire en utilisant la balise <code><pre>
&lt;input&gt;
</pre></code>
:
</p>
 
<p>
<code><pre>
&lt;input type=&quot;hidden&quot;
				name=&quot;parametre1&quot; value=&quot;valeur1&quot; /&gt;
</pre></code>

</p>
 
<p>

</p>
 
<p>
Pour valoriser les attributs <code><pre>
name
</pre></code>
 et <code><pre>
value
</pre></code>
 , référez-vous au chapitre 
<b>Dictionnaire de
				données</b>.
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

</p>
 
<p>
Toutes les données du formulaire doivent être encodées en 
<b>UTF-8. </b>
</p>
 
<p>
Les caractères spéciaux (accents, ponctuation etc…) seront ainsi correctement interprétés par la plateforme de paiement. Dans le cas contraire, le calcul de signature sera erroné et le formulaire sera rejeté.
</p>
 
<p>

</p>
 
<p>

<u>Le bouton 
<b>Payer</b> qui va permettre l’envoi des données :</u>
</p>
 
<p>
<code><pre>
&lt;input type=&quot;submit&quot;
				name=&quot;payer&quot; value=&quot;Payer&quot;/&gt;
</pre></code>

</p>
 
<p>

</p>
 
<p>
Des cas d’utilisation sont présentés dans les chapitres suivants. Ils vous permettront de construire votre formulaire de paiement en fonction de vos besoins.
</p>
 
<p>
  
<ul>
 <li>
Créer un paiement comptant immédiat.
</li>
 <li>
Créer un paiement comptant différé.
</li>
 <li>
Créer un paiement en plusieurs fois.
</li>
 <li>
Créer une autorisation sans remise.
</li>
 
</ul>
 
</p>
 <!-- emm1405086126734.xml -->
<h2>
7.1. Créer un paiement comptant immédiat
</h2>
  
<p>
En mode paiement comptant immédiat, l’acheteur règle la totalité de son achat en une seule fois. 
</p>
 
<p>
Le paiement est remis en banque le jour même.
</p>
  <ol>
  <li>
 
 <p>
Utilisez l&#x27;ensemble des champs présents dans le tableau ci-après pour construire votre formulaire de paiement.
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

<b>INTERACTIVE</b>
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

<b>0</b>
   </td>
 
  </tr>
   <tr>
    <td>
vads_validation_mode
   </td>
    <td>
Mode de validation
   </td>
    <td>

<b>0</b> (Automatique)
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_payment_config</b> à 
<b>SINGLE</b>.
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_capture_delay</b> à 
<b>0</b>.
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_validation_mode</b> à 
<b>0</b> pour une validation automatique (le paiement sera remis de manière automatique à la banque).
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

<u>Exemple de formulaire pour le paiement comptant :</u>
</p>
 
<p>
 <code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

			
</p>
 
</p>
 <!-- tla1406042467751.xml -->
<h2>
7.2. Créer un paiement comptant différé
</h2>
 Un paiement comptant différé est un paiement débité en une seule fois dont le délai de remise en banque est strictement supérieur à 0 jour.
<p>
 
<ul>
  <li>
Une demande d&#x27;autorisation sera réalisée pour le montant global si le délai de remise est inférieur ou égal à la durée de validité d&#x27;une demande d&#x27;autorisation (voir <a href="#TODO-tla1416990314409.xml">tableau</a>).
 </li>
 
</ul>
 
</p>

<p>
 
<ul>
  <li>
Une demande d&#x27;autorisation à 1 €
 </li>
 
</ul>
 
</p>
 <ol>
  <li>
 
 <p>
Utilisez l&#x27;ensemble des champs présents dans le tableau ci-après pour construire votre formulaire de paiement.
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

<b>INTERACTIVE</b>
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

<b>&gt; 0 Ex: 3</b>
   </td>
 
  </tr>
   <tr>
    <td>
vads_validation_mode
   </td>
    <td>
Mode de validation
   </td>
    <td>

<b>0</b> (automatique) ou 
<b>1</b> (manuel)
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_payment_config</b> à 
<b>SINGLE</b>.
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_capture_delay</b> avec une valeur 
<b>supérieure à 0</b>.
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_validation_mode</b> à 
<b>0</b> pour une validation automatique (le paiement sera remis de manière automatique à la banque) ou à 
<b>1</b> pour une validation manuelle (le paiement sera remis en banque après une validation manuelle dans le Back Office).
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

<u>Exemple de formulaire de paiement comptant différé :</u><code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;3&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406043754066.xml -->
<h2>
7.3. Créer un paiement en plusieurs fois
</h2>
  
<p>
Ce mode de paiement permet au marchand de proposer une facilité de paiement à l’acheteur. 
</p>
 
<p>
Le formulaire de paiement définit le nombre d’échéances et l’intervalle qui les sépare. 
</p>
 
<p>
La première échéance fonctionne de la même manière qu&#x27;un paiement comptant immédiat.
</p>
 
<p>
La ou les échéance(s) suivante(s) s&#x27;apparente(nt) à un ou des paiement(s) comptant(s) différé(s).
</p>
 
<p>

<u>Rappel</u> : 
</p>
 
<p>
Des règles de notifications doivent être activées selon l&#x27;échéance. Référez-vous au chapitre <a href="#TODO-emm1405085350214.xml">
<b>Paramétrer les notifications</b></a> pour plus de détails.
</p>
 
<p>

<u>Précisions</u> :
</p>
 
<p>
Le jour du paiement, le marchand n’est pas crédité de la totalité du montant et la garantie de paiement ne peut s’appliquer sur les échéances futures.
</p>
  <ol>
  <li>
 
 <p>
Utilisez l&#x27;ensemble des champs présents ci-dessous pour construire votre formulaire de paiement.
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

<b>INTERACTIVE</b>
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
 
   <p>
voir étape 2.
   </p>
 
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
vads_validation_mode
   </td>
    <td>
Mode de validation
   </td>
    <td>

<b>0</b> (automatique) ou 
<b>1</b> (manuel)
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_payment_config</b> en respectant la syntaxe suivante:
 </p>
 
 <p>
 
 <ul>
   <li>

<u>Montants et dates d&#x27;échéances fixes</u> :
  <p>

<b>MULTI:first=1000;count=3; period=30</b> où :
  </p>

  <p>
&quot;first&quot; correspond au montant (dans la plus petite unité de la devise) du premier paiement réalisé le jour du paiement,
  </p>

  <p>
&quot;count&quot; représente le nombre total d&#x27;échéances,
  </p>

  <p>
&quot;period&quot; détermine l&#x27;intervalle entre chaque échéance.
  </p>

  </li>
   <li>

<u>Montants et dates d&#x27;échéance personnalisés</u> :
  <p>

<b>MULTI_EXT:date1=montant1;date2=montant2;date3=montant3</b> où :
  </p>

  <p>
date1=montant1 définit la date et le montant du premier versement.
  </p>

  <p>
Les montants sont exprimés dans la plus petite unité de la devise. La somme de tous les montants doit être égale à la valeur du champ 
<b>vads_amount</b>.
  </p>

  <p>
Les dates sont exprimées au format YYYYMMDD. 
  </p>

  </li>
 
 </ul>
 
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_capture_delay</b> à 
<b>0</b>. Le 1er paiement sera remis en banque le jour même.
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_validation_mode</b> à 
<b>0</b> pour une validation automatique (le paiement sera remis de manière automatique à la banque) ou à 
<b>1</b> pour une validation manuelle (opération manuelle effectuée depuis le Back Office).
 </p>
 
 <p>
Le mode de validation s&#x27;applique à toutes les échéances.
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

<u>Exemple de formulaire de paiement en plusieurs fois (Montants et dates d&#x27;échéances fixes): </u><code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<u>Exemple de formulaire de paiement en plusieurs fois (Montants et dates d&#x27;échéances personnalisés) :</u><code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;3000&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406101311911.xml -->
<h2>
7.4. Créer une autorisation sans remise
</h2>
  
<p>
Ce mode de paiement permet de s’assurer de la validité des données de la carte de l&#x27;acheteur sans la débiter.
</p>
 
<p>
Au besoin, le marchand pourra débiter cette carte du montant souhaité en utilisant la fonction 
<b>Dupliquer</b> du 
<b>Back Office</b>. Pour cela :
</p>
 
<p>
 
<ul>
  <li>
le mode de validation manuelle est utilisé,
 </li>
  <li>
le marchand ne doit pas valider manuellement les transactions.
 </li>
 
</ul>
 
</p>
  <ol>
  <li>
 
 <p>
Utilisez l’ensemble des champs présents dans le tableau ci-après pour construire votre formulaire de paiement.
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

<b>100</b> (pour 1 euro)
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

<b>INTERACTIVE</b>
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

<b>0</b>
   </td>
 
  </tr>
   <tr>
    <td>
vads_validation_mode
   </td>
    <td>
Mode de validation du paiement
   </td>
    <td>
1
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_amount</b> avec un petit montant. Il n&#x27;aura pas d&#x27;impact sur le plafond d&#x27;autorisation de la carte. 
 </p>
 
 </li>
  <li>
 
 <p>
Valorisez le champ 
<b>vads_validation_mode</b> à 
<b>1</b>.
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

<u>Exemple de formulaire pour une autorisation sans remise :</u><code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;100&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_capture_delay&quot; value=&quot;0&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 <!-- tla1406101932153.xml -->
