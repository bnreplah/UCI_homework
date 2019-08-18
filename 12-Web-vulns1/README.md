# OWASP Research
This week, you studied SQL, Burp Suite, and XSS vulnerabilities.

XSS is one of the most prevalent vulnerabilities affecting the web, and belongs to a class of attacks known as **injections**. Next week, you'll study two more important injection attacks:
- SQL Injection
- Command Injection

In this assignment, you will leverage what you know of XSS to study SQL and Command injections in advance of next week. In addition, you'll study **Broken Authentication** and **Security Misconfigurations**.

We have provided questions and links to readings in [Report.md](Report.md). Your task is to replace the `TODO` comments with your answers. At the end of it, you'll have a fully documented technical write-up about **Injection Vulnerabilities**.

Mastery of this material is compelling experience for those intending to apply for **Application Security** or **Penetration Testing**.

---

Launch DVWA by launching a Terminal and running `start_dvwa`.

Then, follow the instructions below.

## Instructions
## OWASP Research
Refer to the most recent [OWASP Top 10 document](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

In class, you studied **XSS (Cross-Site Scripting)**. Now, you'll expand on what you know of XSS, and research the following vulnerabilities:
- **Command Injection**
- **SQL Injection**
- **Broken Authentication**
- **Security Misconfiguration**

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

You'll fill out the above in the provided [ReportTemplate.md](ReportTemplate.md). That document contains sections for each of the 10 vulnerabilities in the OWASP Top 10, along with `TODO` comments with specific instructions as to how to complete each section. You'll be expected to replace the `TODO` instructions with your own solutions.

You should edit the document in [Stack Edit](https://stackedit.io), an in-browser markdown editor that integrates with Google Drive. 
- Use [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=EAIaIQobChMIrpmT0qfi3wIVq6GzCh1qwQQFEAAYASAAEgKX7_D_BwE&gclsrc=aw.ds) to download the [StackEdit Extension](https://chrome.google.com/webstore/detail/stackedit/iiooodelglhkcpgbajoejffhijaclcdg/related). 
- Click on the StackEdit icon, then on the **Menu** in the top right.
- Sign in with your Google account.
- Copy the contents of `Report.md` into a new Stack Edit document, and save it as `Report_LastName`.

You can then edit the report with the text editing tools in the top navigation bar. Pressing `Ctrl + S` will save your work, and other shortcuts will work just like in a normal text editor.

Finish the report by replacing the `TODO` instructions in the report with your solutions. 

When you finish:
- Click **Export to Disk** in the right sidebar
- Select **Export as Markdown**
- Submit the mardown file with the name `Report_LastName`

**Good luck!**
