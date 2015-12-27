---
layout: docs
permalink: /docs/chap-5/
title: chap-5
---
<h1>
5. Établir le dialogue avec la plateforme de paiement
</h1>
 <!-- emm1405084806450.xml -->
<h2>
5.1. Définir l&#x27;URL de la page de paiement
</h2>
 Le site marchand communique avec la plateforme de paiement en redirigeant l’acheteur vers la page :
<table>
     <tr>
   <td>
<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>
  </td>
 
 </tr>
   
</table>
 <!-- emm1405084895977.xml -->
<h2>
5.2. S&#x27;identifier lors des échanges
</h2>
  
<p>
Pour dialoguer avec la plateforme de paiement, le marchand a besoin de deux informations :
</p>
 
<p>
 
<ul>
  <li>

<b>L’identifiant boutique</b>: permet d&#x27;identifier le site marchand durant les échanges. Sa valeur est transmise dans le champ 
<b>vads_site_id.</b>
 </li>
  <li>

<b>Le certificat </b>: permet de calculer la signature numérique transmise dans le champ 
<b>signature</b>. 
 </li>
 
</ul>
 
</p>
 
<p>
Pour récupérer ces valeurs :
</p>
  <ol>
  <li>
 
 <p>
Connectez-vous à votre Back Office : <a href="https://secure.payzen.eu/vads-merchant/">https://secure.payzen.eu/vads-merchant/</a>
 </p>
 
 </li>
  <li>
 
 <p>
Cliquez sur 
<b>Paramétrage &gt; Boutique</b>.
 </p>
 
 </li>
  <li>
 
 <p>
Sélectionnez l’onglet 
<b>Certificats</b>.
 </p>
 
 <p>
 
 <p>
Visualiser l’identifiant de la boutique et le certificat
 </p>
<img src="/docs_img/tla1413904451582.image" alt="OngletCertificat"/> 
 </p>
 
 </li>
 
</ol>
 
<p>
 
<p>
Deux types de certificat sont mis à disposition :
</p>
 
<p>
 
<ul>
  <li>
Le 
<b>certificat de test </b> qui permet de générer la signature d’un formulaire en mode test.
 </li>
  <li>
Le 
<b>certificat de production </b>qui permet de générer la signature d&#x27;un formulaire en mode production.
 </li>
 
</ul>
 
</p>
 
</p>
 <!-- emm1405084935055.xml -->
<h2>
5.3. Choisir le mode Test ou Production
</h2>
 
<p>
Le choix du mode 
<b>TEST</b> ou 
<b>PRODUCTION</b> s&#x27;effectue en utilisant le champ 
<b>vads_ctx_mode</b> (Voir chapitre 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>).
</p>
 
<p>
 
<ul>
  <li>
Le mode 
<b>TEST</b> permet de réaliser des paiements de test. 
 <p>

<b>Il est toujours disponible</b>, même après la génération du certificat de production.
 </p>
Si vous créez un nouveau site marchand (ou disposez d’un environnement de recette), vous pourrez effectuer vos tests sans impacter le site actuellement en production. 
 <p>
Les transactions de TEST sont visibles dans le Back Office depuis le menu 
<b>Gestion</b> &gt; 
<b>Transactions de Test</b>
 </p>
 
 <p>
Visualiser les transactions de test
 </p>
<img src="/docs_img/tla1437559365689.image" alt="MenuTransactionTest"/>
 </li>
  <li>
Le mode 
<b>PRODUCTION</b> n’est disponible qu’une fois le certificat de production généré (voir chapitre 
<b>Activer la boutique en mode PRODUCTION</b>
 </li>
 
</ul>
 
</p>
 
<p>

</p>
 <!-- emm1405084980499.xml -->
<h2>
5.4. Gérer le dialogue vers le site marchand
</h2>
 
<p>
La gestion du dialogue vers le site marchand est réalisée grâce à deux types d’URL :
</p>
 
<p>
 
<ul>
  <li>

<b>Url de notification instantanée</b>, également appelée IPN (Instant Payment Notification),
 </li>
  <li>

<b>Url de retour</b> vers le site marchand.
 </li>
 
</ul>
 
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<u>Url de notification instantanée - IPN (Instant Payment Notification)</u>
</p>
 
<p>
La plateforme de paiement notifie automatiquement au site marchand le résultat du paiement. Les données sont envoyées en mode 
<b>POST</b>. 
</p>
 
<p>
La plateforme est capable de contacter le site marchand quel que soit le protocole utilisé (http ou https).
</p>
 
<p>

</p>
 
<p>

<b>Pour traiter</b> ces notifications, le marchand doit 
<b>créer une page</b> sur son site qui :
</p>
 
<p>
 
<ul>
  <li>
analyse les données reçues en mode 
<b>POST</b>,
 </li>
  <li>
s’assure de l’intégrité des informations reçues en calculant la signature,
 </li>
  <li>
vérifie qu’il ne s’agit pas d’un doublon de notification (renvoi de la notification depuis le Back Office par exemple),
 </li>
  <li>
déclenche la mise à jour de sa base de données (état de la commande, stock, etc…),
 </li>
  <li>
envoie des e-mails à l’acheteur (facture, suivi de commande, etc…).
 </li>
 
</ul>
 
</p>
 
<p>
Le temps de traitement influe directement sur le délai d’affichage de la page de résumé du paiement. Plus le traitement est long, plus l’affichage est retardé.
</p>
 
<p>

<b>Pour recevoir</b> les notifications, le marchand doit 
<b>paramétrer</b> les règles de notifications depuis son Back Office (voir chapitre 
<b>Paramétrer les notifications</b>). 
</p>
 
<p>
En cas de problème de communication vers le site marchand, la plateforme de paiement envoie un e-mail à l’administrateur de la boutique, précisant la raison de l’échec (erreur http, etc. …) ainsi que la procédure à suivre pour renvoyer la notification depuis le Back Office.
</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

</p>
 
<p>

<u>Url de retour vers le site marchand</u>
</p>
 
<p>
 
</p>
 
<p>
Le marchand peut paramétrer dans le Back Office les URL de retour &quot;par défaut&quot; depuis le menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; onglet 
<b>Configuration</b>) :
</p>
 
