# Lab 1

## Lab: Basic SSRF against the local server

## Excercise: 
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

#

Level: Apprendice

Reference: https://portswigger.net/web-security/ssrf

## Context

Server-side request forgery (also known as SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make requests to an unintended location (ie: Redirect to another endpoint).

In this case, we need to delete an user from the admin panel over the vulnerable endpoint.

## Solution

Select any product to view details and then select "Check Stock". If we intercept the request with BurpSuite while we select the last option, we can see the body that 