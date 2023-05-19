# Automate the Boring Stuff
Using the book as a proxy for a beginner's course. The learnings here will be based on the 2nd edition of the book.

### 0. What is programming?
Programming is simply the act of entering instructions for the computer to perform. All programs use basic instructions 
as building blocks. You can combine these building blocks to implement more intricate decisions

### 1. Python Basics

#### 1.1 Expressions
In Python, the most basic kind of programming instruction is called an expression (e.g 2+2). Expressions consist of 
values (2) and operators (+), and they can always evaluate (that is, reduce) down to a single value. That means you can 
use expressions anywhere in Python code that you could also use a value. A single value with no operators is also 
considered an expression, though it evaluates only to itself. There are many other math operators in python, such as:

| Operator | Operation         | Example | Evaluation |
|----------|-------------------|---------|------------|
| **       | Exponent          | 2 ** 3  | 8          |
| %        | Modulus/remainder | 22 % 8  | 6          |
| //       | Integer division  | 22 // 8 | 2          |
| /        | Division          | 22 / 8  | 2.75       |
| *        | Multiplication    | 3 * 5   | 15         |
| -        | Subtraction       | 5 - 2   | 3          |
| +        | Addition          | 2 + 2   | 4          |

The order of operations (precedence) follows mathematics. You can use parentheses to override the usual precedence if 
you need to. Whitespace in between the operators and values doesn’t matter for Python (except for the indentation at the
beginning of the line), but a single space is convention. These rules for putting operators and values together to form 
expressions are a fundamental part of Python as a programming language, just like the grammar rules that help us 
communicate.

#### 1.2 Data Types
A data type is a category for values, and every value belongs to exactly one data type. The most common data types in 
Python are:
- Integer (or int) data type indicates values that are whole numbers
- Floating-point numbers (or floats) are numbers with a decimal point
- Strings (or strs) are text values. Surround your string in single quote (') characters so Python knows where the 
string begins and ends

NB: The meaning of an operator may change based on the data types of the values next to it, e.g. a "+" operator will add
int values together but concatenate strings