<p>

</p>
 
<p>
Spécification des URL de retour
</p>
<img src="/docs_img/tla1437559683519.image" alt="URLRetourV2.3"/> 
<p>
Il peut configurer une URL de retour à la boutique différente en fonction du mode.
</p>
 
<p>
Par défaut, l&#x27;acheteur est redirigé vers l&#x27;URL de retour, et ce, quel que soit le résultat du paiement.
</p>
 
<p>
Si toutefois aucune URL n’est configurée à ce niveau, alors la redirection utilisera l&#x27;URL principale de la boutique (paramètre 
<b>URL</b> défini dans l&#x27;encadré 
<b>Détails</b> de la boutique). 
</p>
 
<p>

</p>
 
<p>
Le marchand a la possibilité de surcharger cette configuration dans son formulaire de paiement (voir chapitre 
<b>Définir les URL de retour</b>).
</p>
 
<p>
 
</p>
 
<p>

<u>Remarque</u> :
</p>
 
<p>
Le statut de la règle &quot;URL de notification à la fin du paiement&quot; (IPN) est affiché dans cet écran. Si cette dernière est non paramétrée, veillez à la renseigner (voir chapitre 
<b>Paramétrer les notifications</b>) . 
</p>
 <!-- emm1405084278441.xml -->
<h2>
5.5. Gérer la sécurité
</h2>
 
<p>
Plusieurs moyens sont mis en place afin d’assurer la sécurité des transactions de paiement en ligne.
</p>
 <!-- emm1405084338582.xml -->
 <h3>
5.5.1.  Gérer la sécurité au moyen de la signature
</h3>
 
 <p>

 </p>
 
 <p>
L’intégrité des informations échangées est garantie par un échange de signatures numériques entre la plateforme de paiement et le site marchand. 
 </p>
 
 <p>

 </p>
 
 <p>
Le dialogue entre la plateforme de paiement et le site marchand s’effectue par soumission de formulaires HTML. 
 </p>
 
 <p>
Un formulaire contient une liste de champs spécifiques (voir 
<b><a href="#TODO-emm1405083451541.xml">Générer un formulaire de paiement</a></b>) utilisés pour calculer sa signature numérique (voir chapitre 
<b><a href="#TODO-emm1405088305497.xml">Calculer la signature</a></b>).
 </p>
 
 <p>
Le résultat de ce calcul doit être envoyé dans le champ 
<b>signature</b>.
 </p>
 
 <p>

 </p>
 
 <p>
Nous utilisons la fonction de hachage « SHA-1 » pour chiffrer la signature.
 </p>
 
 <p>
SHA-1 est disponible dans la plupart des langages utilisés dans le développement d’applications Web.
 </p>
 
 <p>

 </p>
 
 <p>
En fonction du language choisi, vous aurez peut être à coder vous-même les fonctions de hachage SHA-1 (comme en ASP par exemple). 
 </p>
 
 <p>

 </p>
 
 <p>
Pour vous aider, voici le résultat du SHA-1 du caractère &quot; a &quot; :
 </p>
 
 <p>
SHA1( &quot; a &quot;) = 86f7e437faa5a7fce15d1ddcb9eaeaea377667b8
 </p>
 
 <p>

 </p>
 
 <p>

<u>Modélisation des mécanismes de sécurité :</u>
 </p>
 
 <p>

 </p>

 <p>
Diagramme mécanisme de sécurité
 </p>
<img src="/docs_img/tla1437748696912.image" alt="DiagrammeSignature"/> 
 <ol>
   <li>
Le site marchand récolte les données du formulaire et calcule la signature.
  </li>
   <li>
Le site marchand soumet le formulaire à la plateforme.
  </li>
   <li>
La plateforme réceptionne les données du formulaire et calcule la signature.
  </li>
   <li>
La plateforme compare la signature calculée avec la signature transmise par le site marchand.
  </li>
   <li>
Si les signatures diffèrent, la demande de paiement est rejetée.
  <p>
 Sinon, la plateforme procède au paiement.
  </p>

  </li>
   <li>
