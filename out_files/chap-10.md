---
layout: docs
permalink: /docs/chap-10/
title: chap-10
---
<h1>
10. Envoyer la demande de paiement
</h1>
 
<p>
Pour chaque transaction, l’acheteur doit être redirigé vers la page de paiement afin de finaliser son achat.
</p>
 
<p>
Son navigateur doit transmettre les données du formulaire de paiement.
</p>
 <!-- emm1405088418431.xml -->
<h2>
10.1. Rediriger l&#x27;acheteur vers la page de paiement
</h2>
 
<p>
L’URL de la plateforme de paiement est la suivante : 
<table>
    
 <tr>
 
  <td>
<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>
  </td>
 
 </tr>
   
</table>

</p>
 
<p>

<u>Exemple de paramètres envoyés à la plateforme de paiement</u>:<code><pre>

<b>&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;</b>
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt; 
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;2990
</pre></code>

</p>
 <!-- emm1405088431924.xml -->
<h2>
10.2. Gérer les erreurs
</h2>
 
<p>
Si la plateforme détecte une anomalie lors de la réception du formulaire, un message d’erreur sera affiché et l’acheteur ne pourra pas procéder au paiement. 
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<u>En mode TEST</u>
</p>
 
<p>
Le message indique l’origine de l’erreur et propose un lien vers la FAQ pour vous aider à la corriger. 
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<u>En mode PRODUCTION</u>
</p>
 
<p>
Le message indique simplement à l’acheteur qu’un problème technique est survenu.
</p>
 
<p>

</p>
 
<p>
Dans les deux cas, le marchand reçoit un e-mail d&#x27;avertissement.
</p>
 
<p>
Il contient:

<ul>
 
 <li>
l’origine de l’erreur
 </li>
 
 <li>
un lien vers la FAQ pour faciliter le diagnostic
 </li>
 
 <li>
l’ensemble des champs contenus dans le formulaire.
 </li>
 
</ul>

</p>
 
<p>
 
</p>
 
<p>
La FAQ est disponible à cette adresse : <a href="https://secure.payzen.eu/html/error_code/">https://secure.payzen.eu/html/error_code/</a>
</p>
 <!-- emm1405088484151.xml -->
