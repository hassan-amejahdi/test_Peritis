 1)Indiquer par pays, le nombre de clients qui nont pas effectué de commandes :

sql

SELECT c.Country, COUNT(*) AS NumberOfCustomersWithoutOrders
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.CustomerID IS NULL
GROUP BY c.Country;

 2) Indiquer l ID du produit ainsi que la somme des quantités achetées pour ce produit :

sql

SELECT OrderDetails.ProductID, SUM(OrderDetails.Quantity) AS TotalQuantityPurchased
FROM OrderDetails
GROUP BY OrderDetails.ProductID;

 3) Indiquer la moyenne des années de naissance des employés arrondie à l entier le plus proche :

sql

SELECT ROUND(AVG(YEAR(HireDate)), 0) AS AverageBirthYear
FROM Employees;

4)  Indiquer les villes et leur pays respectif ainsi que leur nombre de clients dont le nombre de clients est strictement supérieur à 3 :

sql

SELECT c.City,c.Country,count(*) as nombre 
FROM Customers c
group by c.City,c.Country
having nombre > 3;



