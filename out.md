# Historique du document
 
       
|  Version|  Date|  Commentaire|  
| - | - | - |   
|  3.5|  23/11/2015|   
**Dictionnaire de données** 
 * vads_payment_cards et vads_contracts : ajout de valeurs.
 * Précisions apportées sur le format des champs :
 * vads_cust_address
 
 * vads_ship_to_street
 * vads_ship_to_street2
 
 * vads_trans_status : ajout du statut **INITIAL** dans la liste des statuts possibles.
 * vads_change_rate
 * vads_recurrence_number
  |   
|  3.4|  01/10/2015|  
Correction du montant pour une pré autorisation**Dictionnaire de données**
 
 * Correction du format du champ vads_product_labelN
 * Correction du nom du champ vads_product_vatN
 * Ajout du champ :
 * vads_cust_national_id
 
  |   
|  3.3a|  24/07/2015|  **Chapitre supplémentaire**
 
 * Configurer la notification sur modification par batch
  
Modification des chapitres :
 
 * Utiliser une i-frame
 * vads_trans_id
  |   
|  3.3|  07/07/2015|  
**Chapitres supplémentaires**
 
 * Configurer les e-mails envoyés à l'acheteur.
 * Configurer les e-mails envoyés au marchand.
  

Complément d'information sur l'utilisation d'une i-frame.
**Dictionnaire de données**
 
 * Ajout des champs :
 * vads_trans_uuid
 * vads_risk_assessment_result
 * vads_product_vatN
 
  
 
 * vads_bank_product : ajout des valeurs pour les cartes CB pures.
 * vads_risk_analyzis_result : ajout de valeurs.
 * vads_payment_cards : ajout de valeurs.
  |   
|  3.2|  27/04/2015|  **Dictionnaire de données**
Correction d’une erreur pour le champ vads_ship_to_type|   
|  3.1|  02/03/2015|   
URL Serveur renommé en URL de notification 
**Chapitres supplémentaires** 
 
 * Gérer les paramètres de votre boutique par fichier de configuration
 * Activer le rejeu automatique
 * Rejouer manuellement la notification
   
 
Complément d'information sur l'utilisation d'une i-frame. 
 
**Dictionnaire de données** 
 
 * Ajout des champs :
 * vads_payment_seq
 * vads_cust_legal_name
 * vads_ship_to_legal_name
 
   
 
 * Ajout de la valeur E_CV dans la liste des moyens de paiement (réseau ANCV)
 * Précision sur le champ vads_url_check
    |   
|  3.0|  21/11/2014|  Refonte globale de la documentation.|       
 
 
 
 
 
 
 
 
 
 
 
     
|   **Confidentialité** |   
|   Toutes les informations contenues dans ce document sont considérées comme confidentielles. L’utilisation de celles-ci en dehors du cadre de cette consultation ou la divulgation à des personnes extérieures est soumise à l’approbation préalable de Lyra Network. |       

# Contacter l'assistance technique
 
En cas de problème de connexion au Back Office, utilisez le lien « mot de passe oublié ou compte bloqué ». 
 
Pour toute question technique ou demande d'assistance, nos services sont disponibles du lundi au vendredi, de 9h à 18hde 8h à 17h : 
 
        
|  |  par téléphone au : |    depuis la France,la Suisse,l'Allemagnele Brésil
  Accessible 24H sur 24 (Tarification de ce numéro : coût d'un appel local depuis un poste fixe.) 
 pour les clients Banque Populaire 
  pour les clients Caisse d'Epargne

()

|   
|  |  |   depuis l'étranger,

|   
|  |  par e-mail :|  |       
 
Pour faciliter le traitement de vos demandes, il vous sera demandé de communiquer votre identifiant de boutique (numéro à 8 chiffres). 
Cette information est disponible dans l'e-mail d'inscription de votre boutique, ou dans le Back Office (menu **Paramétrage** > **Boutique** > **Configuration**). 
 

# Les différents types de paiement


## Paiement comptant immédiat
 
Un paiement est considéré comme **comptant immédiat** si :
 * le montant est débité en une seule fois,
 * le délai de remise en banque est de 0 jour.
   
Une demande d'autorisation pour le montant global est effectuée. Le paiement est remis en banque dès que possible.  

## Paiement comptant différé
 
Un paiement est considéré comme **comptant différé** si : 
 
 * le montant est débité en une seule fois,
 * le délai de remise en banque est strictement supérieur à 0 jour.
La date de remise ne peut être supérieure à 12 mois après la date d’enregistrement du paiement.
     
 
Il existe deux types de paiements comptants différés : 
 
 * **Délai de remise inférieur à la durée de validité de l'autorisation** (voir section **Validité d'une autorisation** présentée plus bas)
   
Une demande d'autorisation pour le montant global est effectuée. Sans modification du marchand, le paiement est remis en banque à la date de présentation demandée. 
 
 * **Délai de remise supérieur à la durée de validité de l'autorisation** (voir section **Validité d'une autorisation** présentée plus bas)
   
Une demande d'autorisation à 1 euro100 XPF1 CHF1 BRL est effectuée au moment de l’enregistrement du paiement pour s’assurer de la validité de la carte.  
Si cette autorisation à 1 euro100 XPF1 CHF1 BRL est acceptée, le paiement est enregistré.  
J-1 à la date de présentation demandée, une demande d’autorisation pour le montant global est effectuée.  
Le paiement peut être accepté ou refusé. Le marchand doit donc être très vigilant sur ce type de paiement avant de délivrer un bien / un service à l'acheteur.    

## Paiement en plusieurs fois
 
Un paiement est dit "en plusieurs fois" dès lors que l'acheteur est débité du montant de son achat en plusieurs échéances.  
La première échéance fonctionne de la même manière qu'un paiement comptant immédiat. 
La ou les échéance(s) suivante(s) s'apparente(nt) à un ou des paiement(s) comptant(s) différé(s). 
Seule la première échéance peut faire l’objet d’une garantie pour le marchand à condition que la date de présentation demandée de la première échéance soit inférieure à la date de validité de l'autorisation en fonction du moyen de paiement. (voir section **Validité d'une autorisation** présentée plus bas) 

## Demande d'autorisation
 
Message adressé par la plateforme de paiement à l'émetteur de la carte afin d'obtenir son accord pour le paiement de la transaction. 
De manière générale, le débit n'est effectif qu'après la remise en banque de la transaction.  
Certains émetteurs de carte prépayées ou d'origine espagnole et canadienne débitent le montant de l'autorisation en temps réel et le re-creditent lorsque l'autorisation est échue (voir tableau ci-après). 
 
