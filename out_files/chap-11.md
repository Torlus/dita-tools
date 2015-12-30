---
layout: docs
permalink: /docs/chap-11/
title: chap-11
---
<h1>
11. Analyser le résultat du paiement
</h1>
 
<p>
Pour traiter le résultat des paiements, le site marchand doit disposer d&#x27;un script sur une page dédiée (exemple : analyse_paiement.php).
</p>
 
<p>
Cette page sera appelée automatiquement après chaque paiement (accepté ou refusé) : les paramètres liés au résultat du paiement sont envoyés en mode POST par la plateforme de paiement.
</p>
 
<p>

</p>
 
<p>

<b>Prérequis :</b>
</p>
 
<p>
 

<ul>
 
<li>
L&#x27;URL de la page qui analyse le résultat du paiement devra obligatoirement être renseignée dans le Back Office (voir chapitre 
<b>Paramétrer les notifications</b> 
</li>
 
</ul>
 
</p>
  
<p>
 

<ul>
 
<li>
Le marchand doit s&#x27;assurer que cette URL soit joignable par la plateforme de paiement et ce, sans redirection. 
<p>
Les redirections entrainent la perte des données présentes dans le POST.
</p>

</li>
 
</ul>
 
</p>
 
<p>
 

<ul>
 
<li>
En cas de restriction mise en place du côté du site marchand, il faudra autoriser la plage d&#x27;adresses d&#x27;IP 
<b>194.50.38.0/24</b>.
</li>
 
</ul>
 
</p>
 
<p>
 

<ul>
 
<li>
La page ne devra pas comporter d&#x27;affichage HTML. 
<p>
L&#x27;accès aux ressources telles que les images ou feuilles de styles peuvent ralentir les échanges entre la plateforme de paiement et le site marchand.
</p>

<p>
De plus, la plateforme lit systématiquement les 512 premiers caractères retournés par le site marchand.
</p>
Ces caractères sont ensuite affichés dans l&#x27;historique des transactions.
</li>
 
</ul>
 
</p>
 
<p>
 

<ul>
 
<li>
Evitez au maximum d&#x27;intégrer des tâches consommatrices de temps comme la génération de facture ou l&#x27;envoi d&#x27;e-mail dans ce script.
<p>
Le temps du traitement influe directement sur le délai de l’affichage de la page de résumé du paiement. Plus le traitement de la notification est long, plus l’affichage est retardé. 
</p>

<p>
Au delà de 35s, la plateforme considèrera que l&#x27;appel a échoué (timeout).
</p>

</li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<b>Echec de notification (IPN)</b>
</p>
 
<p>
En cas d&#x27;échec de l&#x27;appel à l’URL de notification (IPN), un e-mail d&#x27;avertissement est envoyé à l’adresse spécifiée dans le Back Office (voir chapitre 
<b>Paramétrer les notifications</b>).
</p>
 
<p>
 
</p>
 
<p>
Il contient : 
</p>
 
<p>
 

<ul>
 
<li>
le code HTTP de l’erreur rencontrée,
</li>
 
<li>
des éléments d’analyses en fonction de l’erreur,
</li>
 
<li>
la procédure à suivre depuis le Back Office pour renvoyer la notification. 
</li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<b>Concevoir le script de traitement</b>
</p>
 
<p>
Le script de traitement devra comporter au moins les étapes ci-dessous:
</p>
 
<p>
 

<ul>
 
<li>
Récupérer la liste des champs présents dans la réponse envoyée en POST
</li>
 
<li>
Calculer la signature
</li>
 
<li>
Comparer la signature calculée avec celle réceptionnée
</li>
 
<li>
Analyser la nature de la notification
</li>
 
<li>
Récupérer le résultat du paiement 
</li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>
Le script peut par exemple tester l&#x27;état de la commande (ou l&#x27;information de votre choix) pour vérifier qu&#x27;elle n&#x27;ait pas déja été mise à jour.
</p>
 
<p>
Une fois ces étapes réalisées, le script peut mettre à jour la base de données (nouvel état de la commande, mise à jour du stock, enregistrement des informations du paiement etc...).
</p>
 
<p>

</p>
 
<p>

</p>
  <!-- emm1405088797336.xml -->
<h2>
11.1. Récupérer les données retournées dans la réponse
</h2>
 
<p>
Les données retournées dans la réponse dépendent des paramètres envoyés dans le formulaire de paiement, du type de paiement réalisé et des options de votre boutique. Ces données constituent une liste de champs. Chaque champ contient une valeur réponse. La liste de champs peut être amenée à évoluer.
</p>
 
