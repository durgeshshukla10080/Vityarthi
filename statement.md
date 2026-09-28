# Project Statement: Car Parking Management System

## Problem Statement

Small parking lots are often managed on paper or from memory. Attendants must count occupied slots by hand, remember which car belongs to whom, avoid entering the same car twice, and calculate charges manually. This is slow and leads to mistakes such as overbooking, lost records and incorrect bills.

This project provides a simple program that keeps an accurate, up-to-date record of the parked cars and automates slot checking and billing.

## Scope of the Project

**Included**

- A console (text-based) application written in Python
- A single parking lot with a fixed capacity (10 slots)
- Registering a car with its number and owner name
- Rejecting new cars when the lot is full and rejecting duplicate car numbers
- Searching and listing parked cars
- Showing total, filled and empty slots
- Billing at a flat rate of Rs 20 per hour, calculated from the hours entered by the attendant

**Not included (out of scope for this version)**

- Permanent storage (records are kept in memory only and are lost on exit)
- Automatic entry/exit time tracking
- Multiple vehicle types, discounts or minimum charges
- Graphical interface, online access or multiple users
- Payment processing

## Target Users

- **Parking attendants** of small lots (colleges, shops, apartments, offices) who need a quick way to track cars and generate bills
- **Beginner Python learners** who want a small, readable example of functions, dictionaries and loops in a real-world setting

## High-Level Features

1. Park a car
2. Remove a car and generate the bill
3. Show all parked cars
4. Search a car by number
5. Check empty slots
6. Full-lot protection and duplicate-car detection
7. Menu-driven interface that runs until the user chooses to exit