**Validité d'une autorisation** 
Ci-dessous la liste des moyens de paiement dont la validité de l'autorisation est supérieure à 0 jour.        
|  Moyen de paiement|  Type de cartes (vads_payment_cards)|  Réseau|  Durée de validité d'une autorisation (en jours)|  
| - | - | - | - |   
|  American Express|  AMEX|  AMEX|  7|   
|  Carte Aurore|  AURORE-MULTI|  AURORE|  29|   
|  Carte Cora|  CORA_BLANCHE|  AURORE|  29|   
|  Carte Cora Premium|  CORA_PREM|  AURORE|  29|   
|  Carte Cora Visa|  CORA_VISA|  AURORE|  29|   
|  CB|  CB|  CB|  7|   
|  Visa|  VISA|  CB|  7|   
|  MasterCard|  MASTERCARD|  CB|  7|   
|  Maestro|  MAESTRO|  CB|  30|   
|  Bancontact Mistercash|  BANCONTACT|  CB|  30|   
|  Visa Electron|  VISA_ELECTRON|  CB|  7|   
|  E-carte bleue|  E-CARTEBLEUE|  CB|  7|   
|  Carte Privilège|  CDGP|  CDGP|  30|   
|  Carte cadeau Truffaut|  TRUFFAUT_CDX|  CERIDIAN|  7|   
|  3 fois CB Cofinoga|  COF3XCB|  COF3XCB|  21|   
|  Carte Be Smart|  COFINOGA|  COFINOGA|  7|   
|  Carte Soficarte|  SOFICARTE|  COFINOGA|  30|   
|  Carte Sygma|  SYGMA|  COFINOGA|  30|   
|  Carte Diners Club|  DINERS|  GATECONEX|  3|   
|  Bancontact Mistercash|  BANCONTACT|  GATECONEX|  30|   
|  Carte JCB|  JCB|  JCB|  7|   
|  Bancontact Mistercash|  BANCONTACT|  GICC|  30|   
|  Paylib|  PAYLIB|  PAYLIB|  7|   
|  PayPal|  PAYPAL|  PAYPAL|  3|   
|  POSTFINANCE|  POSTFINANCE|  POSTFINANCE|  1|   
|  Virement SEPA|  SCT|  SEPA|  13|   
|  Prélèvement SEPA|  SDD|  SEPA|  13|   
|  Carte Eccard|  ECCARD|  WIRECARD|  13|             
|  Moyen de paiement|  Type de cartes (vads_payment_cards)|  Réseau|  Durée de validité d'une autorisation (en jours)|  
| - | - | - | - |   
|  American Express|  AMEX|  AMEX|  7|   
|  Carte Aurore|  AURORE-MULTI|  AURORE|  29|   
|  CB|  CB|  CB|  7|   
|  Visa|  VISA|  CB|  7|   
|  MasterCard|  MASTERCARD|  CB|  7|   
|  Maestro|  MAESTRO|  CB|  30|   
|  Visa Electron|  VISA_ELECTRON|  CB|  7|   
|  E-carte bleue|  E-CARTEBLEUE|  CB|  7|   
|  Carte Cofinoga|  COFINOGA|  COFINOGA|  7|   
|  Carte Diners Club *|  DINERS|  GATECONEX|  3|   
|  Carte JCB *|  JCB|  JCB|  7|   
|  PayPal|  PAYPAL|  PAYPAL|  3|   
|  POSTFINANCE *|  POSTFINANCE|  POSTFINANCE|  1|      
        
|  Moyen de paiement|  Type de carte|  Réseau|  Durée de validité d'une autorisation (en jours)|  
| - | - | - | - |   
|  Boleto Bancário|  BOLETO|  BOLETO|  7|   
|  American Express|  AMEX|  CIELO|  4|   
|  Aura|  AURA|  CIELO|  4|   
|  Elo|  CIELO_ELO|  CIELO|  4|   
|  Diners|  DINERS|  CIELO|  4|   
|  Discover|  DISCOVER|  CIELO|  4|   
|  JCB|  JCB|  CIELO|  4|   
|  MasterCard|  MASTERCARD|  CIELO|  4|   
|  Visa|  VISA|  CIELO|  4|   
|  Diners|  DINERS|  ELAVONBR|  4|   
|  Discover|  DISCOVER|  ELAVONBR|  4|   
|  Mastercard|  MASTERCARD|  ELAVONBR|  4|   
|  Visa|  VISA|  ELAVONBR|  4|   
|  Diners|  DINERS|  REDECARD|  4|   
|  Hipercard|  HIPERCARD|  REDECARD|  4|   
|  Mastercard|  MASTERCARD|  REDECARD|  4|   
|  Visa|  VISA|  REDECARD|  4|       
        
|  Moyen de paiement|  Type de cartes (vads_payment_cards)|  Réseau|  Durée de validité d'une autorisation (en jours)|  
| - | - | - | - |   
|  American Express|  AMEX|  AMEX|  7|   
|  CB|  CB|  CB|  7|   
|  Visa|  VISA|  CB|  7|   
|  MasterCard|  MASTERCARD|  CB|  7|   
|  Maestro|  MAESTRO|  CB|  30|   
|  Visa Electron|  VISA_ELECTRON|  CB|  7|   
|  E-carte bleue|  E-CARTEBLEUE|  CB|  7|   
|  Discover|  DINERS|  DINERS|  3|   
|  Diners|  DINERS|  DINERS|  3|   
|  Carte JCB|  JCB|  JCB|  7|   
|  PayPal|  PAYPAL|  PAYPAL|  3|              
|  Moyen de paiement|  Type de cartes (vads_payment_cards)|  Réseau|  Durée de validité d'une autorisation (en jours)|  
| - | - | - | - |   
|  American Express|  AMEX|  AMEXGLOBAL|  7|   
|  Carte Diners Club|  DINERS|  GATECONEX|  3|   
|  e-carte bleue|  E-CARTEBLEUE|  GATECONEX|  7|   
|  Maestro|  MAESTRO|  GATECONEX|  30|   
|  MasterCard|  MASTERCARD|  GATECONEX|  7|   
|  Visa|  VISA|  GATECONEX|  7|   
|  Visa|  VISA|  GICC_VISA|  7|   
|  Visa Electron|  VISA_ELECTRON|  GICC_VISA|  7|   
|  MasterCard|  MASTERCARD|  GICC_MASTERCARD|  7|   
|  Maestro|  MAESTRO|  GICC_MAESTRO|  30|   
|  PayPal|  PAYPAL|  PAYPAL|  3|   
|  PayPal Sandbox|  PAYPAL_SB|  PAYPAL_SB|  3|   
|  PostFinance Card|  POSTFINANCE|  POSTFINANCE|  1|   
|  PostFinance E-finance|  POSTFINANCE_EFIN|  POSTFINANCE|  1|      
* Sous réserve de disponibilité par votre établissement financier 

# Comprendre le déroulement d'un paiement
 
La procédure d’un paiement en ligne s’appréhende de manière différente du point de vue de l’acheteur et du marchand.  

## Définir les étapes d’un paiement - Vue acheteur
 
Le diagramme ci-dessous présente la cinématique des échanges du point de vue de l'acheteur.  
 1. L’acheteur valide son panier.
 2. Le site marchand redirige l’acheteur vers la plateforme de paiement. 
 3. La plateforme de paiement, après vérification des paramètres et de leur signature, présente la page de sélection du moyen de paiement.  
Si le moyen de paiement a été spécifié dans le formulaire, l’acheteur passe directement à l’étape 6.
 4. L’acheteur sélectionne son moyen de paiement.
 5. Il clique sur **Valider**.
 6. Il renseigne le numéro et la date d'expiration de sa carte.   
 7. Il confirme sa saisie en cliquant sur **Valider**.
 8. Si le marchand et la carte de l’acheteur sont enrôlés dans le programme 3D Secure, une authentification 3D Secure a lieu.
 9. Une demande d'autorisation est effectuée auprès de la banque de l’acheteur, l’émetteur, en plus des contrôles de fraudes internes de la plateforme de paiement.
 10. En cas de succès, une page de résumé est présentée à l’acheteur récapitulant les informations de la transaction. 