<p>

</p>
 
<p>
Les données sont toujours envoyées en 
<b>POST</b> par la plateforme de paiement.
</p>
 <!-- emm1405088825989.xml -->
<h2>
11.2. Calculer la signature
</h2>
 La signature se calcule selon la même logique utilisée lors de la création du formulaire de paiement. 
<p>

</p>
Tous les champs reçus doivent être pris en compte. 
<p>

</p>
Pour calculer la signature:
<p>

</p>
 
<ol>
 
 <li>
 
 <p>
Prenez en considération la totalité des champs dont le nom commence par 
<b>vads_</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Triez ces champs par ordre alphabétique.
 </p>
 
 </li>
 
 <li>
 
 <p>

 </p>
 
 </li>
 
 <li>
 
 <p>

 </p>
 
 </li>
 
 <li>
 
 <p>

 </p>
 
 </li>
 
</ol>
 <!-- emm1405088844323.xml -->
<h2>
11.3. Comparer les signatures
</h2>
 
<p>
Pour s’assurer de l’intégrité de la réponse, vous devez comparer la valeur du champ 
<b>signature</b> reçue dans la réponse, avec celle calculée à l’étape précédente. 
</p>
 
<p>

</p>
 
<p>
Si les signatures correspondent, 

<ul>
 
 <li>
alors vous pouvez considérer la réponse comme sûre et procéder à la suite de l’analyse.
 </li>
 
 <li>
sinon, le script devra lever une exception et avertir le marchand de l&#x27;anomalie (voir chapitre 
<b>Traiter les erreurs</b>.
 </li>
 
</ul>

</p>
 
<p>

</p>
 
<p>
Les signatures ne correspondent pas en cas : 
</p>
 
<p>
 

<ul>
 
 <li>
d’erreur d&#x27;implémentation (erreur dans votre calcul, problème d’encodage UTF8, etc.).
 </li>
 
 <li>
d’erreur dans la valeur du certificat utilisé ou dans celle du champ 
<b>vads_ctx_mode</b> (problème fréquent lors du passage en production).
 </li>
 
 <li>
de tentative de corruption des données. 
 </li>
 
</ul>
 
</p>
 <!-- emm1411575961770.xml -->
<h2>
11.4. Analyser la nature de la notification
</h2>
 
<p>
Le champ 
<b>vads_url_check_src</b> permet de différencier les notifications en fonction de leur évènement déclencheur :
</p>
 
<p>
 

<ul>
 
</ul>
 
</p>
 
<p>
Il précise la règle de notification appliquée :
<table>
      
 <tr>
 
  <td>
Valeur
  </td>
 
  <td>
Règle appliquée
  </td>
 
 </tr>
   
 <tr>
 
  <td>

<b>PAY</b>
  </td>
 
  <td>
 
  <p>
La valeur PAY sera envoyée dans les cas suivants :

  <ul>
 
  </ul>

  </p>
 
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>BO</b>
  </td>
 
  <td>
