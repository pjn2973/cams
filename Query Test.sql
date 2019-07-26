SELECT Regulation_Number, Regulation_Text 
FROM Regulation 
INNER JOIN Regulations_Types 
ON Regulation.Regulation_ID = Regulations_Types.Regulation_ID 
WHERE Regulations_Types.Type_ID == 1
ORDER BY Regulation_Number ASC;