![gif](images/gif.gif)

<p align="center">
        <code> [ Have a look at the article: <a href="HaHacking_Mail-Injection.pdf"><code>HaHacking_Mail-Injection.pdf</code></a> / <a href="https://habr.com/ru/articles/774258/">Habr</a> / <a href="https://blog.deteact.com/ru/e-mail-injection/">DeteAct Blog</a> ] </code><br><br>
  	<b>
		<a href="#-overview">Overview</a> | 
		<a href="#%EF%B8%8F-usage">Usage</a> | 
		<a href="#-more-on-the-topic">More on the topic</a>
	</b>
</p><br>

> My research on E-Mail Injection vulnerabilities & samples of vulnerable applications.

<p align="center"><img alt="preview" src="images/preview.jpg"/></p><br>

# 📦 Overview

`[⚠️]  This repository contains samples of purposefully-vulnerable applications!`<br><br>

These applications were developed for **demonstration purposes only**. Read the text of the research to better understand the underlying causes + ways to exploit this kind of vulnerabilities.<br>

&emsp;–&emsp;**CRLF Injection** (SMTP / IMAP Injection)<br>
&emsp;–&emsp;**Arbitrary Command Flag Injection**<br>
&emsp;–&emsp;**Improper Input Validation**<br><br>

<ins>Brief overview of applications</ins>:
| Environment | Technologies | Exploited vulnerabilities |
| :-- | :-- | :-- |
| <img width=16 height=16 alt="NodeJS" src="https://cdn.jsdelivr.net/npm/simple-icons@9.19.0/icons/nodedotjs.svg"/>  [**NodeJS**](nodejs) | Express + `smtp-client` | CRLF Injection (SMTP) |
| <img width=16 height=16 alt="NodeJS" src="https://cdn.jsdelivr.net/npm/simple-icons@9.19.0/icons/php.svg"/>  [**PHP**](php) | `mail()` | CRLF Injection (SMTP) + Arbitrary Command Flag Injection |
| <img width=16 height=16 alt="NodeJS" src="https://cdn.jsdelivr.net/npm/simple-icons@9.19.0/icons/python.svg"/>  [**Python**](python-imap) | Flask + `imaplib` | CRLF Injection (IMAP) |
| <img width=16 height=16 alt="NodeJS" src="https://cdn.jsdelivr.net/npm/simple-icons@9.19.0/icons/python.svg"/>  [**Python**](python-smtp) | Flask + `email` + `smtplib` | Improper Input Validation |

<br>

# ⚙️ Usage

1\)&ensp;Install & Configure an SMTP server (_e.g: Postfix_):
```bash
apt install postfix
nano /etc/postfix/main.cf
postfix start
```
2\)&ensp;Install & Configure an IMAP server (_e.g: Dovecot_):
```bash
apt install dovecot-imapd
nano /etc/dovecot/dovecot.conf
/etc/init.d/dovecot start
```
3\)&ensp;Set the `hahacking.local` domain name in `/etc/hosts` & Add users;<br>// \*Make sure to make changes to the application in case you want to use **your own** domain name
```bash
nano /etc/hosts
adduser contact
...
```
4\)&ensp;Download this repository:
```bash
git clone https://github.com/qwqoro/Mail-Injection
```
5\)&ensp;Start the application by launching any of the proposed backend implementations:
```bash
cd nodejs; npm install express smtp-client; node app.js        # NodeJS
cd php; php -S 127.0.0.1:80                                    # PHP
cd python-imap; python app.py                                  # Python IMAP
cd python-smtp; python app.py                                  # Python Input Validation
```
6\)&ensp;Go to `http://hahacking.local/` OR `http://whateveryourdomainnameis/`<br>
7\)&ensp;Enjoy!

<br>

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
