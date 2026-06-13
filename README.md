# 🚆 Railway Ticket Reservation & Fare Management System

A beginner-friendly Python console application that simulates the railway ticket reservation process for a single passenger. The program validates user inputs, calculates ticket fare based on travel class and passenger age, assigns passenger category, coach, and seat type, and generates a formatted railway e-ticket.

> **Note:** This project was developed using only Python fundamentals (before learning loops and functions) as part of my Python learning journey.



## 📌 Features

- Accepts passenger details:
  - Name
  - Age
  - Gender
  - Source Station
  - Destination Station
  - Travel Class
- Validates user inputs
- Prevents booking when source and destination are the same
- Calculates fare based on travel class
- Applies age-based discounts
- Categorizes passengers (Infant, Child, Adult, Senior Citizen)
- Allocates coach based on travel class
- Assigns berth type based on age
- Generates a formatted railway e-ticket



## 🎫 Supported Travel Classes

| Travel Class | Base Fare |
|--------------|-----------|
| Sleeper | ₹450 |
| AC 2 Tier | ₹900 |
| AC 3 Tier | ₹1500 |



## 🎁 Discount Policy

| Passenger Age | Discount |
|---------------|----------|
| Below 5 years | 100% |
| 5 – 11 years | 50% |
| 60 years and above | 30% |
| Others | No Discount |



## 👤 Passenger Categories

| Age | Category |
|-----|----------|
| Below 5 | Infant |
| 5 – 17 | Child |
| 18 – 59 | Adult |
| 60+ | Senior Citizen |


## 🚉 Coach Allocation

| Travel Class | Coach |
|--------------|-------|
| Sleeper | C1 |
| AC 2 Tier | A1 |
| AC 3 Tier | B2 |



## 🛏️ Berth Allocation

- Lower Berth
  - Passenger age below 12
  - Passenger age 60 or above
- Upper Berth
  - All other passengers


## 🛠️ Python Concepts Used

- Variables
- Data Types
- User Input
- Strings
- Tuples
- Conditional Statements (`if`, `elif`, `else`)
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Membership Operators (`in`, `not in`)
- Formatted Strings (f-strings)


