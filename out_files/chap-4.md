---
layout: docs
permalink: /docs/chap-4/
title: chap-4
---
<h1>
4. Comprendre le déroulement d&#x27;un paiement
</h1>
 
<p>
La procédure d’un paiement en ligne s’appréhende de manière différente du point de vue de l’acheteur et du marchand. 
</p>
 <!-- tla1406022036502.xml -->
<h2>
4.1. Définir les étapes d’un paiement - Vue acheteur
</h2>
 
<p>
Le diagramme ci-dessous présente la cinématique des échanges du point de vue de l&#x27;acheteur.
</p>
 
<p>
Cinématique des échanges – Vue acheteur
</p>
<img src="/docs_img/tla1406022174130.image" alt="DiagrammeFluxAcheteur"/> 
<ol>
 
 <li>
L’acheteur valide son panier.
 </li>
 
 <li>
Le site marchand redirige l’acheteur vers la plateforme de paiement. 
 <p>
Cette redirection s&#x27;effectue sous la forme d&#x27;un formulaire HTML POST en HTTPS. 
 </p>

 <p>
Les paramètres qui le composent sont décrits dans le chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer une demande de paiement</a></b>.
 </p>

 </li>
 
 <li>
La plateforme de paiement, après vérification des paramètres et de leur signature, présente la page de sélection du moyen de paiement. 
 <p>
Sélection du moyen de paiement
 </p>
<img src="/docs_img/tla1437748433397.image" alt="ChoixMoyenPaiement"/> 
 <p>
Si le moyen de paiement a été spécifié dans le formulaire, l’acheteur passe directement à l’étape 6.
 </p>

 </li>
 
 <li>
L’acheteur sélectionne son moyen de paiement.
 </li>
 
 <li>
Il clique sur 
<b>Valider</b>.
 </li>
 
 <li>
Il renseigne le numéro et la date d&#x27;expiration de sa carte. 
 <p>
Si la carte possède un cryptogramme visuel, ce dernier doit obligatoirement être renseigné.
 </p>
 
 <p>
Saisie des informations du moyen de paiement
 </p>
<img src="/docs_img/tla1437748495407.image" alt="SaisieDonneesBancaires"/> 
 </li>
 
 <li>
Il confirme sa saisie en cliquant sur 
<b>Valider</b>.
 </li>
 
 <li>
Si le marchand et la carte de l’acheteur sont enrôlés dans le programme 3D Secure, une authentification 3D Secure a lieu.
 </li>
 
 <li>
Une demande d&#x27;autorisation est effectuée auprès de la banque de l’acheteur, l’émetteur, en plus des contrôles de fraudes internes de la plateforme de paiement.
 </li>
 
 <li>
En cas de succès, une page de résumé est présentée à l’acheteur récapitulant les informations de la transaction. 
 <p>
Un bouton permettant un retour à la boutique est proposé.
 </p>

 </li>
 
</ol>
 
<p>
Récapitulatif de la transaction
</p>
<img src="/docs_img/tla1437748545920.image" alt="DetailPaiement"/> 
<p>
En cas d’échec, un message s’affiche. L’acheteur est informé du refus de la demande de paiement. Un bouton permettant d’annuler et de retourner à la boutique est proposé.
</p>
 
<p>
Page de résumé en cas d’échec de la transaction
</p>
<img src="/docs_img/tla1437748588430.image" alt="PageResumePaiementEchec"/> <!-- tla1406029892365.xml -->
<h2>
4.2. Définir les étapes d&#x27;un paiement - Vue marchand
</h2>
 
<p>
Le paiement en ligne, côté marchand, se déroule de la manière suivante:
</p>
 
<p>
Cinématique des échanges – Vue marchand
</p>
<img src="/docs_img/tla1437748633530.image" alt="DiagrammeFluxMarchand"/> 
<p>
 
<ol>
 
 <li>
L’acheteur valide son panier.
 </li>
 
 <li>
Le site marchand construit le formulaire à partir des données du panier de l’acheteur.
 </li>
 
 <li>
Le site marchand redirige l’acheteur vers la plateforme de paiement. Cette redirection se fait sous la forme d&#x27;un formulaire HTML POST en HTTPS. Les paramètres qui le composent sont décrits dans le chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>.
 </li>
 
 <li>
