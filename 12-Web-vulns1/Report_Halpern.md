# OWASP Top 10 - A Primer
This document explores the 10 vulnerability classes discussed in [OWASP Top 10 - 2017](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

## Vulnerabilities
### A1:2017 - Injections
 #### Definition / Description
 - Injection is the malicious input into a data source that exploits the underlying language to run commands. Any source of data can be used as an injection vector. Injection vectors pose serious threats since they compromise data (confidentiality) opening up more vectors from attacks. Injection can result in data loss, corruption, information leakage, ddos attacks, thus as mentioned opening the system up to many other possible vectors of attack. If data is lost the confidientiality and availabilty of the data is down costing companies millions of dollars.
 - Injection can be used for various things from setting up a backdoor to aquiring data from a database. The main purpose of command injection is to cause a site's underlying language to execute a program or command it was not initially inteded to run.  

 #### How it Works

 - First an attacker must identify if there is an injection point on a site. The easiest injection points are unsanitized data. Even if there is sanitization, they must now understad the type sanitization. Then they must understand what language they can inject with. This can be done by typing in comment signs of different scripting languages to see if it breaks the query or search, looking at the source code and the source links in the source code, typing in commands to see if results yield. Source code review is the best method of detection. Another good method of detection is automated test of all parameters and data points such as headers, URL, cookies, JSON, SOAP, and XML. Once they discover what language and data points are vulnerable they must build their injection payload based of what they choose to accomplish and exploit.

 #### Scenario

 ```
 1 UNION SELECT 1,concat(login,':',password),3,4 FROM 
 ```
 ```
 <http://ptl-f99df351-3bdd4c8f.libcurl.so/cat.php?id=1%20UNION%20SELECT%201,concat(login,%27:%27,password),3,4%20FROM%20users>
 ```
 - The URL contains a union tag which dumps data from row 1,3,4 and concatonates login and password fields with a colon between them to dump the user login data from all users. This method submits the union tag through the id parameter in the URL. The method is also sanitized, so direct injection is not necessary easy, the injection must first get sanitized or submited through a query on the site where the site sanitizes the data. The first value in the injectionis a working database id, then the union tag adds to the command concatinate in a sense a new query along with the previous. This allows the attacker to inject whatever query they desire since the query before the '1' is not visible to the user. The attacker inputed query will yeiled a tidy list of all the usernames and passwords side by side, alowwing the attacker to pick and choose his credentials to use. One strategy to use would be to set the id field to be only submitted if it is under a certain length, or set the id field to only accept integers. Another way to patch this vulnerbility is to not submit the query data through the URL, or make it not visible to the user.

 ### ### After injection ### ###:
 ```
  <!data from id value 1 >
  <!data from id value 1 >
  username:password
  user:pass
  us:ps
  soemthing:something
  admin:admin
  ...
  ...
  <!data from id value 3>
  <!data from id value 4>
 ```

 - An example of a command injection vulnerability can be seen on the DVWA Command Injeciton page which contains a filed in which the user inputs an ip address and the php code behind the page sends the code through system('ping <$ip>'), which is a php module that runs terminal commands. By using a ';', '||' ( OR statement ), '&&' ( AND statement ), or a comment '#' one is able to inject there own commands being run on the victims server. Thus the attacker potentially is able to access the 'passwd' file containing the users of the system, see the current identity of the user they are running as, including the privildges fo the user, potentially even run a reverse shell and gain full terminal access to their machine.
 Command injecton opens up more vulnerabilities than sql injection simply becuase command injection can provide direct immidate access to the victims terminal on most cases. SQL injection can provice the credentails of the usrs and possibly the admin, opening up more attack vectors. SQL injection is dealing with the database side of the code, injecting queries to yield their desired responses and gather data. Code Injection is dealing with a terminal, or scripting language in which an attacker is able to inject their payload and get their service to respond with data, response on a listened port, removal, changing, and or injection of data.



---
### A2:2017 - Broken Authentication
 #### Definition / Description

 - Broken Authentication give attackers access to thousands of millions of valid username and password combinations for bruteforcing, and dictionary attacks. This includes session management attacks such as the use of unexpired session tokens in session hijaking. Broken authentication is due to the poor design and implementation of most identity and access controls. Session management is present in all stateful applications and is the baseline of authentication and access controls. Understanding session managment is vital, allowing attackers to identify broken authentication manually and exploir them using automated tools such as bruteforcing. Broken authentication allows attackers to gain access to a system either by exploiting the authentication either giving them adminstrator credentials or simple credentials in which they can use permission escalation. Attackers gaining only a few accounts can compromise the system. Depending on the domain of the application, compromising the system could mean exploitation of the resources of the domain and possibly compromising integrity and confidentiality of the data within.
 - Through the infilitration through broken authentication, the CIA triad can be disrupted. The data loses its confdentailty and integrity as it is exposed. Due to the system being compromised it is possible for the availability of the site to go down, costing the domain potentially milions of dollars. Gaining access to the system allows the attacker to insert backdoors and further compromise the system let alone the domain. 

 #### How it Works


 #### Scenario
 - The excersize in DVWA qualifies as a broken authentication since, it doesn't have attempt couting ( atleast on low security ), thus the bruteforcer is allowed as many attempts until it is able to crack the passwords of the user and gain access to the authentication. Another reason the example qualifies as broken authentication is because the data is visible in the post request and can be manipulated.
 ---
 #### #### RAW REQUEST #### ####:
 ```
 GET /dvwa/vulnerabilities/brute/?username=&password=&Login=Login HTTP/1.1
 Host: localhost
 User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
 Accept-Language: en-US,en;q=0.5
 Accept-Encoding: gzip, deflate
 Referer: http://localhost/dvwa/vulnerabilities/brute/
 Cookie: security=low; PHPSESSID=ehjttu330l2itksvehcjcov6j0
 Connection: close
 Upgrade-Insecure-Requests: 1
 ```

 #### #### POSITIONS SET IN INTRUDER #### ####:
 ```
 GET /dvwa/vulnerabilities/brute/?username=§§&password=§§&Login=Login HTTP/1.1
 ```

 #### #### RAW REQUEST CONTAINING CORRECT CREDENTIALS #### ####:
 ```
 GET /dvwa/vulnerabilities/brute/?username=admin&password=password&Login=Login HTTP/1.1
 ```

 ##### Mitigation

  - One strategy to preventing this kind of attack is by dropping requests if they are flooded to the server at a certain interval ( meaning the attacker is using an automated bruteforcer ), as well as allowing only a certain number of attempts.
  - Another strategy to preventing this kind of attack is by using a CAPTCHA which requires a user to enter a value or response for ever new log in attempt.

---
### A6:2017 - Security Misconfiguration
 #### Definition / Description

 - Security misconfiguration is caused by lack of patching and and access to default accounts, unused pages, and unprotected direcotires. These can be used to gane knowledge of the system opening up future attack vectors. It can lead to the compromising of a system, as well as the compromising of the CIA triad. By gaining access to the system throguh security misconfigurations, an attacker can discover where uploads are place, and run their own script on the server, cmpromising the availabilty, integrity and confidentiality of data if desired, thus again costing possibly millions of dollars. Security misconfiguration can happen at any level of the application stack. 
 - Misconfiguration resulting in a hack can result in accounts being leaked, the service going under and the domain losing profits, private information beign stolen, as well as custom code installation for future attack vectors.

 #### How it Works

 - allow_url_fopen and allow_url_include work together to allow URI access to files. '..._include' allows wrappers to be used to transverrse pages specifically both local and remotefiles. This allows the RFI vulnerability on DVWA, as the 'page=' parameter in the URI is exploitable as well as the GET-requests. 
 - RFI and LFI are vulnerabities found when a web application allows fro user submited input into files or upload files to a server. LFI allows an attacker to potentially read and execute files on the victims computer. RFI is easier to exploit since it allows the server to send GET requests to other domains and files not found on the client's server. This allows for malicious uploads and escalation to RCE.
 - RFI qualifies as a securiy misconfiguration because configuration, permissions, and proper sanitization was left unchecked on the victims server. These configuration lines, as well as webserver user permissions allow the attacker many vectors of infiltration and privildge escalation. 

 #### Scenario

  ```php
  
  // TODO: Disables allow_url_fopen
  allow_url_fopen= Off
  // TODO: Disables allow_url_include
  allow_url_include= Off

  //OR alternatively run the following in your php file uploaded to the victims server:
  ini_set('allow_url_include', 'Off');
  ini_set('allow_url_fopen', 'Off');

  ```
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