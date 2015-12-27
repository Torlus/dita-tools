---
layout: docs
permalink: /docs/chap-9/
title: chap-9
---
<h1>
9. Calculer la signature
</h1>
  
<p>
Afin de pouvoir calculer la signature vous devez être en possession de la totalité des champs dont le nom commence par 
<b>vads_</b> et du 
<b>certificat</b> (la valeur du certificat permet de calculer la signature numérique.
</p>
 
<p>
Pour calculer la signature :
</p>
  <ol>
 <li>
 
<p>
Triez les champs dont le nom commence par 
<b>vads_</b> par ordre alphabétique.
</p>
 
</li>
 <li>
 
<p>
Assurez-vous que tous les champs soient encodés en UTF-8.
</p>
 
</li>
 <li>
 
<p>
Concaténez les valeurs de ces champs en les séparant avec le caractère &quot;
<b>+</b>&quot;.
</p>
 
</li>
 <li>
 
<p>
Concaténez le résultat avec le certificat de test ou de production, en les séparant avec le caractère &quot;
<b>+</b>&quot;.
</p>
 
</li>
 <li>
 
<p>
Appliquez l’algorithme SHA-1 pour obtenir la valeur de la signature.
</p>
 
</li>
 
</ol>
 
<p>
 
<p>

<u>Exemple de paramètres envoyés à la plateforme de paiement</u>:<code><pre>
&lt;form method=&quot;POST&quot; action=&quot;<a href="https://secure.payzen.eu/vads-payment/">https://secure.payzen.eu/vads-payment/</a>&quot;&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_action_mode&quot; value=&quot;INTERACTIVE&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_amount&quot; value=&quot;1524&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_ctx_mode&quot; value=&quot;TEST&quot; /&gt;
&lt;input type=&quot;hidden&quot; name=&quot;vads_currency&quot; value=value=&quot;978&quot;
</pre></code>

</p>
 
</p>
 
<p>
 
<p>
Cet exemple de formulaire s&#x27;analyse de la manière suivante:
</p>
 
<p>
 
<ol>
 <li>
On trie par ordre 
<b>
<u>alphabétique</u></b> les champs dont le nom commence par 
<b>vads_</b> : 
<ul>
  <li>
vads_action_mode
 </li>
  <li>
vads_amount
 </li>
  <li>
vads_ctx_mode
 </li>
  <li>
vads_currency
 </li>
  <li>
vads_page_action
 </li>
  <li>
vads_payment_config
 </li>
  <li>
vads_site_id
 </li>
  <li>
vads_trans_date
 </li>
  <li>
vads_trans_id
 </li>
  <li>
vads_version
 </li>
 
</ul>

</li>
 <li>
On concatène la valeur de ces champs avec le caractère &quot;
<b>+</b>&quot; : 
<p>

<b>INTERACTIVE+1524+TEST+978+</b>
</p>

</li>
 <li>
On ajoute la valeur du certificat de test à la fin de la chaîne en la séparant par le caractère &quot;
<b>+</b>&quot;). Dans cet exemple, le certificat de Test est 
<b>1122334455667788</b> :
<p>

<b>INTERACTIVE+1524+TEST+978+</b>
<b>20090501193530+654321+V2+1122334455667788</b>
</p>

</li>
 <li>
On applique l’algorithme SHA-1 à la chaîne obtenue. 
<p>
Le résultat à transmettre dans le champ signature est : 
<b>606b369759fac4f0864144c803c73676cbe470ff</b>.
</p>

</li>
 
</ol>
 
</p>
 
</p>
 <!-- tla1406131496729.xml -->
<h2>
9.1. Exemple d&#x27;implémentation en JAVA
</h2>
 Définition d’une classe utilitaire Sha qui contiendra ce qui est nécessaire au traitement de l’algorithme SHA1.<code><pre>
import java.security.MessageDigest; 
import java.security.SecureRandom; 
public class Sha {
       static public final String SEPARATOR =  &quot;+&quot; ;
       public static String encode(String src) {
             try {                   
          		MessageDigest md;
                    md = MessageDigest.getInstance( &quot;SHA-1&quot; );                  
            	   byte bytes[] = src.getBytes( &quot;UTF-8&quot; );                          
				md.update(bytes, 0, bytes. length );                   
            	   byte[] sha1hash = md.digest();                
            	   return convertToHex(sha1hash);
             } catch(Exception e) {                   
            	  throw new RuntimeException(e);
             }       
	   }        	   
        private static String convertToHex(byte[] sha1hash) {
              StringBuilder builder = new StringBuilder(); 
              for (int i = 0; i &lt; sha1hash. length ; i++) {                   
            		byte c = sha1hash[i];                 
            		addHex(builder, (c &gt;&gt; 4) &amp; 0xf);                   
            		addHex(builder, c &amp; 0xf);
              }             
		    return builder.toString();
       }        
	  private static void addHex(StringBuilder builder, int c) { 
            if (c &lt; 10)                   
          	   builder.append((char) (c +  &#x27;0&#x27; ));
            else                   
          	   builder.append((char) (c +  &#x27;a&#x27; - 10));
       }
}
</pre></code>

              
<p>
Fonction qui calcule la signature:
</p>
 
<p>
 <code><pre>
public    ActionForward performCheck(ActionMapping actionMapping, Basivoirorm form, HttpServletRequest request, HttpServletResponse response){
          SortedSet&lt;String&gt; vadsFields = new TreeSet&lt;String&gt;();
          Enumeration&lt;String&gt; paramNames = request.getParameterNames(); 
          // Recupere et trie les noms des champs vads_* par ordre alphabetique
          while (paramNames.hasMoreElements()) {
                String paramName = paramNames.nextElement();
                if (paramName.startsWith( &quot;vads_&quot; )) {
                       vadsFields.add(paramName);
                }
          }
          // Calcule la signature
          String sep = Sha.SEPARATOR;
          StringBuilder sb = new StringBuilder();
          for (String vadsParamName : vadsFields) {
                String vadsParamValue = request.getParameter(vadsParamName);
                if (vadsParamValue != null) {                   
                      sb.append(vadsParamValue);
                }
	           sb.append(sep);
           } 
           sb.append( shaKey );
           String c_sign = Sha.encode(sb.toString());
           return c_sign;}
</pre></code>

			
</p>
  <!-- tla1406132636881.xml -->
<h2>
9.2. Exemple d&#x27;implémentation en PHP
</h2>
  
<p>
 <code><pre>
// Fonction qui calcule la signature
// $params : tableau contentant les champs à envoyer dans le formulaire
function getSignature($params){
	//Initialisation de la variable qui contiendra la chaine à chiffrer
	$contenu_signature  =  &quot;&quot; ;
	
	// tri des champs par ordre alphabétique
	
	ksort($params);
     foreach ($params as $nom =&gt;$valeur)
	{  
	// Récupération des champs vads_ 

       if (substr($nom,0,5)==&#x27;vads_&#x27;) {                   
           // Concaténation avec le séparateur &quot;+&quot;       
           $contenu_signature .= $valeur.&quot;+&quot;;
	  }
	}
// Ajout du certificat à la fin
$contenu_signature .= $key;
// Application de l’algorythme SHA-1
$signature = sha1($contenu_signature);

return $signature ;
}
</pre></code>

			
</p>
  <!-- emm1405088387247.xml -->
