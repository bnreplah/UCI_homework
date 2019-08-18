# OWASP Research
Over the past two weeks, you've studied the most important vulnerabilities in OWASP:
- Cross-Site Scripting (XSS)
- SQL Injection
- Command Injection
- Local and Remote File Inclusion
- File Upload Vulnerabilities

As you recall, the list is called the OWASP **Top 10**—there are still vulnerabilities discover! 

In this assignment, you will research the ones we didn't have time to discuss in class.

At the end of it, you'll have a fully documented technical write-up explaining how to fix them. 

Mastery of this material is compelling experience for those intending to apply for **Application Security** or **Penetration Testing**.

---

Launch DVWA by launching a Terminal and running `start_dvwa`.

Then, follow the instructions below.

## Instructions
### OWASP Research
Refer to the most recent [OWASP Top 10 document](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

In class, you studied the following vulnerabilities:
- **Injections**
- **XSS (Cross-Site Scripting)**
- **Sensitive Data Exposure**
- **Security Misconfiguration**
In this exercise, you'll summarize your knowledge of the above, and research the remaining six OWASP vulnerabilities:
- **XML External Entities (XXE)**
- **Insecure Deserialization**
- **Using Components with Known Vulnerabilities**
- **Insufficient Logging & Monitoring**
---
Your assignment is to use the [Official OWASP Top 10 reference document](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf) to provide the following for each of the 10 vulnerabilities:
- **Definition / Description**: A definition/brief overview of the vulnerability. Refer to the OWASP Document's summaries for this. Your description should include the following information:
  - **Source**: Describes what causes the vulnerability—i.e., developer oversight; use of insecure software/bad dependency management; etc.;
  - **Scope**: Describes who the attack affects (end-users? business executives? security personnel?).
  - **Severity**: Describes how much damage the vulnerability can cause.
- **How it Works**: Provide a technical description of what causes each vulnerability. You'll be expected to explain:
  - Which part of the web application is being exploited
  - What a typical payload looks like, with an explanation of what it does
- **Scenario**: Discuss an example payload and/or explain how an attacker would exploit this vulnerability in a real scenario.

You'll fill out the above in the provided [ReportTemplate.md](ReportTemplate.md). That document contains sections for each of the 10 vulnerabilities in the OWASP Top 10. In each section there are `TODO` comments with specific instructions as to how to complete the section. Replace the `TODO` instructions with your own solutions to finish the report.

You should edit the document in VS Code.
- Copy the contents of `ReportTemplate.md` into a new VS Code file, and save it as `Report_<YourLastName>.md`.
- Finish the report by replacing the `TODO` instructions in the report with your solutions.
- Save and submit the markdown file with the name `Report_<YourLastName>.md` in BCS.

**Good luck!**
