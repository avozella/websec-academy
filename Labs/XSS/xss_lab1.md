# Lab 1

## Lab: Reflected XSS into HTML context with nothing encoded

## Excercise: 
This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the alert function.
#
Level: Apprentice

Reference: https://portswigger.net/web-security/cross-site-scripting/reflected

## Solution

Inside the search box, we need to intert the next payload 

````bash
<script>alert('xss')</script>
````

If we intercept the request, we'll see the payload reflected within the response.

![Alt text](images/lab1_solution.png?raw=true "lab1_solution")

## Credits

+ [avozella](https://github.com/avozella)
+ [irootsec](https://github.com/irootsec)