Après saisie des données du moyen de paiement par l’acheteur, la plateforme procède au paiement.
 </li>
 
 <li>
En fonction du paramétrage de la boutique (voir chapitre 
<b>Paramétrer les notifications</b>), un appel est automatiquement réalisé afin de transmettre le résultat au site marchand. 
 </li>
 
 <li>
Le site marchand analyse et traite le résultat du paiement. 
 </li>
 
 <li>
Il met à jour la base de données (état de la commande, état du stock etc…).
 </li>
 
 <li>
L’acheteur est informé du résultat du paiement sur la plateforme. S’il décide de retourner sur le site marchand, ce dernier le remercie et lui affiche l’état de sa commande.
 </li>
 
</ol>
 
</p>
 <!-- emm1415871023015.xml -->
<h2>
4.3. Cycle de vie des transactions
</h2>
 
<p>
Dans tous les schémas suivants, la légende suivante est adoptée : 
</p>
 
<p>
<img src="/docs_img/tla1415957306283.image" alt="tla1415957306283.image"/> Action du marchand nécessaire - manuelle Back Office ou automatique (webservice)
</p>
 <!-- tla1415949820786.xml -->
 <h3>
4.3.1.  Mode de validation automatique
</h3>
 
 <p>

 </p>
 <!-- tla1415949868132.xml -->
  <h4>
4.3.1.1.   Cycle de vie d’une transaction de paiement comptant immédiat
</h4>
 <img src="/docs_img/tla1415956040247.image" alt="tla1415956040247.image"/> 
  <p>
Suite à la demande de paiement, plusieurs contrôles sont automatiquement mis en oeuvre : 
  </p>
 
  <p>
 
  <ul>
 
   <li>
L’authentification 3D Secure.
   </li>
 
   <li>
Différents contrôles locaux réalisés directement par la plateforme de paiement (ceux-ci incluent potentiellement les contrôles liés à la souscription au service additionnel de contrôles anti-fraude).
   </li>
 
   <li>
Une demande d’autorisation est également effectuée auprès de la banque de l&#x27;acheteur, le jour même de la date de paiement, quelle que soit la date de remise en banque demandée. 
   <p>
Si l’un de ces contrôles échoue, la demande de paiement n’est pas acceptée. L&#x27;acheteur est informé du refus à l’écran. Dans le Back Office, la transaction est consultable avec le statut 
<b>Refusé</b>. 
   </p>

   <p>
Dans le cas contraire, la transaction prend le statut 
<b>En attente de remise</b>. 
   </p>
L&#x27;acheteur est informé de l’acceptation de sa demande de paiement et est destinataire d’un e-mail de confirmation. La transaction partira automatiquement en remise le jour demandé par le marchand. 
   <p>
Dans l’attente de cette remise, le marchand peut modifier la date de remise ainsi que le montant (modification du montant uniquement à la baisse, ce cas correspond à une livraison partielle par le marchand). 
   </p>

   <p>
Si nécessaire, il peut également annuler la transaction : celle-ci prend alors le statut 
<b>Annulé</b>. 
   </p>

   </li>
 
  </ul>
 
  </p>
 <!-- tla1415950397222.xml -->
  <h4>
4.3.1.2.   Cycle de vie d’une transaction de paiement comptant différé
</h4>
 
  <p>

<b>Délai de remise inférieur à la durée de validité de l&#x27;autorisation</b> 
  </p>
 
  <p>
