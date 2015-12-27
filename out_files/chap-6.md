---
layout: docs
permalink: /docs/chap-6/
title: chap-6
---
<h1>
6. Paramétrer les notifications
</h1>
  
<p>
Le Back Office permet de gérer les événements qui génèreront un appel vers le site marchand et de configurer l’URL de la page à contacter.
</p>
 
<p>
Les schémas suivants illustrent, pour chaque événement, le statut de la transaction envoyé dans la notification.
</p>
 
<p>
La légende adoptée pour chacun est la suivante : 
</p>
 
<p>
<img src="/docs_img/tla1415957306283.image" alt="tla1415957306283.image"/> Action du marchand nécessaire - manuelle (Back Office) ou automatique (webservice)
</p>
 
<p>
<img src="/docs_img/tla1415980623200.image" alt="tla1415980623200.image"/> Action de l&#x27;acheteur
</p>
 <!-- tla1426244216726.xml -->
<h2>
6.1. Notifications des différents statuts pour un paiement comptant
		immédiat
</h2>
 
<p>
Diagramme de flux - Paiement comptant immédiat
</p>
<img src="/docs_img/tla1437643182518.image" alt="tla1437643182518.image"/> 
<p>

</p>
 
<p>
 
<table>
       
 <tr>
 
  <td>
Evénement 
  </td>
 
  <td>
Statut notifé
  </td>
 
  <td>
Nom de la règle à paramétrer
  </td>
 
 </tr>
   
 <tr>
 
  <td>
Abandon par l&#x27;acheteur
  </td>
 
  <td>
ABANDONED
  </td>
 
  <td>
URL de notification sur annulation
  </td>
 
 </tr>
 
 <tr>
 
  <td>
Annulation par le marchand
  </td>
 
  <td>
CANCELED
  </td>
 
  <td>
URL de notification sur une opération en provenance du Back Office
  </td>
 
 </tr>
 
 <tr>
 
  <td>
Réponse à la demande d&#x27;autorisation
  </td>
 
  <td>
AUTHORISED_TO_VALIDATE, AUTHORISED, REFUSED 
  </td>
 
  <td>
URL de notification à la fin du paiement
  </td>
 
 </tr>
   
</table>
 
</p>
 
<p>

</p>
 <!-- tla1426244313840.xml -->
<h2>
6.2. Notifications des différents statuts pour un paiement comptant
		différé
</h2>
 
<p>
Diagramme de flux - Paiement comptant différé
</p>
<img src="/docs_img/tla1437643280219.image" alt="tla1437643280219.image"/> 
<p>
Δ : durée de validité d&#x27;autorisation.
</p>
 
<p>
 
<table>
       
 <tr>
 
  <td>
Evénement 
  </td>
 
  <td>
Statut notifé
  </td>
 
  <td>
Nom de la règle à paramétrer
  </td>
 
 </tr>
   
 <tr>
 
  <td>
Abandon par l&#x27;acheteur
  </td>
 
  <td>
ABANDONED
  </td>
 
  <td>
URL de notification sur annulation
  </td>
 
 </tr>
 
 <tr>
 
  <td>
Annulation par le marchand
  </td>
 
  <td>
CANCELED
  </td>
 
  <td>
URL de notification sur une opération en provenance du Back Office
  </td>
 
 </tr>
 
 <tr>
 
  <td>
Validation par le marchand
  </td>
 
  <td>
WAITING_AUTHORISATION
  </td>
 
  <td>
URL de notification sur une opération en provenance du Back Office
  </td>
 
 </tr>
 
 <tr>
 
  <td>
Réponse à la demande d&#x27;autorisation à 
  </td>
 
  <td>
REFUSED, WAITING_AUTHORISATION, WAITING_AUTHORISATION_TO_VALIDATE
  </td>
 
  <td>
URL de notification à la fin du paiement
  </td>
 
 </tr>
 
 <tr>
 
  <td>
Réponse à la demande d&#x27;autorisation
  </td>
 
  <td>
AUTHORISED, REFUSED, AUTHORISED_TO_VALIDATE
  </td>
 
  <td>
URL de notification sur autorisation par batch
  </td>
 
 </tr>
   
</table>
 
</p>
 <!-- tla1426244392911.xml -->
<h2>
6.3. Notifications des différents statuts pour les échéances d&#x27;un paiement en
		plusieurs fois
</h2>
 
