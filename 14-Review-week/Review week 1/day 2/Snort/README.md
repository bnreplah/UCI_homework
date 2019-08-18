## Interpreting Snort Rules

### Scenario

Because of the recent SQL injection attack, one of your technicians has installed Snort onto your network. Your technician has downloaded community Snort rules and has asked you to help them interpret them. Given the following list of rules, you will need to identify what each rule does to contribute to the overall network security. 

In this exercise, you will:

- Interpret rules that fire in response to suspicious ping probes.
- Use the Snort documentation to research additional rule options.

Refer to the Snort rule options documentation as you follow the instructions below: <http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node31.html>

**Good luck!**

### Instructions

#### 1. Explain the following ICMP Echo Reply rules. Be sure to identify the:
- Action
  'alert'
- Protocol
  'icmp'
- Source/destination addresses
  'source any $EXTERNAL_NET to any $HOME_NET
- Meaning of each new rule option
  'icode: checks for specidifc icmp value( echo reply )
  itype: type of response '



```bash
alert icmp $EXTERNAL_NET any -> $HOME_NET any (
    msg:"PROTOCOL-ICMP Echo Reply"; 
    icode:0; itype:0; 
    metadata:ruleset community; 
    classtype:misc-activity; 
    sid:408; 
    rev:8;)
alert icmp $EXTERNAL_NET any -> $HOME_NET any (
    msg:"PROTOCOL-ICMP Echo Reply undefined code"; 
    icode:>0; 
    itype:0; 
    metadata:ruleset community; 
    classtype:misc-activity; 
    sid:409; 
    rev:10;)
```
---

#### 2. Explain the ICMP Unusual PING rule below. Be sure to identify the:
- Action
  'alert'
- Protocol
  'icmp'
- Source/destination addresses
  'source is $HOME_NET to and any $EXTERNAL_NET'
- Meaning of each new rule option
'content: looks for the following information in each packet sent over
fragbits: inspects the fragment and reserved bits in the IP header
  in this case looking for any non MF bit ( more fragment ) bit looking for fragmented packets.
itype: the type of rule( whiche code set ot look at for icode)
  in this case 8 means always run 
reference: allows rules to include references to external attack identification systems( supports systems and URLS )( first time seen, etc)
classtype: used to catagorize rules as detecting an attack that is part of a more general type of attack class( way of grouping the rule)'

```bash
alert icmp $HOME_NET any -> $EXTERNAL_NET any (
    msg:"PROTOCOL-ICMP Unusual PING detected"; 
    icode:0; 
    itype:8; 
    fragbits:!M; 
    content:!"ABCDEFGHIJKLMNOPQRSTUVWABCDEFGHI"; depth:32;
    content:!"0123456789abcdefghijklmnopqrstuv"; depth:32;
    content:!"EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"; depth:36;
    content:!"WANG2";
    content:!"cacti-monitoring-system"; depth:65;
    content:!"SolarWinds"; depth:72;
    metadata:ruleset community; 
    reference:url,krebsonsecurity.com/2014/01/a-closer-look-at-the-target-malware-part-ii/;
    reference:url,krebsonsecurity.com/2014/01/a-first-look-at-the-target-intrusion-malware/;
    classtype:successful-recon-limited;
    sid:29456;
    rev:2;)
```

**Follow-Up Questions** regarding the multiple `content` options in this rule:
  - There's an exclamation mark in front of each content string. Use the documentation to find out what this means.
  - Why do you suppose this rule includes so many?
    'list of safe strings'
---

#### 3. Explain the rule below. Be sure to identify:
   - **Action**: `alert`
   - **Protocol**: `tcp`
   - **Source/Destination Addresses**: `$EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS`. This watches traffic from the public Internet to local HTTP servers.
   - **Meaning of each new rule option**
     - `flow:to_server,established`: Watches traffic flowing from the public Internet _into_ the server on an _established_ connection. I.e., this packet is _not_ a request to initiate a connection—it's being transferred over an existing one.
     - `fast_pattern`: Enables fast pattern matching.
     - `nocase`: Make the search for the content string case-insensitive.
     - `distance:0`: Ignore `0` bytes before looking for the content string.
     - `http_uri`: Restricts the content search to the HTTP URI field, _not_ the rest of the packet.
     - pcre`: Allows the rule writer to specify a regular expression, so they can look for multiple patterns in a single rule.


  ```bash
  alert tcp $EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS (
      msg:"SQL PK-CMS SQL injection attempt"; 
      flow:to_server,established; 
      content:"/default.asp?"; fast_pattern; nocase; http_uri;
      content:"pagina="; distance:0; http_uri; pcre:"/pagina=[^&]*\x27/Ui";
      metadata:service http; 
      reference:url,github.com/BuddhaLabs/PacketStorm-Exploits/blob/master/1309-exploits/pkcms-sql.txt;
      classtype:web-application-attack;
      sid:32768;
      rev:1;)
  ```

**Follow Up Questions:** Based on the reference URL, which exploit does this rule monitor for?

**Follow Up Questions:** Based on your knowledge of SQL injection and the rule above, which of the following carries the SQLi payload? What is the name of the parameter or header that is being attacked?
  - POST data
  - Unsanitized HTTP header
  - GET query parameters)
