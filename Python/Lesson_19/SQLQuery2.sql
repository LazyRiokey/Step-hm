/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [id]
      ,[first_name] as 'Имя'
      ,[last_name]
      ,[birthday]
      ,[phone_number]
  FROM [University].[dbo].[Students]