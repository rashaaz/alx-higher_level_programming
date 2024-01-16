# Project 0x0D. SQL - Introduction

## Overview
This project provides an introduction to SQL and MySQL, covering various tasks related to creating, modifying, and querying databases using MySQL. The tasks are designed to reinforce understanding of fundamental concepts such as databases, SQL syntax, and basic MySQL operations.

## Concepts
In this project, focus on the following concepts:
- Databases
- What's a database and a relational database
- SQL and MySQL basics
- DDL and DML
- Creating and altering tables
- Selecting, inserting, updating, and deleting data
- Subqueries
- Using MySQL functions

## Learning Objectives
By the end of this project, you should be able to explain the following without the help of external resources:

**General**
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for

## Copyright - Plagiarism
Remember, you must come up with solutions for the tasks on your own. Do not copy and paste someone else’s work. Publishing any content related to this project is strictly forbidden and will result in removal from the program.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All SQL queries should have a comment just before (i.e., syntax above)
- All files should end with a new line
- All your files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder, is mandatory
- The length of your files will be tested using wc

## More Info
Comments for your SQL file:
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
## taske
16 mandatory anda 4 advanced