(voir diagramme cycle de vie d&#x27;une transaction de paiement comptant immédiat).
  </p>
 
  <p>

<b>Délai de remise supérieur à la durée de validité de l&#x27;autorisation </b>
  </p>
 
  <p>
Toute transaction de paiement comptant différé réalisée avec le mode de validation automatique, et dont la demande d’autorisation à 1 euro
  </p>
 
  <p>
La demande d’autorisation est automatiquement effectuée : 
  </p>
 
  <p>
 
  <ul>
 
   <li>
fonctionnement par défaut : le jour de la date de remise en banque souhaitée,
   </li>
 
   <li>
fonctionnement avec autorisation anticipée : selon le moyen de paiement sélectionné, à J-Δ (voir <a href="#TODO-tla1415949281462.xml">tableau</a> illustrant la validité d&#x27;une autorisation) avant la date de remise en banque souhaitée. 
   <p>
Le mode par autorisation anticipée doit faire l&#x27;objet d&#x27;une demande auprès du Service Client. 
   </p>

   <p>
En cas de refus de type non frauduleux (voir <a href="#TODO-tla1408548356588.xml">tableau</a>), l&#x27;autorisation sera réitérée chaque jour jusqu&#x27;à J-2 avant la date de remise en banque
   </p>
Dans l’attente, le marchand peut annuler la transaction ou en modifier le montant (à la baisse uniquement) et/ou la date de remise. 
   </li>
 
  </ul>
 
  </p>
 
  <p>

  </p>
 
  <p>
Le diagramme suivant résume les différents statuts pouvant être pris par ce type de transaction (cas d&#x27;une demande d&#x27;autorisation non rejouée) : 
  </p>
 <img src="/docs_img/tla1415956296508.image" alt="tla1415956296508.image"/> <!-- tla1415950704803.xml -->
  <h4>
4.3.1.3.   Cycle de vie d’une transaction de paiement en plusieurs fois
</h4>
 
  <p>
La première échéance du paiement en plusieurs fois se comportera exactement comme une transaction de paiement comptant immédiat ou une transaction de paiement différé selon sa date de remise en banque. 
  </p>
 
  <p>
Les échéances suivantes sont par défaut positionnées en statut 
<b>En attente d’autorisation</b>. La banque de l&#x27;acheteur pourra refuser la demande d’autorisation. La plateforme de paiement informe alors le marchand du refus de la transaction par e-mail. 
  </p>
 
  <p>
Les demandes d’autorisation des échéances suivantes sont automatiquement effectuées comme une transaction de paiement différé, donc avec deux dates possibles : 
  <ul>
 
   <li>
fonctionnement par défaut : le jour de la date de remise en banque souhaitée,
   </li>
 
   <li>
fonctionnement avec autorisation anticipée : selon le moyen de paiement sélectionné, à J-Δ (voir <a href="#TODO-tla1415949281462.xml">tableau</a> illustrant la validité d&#x27;une autorisation) avant la date de remise en banque souhaitée. 
   </li>
 
  </ul>

  </p>
 
  <p>

  </p>
 
  <p>
Les échéances ultérieures suivent le diagramme d’état suivant (cas d&#x27;une demande d&#x27;autorisation non rejouée) :
  </p>
 
  <p>

  </p>
 <img src="/docs_img/tla1415956443007.image" alt="tla1415956443007.image"/> 
  <p>
L’annulation d’une échéance n’implique en aucun cas l’annulation des échéances suivantes restant à remettre en banque. 
  </p>
 <!-- tla1415950960317.xml -->
 <h3>
4.3.2.  Mode de validation manuelle
</h3>
 
 <p>

 </p>
 <!-- tla1415950986116.xml -->
  <h4>
4.3.2.1.   Cycle de vie d’une transaction de paiement comptant immédiat
</h4>
 
  <p>
Suite à la demande de paiement, des contrôles sont automatiquement mis en oeuvre : 
  </p>
 
  <p>
 
  <ul>
 
   <li>
L’authentification 3D Secure.
   </li>
 
  </ul>
 
  </p>
 
  <p>
 
  <ul>
 
   <li>
Différents contrôles locaux réalisés directement par la plateforme de paiement (ceux-ci incluent potentiellement les contrôles liés à la souscription au service additionnel du contrôle des risques).
   </li>
 
  </ul>
 
  </p>
 
  <p>
 
  <ul>
 
   <li>
Une demande d’autorisation est effectuée auprès de la banque de l&#x27;acheteur.
   </li>
 
  </ul>
 
  </p>
 
  <p>
Si l’un de ces contrôles échoue, la demande de paiement n’est pas acceptée. L&#x27;acheteur est informé du refus à l’écran. Dans le Back Office, la transaction est consultable avec le statut 
<b>Refusé</b>. 
  </p>
 
  <p>

  </p>
 
  <p>
Dans le cas contraire le paiement est accepté et la transaction est consultable dans le Back Office avec le statut 
<b>A Valider</b>.
  </p>
 
  <p>
Le marchand doit alors obligatoirement valider la transaction avant la date de remise demandée. Dans le cas contraire, la transaction prend le statut 
<b>Expiré</b> et ne peut plus être remise en banque.
  </p>
 
  <p>
 
  </p>
 
  <p>
Dès lors qu’une transaction est validée, elle passe en statut 
<b>En attente de remise</b>. 
  </p>
   
  <p>
Il peut également annuler la transaction si nécessaire. La transaction prend alors le statut 
<b>Annulé</b>.
  </p>
 <img src="/docs_img/tla1415956574473.image" alt="tla1415956574473.image"/> <!-- tla1415951388962.xml -->
  <h4>
4.3.2.2.   Cycle de vie d’une transaction de paiement comptant différé 
</h4>
 
  <p>

<b>Délai de remise inférieur à la durée de validité de l&#x27;autorisation</b> 
  </p>
 
  <p>
(voir diagramme cycle de vie d&#x27;une transaction de paiement comptant immédiat)
  </p>
 
  <p>

<b>Délai de remise supérieur à la durée de validité de l&#x27;autorisation </b>
  </p>
 
  <p>
Toute transaction de paiement comptant différé réalisée avec le mode de validation manuelle et dont la demande d’autorisation à 1 euro
  </p>
 
  <p>
La demande d’autorisation est automatiquement effectuée le jour de la remise en banque demandé, sous réserve que le marchand ait précédemment validé la transaction. 
  </p>
 
  <p>
Dans l’attente de la remise, le marchand peut annuler la transaction ou en modifier le montant et/ou la date de remise en banque. 
  </p>
 
  <p>
Ces transactions suivent le diagramme d’état suivant : 
  </p>
 <img src="/docs_img/tla1415983511186.image" alt="tla1415983511186.image"/> <!-- tla1415951699874.xml -->
  <h4>
4.3.2.3.   Cycle de vie d’une transaction de paiement en plusieurs fois 
</h4>
 
  <p>
La première échéance du paiement en plusieurs fois se comportera exactement comme une transaction de paiement comptant immédiat ou une transaction de paiement différé, selon la date de remise en banque demandée. 
  </p>
 
  <p>
Les échéances suivantes sont par défaut positionnées en statut 
<b>A valider et autoriser</b> tant que la première échéance n’aura pas été validée par le marchand. Leur bonne fin n’est pas garantie pour le marchand. En effet, la banque de l&#x27;acheteur peut refuser la demande d’autorisation. 
  </p>
 
  <p>

  </p>
 
  <p>

<b>La validation de la 1ère échéance vaut validation de toutes les échéances suivantes. Par contre, l’annulation d’une échéance ne vaut pas annulation des échéances ultérieures. </b>
  </p>
 
  <p>

  </p>
 <img src="/docs_img/tla1415983766360.image" alt="tla1415983766360.image"/> <!-- tla1415951899582.xml -->
 <h3>
4.3.3.  Spécificités liées aux autorisations anticipées
</h3>
 
 <p>
Pour activer les autorisations anticipées, veuillez contacter le service clients de la plateforme de paiement.
 </p>
 
 <p>
Ce processus s&#x27;applique uniquement pour les demandes d’autorisation : 
 <ul>
 
  <li>
du paiement comptant différé, 
  </li>
 
  <li>
des échéances, autres que la première, pour le paiement en plusieurs fois. 
  </li>
 
 </ul>

 </p>
 
 <p>
Le déclenchement de l&#x27;autorisation s&#x27;effectuera à J-Δ (voir durée de validité d&#x27;une autorisation pour chaque moyen de paiement) avant la date de remise en banque souhaitée.
 </p>
 
 <p>
En cas de refus par le serveur d&#x27;autorisation de la banque de l&#x27;acheteur, exclusivement pour un motif non frauduleux (voir <a href="#TODO-tla1408548356588.xml">tableau</a>), un processus réitère automatiquement les demandes d&#x27;autorisation jusqu&#x27;à J-2.
 </p>
   
 <p>
En cas de refus pour un motif frauduleux la transaction est considérée comme définitivement refusée.
 </p>
 <!-- emm1405084721287.xml -->
