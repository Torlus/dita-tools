---
layout: docs
permalink: /docs/chap-3/
title: chap-3
---
<h1>
3. Les différents types de paiement
</h1>
<!-- tla1416990214312.xml -->
<h2>
3.1. Paiement comptant immédiat
</h2>
 
<p>
Un paiement est considéré comme 
<b>comptant immédiat</b> si :
<ul>
  <li>
le montant est débité en une seule fois,
 </li>
  <li>
le délai de remise en banque est de 0 jour.
 </li>
  
</ul>

</p>
 
<p>
Une demande d&#x27;autorisation pour le montant global est effectuée. Le paiement est remis en banque dès que possible.
</p>
  <!-- tla1416990255326.xml -->
<h2>
3.2. Paiement comptant différé
</h2>
 
<p>
Un paiement est considéré comme 
<b>comptant différé</b> si :
</p>
 
<p>
 
<ul>
  <li>
le montant est débité en une seule fois,
 </li>
  <li>
le délai de remise en banque est strictement supérieur à 0 jour.
 <p>
La date de remise ne peut être supérieure à 12 mois après la date d’enregistrement du paiement.
 </p>

 </li>
 
</ul>
 
</p>
   
<p>

</p>
 
<p>
Il existe deux types de paiements comptants différés :
</p>
 
<p>
 
<ul>
  <li>

<b>Délai de remise inférieur à la durée de validité de l&#x27;autorisation</b> (voir section 
<b>Validité d&#x27;une autorisation</b> présentée plus bas)
 </li>
 
</ul>
 
</p>
 
<p>
Une demande d&#x27;autorisation pour le montant global est effectuée. Sans modification du marchand, le paiement est remis en banque à la date de présentation demandée.
</p>
 
<p>
 
<ul>
  <li>

<b>Délai de remise supérieur à la durée de validité de l&#x27;autorisation</b> (voir section 
<b>Validité d&#x27;une autorisation</b> présentée plus bas)
 </li>
 
</ul>
 
</p>
 
<p>
Une demande d&#x27;autorisation à 1 euro
</p>
 
<p>
Si cette autorisation à 1 euro
</p>
 
<p>
J-1 à la date de présentation demandée, une demande d’autorisation pour le montant global est effectuée. 
</p>
 
<p>
Le paiement peut être accepté ou refusé. Le marchand doit donc être très vigilant sur ce type de paiement avant de délivrer un bien / un service à l&#x27;acheteur. 
</p>
   <!-- tla1416990290134.xml -->
<h2>
3.3. Paiement en plusieurs fois
</h2>
 
<p>
Un paiement est dit &quot;en plusieurs fois&quot; dès lors que l&#x27;acheteur est débité du montant de son achat en plusieurs échéances. 
</p>
 
<p>
La première échéance fonctionne de la même manière qu&#x27;un paiement comptant immédiat.
</p>
 
<p>
La ou les échéance(s) suivante(s) s&#x27;apparente(nt) à un ou des paiement(s) comptant(s) différé(s).
</p>
 
<p>
Seule la première échéance peut faire l’objet d’une garantie pour le marchand à condition que la date de présentation demandée de la première échéance soit inférieure à la date de validité de l&#x27;autorisation en fonction du moyen de paiement. (voir section 
<b>Validité d&#x27;une autorisation</b> présentée plus bas)
</p>
 <!-- tla1416990314409.xml -->
<h2>
3.4. Demande d&#x27;autorisation
</h2>
 
<p>
Message adressé par la plateforme de paiement à l&#x27;émetteur de la carte afin d&#x27;obtenir son accord pour le paiement de la transaction.
</p>
 
<p>
De manière générale, le débit n&#x27;est effectif qu&#x27;après la remise en banque de la transaction. 
</p>
 
<p>
Certains émetteurs de carte prépayées ou d&#x27;origine espagnole et canadienne débitent le montant de l&#x27;autorisation en temps réel et le re-creditent lorsque l&#x27;autorisation est échue (voir tableau ci-après).
</p>
 
<p>

</p>
 
<p>

<b>Validité d&#x27;une autorisation</b>
</p>
 
<p>
Ci-dessous la liste des moyens de paiement dont la validité de l&#x27;autorisation est supérieure à 0 jour. 
<table>
        <tr>
   <td>
Moyen de paiement
  </td>
   <td>
Type de cartes (vads_payment_cards)
  </td>
   <td>
Réseau
  </td>
   <td>
Durée de validité d&#x27;une autorisation (en jours)
  </td>
 
 </tr>
    <tr>
   <td>