Un bouton permettant un retour à la boutique est proposé.
   
En cas d’échec, un message s’affiche. L’acheteur est informé du refus de la demande de paiement. Un bouton permettant d’annuler et de retourner à la boutique est proposé.  

## Définir les étapes d'un paiement - Vue marchand
 
Le paiement en ligne, côté marchand, se déroule de la manière suivante:  
 
 1. L’acheteur valide son panier.
 2. Le site marchand construit le formulaire à partir des données du panier de l’acheteur.
 3. Le site marchand redirige l’acheteur vers la plateforme de paiement. Cette redirection se fait sous la forme d'un formulaire HTML POST en HTTPS. Les paramètres qui le composent sont décrits dans le chapitre ****.
 4. Après saisie des données du moyen de paiement par l’acheteur, la plateforme procède au paiement.
 5. En fonction du paramétrage de la boutique (voir chapitre **Paramétrer les notifications**), un appel est automatiquement réalisé afin de transmettre le résultat au site marchand. 
 6. Le site marchand analyse et traite le résultat du paiement. 
 7. Il met à jour la base de données (état de la commande, état du stock etc…).
 8. L’acheteur est informé du résultat du paiement sur la plateforme. S’il décide de retourner sur le site marchand, ce dernier le remercie et lui affiche l’état de sa commande.
   

## Cycle de vie des transactions
 
Dans tous les schémas suivants, la légende suivante est adoptée :  
 Action du marchand nécessaire - manuelle Back Office ou automatique (webservice) 

### Mode de validation automatique
 
 

#### Cycle de vie d’une transaction de paiement comptant immédiat
  
Suite à la demande de paiement, plusieurs contrôles sont automatiquement mis en oeuvre :  
 
 * L’authentification 3D Secure.
 * Différents contrôles locaux réalisés directement par la plateforme de paiement (ceux-ci incluent potentiellement les contrôles liés à la souscription au service additionnel de contrôles anti-fraude).
 * Une demande d’autorisation est également effectuée auprès de la banque de l'acheteur, le jour même de la date de paiement, quelle que soit la date de remise en banque demandée. 
Si l’un de ces contrôles échoue, la demande de paiement n’est pas acceptée. L'acheteur est informé du refus à l’écran. Dans le Back Office, la transaction est consultable avec le statut **Refusé**. 
Dans le cas contraire, la transaction prend le statut **En attente de remise**. L'acheteur est informé de l’acceptation de sa demande de paiement et est destinataire d’un e-mail de confirmation. La transaction partira automatiquement en remise le jour demandé par le marchand. 
Dans l’attente de cette remise, le marchand peut modifier la date de remise ainsi que le montant (modification du montant uniquement à la baisse, ce cas correspond à une livraison partielle par le marchand). 
Si nécessaire, il peut également annuler la transaction : celle-ci prend alors le statut **Annulé**. 
   

#### Cycle de vie d’une transaction de paiement comptant différé
 