Exécution de la notification depuis le Back Office (clic droit sur une transaction &gt; 
<b>Executer l&#x27;url de notification</b>).
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>BATCH_AUTO</b>
  </td>
 
  <td>

  <p>
La valeur BATCH_AUTO sera envoyée dans les cas suivants:

  <ul>
 
   <li>
paiement différé à plus de 7 jours
   </li>
 
   <li>
échéances d&#x27;un paiement en plusieurs fois (hormis la première)
   <p>
uniquement si le marchand a configuré la règle 
<b>URL de notification sur autorisation par batch</b>. 
   </p>

   </li>
 
  </ul>

  </p>

  <p>

  </p>

  <p>
La notification sera envoyée lors de la demande d’autorisation d&#x27;un paiement dont le statut est &quot;En attente d’autorisation&quot;.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>REC</b>
  </td>
 
  <td>

  <p>
La valeur REC sera envoyée uniquement pour les paiements par abonnement si le marchand a configuré la règle 
<b>URL de notification à la création d&#x27;un paiement par récurrence</b>.
  </p>

  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>MERCH_BO</b>
  </td>
 
  <td>
La valeur MERCH_BO sera envoyée :
  <p>
 

  <ul>
 
   <li>
lors d&#x27;une opération réalisée depuis le Back Office (remboursement, modification, validation, duplicata), si le marchand a configuré la règle de notification : 
<b>URL de notification sur une opération provenant du Back Office</b>
   </li>
 
   <li>
lors d&#x27;une annulation réalisée depuis le Back Office, si le marchand a configuré la règle de notification : 
<b>URL de notification sur annulation</b>
   </li>
 
  </ul>
 
  </p>

  </td>
 
 </tr>
   
</table>

</p>
 
<p>
En testant sa valeur, le script pourra réaliser un traitement différent en fonction de la nature de la notification.
</p>
 
<p>

<u>Par exemple :</u>
</p>
 
<p>
Si 
<b>vads_url_check_src</b> est valorisé à 
<b>PAY</b> ou 
<b>BATCH_AUTO</b> alors le script mettra à jour le statut de la commande, ...
</p>
 
<p>
Si 
<b>vads_url_check_src</b> est valorisé à 
<b>REC</b> alors le script récupèrera la référence de l&#x27;abonnement et incrémentera le nombre d&#x27;échéances échues en cas de paiement accepté, ...
</p>
 <!-- emm1412779631523.xml -->
<h2>
11.5. Identifier le type d&#x27;opération
</h2>
 
<p>
Le champ 
<b>vads_operation_type</b> permet de différencier :
</p>
 
<p>
 

<ul>
 
 <li>
une opération de débit.
 </li>
 
 <li>
une opération de remboursement.
 </li>
 
</ul>
 
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

<b>DEBIT</b>
  </td>
 
  <td>
Opération de débit.
  </td>
 
 </tr>
 
 <tr>
 
  <td>

<b>CREDIT</b>
  </td>
 
  <td>
Opération de remboursement.
  </td>
 
 </tr>
   
</table>
 
</p>
 
<p>

<u>Par exemple :</u>
</p>
 
<p>
Si 
<b>vads_operation_type</b> est valorisé à 
<b>DEBIT</b>, le script met à jour la commande et enregistre les informations de la transaction.
</p>
 
<p>
Si 
<b>vads_operation_type</b> est valorisé à 
<b>CREDIT</b>, le script met à jour le montant payé ou ajoute une nouvelle ligne de transaction dans la commande.
</p>
 <!-- emm1411733020401.xml -->
<h2>
11.6. Traiter les données de la réponse
</h2>
  
<p>
Ci-dessous un exemple d&#x27;analyse pour vous guider pas à pas lors du traitement des données de la réponse.
</p>
  
<ol>
 
 <li>
 
 <p>
Identifiez la commande en récupérant la valeur du champ 
<b>vads_order_id</b> si vous l&#x27;avez transmis dans le formulaire de paiement.
 </p>
 
 <p>
Vérifiez que le statut de la commande n&#x27;a pas déja été mis à jour.
 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez le résultat du paiement transmis dans le champ 
<b>vads_trans_status</b>.
 </p>
 
 <p>
Sa valeur vous permet de définir le statut de la commande.
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
Récupérez la référence du paiement transmise dans le champ 
<b>vads_trans_id</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Analysez le champ 
<b>vads_payment_config</b> pour déterminer s&#x27;il s&#x27;agit d&#x27;un 
<b>paiement comptant</b> (unitaire) ou d&#x27;un 
<b>paiement en plusieurs fois</b>.
 </p>
 
 <p>
Ce champ peut être valorisé à:
 </p>
 
 <p>

 <table>
       
  <tr>
 
   <td>
Nom du champ
   </td>
 
   <td>
Valeur pour un paiement comptant 
   </td>
 
   <td>
Valeur pour un paiement en plusieurs fois
   </td>
 
  </tr>
   
  <tr>
 
   <td>

<b>vads_payment_config</b>
   </td>
 
   <td>
SINGLE 
   </td>
 
   <td>
MULTI
   <p>
(dont la systaxe exacte est MULTI:first=X;count=Y;period=Z)
   </p>

   </td>
 
  </tr>
   
 </table>
S&#x27;il s&#x27;agit d&#x27;un paiement en plusieurs fois, identifiez le numéro de l&#x27;échéance en récupérant la valeur du champ 
<b>vads_sequence_number</b>.
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
1
   </td>
 
   <td>
Première échéance
   </td>
 
  </tr>
 
  <tr>
 
   <td>
2
   </td>
 
   <td>
Deuxième échéance
   </td>
 
  </tr>
 
  <tr>
 
   <td>
3
   </td>
 
   <td>
Troisième échéance
   </td>
 
  </tr>
 
  <tr>
 
   <td>
n
   </td>
 
   <td>
N échéance
   </td>
 
  </tr>
   
 </table>

 </p>
 
 <p>
Pour un paiement comptant (unitaire) le champ 
<b>vads_sequence_number</b> est valorisé à 
<b>1</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez la valeur du champ 
<b>vads_trans_date</b> pour identifier la date du paiement. 
 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez la valeur du champ 
<b>vads_capture_delay</b> pour identifier le nombre de jours avant la remise en banque.
 </p>
 
 <p>
Ceci vous permettra d&#x27;identifier s&#x27;il s&#x27;agit d&#x27;un paiement immédiat ou différé.
 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez le montant et la devise utilisée. Pour cela, récupérez les valeurs des champs suivants:
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

<b>vads_amount</b>
   </td>
 
   <td>
Montant du paiement dans sa plus petite unité monétaire.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_currency</b>
   </td>
 
   <td>
Code de la devise utilisée pour le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_change_rate</b>
   </td>
 
   <td>
Taux de change utilisé pour calculer le montant réél du paiement (voir vads_effective_amount).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_effective_amount</b>
   </td>
 
   <td>
Montant du paiement dans la devise réellement utilisée pour effectuer la remise en banque.
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 <p>

<i>Remarque : </i>
 </p>
 
 <p>

<i>Lorsque le champ 
<b>vads_page_action</b> est valorisé à 
<b>REGISTER_SUBSCRIBE</b>, le champ 
<b>vads_amount</b> est valorisé à 
<b>0</b>, même si aucun paiement a été réalisé.</i>
 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez la valeur du champ 
<b>vads_auth_result</b> pour connaître le résultat de la demande d&#x27;autorisation.
 </p>
 
 <p>

 </p>
 
 <p>

 </p>
 
 <p>
La liste complète des codes renvoyés est consultable dans le dictionnaire de données.
 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez le résultat de l&#x27;authentification 3D Secure. Pour cela:
 </p>
 
 <p>
 

 <ol>
 
  <li>
Récupérez la valeur du champ 
<b>vads_threeds_enrolled</b> pour déterminer le statut de l’enrollement de la carte.
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

<b>Vide</b>
    </td>
 
    <td>
Processus 3DS non réalisé (3DS désactivé dans la demande, marchand non enrôlé ou moyen de paiement non éligible au 3DS).
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>Y</b>
    </td>
 
    <td>
Authentification disponible, porteur enrôlé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>N</b>
    </td>
 
    <td>
Porteur non enrôlé.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>U</b>
    </td>
 
    <td>
Impossible d’identifier le porteur ou carte non éligible aux tentatives d’authentification (ex. Cartes commerciales ou prépayées).
    </td>
 
   </tr>
   
  </table>

  </li>
 
  <li>
Récupérez le résultat de l’authentification 3D Secure en récupérant la valeur du champ 
<b>vads_threeds_status</b>.
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

<b>Vide</b>
    </td>
 
    <td>
Authentification 3DS non réalisée (3DS désactivé dans la demande, porteur non enrôlé ou moyen de paiement non éligible au 3DS).
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>Y</b>
    </td>
 
    <td>
Porteur authentifié avec succès.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>N</b>
    </td>
 
    <td>
Erreur d’authentification du porteur.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>U</b>
    </td>
 
    <td>
Authentification impossible.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>A</b>
    </td>
 
    <td>
Tentative d’authentification mais authentification non réalisée.
    </td>
 
   </tr>
   
  </table>

  </li>
 
 </ol>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez le résultat des contrôles associés à la fraude en identifiant la valeur du champ 
<b>vads_risk_control</b>. Ce champ est envoyé uniquement si le marchand a:
 </p>
 
 <p>
 

 <ul>
 
  <li>
souscrit à l’option « 
<b>Aide à la décision</b> »
  </li>
 
  <li>
activé au moins un contrôle depuis son Back Office (menu 
<b>Paramétrage</b> &gt; 
<b>Contrôle des risques</b>).
  </li>
 
 </ul>
 
 </p>
 
 <p>
Il prend comme valeur une liste de valeurs séparées par un « ; » dont la syntaxe est: 
<b>vads_risk_control = control1=result1;control2=result2</b>
 </p>
 
 <p>
Les différentes valeurs possibles pour 
<b>control</b> sont :
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

<b>CARD_FRAUD</b>
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
Contrôle la présence du pays émetteur de la carte de l&#x27;acheteur dans la liste des pays interdits.
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

<b>CREDIT_LIMIT</b>
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
Contrôle la présence du code BIN de la carte dans la liste grise des codes BIN.
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

<b>CARD_COMMERCIAL</b>
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
Contrôle la présence du pays de l&#x27;acheteur, identifié par son adresse IP, dans la liste des pays interdits.
   </td>
 
  </tr>
   
 </table>

 </p>
 
 <p>
Les différentes valeurs possibles pour 
<b>result</b> sont :
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
OK.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>WARNING</b>
   </td>
 
   <td>
Contrôle informatif échoué.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>ERROR</b>
   </td>
 
   <td>
Contrôle bloquant échoué.
   </td>
 
  </tr>
   
 </table>

 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez le type de carte utilisé pour le paiement.
 </p>
 
 <p>
Deux cas de figures peuvent se présenter:
 </p>
 
 <p>
 

 <ul>
 
  <li>
Pour un paiement réalisé avec 
<b>une seule carte</b>. Les champs à traiter sont les suivants:
  </li>
 
 </ul>
 
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

<b>vads_card_brand</b>
   </td>
 
   <td>
Type de carte utilisée pour le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_card_number</b>
   </td>
 
   <td>
Numéro de la carte utilisée pour réaliser le paiement.
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_expiry_month</b>
   </td>
 
   <td>
Mois d’expiration entre 1 et 12 (ex: 3 pour mars, 10 pour octobre).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_expiry_year</b>
   </td>
 
   <td>
Année d’expiration sur 4 chiffres (ex : 2023).
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_bank_code</b>
   </td>
 
   <td>
Code de la banque émettrice
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_bank_product</b>
   </td>
 
   <td>
Code produit de la carte
   </td>
 
  </tr>
 
  <tr>
 
   <td>

<b>vads_card_country</b>
   </td>
 
   <td>
Code Pays du pays d’émission de la carte (Code alpha ISO 3166-2 ex : France=FR).
   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 <p>
 

 <ul>
 
  <li>
Pour un 
<b>paiement fractionné</b> (c&#x27;est-à-dire une transaction utilisant plusieurs moyens de paiement), les champs à traiter sont les suivants :
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

<b>vads_card_brand</b>
    </td>
 
    <td>
MULTI 
    </td>
 
    <td>
Plusieurs types de cartes sont utilisés pour le paiement.
    </td>
 
   </tr>
 
   <tr>
 
    <td>

<b>vads_payment_seq</b>
    </td>
 
    <td>
Au format json, voir détails ci-dessous.
    </td>
 
    <td>
Détails des transactions réalisées.
    </td>
 
   </tr>
   
  </table>
 
  </p>
Le champ 
<b>vads_payment_seq</b> (format json) décrit la séquence de paiement fractionné. Il contient les éléments :
  <p>
 

  <ol>
 
   <li>
&quot;trans_id&quot; : identifiant de la transaction global à la séquence de paiement.
   </li>
 
   <li>
&quot;transaction&quot; : tableau des transactions de la séquence. Les éléments qui le composent sont les suivants :
   </li>
 
  </ol>
 
  </p>

  </li>
 
 </ul>
 
 </p>
 
 <p>
 
 <p>
 
 <table>
   
  <tr>
 
   <td>

   </td>
 
  </tr>
   
 </table>
 
 </p>
 
 </p>
 
 <p>

<u>Remarque</u> : les transactions annulées sont également présentes dans le tableau.
 </p>
 
 <p>

<u> Exemple d&#x27;un paiement réalisé avec une carte prépayée et le complément en carte VISA:</u>
 <p>
  <code><pre>
{&quot;trans_id&quot;:&quot;599495&quot;,
&quot;transactions&quot;:       
  {&quot;amount&quot;:&quot;1000&quot;,   
	&quot;operation_type&quot;:&quot;DEBIT&quot;,   
	&quot;capture_delay&quot;:&quot;0&quot;,   
	&quot;card_brand&quot;:&quot;ILLICADO_SB&quot;,      
	&quot;card_number&quot;:&quot;925000XXXXXXXXX1581&quot;,      
	&quot;payment_certificate&quot;:&quot;5d49440418b44cf957ee509cccdefeb6ebaa3b23&quot;,   
	&quot;presentation_date&quot;:&quot;2015-01-26T14:39:10Z&quot;,   
	&quot;trans_id&quot;:&quot;599495&quot;,    
	&quot;ext_trans_id&quot;:&quot;123456&quot;,   
	&quot;sequence_number&quot;:&quot;1&quot;,   
	&quot;trans_status&quot;:&quot;CAPTURED&quot;
  },    
  {&quot;amount&quot;:&quot;9000&quot;,       
	&quot;operation_type&quot;:&quot;DEBIT&quot;,       
	&quot;auth_number&quot;:&quot;3fee2a&quot;,       
	&quot;capture_delay&quot;:&quot;0&quot;,       
	&quot;card_brand&quot;:&quot;VISA&quot;,      
	&quot;card_number&quot;:&quot;497010XXXXXX0000&quot;,       
	&quot;expiry_month&quot;:&quot;6&quot;,       
	&quot;expiry_year&quot;:&quot;2015&quot;,      
	&quot;payment_certificate&quot;:&quot;7696aeeb76444595a6c027fa050aa6657764178c&quot;,        
	&quot;presentation_date&quot;:&quot;2015-01-26T14:39:30Z&quot;,       
	&quot;trans_id&quot;:&quot;599495&quot;,        
	&quot;sequence_number&quot;:&quot;2&quot;,       
	&quot;trans_status&quot;:&quot;AUTHORISED&quot;
  }        
]}
 </pre></code>

					
 </p>

 </p>
 
 </li>
 
 <li>
 
 <p>
Récupérez toutes les informations concernant le détail de la commande, le détail de l&#x27;acheteur et le détail de la livraison. 
 </p>
 
 <p>
Ces données sont présentes dans la réponse que si elles ont été envoyées dans le formulaire de paiement.
 </p>
 
 <p>
Leur valeur est identique à celle soumise dans le formulaire.
 </p>
 
 </li>
 
 <li>
 
 <p>
Procédez à la mise à jour de la commande.
 </p>
 
 </li>
 
</ol>
 <!-- emm1415811227559.xml -->
<h2>
11.7. Traiter les erreurs
</h2>
 
<p>

<u>Mise en place d&#x27;un fichier de log</u>
</p>
 
<p>
Durant la phase d&#x27;implémentation, il sera utile de disposer de logs notamment en cas de difficultés pour calculer la signature.
</p>
 
<p>
Nous conseillons toutefois de mettre en place un fichier de log journalier même après la mise en production du site marchand. 
</p>
 
<p>
Cela vous permettra d&#x27;analyser les données en cas de problèmes.
</p>
 
<p>
Idéalement le fichier de log devra contenir les données envoyées ou reçues, la chaîne obtenue lors du calcul de signature, avant l&#x27;application de l&#x27;algorithme SHA-1.
</p>
 
<p>

<u>Code d&#x27;erreur HTTP</u> 
</p>
 
<p>
En cas d&#x27;erreur durant les notifications, l&#x27;e-mail d&#x27;avertissement envoyé précise le code retour du protocole HTTP.
</p>
 
<p>
Il existe 5 catégories de codes retour :
</p>
 
<p>
 
<table>
     
 <tr>
 
  <td>
Catégorie de codes 
  </td>
 
  <td>
Description
  </td>
 
 </tr>
   
 <tr>
 
  <td>
1XX
  </td>
 
  <td>
Information
  </td>
 
 </tr>
 
 <tr>
 
  <td>
2XX
  </td>
 
  <td>
Succès
  </td>
 
 </tr>
 
 <tr>
 
  <td>
3XX
  </td>
 
  <td>
Redirection
  </td>
 
 </tr>
 
 <tr>
 
  <td>
4XX
  </td>
 
  <td>
Erreur du client
  </td>
 
 </tr>
 
 <tr>
 
  <td>
5XX
  </td>
 
  <td>
Erreur du serveur
  </td>
 
 </tr>
   
</table>
 
</p>
 
<p>
Les codes d&#x27;erreur les plus fréquemment retournés sont décrits dans la FAQ 
</p>
 
<p>

<b>Erreur fréquente</b> : 
</p>
 
<p>
Un fichier htaccess peut bloquer l&#x27;appel à l&#x27;URL de notification instantanée. 
</p>
 
<p>
Les fichiers .htaccess sont des fichiers de configuration des serveurs web Apache. Ils peuvent être placés dans n&#x27;importe quel répertoire du site marchand (la configuration s&#x27;applique au répertoire et à tous ceux qu&#x27;il contient n&#x27;ayant pas de tel fichier à l&#x27;intérieur).
</p>
 <!-- emm1415803124513.xml -->