<p>
Diagramme de flux - Echéances d&#x27;un paiement en plusieurs fois
</p>
<img src="/docs_img/tla1437643349015.image" alt="tla1437643349015.image"/> 
<p>
Δ : durée de validité d&#x27;autorisation.
</p>
 
<p>

</p>
 
<p>
 
<table>
       
 <tr>
 
  <td>
Evénement 
  </td>
 
  <td>
Statut notifé
  </td>
 
  <td>
Nom de la règle à paramétrer
  </td>
 
 </tr>
   
 <tr>
 
  <td>
Annulation par le marchand
  </td>
 
  <td>
CANCELED
  </td>
 
  <td>
URL de notification sur une opération en provenance du Back Office
  </td>
 
 </tr>
 
 <tr>
 
  <td>
Réponse à la demande d&#x27;autorisation
  </td>
 
  <td>
AUTHORISED, REFUSED 
  </td>
 
  <td>
URL de notification sur autorisation par batch
  </td>
 
 </tr>
   
</table>
 
</p>
 <!-- tla1437400690314.xml -->
<h2>
6.4. Configurer les notifications
</h2>
 
<p>
Plusieurs types de notifications sont mises à disposition dans le Back Office. Elle permettent de gérer les évènements (abandon par l&#x27;acheteur, annulation par le marchand, validation par le marchand...) qui génèreront un appel vers le site marchand et de configurer l&#x27;URL de la page à contacter.
</p>
 
<p>
Pour accéder à la gestion des règles de notification : 
</p>
 
<p>
 
<ol>
 
 <li>
Connectez-vous à : <a href="https://secure.payzen.eu/vads-merchant/">https://secure.payzen.eu/vads-merchant/</a>.
 </li>
 
 <li>
Allez dans le menu : 
<b>Paramétrage</b> &gt; 
<b>Règles de notifications</b>. 
 <p>
Règles de notification
 </p>
<img src="/docs_img/tla1425653374072.image" alt="ListeURLNotification"/><img src="/docs_img/tla1444725978675.image" alt="ListeURLNotificationSepaAll"/>
 </li>
 
</ol>
 
</p>
 <!-- emm1405085388157.xml -->
 <h3>
6.4.1.  Configurer la notification à la fin du paiement
</h3>
  
 <p>
Cette notification est indispensable pour communiquer le résultat d&#x27;une demande de paiement.
 </p>
  
 <ol>
   
  <li>
 
  <p>
Effectuez un clic droit sur la ligne 
<b>URL de notification à la fin du paiement.</b>
  </p>
  
  </li>
 
  <li>
 
  <p>
Sélectionnez 
<b>Gérer la règle</b>.
  </p>
 
  </li>
 
  <li>
 
  <p>
 Renseignez l’URL de votre page dans les champs 
<b>URL à appeler en mode TEST </b>et
<b> URL à appeler en mode PRODUCTION.</b> 
  </p>
 
  <p>
 
  <p>
URL de notification à la fin du paiement
  </p>
<img src="/docs_img/tla1425654122255.image" alt="GererURLNotifFinPaiement"/> 
  </p>
 
  </li>
 
  <li>
 
  <p>
Renseignez le champ 
<b>Adresse(s) e-mail(s) à avertir en cas d’échec</b>. 
  </p>
 
  </li>
 
  <li>
 
  <p>
Pour spécifier plusieurs adresses e-mails, séparez-les par un point-virgule.
  </p>
 
  </li>
 
 </ol>
 
 <p>
Si la plateforme n&#x27;arrive pas à joindre l&#x27;URL de votre page, alors un e-mail est envoyé à l&#x27;adresse spécifiée à l&#x27;étape 6.
 <p>
Il contient :
 </p>

 <p>
 
 <ul>
 
  <li>
Le code HTTP de l&#x27;erreur rencontrée
  </li>
 
  <li>
Des éléments d&#x27;analyse en fonction de l&#x27;erreur
  </li>
 
  <li>
Ses conséquences 
  </li>
 
  <li>
La procédure à suivre depuis le Back Office 
  </li>
 
 </ul>
 
 </p>

 </p>
 <!-- tla1406037302300.xml -->
 <h3>
6.4.2.  Configurer la notification du résultat final d’un paiement différé
</h3>
 
 <p>
Cette notification est indispensable pour communiquer le résultat d’un paiement différé :
 </p>

 <p>
 
 <ul>
 
  <li>
En cas de paiement accepté.
  </li>
 
  <li>
En cas de paiement refusé.
  </li>
 
 </ul>
 
 </p>

 <p>
Elle permet au site marchand d’être notifié lors d’une demande d’autorisation. 
 </p>

 <p>

<b>Exemple</b>:
 </p>
Pour un paiement différé avec un délai de remise à 60 jours, la demande d’autorisation n’est pas faite lors du paiement. Le site marchand sera contacté lors de la demande d’autorisation par la règle 
<b>URL de notification sur autorisation par batch</b>.
 <p>
Cette règle est 
<b>désactivée par défaut.</b>
 </p>

 <p>

 </p>

 <p>
Pour paramétrer cette notification :
 </p>
 
 <ol>
   
  <li>
 
  <p>
Effectuez un clic droit sur la ligne 
<b>URL de notification sur autorisation par batch</b>.
  </p>
 
  <p>
  
  </p>
 
  </li>
 
  <li>
 
  <p>
Sélectionnez 
<b>Gérer la règle</b>.
  </p>
 
  </li>
 
  <li>
 
  <p>
Renseignez l’URL de votre page dans les champs 
<b>URL à appeler en mode TEST </b> et
<b> URL à appeler en mode </b>
<b>PRODUCTION</b>.
  </p>
 
  <p>
  
  <p>
Configurer la notification sur autorisation par batch
  </p>
<img src="/docs_img/tla1425654452351.image" alt="GererURLNotifSurAutoParBatch"/> 
  </p>
 
  </li>
 
  <li>
 
  <p>
Renseignez le champ 
<b>Adresses(s) e-mail(s) à avertir en cas d’échec</b>.
  </p>
 
  </li>
 
  <li>
 
  <p>
Pour spécifier plusieurs adresses e-mails, séparez-les par un point-virgule.
  </p>
 
  </li>
 
  <li>
 
  <p>
Configurez le 
<b>Rejeu automatique en cas d’échec</b>.
  </p>
 
  <p>
Cette option permet de renvoyer automatiquement la notification vers le site marchand en cas d&#x27;échec, et ce, jusqu&#x27;à 4 fois.
  </p>
 
  <p>
Pour plus d&#x27;informations, reportez-vous au chapitre 
<b>Activer le rejeu automatique</b>.
  </p>
 
  </li>
 
  <li>
 
  <p>
Sauvegardez vos modifications.
  </p>
 
  </li>
 
  <li>
 
  <p>
Activez la règle, en effectuant un clic droit sur 
<b>URL de notification sur autorisation par batch</b> et sélectionnez 
<b>Activer la règle</b>.
  </p>
 
  </li>
 
 </ol>
 
 <p>
 
 <p>
Si la plateforme n’arrive pas à joindre l’URL de votre page, alors un e-mail est envoyé à l’adresse spécifiée à l&#x27;étape 6. 
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
des pistes d’analyse en fonction de l’erreur,
  </li>
 
  <li>
la procédure à suivre depuis le 
<b>Back Office</b> pour renvoyer la requête vers l’URL définie à l’étape 5.
  </li>
 
 </ul>
 
 </p>
 
 </p>
 <!-- tla1406039141891.xml -->
 <h3>
6.4.3.  Configurer la notification en cas d&#x27;abandon/annulation
</h3>
 La plateforme de paiement peut notifier systématiquement le site marchand :
 <p>
 
 <ul>
 
  <li>
En cas d’abandon/annulation de la part de l’acheteur, via le bouton 
<b>Annuler et retourner à la boutique</b>.
  </li>
 
  <li>
Lorsque l&#x27;acheteur n&#x27;a pas terminé son paiement avant l&#x27;expiration de sa session de paiement. 
  <p>

<b>La durée maximale d&#x27;une session de paiement est de 10 minutes</b>. 
  </p>

  </li>
 
 </ul>
 
 </p>

 <p>

 </p>

 <p>

 </p>

 <p>
Pour paramétrer cette notification:
 </p>
 
 <ol>
   
  <li>
 
  <p>
Effectuez un clic droit sur la ligne 
<b>URL de notification sur annulation</b>.
  </p>
 
  </li>
 
  <li>
 
  <p>
Sélectionnez 
<b>Gérer la règle.</b>
  </p>
 
  </li>
 
  <li>
 
  <p>
Renseignez l’URL de votre page dans les champs 
<b>URL à appeler en mode TEST </b>et
<b> URL à appeler en mode PRODUCTION.</b>
  </p>
 
  </li>
 
  <li>
 
  <p>
Renseignez 
<b>Adresses(s) e-mail(s) à avertir en cas d’échec.</b> 
  </p>
 
  </li>
 
  <li>
 
  <p>
Pour spécifier plusieurs adresses séparez-les par un point-virgule.
  </p>
 
  </li>
 
  <li>
 
  <p>
Configurez le 
<b>Rejeu automatique en cas d’échec</b>.
  </p>
 
  <p>
Cette option permet de renvoyer automatiquement la notification vers le site marchand en cas d&#x27;échec, et ce, jusqu&#x27;à 4 fois.
  </p>
 
  <p>
Pour plus d&#x27;informations, reportez-vous au chapitre 
<b>Activer le rejeu automatique</b>
  </p>
 
  </li>
 
  <li>
 
  <p>
Sauvegardez vos modifications.
  </p>
 
  </li>
 
 </ol>
 
 <p>
  
 <p>
Si la plateforme n’arrive pas à joindre l’URL de votre page, alors un e-mail est envoyé à l’adresse spécifiée à l&#x27;étape 6. 
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
des éléments d’analyse en fonction de l’erreur,
  </li>
 
  <li>
la procédure à suivre depuis le Back Office 
  </li>
 
 </ul>
 
 </p>
 
 </p>
 <!-- vin1426004375534.xml -->
 <h3>
6.4.4.  Configurer la notification sur modification par batch
</h3>
  
 <p>
La plateforme de paiement peut notifier systématiquement le site marchand lorsqu&#x27;une transaction avec un statut 
<b>A valider</b> est expirée. L&#x27;expiration déclenche la notification. Le statut 
<b>Expiré</b> est définitif. 
 </p>
 
 <p>
Il est recommandé d&#x27;activer cette notification pour des transactions PayPal (mode Order) afin d&#x27;être notifié de la remise.
 </p>
  
 <ol>
   
  <li>
 
  <p>
Effectuez un clic droit sur la ligne 
<b>URL de notification sur modification par batch.</b>
  </p>
 
  </li>
 
  <li>
 
  <p>
Sélectionnez 
<b>Gérer la règle</b>.
  </p>
 
  </li>
 
  <li>
 
  <p>
 Renseignez l’URL de votre page dans les champs 
<b>URL à appeler en mode TEST </b>et
<b> URL à appeler en mode PRODUCTION.</b> 
  </p>
 
  </li>
 
  <li>
 
  <p>
Renseignez le champ 
<b>Adresse(s) e-mail(s) à avertir en cas d’échec</b>. 
  </p>
 
  </li>
 
  <li>
 
  <p>
Pour spécifier plusieurs adresses e-mails, séparez-les par un point-virgule.
  </p>
 
  </li>
 
 </ol>
 
 <p>
Si la plateforme n&#x27;arrive pas à joindre l&#x27;URL de votre page, alors un e-mail est envoyé à l&#x27;adresse spécifiée à l&#x27;étape 6.
 <p>
Il contient :
 </p>

 <p>
 
 <ul>
 
  <li>
Le code HTTP de l&#x27;erreur rencontrée
  </li>
 
  <li>
Des éléments d&#x27;analyse en fonction de l&#x27;erreur
  </li>
 
  <li>
Ses conséquences 
  </li>
 
  <li>
La procédure à suivre depuis le Back Office 
  </li>
 
 </ul>
 
 </p>

 </p>
 <!-- tla1424363402385.xml -->
<h2>
6.5. Activer le rejeu automatique
</h2>
  
<p>
Cette option permet de renvoyer automatiquement la notification vers le site marchand en cas d&#x27;échec, et ce, jusqu&#x27;à 4 fois.
</p>
  
<ol>
 
 <li>
 
 <p>
Connectez-vous à : <a href="https://secure.payzen.eu/vads-merchant/">https://secure.payzen.eu/vads-merchant/</a>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Allez dans le menu : 
<b>Paramétrage</b> &gt; 
<b>Règles de notifications</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Effectuez un clic droit sur une des règles de notifications affichées.
 </p>
 
 </li>
 
 <li>
 
 <p>
Sélectionnez 
<b>Gérer la règle</b>.
 </p>
 
 <p>
 
 <p>
URL de notification à la fin du paiement
 </p>
<img src="/docs_img/tla1425654122255.image" alt="GererURLNotifFinPaiement"/> 
 </p>
 
 </li>
 
 <li>
 
 <p>
Renseignez le champ 
<b>Adresse(s) e-mail(s) à avertir en cas d’échec</b>. 
 </p>
 
 </li>
 
 <li>
 
 <p>
Pour spécifier plusieurs adresses e-mails, séparez-les par un point-virgule.
 </p>
 
 </li>
 
</ol>
 
<p>

<b>Remarque : </b>
<p>
Lors du rejeu automatique, certaines informations ne sont pas enregistrées en base de données ou sont modifiées.
</p>

<p>

</p>

<p>

<b>Exemples de champs non disponibles / non enregistrés en base de données : </b>
</p>

<p>
 
<ul>
 
 <li>

<b>vads_page_action</b> 
 </li>
 
 <li>

<b>vads_payment_config</b> 
 </li>
 
 <li>

<b>vads_action_mode</b> 
 </li>
 
</ul>
 
</p>

<p>

</p>

<p>

<b>Exemples de champs envoyés avec des valeurs différentes : </b>
</p>

<p>
 
<ul>
 
 <li>

<b>vads_url_check_src</b> valorisé à 
<b>RETRY</b>,
 </li>
 
 <li>

<b>vads_trans_status</b>. Le statut de la transaction suite à cette opération varie en fonction de son statut au moment où l&#x27;URL est appelée (voir chapitre 
<b>Cycle de vie des transactions</b>
 </li>
 
 <li>

<b>vads_hash</b> valorisé différemment en tenant compte des nouvelles valeurs,
 </li>
 
 <li>

<b>signature</b> valorisé différemment en tenant compte des nouvelles valeurs.
 </li>
 
</ul>
 
</p>

</p>
 <!-- tla1424437576553.xml -->
<h2>
6.6. Rejouer manuellement la notification
</h2>
  
<p>
Cette option permet de réexécuter manuellement l&#x27;URL de notification depuis le Back Office lorsqu&#x27;une transaction est en erreur.
</p>
  
<ol>
 
 <li>
 
 <p>
Connectez-vous à : <a href="https://secure.payzen.eu/vads-merchant/">https://secure.payzen.eu/vads-merchant/</a>
 </p>
 
 </li>
 
 <li>
 
 <p>
Recherchez la transaction pour laquelle vous souhaitez rejouer manuellement la notification.
 </p>
 
 </li>
 
 <li>
 
 <p>
Effectuez un clic droit sur la transaction et sélectionnez 
<b>Exécuter l&#x27;URL de notification</b>.
 </p>
 
 <p>
Un message vous informe de la bonne exécution de cette commande si votre application est à nouveau disponible.
 </p>
 
 <p>
 
 <p>
Vous pourrez, dans tous les cas, visualiser le résultat de votre action dans l&#x27;historique des évènements de la transaction et éventuellement analyser les messages d&#x27;erreur si le problème persiste.
 </p>
 
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>
 
</p>
 
<p>
Lorsque le rejeu est effectué manuellement depuis le Back Office, certaines informations ne sont pas enregistrées en base de données ou sont modifiées.
</p>
 
<p>

</p>
 
<p>

<b>Exemples de champs non disponibles / non enregistrés en base de données : </b>
</p>
 
<p>
 
<ul>
 
 <li>

<b>vads_page_action</b> 
 </li>
 
 <li>

<b>vads_payment_config</b> 
 </li>
 
 <li>

<b>vads_action_mode</b> 
 </li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>

<b>Exemples de champs envoyés avec des valeurs différentes : </b>
</p>
 
<p>
 
<ul>
 
 <li>

<b>vads_url_check_src</b> valorisé à 
<b>BO</b>, 
 </li>
 
 <li>

<b>vads_trans_status</b>. Le statut de la transaction suite à cette opération varie en fonction de son statut au moment où l&#x27;URL est appelée (voir chapitre 
<b><a href="#TODO-emm1415871023015.xml">Cycle de vie des transactions</a></b>
 </li>
 
 <li>

<b>vads_hash</b> valorisé différemment en tenant compte des nouvelles valeurs,
 </li>
 
 <li>

<b>signature</b> valorisé différemment en tenant compte des nouvelles valeurs.
 </li>
 
</ul>
 
</p>
 
<p>

</p>
 
</p>
 <!-- tla1433144988275.xml -->
<h2>
6.7. Configurer les e-mails envoyés à l&#x27;acheteur
</h2>
  
<p>
Le Back Office offre la possibilité au marchand de configurer des e-mails à destination de l&#x27;acheteur :
</p>
 
<p>
 
<ul>
 
 <li>
E-mail de confirmation d&#x27;abonnement.
 </li>
 
 <li>
E-mail de confirmation de paiement.
 </li>
 
 <li>
E-mail de confirmation d&#x27;inscription.
 </li>
 
</ul>
 
</p>
  
<ol>
 
 <li>
 
 <p>
Connectez-vous à : <a href="https://secure.payzen.eu/vads-merchant/">https://secure.payzen.eu/vads-merchant/</a>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Allez dans le menu : 
<b>Paramétrage</b> &gt; 
<b>Règles de notifications</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Sélectionnez l&#x27;onglet 
<b>E-mail envoyé à l&#x27;acheteur</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Effectuez un clic droit sur le libellé d&#x27;un e-mail et sélectionnez 
<b>Activer la règle</b>.
 </p>
 
 <p>
Pour personnaliser un e-mail :
 </p>
 
 </li>
 
 <li>
 
 <p>
Effectuez un clic droit sur le libellé d&#x27;un e-mail dont la règle est activée et sélectionnez 
<b>Gérer la règle</b>.
 </p>
 
 <p>
Trois onglets sont mis à disposition. 
 </p>
 
 <p>
 
 <ul>
 
  <li>

<b>Paramétrage </b>
  <p>
Il permet de personnaliser l&#x27;e-mail qui sera envoyéle libellé de la règle.
  </p>

  </li>
 
  <li>

<b>Conditions de la règle</b>
  <p>
Il permet de créer une liste (éventuellement vide) de conditions d&#x27;exécution de la règle (dépend de l&#x27;évènement déclencheur). Une condition est constituée d&#x27;une variable, d&#x27;un opérateur de comparaison et d&#x27;une valeur de référence. 
  </p>

  <p>
Exemple : &quot;mode = TEST&quot;, &quot;montant supérieur à 1000&quot;. Lors de l&#x27;exécution d&#x27;une règle, la valeur de la variable est récupérée et comparée à la valeur de référence. Toutes les conditions doivent être validées pour que la règle soit exécutée.
  </p>

  </li>
 
  <li>

<b>Informations</b>
  <p>
Il affiche un résumé de la règle.
  </p>

  </li>
 
 </ul>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Sélectionnez l&#x27;onglet 
<b>Paramétrage</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Personnalisez le contenu de l&#x27;e-mail en fonction de vos besoins.
 </p>
 
 <p>
 
 <ol>
 
  <li>
Cliquez sur 
<b>Paramétrage e-mail acheteur</b> pour afficher le contenu de l&#x27;e-mail &quot;par défaut&quot; commun à tous les marchands utilisant la plateforme de paiement.
  </li>
 
  <li>
Sélectionnez l&#x27;onglet correspondant à la langue de l&#x27;e-mail que vous souhaitez personnaliser.
  </li>
 
  <li>
Cliquez sur 
<b>Personnaliser des valeurs de texte par défaut</b>.
  </li>
 
  <li>
Modifiez le texte de l&#x27;e-mail.
  </li>
 
  <li>
Cliquez sur 
<b>Champs à inclure</b> pour afficher la liste des champs disponibles pour personnaliser l&#x27;e-mail.
  </li>
 
  <li>
Sélectionnez les champs que vous souhaitez inclure dans l&#x27;e-mail. Un récapitulatif détaillé du traitement de la demande sera ajouté au contenu de l&#x27;e-mail.
  </li>
 
 </ol>
 
 </p>
 
 <p>

<i>
<u>Remarque :</u></i>
 </p>
 
 <p>

<i>Pour visualiser au préalable les modifications effectuées, cliquez sur 
<b>Prévisualiser l&#x27;e-mail</b> situé en bas de la boîte de dialogue.</i>
 </p>
 
 </li>
 
</ol>
 <!-- tla1433405116487.xml -->
<h2>
6.8. Configurer les e-mails envoyés au marchand
</h2>
  
<p>
Par défaut la plateforme de paiement peut notifier le marchand dans les cas suivants :
</p>
 
<p>
 
<ul>
 
 <li>
E-mail de confirmation de paiement 
 </li>
 
 <li>
E-mail de refus de paiement différé
 </li>
 
 <li>
E-mail de confirmation d&#x27;inscription client 
 </li>
 
 <li>
E-mail de refus échéance de paiement en n fois
 </li>
 
 <li>
E-mail de confirmation d&#x27;abonnement
 </li>
 
 <li>
E-mail de re-génération du certificat
 </li>
 
</ul>
 
</p>
  
<ol>
 
 <li>
 
 <p>
Connectez-vous à : <a href="https://secure.payzen.eu/vads-merchant/">https://secure.payzen.eu/vads-merchant/</a>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Allez dans le menu : 
<b>Paramétrage</b> &gt; 
<b>Règles de notifications</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Sélectionnez l&#x27;onglet 
<b>E-mail envoyé au marchand</b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Effectuez un clic droit sur le libellé d&#x27;un e-mail et sélectionnez 
<b>Activer la règle</b>.
 </p>
 
 <p>
Pour personnaliser un e-mail :
 </p>
 
 </li>
 
 <li>
 
 <p>
Effectuez un clic droit sur le libellé d&#x27;un e-mail dont la règle est activée et sélectionnez 
<b>Gérer la règle</b>.
 </p>
 
 <p>
Trois onglets sont mis à disposition.
 </p>
 
 <p>

 </p>
 
 <p>
 
 <ul>
 
  <li>

<b>Paramétrage </b>
  <p>
Il permet de personnaliser l&#x27;e-mail qui sera envoyé.
  </p>

  </li>
 
  <li>

<b>Conditions de la règle</b>
  <p>
Il permet de créer une liste (éventuellement vide) de conditions d&#x27;exécution de la règle (dépend de l&#x27;évènement déclencheur). Une condition est constituée d&#x27;une variable, d&#x27;un opérateur de comparaison et d&#x27;une valeur de référence. 
  </p>

  <p>
Exemple : &quot;mode = TEST&quot;, &quot;montant supérieur à 1000&quot;. Lors de l&#x27;exécution d&#x27;une règle, la valeur de la variable est récupérée et comparée à la valeur de référence. Toutes les conditions doivent être validées pour que la règle soit exécutée.
  </p>

  </li>
 
  <li>

<b>Informations</b>
  <p>
Il affiche un résumé de la règle.
  </p>

  </li>
 
 </ul>
 
 </p>
 
 </li>
 
 <li>
 
 <p>
Sélectionnez l&#x27;onglet 
<b>Paramétrage </b>.
 </p>
 
 </li>
 
 <li>
 
 <p>
Personnalisez le contenu de l&#x27;e-mail en fonction de vos besoins.
 </p>
 
 <p>
 
 <ol>
 
  <li>
Cliquez sur 
<b>Paramétrage général</b> pour spécifier l&#x27;adresse e-mail à notifier et facultativement, le gestionnaire de la société et/ou le contact technique de la société et/ou le gestionnaire de la boutique.
  </li>
 
  <li>
Cliquez sur 
<b>Paramétrage e-mail</b> pour afficher le contenu de l&#x27;e-mail &quot;par défaut&quot; commun à tous les marchands utilisant la plateforme de paiement.
  </li>
 
  <li>
Sélectionnez l&#x27;onglet correspondant à la langue de l&#x27;e-mail que vous souhaitez personnaliser.
  </li>
 
  <li>
Cliquez sur 
<b>Personnaliser des valeurs de texte par défaut</b>.
  </li>
 
  <li>
Modifiez le texte de l&#x27;e-mail.
  </li>
 
  <li>
Cliquez sur 
<b>Champs à inclure</b> pour afficher la liste des champs disponibles pour personnaliser l&#x27;e-mail.
  </li>
 
  <li>
Sélectionnez les champs que vous souhaitez inclure dans l&#x27;e-mail. Un récapitulatif détaillé du traitement de la demande sera ajouté au contenu de l&#x27;e-mail.
  </li>
 
 </ol>
 
 </p>
 
 <p>

<i>
<u>Remarque :</u></i>
 </p>
 
 <p>

<i>Pour visualiser au préalable les modifications effectuées, cliquez sur 
<b>Prévisualiser l&#x27;e-mail</b> situé en bas de la boîte de dialogue.</i>
 </p>
 
 </li>
 
</ol>
 <!-- emm1405083451541.xml -->
