![png](images/gif.gif)

<p align="center">
  <b>
		<a href="#-overview">Overview</a> | 
		<a href="#%EF%B8%8F-usage">Usage</a> | 
		<a href="#-more-on-the-topic">More on the topic</a>
	</b>
</p><br>


# 📦 Overview

`[⚠️]  This repository contains samples of purposefully-vulnerable applications!`<br><br>

These applications were developed for **demonstration purposes only**.<br>

&emsp;–&emsp;**CRLF Injection** (SMTP / IMAP Injection)<br>
&emsp;–&emsp;**Arbitrary Command Flag Injection**<br>
&emsp;–&emsp;**Improper Input Validation**<br><br>

<ins>Brief overview of applications</ins>:
| Environment | Extras | Exploited vulnerabilities |
| :-- | :-- | :-- |
| **NodeJs** | Express + `smtp-client` | CRLF Injection (SMTP) |
| **PHP** | `mail()` | CRLF Injection (SMTP) + Arbitrary Command Flag Injection |
| **Python** | Flask + `email` | Improper Input Validation |

# ⚙️ Usage

1\)&ensp;Download this repository:
```bash
git clone https://github.com/qwqoro/Mail-Injection
```
2\)&ensp;Install & Configure some MTA (_e.g: Postfix_):
```bash
apt install postfix
nano /etc/postfix/main.cf
```
3\)&ensp;*Set the `hahacking.local` domain name in `/etc/hosts` & Add users || Make changes to the application to use your own
```bash
nano /etc/hosts
adduser contact
```
4\)&ensp;Start the application by launching any of the proposed backend implementations:
```bash
cd nodejs; npm install express smtp-client; node app.js     # NodeJS
cd php; php -S 127.0.0.1:80                                 # PHP
cd python; python app.py                                    # Python
```
5\)&ensp;Go to `http://hahacking.local/`<br>
6\)&ensp;Enjoy!

# 📑 More on the topic

- `[CRLF Injection]` `[SMTP]` `[IMAP]`<br>
**OWASP** ‟Testing for IMAP SMTP Injection”:&emsp;[owasp.org/...Testing_for_IMAP_SMTP_Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/10-Testing_for_IMAP_SMTP_Injection)

- `[CRLF Injection]` `[SMTP]`<br>
**Invicti** ‟E-Mail Injection”:&emsp;[invicti.com/.../email-injection](https://www.invicti.com/learn/email-injection/)

- `[CRLF Injection]` `[SMTP]`<br>
**VK9 Security** ‟SMTP Injection”:&emsp;[vk9-sec.com/smtp-injection-attack](https://vk9-sec.com/smtp-injection-attack/)

- `[CRLF Injection]` `[SMTP]`<br>
MBSD **Takeshi Terada** ‟SMTP Injection via recipient email addresses”:&emsp;[mbsd.jp/.../smtpi.pdf](https://www.mbsd.jp/Whitepaper/smtpi.pdf)

- `[CRLF Injection]` `[SMTP]` `[IMAP]`<br>
**Vicente Aguilera Díaz** “MX Injection: Capturing and Exploiting Hidden Mail Servers”:&emsp;[webappsec.org/.../121106.pdf](http://www.webappsec.org/projects/articles/121106.pdf)

- `[Arbitrary Command Flag Injection]`<br>
**][akep** (aLLy) ‟Эксплуатируем критическую уязвимость в PHPMailer и фреймворках, которые его используют”:&emsp;[xakep.ru/.../phpmailer-exploit](https://xakep.ru/2017/01/12/phpmailer-exploit/)