**Délai de remise inférieur à la durée de validité de l'autorisation**  
(voir diagramme cycle de vie d'une transaction de paiement comptant immédiat). 
**Délai de remise supérieur à la durée de validité de l'autorisation ** 
Toute transaction de paiement comptant différé réalisée avec le mode de validation automatique, et dont la demande d’autorisation à 1 euro100 XPF1 CHF1 BRL a été réalisée avec succès, est consultable dans le Back Office avec le statut **En attente d’autorisation**.  
La demande d’autorisation est automatiquement effectuée :  
 
 * fonctionnement par défaut : le jour de la date de remise en banque souhaitée,
 * fonctionnement avec autorisation anticipée : selon le moyen de paiement sélectionné, à J-Δ (voir  illustrant la validité d'une autorisation) avant la date de remise en banque souhaitée. 
Le mode par autorisation anticipée doit faire l'objet d'une demande auprès du Service Client. 
En cas de refus de type non frauduleux (voir ), l'autorisation sera réitérée chaque jour jusqu'à J-2 avant la date de remise en banqueDans l’attente, le marchand peut annuler la transaction ou en modifier le montant (à la baisse uniquement) et/ou la date de remise. 
   
 
Le diagramme suivant résume les différents statuts pouvant être pris par ce type de transaction (cas d'une demande d'autorisation non rejouée) :     

#### Cycle de vie d’une transaction de paiement en plusieurs fois
 
La première échéance du paiement en plusieurs fois se comportera exactement comme une transaction de paiement comptant immédiat ou une transaction de paiement différé selon sa date de remise en banque.  
Les échéances suivantes sont par défaut positionnées en statut **En attente d’autorisation**. La banque de l'acheteur pourra refuser la demande d’autorisation. La plateforme de paiement informe alors le marchand du refus de la transaction par e-mail.  
Les demandes d’autorisation des échéances suivantes sont automatiquement effectuées comme une transaction de paiement différé, donc avec deux dates possibles : 
 * fonctionnement par défaut : le jour de la date de remise en banque souhaitée,
 * fonctionnement avec autorisation anticipée : selon le moyen de paiement sélectionné, à J-Δ (voir  illustrant la validité d'une autorisation) avant la date de remise en banque souhaitée. 
  
 
Les échéances ultérieures suivent le diagramme d’état suivant (cas d'une demande d'autorisation non rejouée) : 
  
L’annulation d’une échéance n’implique en aucun cas l’annulation des échéances suivantes restant à remettre en banque.  

### Mode de validation manuelle
 
 

#### Cycle de vie d’une transaction de paiement comptant immédiat
 
Suite à la demande de paiement, des contrôles sont automatiquement mis en oeuvre :  
 
 * L’authentification 3D Secure.
   
 
 * Différents contrôles locaux réalisés directement par la plateforme de paiement (ceux-ci incluent potentiellement les contrôles liés à la souscription au service additionnel du contrôle des risques).
   
 
 * Une demande d’autorisation est effectuée auprès de la banque de l'acheteur.
   
Si l’un de ces contrôles échoue, la demande de paiement n’est pas acceptée. L'acheteur est informé du refus à l’écran. Dans le Back Office, la transaction est consultable avec le statut **Refusé**.  
 
Dans le cas contraire le paiement est accepté et la transaction est consultable dans le Back Office avec le statut **A Valider**. 
Le marchand doit alors obligatoirement valider la transaction avant la date de remise demandée. Dans le cas contraire, la transaction prend le statut **Expiré** et ne peut plus être remise en banque. 
  
Dès lors qu’une transaction est validée, elle passe en statut **En attente de remise**.    
Il peut également annuler la transaction si nécessaire. La transaction prend alors le statut **Annulé**.  

#### Cycle de vie d’une transaction de paiement comptant différé 
 
**Délai de remise inférieur à la durée de validité de l'autorisation**  
(voir diagramme cycle de vie d'une transaction de paiement comptant immédiat) 
**Délai de remise supérieur à la durée de validité de l'autorisation ** 
Toute transaction de paiement comptant différé réalisée avec le mode de validation manuelle et dont la demande d’autorisation à 1 euro100 XPF1 CHF1 BRL a été réalisée avec succès, est consultable dans le Back Office avec le statut **A valider et à autoriser**.  
La demande d’autorisation est automatiquement effectuée le jour de la remise en banque demandé, sous réserve que le marchand ait précédemment validé la transaction.  
Dans l’attente de la remise, le marchand peut annuler la transaction ou en modifier le montant et/ou la date de remise en banque.  
Ces transactions suivent le diagramme d’état suivant :     

#### Cycle de vie d’une transaction de paiement en plusieurs fois 
 
La première échéance du paiement en plusieurs fois se comportera exactement comme une transaction de paiement comptant immédiat ou une transaction de paiement différé, selon la date de remise en banque demandée.  
Les échéances suivantes sont par défaut positionnées en statut **A valider et autoriser** tant que la première échéance n’aura pas été validée par le marchand. Leur bonne fin n’est pas garantie pour le marchand. En effet, la banque de l'acheteur peut refuser la demande d’autorisation.  
 
**La validation de la 1ère échéance vaut validation de toutes les échéances suivantes. Par contre, l’annulation d’une échéance ne vaut pas annulation des échéances ultérieures. ** 
  

### Spécificités liées aux autorisations anticipées
 
Pour activer les autorisations anticipées, veuillez contacter le service clients de la plateforme de paiement. 
Ce processus s'applique uniquement pour les demandes d’autorisation : 
 * du paiement comptant différé, 
 * des échéances, autres que la première, pour le paiement en plusieurs fois. 
  
Le déclenchement de l'autorisation s'effectuera à J-Δ (voir durée de validité d'une autorisation pour chaque moyen de paiement) avant la date de remise en banque souhaitée. 
En cas de refus par le serveur d'autorisation de la banque de l'acheteur, exclusivement pour un motif non frauduleux (voir ), un processus réitère automatiquement les demandes d'autorisation jusqu'à J-2.   
En cas de refus pour un motif frauduleux la transaction est considérée comme définitivement refusée. 

# Établir le dialogue avec la plateforme de paiement
 
Le dialogue avec la plateforme de paiement est décrit dans le guide d'implémentation du formulaire de paiement disponible ici:  
Il fonctionne de la même manière que pour le paiement unitaire classique, à savoir sur la base d’échange de formulaires HTTP.  
Le dialogue entre le site marchand et la plateforme de paiement s’effectue par un échange de données.  
Pour créer un paiement, ces données sont envoyées au moyen d'un formulaire HTML via le navigateur de l’acheteur.  
A la fin du paiement, le résultat est transmis au site marchand de deux manières:
 * automatiquement au moyen de notifications appelées URL de notification instantanée (également appelée IPN pour Instant Payment Notification), voir chapitre **Paramétrer les notifications**,
 * par le navigateur lorsque l’acheteur clique sur le bouton pour revenir au site marchand , voir chapitre **Gérer le retour vers le site marchand**.
  
Pour assurer la sécurité des échanges, les données sont signées au moyen d’un certificat connu uniquement du marchand et de la plateforme de paiement. 



## Choisir le mode Test ou Production
 
Le choix du mode **TEST** ou **PRODUCTION** s'effectue en utilisant le champ **vads_ctx_mode** (Voir chapitre ****). 
 
 * Le mode **TEST** permet de réaliser des paiements de test. 
**Il est toujours disponible**, même après la génération du certificat de production.Si vous créez un nouveau site marchand (ou disposez d’un environnement de recette), vous pourrez effectuer vos tests sans impacter le site actuellement en production. 
Les transactions de TEST sont visibles dans le Back Office depuis le menu **Gestion** > **Transactions de Test** 
 * Le mode **PRODUCTION** n’est disponible qu’une fois le certificat de production généré (voir chapitre **Activer la boutique en mode PRODUCTION** du guide d'implémentation du formulaire disponible sur notre site documentaire :  ).
Il permet de réaliser des paiements réels.Les transactions de PRODUCTION sont visibles dans le Back Office depuis le menu **Gestion** > **Transactions**.

   
 

## Gérer le dialogue vers le site marchand
 
La gestion du dialogue vers le site marchand est réalisée grâce à deux types d’URL : 
 
 * **Url de notification instantanée**, également appelée IPN (Instant Payment Notification),
 * **Url de retour** vers le site marchand.
   
 
 
<u>Url de notification instantanée - IPN (Instant Payment Notification)</u> 
La plateforme de paiement notifie automatiquement au site marchand le résultat du paiement. Les données sont envoyées en mode **POST**.  
La plateforme est capable de contacter le site marchand quel que soit le protocole utilisé (http ou https). 
 
**Pour traiter** ces notifications, le marchand doit **créer une page** sur son site qui : 
 
 * analyse les données reçues en mode **POST**,
 * s’assure de l’intégrité des informations reçues en calculant la signature,
 * vérifie qu’il ne s’agit pas d’un doublon de notification (renvoi de la notification depuis le Back Office par exemple),
 * déclenche la mise à jour de sa base de données (état de la commande, stock, etc…),
 * envoie des e-mails à l’acheteur (facture, suivi de commande, etc…).
   
Le temps de traitement influe directement sur le délai d’affichage de la page de résumé du paiement. Plus le traitement est long, plus l’affichage est retardé. 
**Pour recevoir** les notifications, le marchand doit **paramétrer** les règles de notifications depuis son Back Office (voir chapitre **Paramétrer les notifications**).  
En cas de problème de communication vers le site marchand, la plateforme de paiement envoie un e-mail à l’administrateur de la boutique, précisant la raison de l’échec (erreur http, etc. …) ainsi que la procédure à suivre pour renvoyer la notification depuis le Back Office. 
 
 
 
<u>Url de retour vers le site marchand</u> 
  
Le marchand peut paramétrer dans le Back Office les URL de retour "par défaut" depuis le menu **Paramétrage** > **Boutique** > onglet **Configuration**) : 
  
Il peut configurer une URL de retour à la boutique différente en fonction du mode. 
Par défaut, l'acheteur est redirigé vers l'URL de retour, et ce, quel que soit le résultat du paiement. 
Si toutefois aucune URL n’est configurée à ce niveau, alors la redirection utilisera l'URL principale de la boutique (paramètre **URL** défini dans l'encadré **Détails** de la boutique).  
 
Le marchand a la possibilité de surcharger cette configuration dans son formulaire de paiement (voir chapitre **Définir les URL de retour**). 
  
<u>Remarque</u> : 
Le statut de la règle "URL de notification à la fin du paiement" (IPN) est affiché dans cet écran. Si cette dernière est non paramétrée, veillez à la renseigner (voir chapitre **Paramétrer les notifications**) .  

## Gérer la sécurité
 
Plusieurs moyens sont mis en place afin d’assurer la sécurité des transactions de paiement en ligne. 

### Gérer la sécurité au moyen de la signature
 
 
L’intégrité des informations échangées est garantie par un échange de signatures numériques entre la plateforme de paiement et le site marchand.  
 
Le dialogue entre la plateforme de paiement et le site marchand s’effectue par soumission de formulaires HTML.  
Un formulaire contient une liste de champs spécifiques (voir ****) utilisés pour calculer sa signature numérique (voir chapitre ****). 
Le résultat de ce calcul doit être envoyé dans le champ **signature**. 
 
Nous utilisons la fonction de hachage « SHA-1 » pour chiffrer la signature. 
SHA-1 est disponible dans la plupart des langages utilisés dans le développement d’applications Web. 
 
En fonction du language choisi, vous aurez peut être à coder vous-même les fonctions de hachage SHA-1 (comme en ASP par exemple).  
 
Pour vous aider, voici le résultat du SHA-1 du caractère " a " : 
SHA1( " a ") = 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8 
 
<u>Modélisation des mécanismes de sécurité :</u> 
 
 1. Le site marchand récolte les données du formulaire et calcule la signature.
 2. Le site marchand soumet le formulaire à la plateforme.
 3. La plateforme réceptionne les données du formulaire et calcule la signature.
 4. La plateforme compare la signature calculée avec la signature transmise par le site marchand.
 5. Si les signatures diffèrent, la demande de paiement est rejetée.
 Sinon, la plateforme procède au paiement.
 6. La plateforme réceptionne les données du résultat et calcule la signature de la réponse.
 7. En fonction du paramétrage de la boutique (voir chapitre **Paramétrer les notifications**), la plateforme soumet le résultat du paiement au site marchand.
 8. Le site marchand réceptionne les données et calcule la signature. Il compare la signature calculée avec la signature transmise par la plateforme.
 9. Si les signatures diffèrent, le marchand analyse l’origine de l’erreur (erreur dans le calcul, tentative de fraude etc...) 
Sinon, le site marchand procède à la mise à jour de sa base de données (état du stock, état de la commande etc…).
  

### Conserver le certificat de production
 
Dès le premier paiement réalisé avec une carte réelle, le certificat de production est masqué pour des raisons de sécurité. 
 
Nous vous conseillons fortement de conserver ce certificat en lieu sûr (fichier chiffré, base de données etc…). 
 
En cas de perte, le marchand aura la possibilité d’en générer un nouveau depuis son Back Office. 
Pour rappel, le certificat de production est visible dans le Back Office depuis le menu **Paramétrage** > **Boutique** > onglet **Certificats**.  

### Gérer les données sensibles
 
Des règles strictes régissent les transactions de paiement en ligne (Certification PCI-DSS). 
 
En tant que marchand, vous devez vous assurer de ne jamais retranscrire en clair des données qui pourraient s’apparenter à un numéro de carte bancaire. Votre formulaire serait rejeté (code 999 - Sensitive data detected). 
 
Evitez notamment les numéros de commandes de longueur comprise entre 13 et 16 caractères numériques et commençant par 3, 4 ou 5. 

## Utiliser une i-frame
 
Une i-frame (in line frame) est utilisée pour afficher une page web dans une autre page web.  

  
 
<u>Exemples de codes</u> :  

## Gérer les paramètres de votre boutique par fichier de configuration
 
L'utilisation d'un fichier de configuration permet d'éviter de mettre des valeurs en dur dans le code. 
Les fichiers de configuration peuvent contenir : 
 
 * l'URL de la page de paiement, 
 * la valeur du certificat, 
 * la valeur de l'identifiant de la boutique,
 * etc...
   
Ces fichiers permettent de typer les données à sauvegarder. 
Le programme qui génère le formulaire de paiement appelera le fichier de configuration avec le paramètre pour utiliser la valeur. 
Il incombe au marchand de s'assurer : 
 
 * des droits sur le fichier pour ne pas qu'il soit accessible de l'exterieur.
 * de répondre aux spécificités liées au langage de programmation utilisé.
   
<u>Exemple de fichier de configuration "conf.txt"</u> : 
<u>Exemple d'appel de fichier de configuration dans le formulaire de paiement</u> : 

# Paramétrer les notifications
 
Le Back Office permet de gérer les événements qui génèreront un appel vers le site marchand et de configurer l’URL de la page à contacter. 
Les schémas suivants illustrent, pour chaque événement, le statut de la transaction envoyé dans la notification. 
La légende adoptée pour chacun est la suivante :  
 Action du marchand nécessaire - manuelle (Back Office) ou automatique (webservice) 
 Action de l'acheteur 
 

## Notifications des différents statuts pour un paiement comptant  immédiat
  
 
        
|  Evénement |  Statut notifé|  Nom de la règle à paramétrer|  
| - | - | - |   
|  Abandon par l'acheteur|  ABANDONED|  URL de notification sur annulation|   
|  Annulation par le marchand|  CANCELED|  URL de notification sur une opération en provenance du Back Office|   
|  Réponse à la demande d'autorisation|  AUTHORISED_TO_VALIDATE, AUTHORISED, REFUSED |  URL de notification à la fin du paiement|       
 

## Notifications des différents statuts pour un paiement comptant  différé
  
Δ : durée de validité d'autorisation. 
        
|  Evénement |  Statut notifé|  Nom de la règle à paramétrer|  
| - | - | - |   
|  Abandon par l'acheteur|  ABANDONED|  URL de notification sur annulation|   
|  Annulation par le marchand|  CANCELED|  URL de notification sur une opération en provenance du Back Office|   
|  Validation par le marchand|  WAITING_AUTHORISATION|  URL de notification sur une opération en provenance du Back Office|   
|  Réponse à la demande d'autorisation à 1 BRL1 euro100 XPF1 CHF|  REFUSED, WAITING_AUTHORISATION, WAITING_AUTHORISATION_TO_VALIDATE|  URL de notification à la fin du paiement|   
|  Réponse à la demande d'autorisation|  AUTHORISED, REFUSED, AUTHORISED_TO_VALIDATE|  URL de notification sur autorisation par batch|       

## Notifications des différents statuts pour les échéances d'un paiement en  plusieurs fois
  
Δ : durée de validité d'autorisation. 
 
        
|  Evénement |  Statut notifé|  Nom de la règle à paramétrer|  
| - | - | - |   
|  Annulation par le marchand|  CANCELED|  URL de notification sur une opération en provenance du Back Office|   
|  Réponse à la demande d'autorisation|  AUTHORISED, REFUSED |  URL de notification sur autorisation par batch|       

## Configurer les notifications
 
Plusieurs types de notifications sont mises à disposition dans le Back Office. Elle permettent de gérer les évènements (abandon par l'acheteur, annulation par le marchand, validation par le marchand...) qui génèreront un appel vers le site marchand et de configurer l'URL de la page à contacter. 
Pour accéder à la gestion des règles de notification :  
 
 1. Connectez-vous à : .
 2. Allez dans le menu : **Paramétrage** > **Règles de notifications**. 
   









# Générer un formulaire de paiement
 
Pour générer une demande de paiement, vous devez construire un formulaire html comme suit : 
 
Il contient: 
 
<u>Les éléments techniques suivants : </u> 
 
 * Les balises ```
<form>
```
 et ```
</form>
```
 qui permettent de créer un formulaire HTML.
 * L’attribut ```
method="POST"
```
 qui spécifie la méthode utilisée pour envoyer les données.
 * L’attribut ```
action=""
```
 qui spécifie où envoyer les données du formulaire.
   
 
<u>Les données du formulaire :</u> 
 
 * L’identifiant de la boutique,
 * Les caractéristiques du paiement en fonction du cas d’utilisation(voir chapitres suivants),
 * Les informations complémentaires en fonction de vos besoins (voir chapitre **Utiliser des fonctions complémentaires** ),
 * La signature qui assure l'intégrité du formulaire (voir chapitre **Calculer la signature**).
   
 
Ces données sont ajoutées au formulaire en utilisant la balise ```
<input>
```
: 
```
<input type="hidden" name="parametre1" value="valeur1" />
```
 
 
Pour valoriser les attributs ```
name
```
 et ```
value
```
 , référez-vous au chapitre **Dictionnaire de données**. 
Pour valoriser les attributs ```
name
```
 et ```
value
```
 , référez-vous au chapitre **Dictionnaire de données** du guide d'implémentation du formulaire.  
 
 
Toutes les données du formulaire doivent être encodées en **UTF-8. ** 
Les caractères spéciaux (accents, ponctuation etc…) seront ainsi correctement interprétés par la plateforme de paiement. Dans le cas contraire, le calcul de signature sera erroné et le formulaire sera rejeté. 
 
<u>Le bouton <b>Payer</b> qui va permettre l’envoi des données :</u> 
```
<input type="submit" name="payer" value="Payer"/>
```
 
 
Des cas d’utilisation sont présentés dans les chapitres suivants. Ils vous permettront de construire votre formulaire de paiement en fonction de vos besoins. 
  
 * Créer un paiement comptant immédiat.
 * Créer un paiement comptant différé.
 * Créer un paiement en plusieurs fois.
 * Créer une autorisation sans remise.
   





# Utiliser des fonctions complémentaires
 
PayPal a mis en place un programme de protection des marchands qui permet de protéger un marchand en cas de litige avec son acheteur. 
Afin de bénéficier de cette protection lors de la vente d'objets physiques, il faut **impérativement** transmettre **la description des produits** et **l'adresse de livraison** à la plateforme de paiement afin que celle-ci les transmette à son tour à PayPal.  
Les données de livraison correspondent à tous les champs qui commencent par **vads_ship_**. Pour plus de détails, veuillez vous référer au chapitre **Transmettre les données de la livraison**. 
Si ces informations ne sont pas transmises à PayPal, le marchand ne pourra bénéficier d'aucune protection. 
La protection n’est pas automatiquement attribuée à tous les marchands. Pour plus de renseignements, veuillez contacter PayPal ou rendez-vous sur leur site internet à l'adresse . 
Pour obtenir un formulaire personnalisé et adapté à vos besoins, vous pouvez utiliser des fonctions complémentaires parmi la liste ci-dessous : 
 * Gérer les moyens de paiement proposés à l'acheteur sur la page de paiement
 * Gérer la sélection de l'option de paiement
 * Definir le mode de remise en banque (mode de validation) 
 * Transmettre des informations sur l’acheteur (civilité, adresse e-mail..)
 * Transmettre des informations sur la livraison (adresse…)
 * Transmettre des informations sur la commande (référence, contenu du panier…)
 * Activer ou désactiver 3D Secure
 * Définir le contrat commerçant à utiliser pour le paiement
 * Personnaliser des élements de la page de paiement
 * Surcharger l’url de notification instantanée (également appelée IPN)
 * Pré-remplir le formulaire de saisie
 * Personnaliser la RUM
 * Modifier la date d'échéance d'un prélèvement
 * Définir un montant différent pour la ou les première(s) échéance(s)
 * Gérer les URL de retour vers le site marchand
 * Activer le retour automatique vers le site marchand à la fin du paiement
 * Réaliser un paiement sans rediriger l'acheteur vers la page de paiement
 * Créer des champs spécifiques en fonction de vos besoins
  
 
Ces fonctionnalités sont présentées dans les chapitres suivants. Ces chapitres vous permettront de construire facilement votre formulaire de paiement. 
D’autres fonctionnalités sont présentées dans le guide d’implémentation du formulaire de paiement. Elles vous permettront de construire facilement votre formulaire de paiement. 







## Gérer le retour vers le site marchand
 
A la fin du paiement, l’acheteur a la possibilité de revenir sur le site marchand sur une page appelée **URL de retour**.  
A ne pas confondre avec l’**URL de notification instantanée (également appelée IPN)** (voir chapitre ****).  

### Définir les URL de retour
  
Dans le formulaire de paiement, le marchand peut surcharger la configuration du Back Office. Pour cela il peut: 
 
 * Utiliser 4 URL différentes en fonction du résultat du paiement:
 * Paiement accepté.
 * Paiement refusé.
 * Paiement abandonné.
 * Paiement en erreur.
 
 * Utiliser une seule URL quel que soit le résultat du paiement.
   





## Personnaliser la page de paiement
 
Vous pouvez personnaliser certains éléments de la page de paiement: 
 
 * les moyens de paiement proposés au moment du paiement,
 * la langue dans laquelle seront affichées les pages de paiement,
 * les langues proposées à l’acheteur sur les pages de paiement (drapeaux),
 * le nom et l’url de la boutique,
 * le libellé du bouton **Retourner à la boutique**.
   
 
En souscrivant à l'option **personnalisation avancée**, vous pourrez modifier la page de paiement afin de la rendre visuellement proche de votre site marchand. Ceci aura pour effet de conforter l’acheteur et d’instaurer une confiance lors de la redirection pour procéder au paiement. Référez-vous au "manuel utilisateur de la personnalisation avancée" disponible sur le site documentaire . Pour plus d'informations, veuillez vous adresser au support technique. 











# Envoyer la demande de paiement
 
Pour chaque transaction, l’acheteur doit être redirigé vers la page de paiement afin de finaliser son achat. 
Son navigateur doit transmettre les données du formulaire de paiement. 

## Rediriger l'acheteur vers la page de paiement
 
L’URL de la plateforme de paiement est la suivante :     
|  |      
<u>Exemple de paramètres envoyés à la plateforme de paiement</u>: 

## Gérer les erreurs
 
Si la plateforme détecte une anomalie lors de la réception du formulaire, un message d’erreur sera affiché et l’acheteur ne pourra pas procéder au paiement.  
 
 
<u>En mode TEST</u> 
Le message indique l’origine de l’erreur et propose un lien vers la FAQ pour vous aider à la corriger.  
 
 
<u>En mode PRODUCTION</u> 
Le message indique simplement à l’acheteur qu’un problème technique est survenu. 
 
Dans les deux cas, le marchand reçoit un e-mail d'avertissement. 
Il contient:
 * l’origine de l’erreur
 * un lien vers la FAQ pour faciliter le diagnostic
 * l’ensemble des champs contenus dans le formulaire.
  
  
La FAQ est disponible à cette adresse :  
Une FAQ est disponible sur notre site documentaire. 

# Analyser le résultat du paiement
 
Pour traiter le résultat des paiements, le site marchand doit disposer d'un script sur une page dédiée (exemple : analyse_paiement.php). 
Cette page sera appelée automatiquement après chaque paiement (accepté ou refusé) : les paramètres liés au résultat du paiement sont envoyés en mode POST par la plateforme de paiement. 
 
**Prérequis :** 
 
 * L'URL de la page qui analyse le résultat du paiement devra obligatoirement être renseignée dans le Back Office (voir chapitre **Paramétrer les notifications** du guide d'implémentation du formulaire). 
    
 
 * Le marchand doit s'assurer que cette URL soit joignable par la plateforme de paiement et ce, sans redirection. 
Les redirections entrainent la perte des données présentes dans le POST.
   
 
 * En cas de restriction mise en place du côté du site marchand, il faudra autoriser la plage d'adresses d'IP **194.50.38.0/24**.
   
 
 * La page ne devra pas comporter d'affichage HTML. 
L'accès aux ressources telles que les images ou feuilles de styles peuvent ralentir les échanges entre la plateforme de paiement et le site marchand.
De plus, la plateforme lit systématiquement les 512 premiers caractères retournés par le site marchand.Ces caractères sont ensuite affichés dans l'historique des transactions.
   
 
 * Evitez au maximum d'intégrer des tâches consommatrices de temps comme la génération de facture ou l'envoi d'e-mail dans ce script.
Le temps du traitement influe directement sur le délai de l’affichage de la page de résumé du paiement. Plus le traitement de la notification est long, plus l’affichage est retardé. 
Au delà de 35s, la plateforme considèrera que l'appel a échoué (timeout).
   
 
 
**Echec de notification (IPN)** 
En cas d'échec de l'appel à l’URL de notification (IPN), un e-mail d'avertissement est envoyé à l’adresse spécifiée dans le Back Office (voir chapitre **Paramétrer les notifications**). 
 En cas d'échec de l'appel à l’URL de notification (IPN), un e-mail d'avertissement est envoyé à l’adresse spécifiée dans le Back Office (voir chapitre **Paramétrer les notifications** du guide d'implémentation du formulaire). 
Il contient :  
 
 * le code HTTP de l’erreur rencontrée,
 * des éléments d’analyses en fonction de l’erreur,
 * la procédure à suivre depuis le Back Office pour renvoyer la notification. 
   
 
 
**Concevoir le script de traitement** 
Le script de traitement devra comporter au moins les étapes ci-dessous: 
 
 * Récupérer la liste des champs présents dans la réponse envoyée en POST
 * Calculer la signature
 * Comparer la signature calculée avec celle réceptionnée
 * Analyser la nature de la notification
 * Récupérer le résultat du paiement 
   
 
Le script peut par exemple tester l'état de la commande (ou l'information de votre choix) pour vérifier qu'elle n'ait pas déja été mise à jour. 
Une fois ces étapes réalisées, le script peut mettre à jour la base de données (nouvel état de la commande, mise à jour du stock, enregistrement des informations du paiement etc...). 
 
  

## Récupérer les données retournées dans la réponse
 
Les données retournées dans la réponse dépendent des paramètres envoyés dans le formulaire de paiement, du type de paiement réalisé et des options de votre boutique. Ces données constituent une liste de champs. Chaque champ contient une valeur réponse. La liste de champs peut être amenée à évoluer. 
 
Les données sont toujours envoyées en **POST** par la plateforme de paiement. 
La première étape consiste donc à récupérer le contenu reçu en mode POST. 
Exemples : 
 *  
En PHP, les données seront stockées dans la super globale **$_POST**. 
 *  
En ASP.NET (C#), vous devez utiliser la propriété **Form** de la classe **HttpRequest**. 
 *  
En java, vous devez utiliser la méthode **getParameter** de l'interface **HttpServletRequest**.  
Le script devra effectuer une boucle pour récupérer la totalité des champs transmis. 
  
<u>Exemple de données envoyées lors de la notification d’un paiement :</u> 
<u>Exemple de données envoyées lors de la notification d’un prélèvement SEPA ponctuel :</u> 


## Comparer les signatures
 
Pour s’assurer de l’intégrité de la réponse, vous devez comparer la valeur du champ **signature** reçue dans la réponse, avec celle calculée à l’étape précédente.  
 
Si les signatures correspondent, 
 * alors vous pouvez considérer la réponse comme sûre et procéder à la suite de l’analyse.
 * sinon, le script devra lever une exception et avertir le marchand de l'anomalie (voir chapitre **Traiter les erreurs** du guide d'implémentation du formulaire disponible sur notre site documentaire ).
  
 
Les signatures ne correspondent pas en cas :  
 
 * d’erreur d'implémentation (erreur dans votre calcul, problème d’encodage UTF8, etc.).
 * d’erreur dans la valeur du certificat utilisé ou dans celle du champ **vads_ctx_mode** (problème fréquent lors du passage en production).
 * de tentative de corruption des données. 
   

## Analyser la nature de la notification
 
Le champ **vads_url_check_src** permet de différencier les notifications en fonction de leur évènement déclencheur : 
 
 * l'enregistrement d'un mandat (avec ou sans définition d'un abonnement).
 * paiement d'une échéance d'un abonnement.
 * création d'une transaction.
 * renvoi de la notification depuis le Back Office par le marchand.
   
Il précise la règle de notification appliquée :      
|  Valeur|  Règle appliquée|  
| - | - |   
|  **PAY**|   
La valeur PAY sera envoyée dans les cas suivants :
 * demande d'enregistrement d'un mandatalias (REGISTER)
 * demande d'enregistrement d'unmandatalias avec définition d'un abonnement (REGISTER_SUBSCRIBE)
 * paiement immédiat (paiement comptant ou première échéance d'un paiement en plusieurs fois) 
 * paiement différé à moins de 7 jours
uniquement si le marchand a configuré la règle **URL de notification à la fin du paiement**. 
 *  
paiement abandonné ou annulé par l'acheteur  
uniquement si le marchand a configuré la règle **URL de notification sur annulation**. 
  |   
|  **BO**|  Exécution de la notification depuis le Back Office (clic droit sur une transaction > **Executer l'url de notification**).|   
|  **BATCH_AUTO**|  
La valeur BATCH_AUTO sera envoyée dans les cas suivants:
 * paiement différé à plus de 7 jours
 * échéances d'un paiement en plusieurs fois (hormis la première)
uniquement si le marchand a configuré la règle **URL de notification sur autorisation par batch**. 
 

La notification sera envoyée lors de la demande d’autorisation d'un paiement dont le statut est "En attente d’autorisation".Non applicable pour le prélèvement ponctuel.|   
|  **REC**|  
La valeur REC sera envoyée uniquement pour les paiements par abonnement si le marchand a configuré la règle **URL de notification à la création d'un paiement par récurrence**.Non applicable pour le prélèvement ponctuel.|   
|  **MERCH_BO**|  La valeur MERCH_BO sera envoyée :
 
 * lors d'une opération réalisée depuis le Back Office (remboursement, modification, validation, duplicata), si le marchand a configuré la règle de notification : **URL de notification sur une opération provenant du Back Office**
 * lors d'une annulation réalisée depuis le Back Office, si le marchand a configuré la règle de notification : **URL de notification sur annulation**
  |      
En testant sa valeur, le script pourra réaliser un traitement différent en fonction de la nature de la notification. 
<u>Par exemple :</u> 
Si **vads_url_check_src** est valorisé à **PAY** ou **BATCH_AUTO** alors le script mettra à jour le statut de la commande, ... 
Si **vads_url_check_src** est valorisé à **REC** alors le script récupèrera la référence de l'abonnement et incrémentera le nombre d'échéances échues en cas de paiement accepté, ... 

## Identifier le type d'opération
 
Le champ **vads_operation_type** permet de différencier : 
 
 * une opération de débit.
 * une opération de remboursement.
   
       
|  Valeur|  Description|  
| - | - |   
|  **DEBIT**|  Opération de débit.|   
|  **CREDIT**|  Opération de remboursement.|       
<u>Par exemple :</u> 
Si **vads_operation_type** est valorisé à **DEBIT**, le script met à jour la commande et enregistre les informations de la transaction. 
Si **vads_operation_type** est valorisé à **CREDIT**, le script met à jour le montant payé ou ajoute une nouvelle ligne de transaction dans la commande. 


## Traiter les erreurs
 
<u>Mise en place d'un fichier de log</u> 
Durant la phase d'implémentation, il sera utile de disposer de logs notamment en cas de difficultés pour calculer la signature. 
Nous conseillons toutefois de mettre en place un fichier de log journalier même après la mise en production du site marchand.  
Cela vous permettra d'analyser les données en cas de problèmes. 
Idéalement le fichier de log devra contenir les données envoyées ou reçues, la chaîne obtenue lors du calcul de signature, avant l'application de l'algorithme SHA-1. 
<u>Code d'erreur HTTP</u>  
En cas d'erreur durant les notifications, l'e-mail d'avertissement envoyé précise le code retour du protocole HTTP. 
Il existe 5 catégories de codes retour : 
      
|  Catégorie de codes |  Description|  
| - | - |   
|  1XX|  Information|   
|  2XX|  Succès|   
|  3XX|  Redirection|   
|  4XX|  Erreur du client|   
|  5XX|  Erreur du serveur|       
Les codes d'erreur les plus fréquemment retournés sont décrits dans la FAQ de notre site documentaire  
**Erreur fréquente** :  
Un fichier htaccess peut bloquer l'appel à l'URL de notification instantanée.  
Les fichiers .htaccess sont des fichiers de configuration des serveurs web Apache. Ils peuvent être placés dans n'importe quel répertoire du site marchand (la configuration s'applique au répertoire et à tous ceux qu'il contient n'ayant pas de tel fichier à l'intérieur). 

# Traiter le retour à la boutique
 
Par défaut, lorsque l'acheteur revient sur le site marchand, aucun paramètre n'est transmis par son navigateur. 
Néanmoins si le champ **vads_return_mode** a été transmis dans le formulaire de paiement (voir chapitre **Gérer le retour vers le site marchand**  du guide d'implémentation du formulaire disponible sur notre site documentaire ) il sera possible de récupérer les données : 
 * soit en GET : données présentes dans l’url sous la forme : ?param1=valeur1&param2=valeur2.
 * soit en POST : données envoyées dans un formulaire POST.
  
 
Les données transmises au navigateur sont les mêmes que lors des notifications (IPN). 
Seuls les champs **vads_url_check_src** et **vads_hash** ne seront envoyés que dans la notification instantanée. 
 
Vous pouvez vous référer au chapitre **Analyser le résultat du paiement** pour analyser ces données. 
 
 
**Remarque** : le retour à la boutique doit vous permettre uniquement d'afficher un contexte visuel à l'acheteur. N'utilisez pas les données reçues pour effectuer le traitement en base de données.  

# Procéder à la phase de test
 
Préalablement au passage en production de la boutique, il est nécessaire de réaliser des tests pour s’assurer du bon fonctionnement entre le site marchand et la plateforme de paiement. 
Ces tests doivent impérativement être réalisés avant de demander le passage en production.  

## Réaliser des tests de paiement
 
Les demandes de paiement de test adressées via le formulaire HTTP POST doivent: 
 
 * Contenir la donnée **vads_ctx_mode** valorisée à **TEST**. 
 * Utiliser **le certificat de test** précédemment récupéré pour le calcul de la signature. 
   
En phase de test, le marchand peut tester les configurations 3D Secure (si ce dernier est enrôlé 3DS et si l’option 3DS n’est pas désactivée). 
Différents cas de paiements peuvent être simulés en utilisant les numéros de carte de test précisés sur la page de paiement. 
Toutes les transactions réalisées en mode test sont consultables par les personnes habilitées à utiliser le Back Office à l’adresse suivante :    
|  |      
Ces transactions sont consultables depuis le menu **Gestion >Transaction de test** situé en haut à gauche du Back Office. 

## Tester l'URL de notification instantanée (IPN)
 
Vérifiez tout d'abord l'état de l'URL de notification instantanée (également appelée IPN) dans le Back Office. 
Pour cela: 
 
 1. Effectuez un clic droit sur une transaction.
 2. Sélectionnez **Afficher le détail de la transaction**.
 3. Vérifiez le statut de l'URL de notification instantanée (IPN). 
 * Dans le cas où le statut est **Envoyé**, cela signifie que vous avez correctement renseigné l'URL dans le Back Office. 
 * Dans le cas où le statut apparaît en **URL non définie**, cela signifie que vous n'avez pas renseigné l'URL dans le Back Office. 
 1. Vérifiez l'adresse de l'URL de notification instantanée saisie en mode TEST et PRODUCTION. 
 2. Cliquez sur **Paramétrage** > **Règles de notification**.
 3. Renseignez l'URL de notification de paiement instantanée (URL de notification à la fin du paiement). 
Ne saisissez pas une adresse en "localhost". L'appel à cette l'URL se fait de serveur à serveur.
 4. Cliquez sur **Sauvegarder**.
 
 
 * Dans le cas où le statut est **Echoué**, se reporter au chapitre **Traiter les erreurs** du guide d'implémentation du formulaire disponible sur notre site documentaire ).
 
   

# Activer la boutique en mode production
 
Ce chapitre vous détaille de quelle manière vous pouvez : 
 * Générer le certificat de production.
 * Basculer votre site marchand en production.
 * Réaliser un premier paiement en production.
 * Régénérer le certificat de production (en cas de problème).
  

## Générer le certificat de production
 
Vous pouvez générer le certificat de production depuis le menu **Paramétrage** > **Boutique** > Onglet **Certificats** > bouton **Générer le certificat de production**. 
Une fois le certificat de production généré, sa valeur apparaît sous l'onglet **Certificats**. 
Un e-mail est envoyé à l'interlocuteur en charge du dossier (responsable administratif de la société) pour lui confirmer la génération du certificat de production. 

## Basculer le site marchand en production
 
 
 1. Valorisez le champ **vads_ctx_mode** à **PRODUCTION**.
 2. Modifiez la valeur du certificat de test avec la valeur de votre certificat de production pour calculer la signature.
 3. Renseignez correctement l'URL de notification de paiement instantanée (URL server à la fin du paiement) en mode PRODUCTION depuis le menu **Paramétrage** > **Règles de notification**.
   

## Réaliser un premier paiement de production
 
Nous vous conseillons de vérifier les deux points suivants : 
 
 * Le bon fonctionnement en environnement de production de bout-en-bout. 
Pour ce faire, effectuez une transaction réelle.
Cette transaction pourra être annulée par la suite depuis le Back Office via le menu **Gestion** > **Transaction** > onglet **Paiements en cours**. Cette transaction ne sera donc pas remise en banque.
   
 
 * Le bon fonctionnement de l'URL de notification de paiement instantanée (Url de notification à la fin du paiement) renseignée dans le Back Office. 
Pour ce faire, ne cliquez pas sur le bouton **Retour à la boutique** après un paiement. 
Affichez le détail de la transaction dans le Back Office et vérifiez que le statut de l'URL de notification instantanée (Statut URL de notification) est bien **Envoyé.**
   


# FAQ
 
Une FAQ est disponible sur lenotre site Internet . 
Elle répertorie les questions fréquemment posées au sujet des codes d’erreurs retournés lors de l’envoi du formulaire de paiement. 

