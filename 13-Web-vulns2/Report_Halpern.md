# OWASP Top 10 - A Primer
This document explores the 10 vulnerability classes discussed in [OWASP Top 10 - 2017](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

## Vulnerabilities
### A3:2017 - Sensitive Data Exposure
#### Definition / Description
TODO: Use the OWASP document to explain
 - The source, severity, and scope of sensitive data exposure
```
  - Sensitive Data Exposure occurs when information which is transfer is exposed to being exploited and stolen. An easy example of this is the transfering of clear text over a http-post-form requestfrom a client's computer. This vulnerability is generlly caused by poor encryption or unenrypted data floating around. This attack could potentially be very severe depending on the type of data which is stolen or leaked. A manual attack is generally required for the retrieval of this data. If the data is admin or root credentials, or private personal infomration, it can be sold or used for another exploit. This vulnerability can be used to steal sensitive personal information, credentials, personal data, credit cards, anything that is sent over to the server unencrypted. This vulnerability affects any type of internet connected form data. 
```
 - What kind of damage it can do to a business
 ```
  - This type of attack can criple a business. If the admin credentials are exposed, an attacker can do whatever they may please on the server, from installing back doors to transfering money to their accounts. If admin privilidges are not aquired, privilidge escalation can be used to gain admin privilidges.
```
#### How it Works
TODO: Define **Local File Inclusion (LFI)**, and explain why it's an example of a Sensitive Data Exposure vulnerability.

```
  - Local File Inclusion allows the attacker or user to enumerate and execute commands from the local file system to the server. Local File inclusion is the same as Remote File Inclusion however LFI only consists of including local files. The attacker can now gain access to the information on the server by searching and enumerating the server from within. If exploited they now have access to sensitive data used to either further enumerate the system or discover a mode of infiltration. 
```
#### Scenario
TODO: Explain the LFI vulnerability you explored on the DVWA **File 
Inclusion** page.
  

Specifically, explain
- How you perform the attack
  - **Note**: Include the URL you use to demonstrate the LFI, and provide a screenshot of the output it generates.
- Why the attack works
- How the server could be configured to prevent this attack
```
  - You would perform an attack by changing the parameters in the uri, to a known source, such as "/etc/passwd" and see if the file is pulled up by the LFI. After discovering if this is exploitable, you can change slowly enumerate the folders in the system by listing or exploring what files are accessible.
      127.0.0.1/dvwa/vulnerabilities/fi/?page=/etc/passwd
  - local file inclusion, or file inclusion works because the server is trying to request a page form the inputed or changed field. If that parameter is visible or accesible it can be changed and then the server attempts to fetch a page from the injected parameter. If the parameter passes through some sort of filtration and or sanitization it can make it increasingly difficult to perform this attack. Further isolating the parameters to a strict data set such as only the pages you want to link to further secures the local file inclusion.
```
  ---
### A4:2017 - XML External Entities (XXE)
#### Definition / Description
TODO: Use the OWASP document to explain
 - The source, severity, and scope of XXE attacks
 
```
  - XEE attacks are caused by a server reading or interpreting malicious xml code or exploited vulnerable xml code with vulnerable xml processors. The attacker uploads exploited or vulnerable xml documents exploitung vulnerable code, dependecies, and or integreations. Many Xml processors allow specifications of external entities suach as a URI that is derefernced. This URI is evaluated during XML processing, exploiting this URI allows infiltrationa and data extraction, etc.
  This trheat is not quite sever due to the many tools that are available to check for these vulnerabilities. Any xml-based webservice or application that accepts xml directly or xml uploads is vulnerable to this attack.
```
  - What kind of damage it can do to a business

```
 - Exploiting this vulnerability an attacker is able to extract sensitive  data, execute a remote request, scan internal systems, perform a denial-of-service attack, compromising the availability of the website and the integrity and confidentiality of the data. Costing the company thousands if not millions fo dollars, adn losing their data reputability.
```

#### How it Works
TODO: Explain the following:
  - What XML is
```
xml stands for eXtensible Markup Language, and is a language similar to html ( and XHTML ). Xml was designed to store and transport data. Xml is a self descriptive language. THe tags like html are self descriptive, hwever in xml they are far more specific. Xml doesn't take any action, simply organizes the information. Unlike html, xml tags are not predefined they are defined by the author as they go. Xml simplifies data sharing, transport, and availability.

```

  - How web applications use XML


```
Many computer systems contain data in incompatible formats, while xml puts the data in an interexchangable format. Web applications take the data from the xml document and interpret it. Xml works as an interlanguage information carrier.

```
  - Why web applications can be attacked via XML uploads

```
Web applications are vulnerable to xml upload attacks because of XXE (XML External Entity). XXE allows the inclusion of data dynamically from a given resource, be it local or remote. If XML parsers aren't configured to prevent or limit XXE, then they are forced to access the resources specified by the URI. 
```

  - Ways that XXE payloads can be delivered

```
An attacker can upload a file to the server which would execute commands upon run time, or upload a file that sends a reverse tcp connection to a computer allowing the attacker a reverse shell.
Another payload that could be exploited is a blind xml injection, which is the xml document pulling a local file from the server and printing that file's contents as the result of the data being sent over in the xml document. 
You can also use Xml ( not necessarily xxe) to DDOS and bring donw a system. 
An attacker can also use XML ( not necessarily xxe) to create a server side request forgery. 

```

#### Scenario
TODO: Use your knowledge of command injections to explain what each of the following XXE payloads does.

##### Payload 1
```xml
<?xml version="1.0" encoding="ISO-8859-1"?> <!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]> <foo>&xxe;</foo>
 ```
 TODO: Explain what this payload is used for, and identify which other OWASP vulnerability is relevant.
 
 - the payload above ( Payload 1 ) is a blind XXE injection. It is requesting from the server the file "/etc/passwd" and then displaying the contents of the file in the documentation. It is remotely dumping the passwd file to the attacker.

 ##### Payload 2
```xml
<!ENTITY xxe SYSTEM "https://192.168.1.1/private" >]>
 ```
 TODO: Explain what this payload is used for, and identify which other OWASP vulnerability is relevant.

 - The payload above ( Payload 2 ) forces the server to send a request to the ip. This payload can allow an attacker to possible open up areverse tcp connection by making the server send a request to the above URL. By doing so, the attacker can execute code through the URL or on the site.

##### Payload 3
```xml
<!ENTITY xxe SYSTEM "file:///dev/random" >]>
 ```

TODO: Explain why this payload attempts to download an endless file.

- The payload above ( Payload 3 ) attempts to download an endless file, because "/dev/random" is a file that acts as a psudo random number generator as it si a file that is continuously written to. Thus the server attamept to download a file that is constantly being written to as random numbers are consistently being generated.

---
### A5:2017 - Broken Access Control
#### Definition / Description
TODO: Use the OWASP document to explain

- The source, scope, and severity of broken access control vulnerabilities
- What kind of damage it can do to a business

  - Broken Access Control is a common due to the lack of automated detection, as well as the lack of effective functional testing. Access control enforces policy sucha that the users cannot act ourside of their intended permissions. Failure to secure a users position in a system can lead to uncauthorized information disclosure and potential privilidge escalation. 
  The impact of broken access control is that users can elevate their priviliges or act as toehr users or administrators. This can open up various attack vectors as the attacker is able to run adminstartive commands and can exploit this vector and widen it. 
  The attack vector is moderatly severe. Due to detention methods it is possible to detect the absence of access control, however access control detection isn't typically amendable to static or dynamic automated testing. Manual testing is the best and more effective way of testing. 

  - The damage this attack vector, like most attack vectors, when pushed, can be severe and devasting costing millions of dollars. The impact depends on the data being store and the necessity of the CIA triand in the data. If the data/ service isn't critically important in the aspect of availabilty and confidentiality then the impact financially may be lower. There is a higher impact on the integrity of the systems in an attack like this.

#### How it Works
TODO: Explain why LFI also qualifies as a Broken Access Control vulnerability!

- Local file inclusion qualifies as a Broken Access Control becuase is allows an attackers to misuse the permissions/ gain access to files they weren't meant to. If an attacker is able to gain access to files that aren't in the scope of the local file inclusion then the local file inclusion is vulnerable and is also catagorized as a broken acess control.

#### Scenario
Suppose you log into an application as the user `jane`, and get redirected to: `https://example.site/userProfile.php?user=jane`.

Suppose Jane is able to see Bob's profile by navigating to: `https://example.site/userProfile.php?user=bob`

- This is called **Insecure Direct Object Reference (IDOR)** Read about it here: <https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)>.

 - This secenario is both a Broken Access Control vulnerability and XSS vulnerability. By changing the value fo the Directo Object Reference the attacker si able to access data that is out of their scope. As well as the server acceptig unauthenticated access to the changed direct object reference in the URI this display a XSS vulnerability.
