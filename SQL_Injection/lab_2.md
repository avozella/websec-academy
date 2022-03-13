# Lab 2

## SQL injection vulnerability allowing login bypass
#
## Excercise:

This lab contains an SQL injection vulnerability in the login function.

To solve the lab, perform an SQL injection attack that logs in to the application as the administrator user.

#
Level: Apprendice

Reference: https://portswigger.net/web-security/sql-injection
#
## Solution

Go to **My Account** section.

Using BurpSuite or any tool to intercept, complete de form with **Username** as "administrator" and any password. Then, go to BurpSuite and add **'--** at the end of the username

![Alt text](images/lab_2/lab2_auth_attack.png?raw=true "Title")

Afterward, forward the request and in the site will redirect to a site to update the email. Put any email and send it.

![Alt text](images/lab_2/lab2_solution.png?raw=true "Title")