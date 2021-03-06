/*
Problem 183 - Customers Who Never Order

Suppose that a website contains two tables, the Customers table and the 
Orders table. Write a SQL query to find all customers who never order 
anything.
*/

SELECT Name AS Customers FROM Customers
WHERE Id NOT IN (SELECT CustomerId FROM Orders)