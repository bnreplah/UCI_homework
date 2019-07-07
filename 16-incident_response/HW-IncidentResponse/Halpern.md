#### !Alert 4! 
    
    - What activity is Snort reporting on? (Provide a few alert headlines.)
    
```
An attempted administrator privilidge gain. The Vulnerability is ranked as a Priority 1.
```

    - Is there a CVE associated with this alert?
    
```
Yes,
    CVE-2014-7169, CVE-2014-6277, CVE-2014-6274, CVE-2014-6271

```

    - What are the IP Addresses flagged in this alert?

```
172.18.0.3 --> 172.18.0.2
```    

    - Is this attack coming from outside the network?
    
```
The attack seems to be coming from within the network due to the nature of the Ip address. The Ip address shows to be in the same subnet as the other Ip address.
```

    - What is the source port of the activity?
    
```
47232
47238
47244
47250
47256
47292
47298
47304
47310
47316
```

    - What is the destination port of the activity?
    
```
80
```

    - What are the MAC Addresses of the computers involved?

```
02:42:ac:12:00:03
-->
02:42:ac:12:00:02

```    
    
    - Can you confirm the date and time this issue occurred?

```
2018-12-05 00:05:59 
The time matches in the alert log matches up with the time in the pcap 

```
    
    - What was the target of this attack?

```
The target of this attack was a privildge escalation. In the error.log and the acess.log you are able to track the attempts at fuzzing for credentials, as well as the attackers failed attempts at logging in. 
```

    - How can you confirm if the Snort alert is accurate?

```
The logs collaboarte the snort alert as well as the reports coinciding with visible events in the wireshark pcap.

```
    
    - Can you verify whether or not sensitive data has been obtained by the attacker?

```
It doesn't seem that any sensitive data was obtained by the attacker. From the looks of the pcap it seems like a simple dmvwa excercise. THe dmvwa link popped up mulitple times in the pcap, leading to the assumption that the alerts were triggered by the by the the Dvwa excercise, along with there not being anymore suspicious behavior.
```

    - Would you categorize this alert as a `False Positive` or a `True Positive`?

```
False Positive
```

    - If this issue needs to be mitigated, what steps should be taken with the infected machine?

```
False positive, to mitigate the rule, possibly tighten the specifictions around the alert
```

    - Would you categorize this issue as a Web, Email, Network or Application attack?

```
Web attack ( if it were one )

```