---
### A7:2017 - Cross-Site Scripting (XSS)
#### Definition / Description

 
 - XSS is caused by the application including invalidated, unescaped, unchecked user input. XSS can occur as reflected, stored, and DOM. Reflicted causes responses to executed on the victims browser, stored causes a stored malicious response to be store on the server affecting anyone who browses or activates the response, while DOM involves javascript framework, single-page applications to store and dynamically use attacker-controlled data. Cross site scripting includes session stealing, account takeover, cookie hijaking, phishing, DOM node replacement, key loggers, etc. This can lead to impersonation and the compromisation fo credentials. Through those credentials more attack vectors can be discovered. This could potentially escalated to be very severe due to the compromization of the confidentiality of data, as well as impersonation leading the compromization of the integrity of the data being passed on. Left unchecked could be matched with other attack vectors potentially infiltrating the system and breaching the availabilty of the system, costing the domain , once again, millions of dolalars.

 #### How it Works

  - A reflected xss payload gets loaded into the html document through a GET request. If the page is dynamic it can load the request into the domain. If the page is static and the headers of the GET/POST request allow it, the code can get interpreted by the server and returned.
      ```
      Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

      ```
  The above line shows the formatting and type of the accepted requests. 

 #### Scenario

 ```
  http://localhost/dvwa/vulnerabilities/xss_r/?name=%3Cimg+src%3D%22incalid%2F%22+onerror%3D%22alert%281%29%22%2F%3E#
```
 ```
 GET /dvwa/vulnerabilities/xss_r/?name=%3Cimg+src%3D%22incalid%2F%22+onerror%3D%22alert(1)%22%2F%3E HTTP/1.1
 Host: localhost
 User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
 Accept-Language: en-US,en;q=0.5
 Accept-Encoding: gzip, deflate
 Cookie: security=low; PHPSESSID=ehjttu330l2itksvehcjcov6j0
 Connection: close
 Upgrade-Insecure-Requests: 1
 ```
 ### ### REFLECTED PAYLOAD ### ###:
 ```
 <img src="invalid/" onerror="alert(1)"/>
  ```
 - The reflected XSS on DVWA works by passing the input to an output which prints a result to the screen. The output in interpreted in a dynamic javascript statment allowing for html to be passed to it and run on the victims browser. The javascript is seen encoded in the browser thus can be sent to others through a link ina phishing email, etc.

 - If this script is accepted by a comment field or soemthign that is persistant on the site, this paylaod can transition into being a Persistant payload, where it is executed every time someone accesses the comment.