American Express
  </td>
   <td>
AMEX
  </td>
   <td>
AMEX
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
Carte Aurore
  </td>
   <td>
AURORE-MULTI
  </td>
   <td>
AURORE
  </td>
   <td>
29
  </td>
 
 </tr>
  <tr>
   <td>
Carte Cora
  </td>
   <td>
CORA_BLANCHE
  </td>
   <td>
AURORE
  </td>
   <td>
29
  </td>
 
 </tr>
  <tr>
   <td>
Carte Cora Premium
  </td>
   <td>
CORA_PREM
  </td>
   <td>
AURORE
  </td>
   <td>
29
  </td>
 
 </tr>
  <tr>
   <td>
Carte Cora Visa
  </td>
   <td>
CORA_VISA
  </td>
   <td>
AURORE
  </td>
   <td>
29
  </td>
 
 </tr>
  <tr>
   <td>
CB
  </td>
   <td>
CB
  </td>
   <td>
CB
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
Visa
  </td>
   <td>
VISA
  </td>
   <td>
CB
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
MasterCard
  </td>
   <td>
MASTERCARD
  </td>
   <td>
CB
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
Maestro
  </td>
   <td>
MAESTRO
  </td>
   <td>
CB
  </td>
   <td>
30
  </td>
 
 </tr>
  <tr>
   <td>
Bancontact Mistercash
  </td>
   <td>
BANCONTACT
  </td>
   <td>
CB
  </td>
   <td>
30
  </td>
 
 </tr>
  <tr>
   <td>
Visa Electron
  </td>
   <td>
VISA_ELECTRON
  </td>
   <td>
CB
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
E-carte bleue
  </td>
   <td>
E-CARTEBLEUE
  </td>
   <td>
CB
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
Carte Privilège
  </td>
   <td>
CDGP
  </td>
   <td>
CDGP
  </td>
   <td>
30
  </td>
 
 </tr>
  <tr>
   <td>
Carte cadeau Truffaut
  </td>
   <td>
TRUFFAUT_CDX
  </td>
   <td>
CERIDIAN
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
3 fois CB Cofinoga
  </td>
   <td>
COF3XCB
  </td>
   <td>
COF3XCB
  </td>
   <td>
21
  </td>
 
 </tr>
  <tr>
   <td>
Carte Be Smart
  </td>
   <td>
COFINOGA
  </td>
   <td>
COFINOGA
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
Carte Soficarte
  </td>
   <td>
SOFICARTE
  </td>
   <td>
COFINOGA
  </td>
   <td>
30
  </td>
 
 </tr>
  <tr>
   <td>
Carte Sygma
  </td>
   <td>
SYGMA
  </td>
   <td>
COFINOGA
  </td>
   <td>
30
  </td>
 
 </tr>
  <tr>
   <td>
Carte Diners Club
  </td>
   <td>
DINERS
  </td>
   <td>
GATECONEX
  </td>
   <td>
3
  </td>
 
 </tr>
  <tr>
   <td>
Bancontact Mistercash
  </td>
   <td>
BANCONTACT
  </td>
   <td>
GATECONEX
  </td>
   <td>
30
  </td>
 
 </tr>
  <tr>
   <td>
Carte JCB
  </td>
   <td>
JCB
  </td>
   <td>
JCB
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
Bancontact Mistercash
  </td>
   <td>
BANCONTACT
  </td>
   <td>
GICC
  </td>
   <td>
30
  </td>
 
 </tr>
  <tr>
   <td>
Paylib
  </td>
   <td>
PAYLIB
  </td>
   <td>
PAYLIB
  </td>
   <td>
7
  </td>
 
 </tr>
  <tr>
   <td>
PayPal
  </td>
   <td>
PAYPAL
  </td>
   <td>
PAYPAL
  </td>
   <td>
3
  </td>
 
 </tr>
  <tr>
   <td>
POSTFINANCE
  </td>
   <td>
POSTFINANCE
  </td>
   <td>
POSTFINANCE
  </td>
   <td>
1
  </td>
 
 </tr>
  <tr>
   <td>
Virement SEPA
  </td>
   <td>
SCT
  </td>
   <td>
SEPA
  </td>
   <td>
13
  </td>
 
 </tr>
  <tr>
   <td>
Prélèvement SEPA
  </td>
   <td>
SDD
  </td>
   <td>
SEPA
  </td>
   <td>
13
  </td>
 
 </tr>
   
</table>

</p>
 <!-- tla1406021920185.xml -->