La plateforme réceptionne les données du résultat et calcule la signature de la réponse.
  </li>
   <li>
En fonction du paramétrage de la boutique (voir chapitre 
<b>Paramétrer les notifications</b>), la plateforme soumet le résultat du paiement au site marchand.
  </li>
   <li>
Le site marchand réceptionne les données et calcule la signature. Il compare la signature calculée avec la signature transmise par la plateforme.
  </li>
   <li>
Si les signatures diffèrent, le marchand analyse l’origine de l’erreur (erreur dans le calcul, tentative de fraude etc...) 
  <p>
Sinon, le site marchand procède à la mise à jour de sa base de données (état du stock, état de la commande etc…).
  </p>

  </li>
 
 </ol>
 <!-- emm1405084393028.xml -->
 <h3>
5.5.2.  Conserver le certificat de production
</h3>
 
 <p>
Dès le premier paiement réalisé avec une carte réelle, le certificat de production est masqué pour des raisons de sécurité.
 </p>
 
 <p>

 </p>
 
 <p>
Nous vous conseillons fortement de conserver ce certificat en lieu sûr (fichier chiffré, base de données etc…).
 </p>
 
 <p>

 </p>
 
 <p>
En cas de perte, le marchand aura la possibilité d’en générer un nouveau depuis son Back Office.
 </p>
 
 <p>
Pour rappel, le certificat de production est visible dans le Back Office depuis le menu 
<b>Paramétrage</b> &gt; 
<b>Boutique</b> &gt; onglet 
<b>Certificats</b>. 
 </p>
 <!-- emm1405084529041.xml -->
 <h3>
5.5.3.  Gérer les données sensibles
</h3>
 
 <p>
Des règles strictes régissent les transactions de paiement en ligne (Certification PCI-DSS).
 </p>
 
 <p>

 </p>
 
 <p>
En tant que marchand, vous devez vous assurer de ne jamais retranscrire en clair des données qui pourraient s’apparenter à un numéro de carte bancaire. Votre formulaire serait rejeté (code 999 - Sensitive data detected).
 </p>
 
 <p>

 </p>
 
 <p>
Evitez notamment les numéros de commandes de longueur comprise entre 13 et 16 caractères numériques et commençant par 3, 4 ou 5.
 </p>
 <!-- emm1405084624469.xml -->
<h2>
5.6. Utiliser une i-frame
</h2>
 
<p>
Une i-frame (in line frame) est utilisée pour afficher une page web dans une autre page web.
</p>
  
<p>

</p>

<p>

</p>
  
<p>

</p>
 
<p>

<u>Exemples de codes</u> :<code><pre>
&lt;FRAMESET&gt;     
	&lt;FRAME SRC=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;  
&lt;/FRAMESET&gt;
</pre></code>

</p>
 <code><pre>
&lt;iframe src=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;&lt;/iframe&gt;
</pre></code>

	<!-- tla1423737652888.xml -->
<h2>
5.7. Gérer les paramètres de votre boutique par fichier de configuration
</h2>
 
<p>
L&#x27;utilisation d&#x27;un fichier de configuration permet d&#x27;éviter de mettre des valeurs en dur dans le code.
</p>
 
<p>
Les fichiers de configuration peuvent contenir :
</p>
 
<p>
 
<ul>
  <li>
l&#x27;URL de la page de paiement, 
 </li>
  <li>
la valeur du certificat, 
 </li>
  <li>
la valeur de l&#x27;identifiant de la boutique,
 </li>
  <li>
etc...
 </li>
 
</ul>
 
</p>
 
<p>
Ces fichiers permettent de typer les données à sauvegarder.
</p>
 
<p>
Le programme qui génère le formulaire de paiement appelera le fichier de configuration avec le paramètre pour utiliser la valeur.
</p>
 
<p>
Il incombe au marchand de s&#x27;assurer :
</p>
 
<p>
 
<ul>
  <li>
des droits sur le fichier pour ne pas qu&#x27;il soit accessible de l&#x27;exterieur.
 </li>
  <li>
de répondre aux spécificités liées au langage de programmation utilisé.
 </li>
 
</ul>
 
</p>
 
<p>

<u>Exemple de fichier de configuration &quot;conf.txt&quot;</u> :<code><pre>
vads_site_id = 11111111
TEST_key = 2222222222222222
PROD_key = 3333333333333333
vads_ctx_mode = TEST
</pre></code>

</p>
 
<p>

<u>Exemple d&#x27;appel de fichier de configuration dans le formulaire de paiement</u> :<code><pre>
$conf_txt = parse_ini_file(&quot;conf.txt&quot;);
	if ($conf_txt[&#x27;vads_ctx_mode&#x27;] == &quot;TEST&quot;) $conf_txt[&#x27;key&#x27;] = $conf_txt[&#x27;TEST_key&#x27;];
	if ($conf_txt[&#x27;vads_ctx_mode&#x27;] == &quot;PRODUCTION&quot;) $conf_txt[&#x27;key&#x27;] = $conf_txt[&#x27;PROD_key&#x27;];
</pre></code>

</p>
 <!-- emm1405085350214.xml -->