### A8:2017 - Insecure Deserialization
#### Definition / Description
TODO: Use the OWASP document and this [Acutenix article](https://www.acunetix.com/blog/articles/what-is-insecure-deserialization/) to explain the following:
- What serialization is

```
Serialization is the process of conerting an object into a format which can be saved, or transmitted. The way an object is serialized is in either binary or structured text such as json or XML. 
```

- What deserialization is

```
Deserialization is the opposite or inverse of serialization. It is the transfer of data from binary or strcutrued data over a sock(et) or network,stream, etc into a file or object. 
```

- What web applications use serialization/deserialization for

```
Web applications use serialization in the transfer of data in a general basis. Safe deserialization of obejcts is normal practice, however the issue arries upon untrusted useer input. An example of serialization and de serialization is in the post request of a form from a sight. The text is serialized into json formatted informationa nd sent over the http protocol to the server, where is deserialized into an object and than interpreted. 

```

- What kinds of attacks can be carried out by exploiting insecure deserialization bugs

```
An attacker is able to carry out many attacks exploiting insecure deserialization. Using insecure deserialization they are able to carry out DOS attacks, authentications bypasses, and remote code executions. Through these attacks theya re able to thus further expand the attack vector and use these exploitable attacks to further push the attack vector and gain access ot the system. 
```
- 
#### How it Works / Scenario
TODO: Explain how the exploit discussed in the Acutenix article achieves remote code execution (RCE). 


```
The Acutenix article achieves remote code execution by using python through the use of the module pcikle. It deserializes using pickle.loads(). The attacker serializes data and then sends it over to the victims server to be deserialized and interpreted. In order to attempt to avoid insecure binary deserialization is the use of json, xml, yaml. However even these are vulnerable, XXE as mentioned before falls under this scope. through XXE or YAML one can inject data to achieve RCE through an insecure deserialization of the structured text data. In order to secure oneself, it is safe practice not to deserialize data sent over a network from an unknown location. A pyYAML method was created for more secure deserialization: yaml.safe_load()

```

### A9:2017 - Using Components with Known Vulnerabilities
#### Definition / Description
TODO: Use the OWASP document to define the vulnerability.

 - Using components with known vulnerabilities becomes an issue when software is not kept up to date and the software in use or used in the applciation or API aren't secure. This opens up multiple attack vectors that could easily be exploited and in many cases possibly avoided.
 - Some of the largest breaches in data have occured due to exploitations of known vulnerabilties. Hoever this Attack vector doesn't stop on known vulnerabilties. If the applications beign used or the software along the manufacture chain are vulnerable or exploited, it could lead to custom built exploits.

#### How it Works
TODO: Use [this article](https://news.thomasnet.com/featured/new-nist-framework-focuses-on-supply-chain-security/) to explain supply chain risk in general.

```
Supply Chain vulnerabilities are caused by many facotrs ranging from poor manufacturing to untrustworthy partnerships, tampering, mergers, and malicious code injection. A Supply Chain attack is defined as a vulnerability in the development level of the code, prgoram, or object. This can lead to further exploitions, straining of software, and bypassing authentication, etc.
```


#### Scenario
TODO: Read about the [leftpad incident](https://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos/), and discuss how this scenario almost seems like an accidental DoS attack.

```
Due to the base of the open-source platform NPM was hosting, many projects built their systems off of the packages found in NPM. However due to the open-source nature, if the author unpublisehd his package, it is like decredited a pacakage and the package is no longer usable. The package in this case was written by an author who was frustrated by the legal strifes of NPM lawyers, etc. The author unpublished all his work. The pacakges which he published were used in the base of many open-sourced application. Unpublishing his package removed them from the dependency trees, inadvertanlty crashing all the opensource software that was building off of it.
```


### A10:2017 - Insufficient Logging & Monitoring
#### Definition / Description
TODO: Use the OWASP document to define the vulnerability.

 - Attackers rely ont he lack of proper response to make way for any of their chose attacks. If there is insufficient logging and poor or lack of monitoring there is likely a very large response time. This means the attacker is able to proceed unnoticed for large periods of time. The most succesful attacks begin with vulnerabiltiy probing. In the detection of these probings, it is easier to stop the attack before it happens.

#### How it Works / Scenario
TODO: Give an example scenario in which insufficient logging/monitoring hindered forensic or defensive efforts.

```
The OWASP document speaks of a scenario where a US retailer was implementing internal malware analysis analyzing attachments. THe detection detected unwanted software, however no one was around/ no one responded to this event thus the event went unchecked for some time as the detection service continued to produce warnings. This example shows that with monitoring and detection, a vulnerability can still be exploited. Alerts are created for responses, not just to be alreated.
```

