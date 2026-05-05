# E-Commerce Data Analysis — Python (Pandas)

This is a small data analysis project I built using Python and pandas.
The goal was to practice working with real data and understand how to extract useful information from it.

---

## Description

The script reads an e-commerce dataset from a CSV file and prints a simple report in the console.

It focuses on:

* calculating revenue and profit
* analyzing customer behavior
* understanding returns
* grouping data to find patterns

I tried to write clean and organized code by separating each task into its own function.

---

## What the program does

### Revenue analysis

* Calculates total revenue for each product category
* Shows which categories generate the most money
* Calculates revenue by country (only for completed orders)

---

### Customer behavior

* Counts how many orders are:

  * completed
  * abandoned
  * cancelled
* Shows the percentage of each
* Calculates abandonment rate by country

---

### Returns analysis

* Calculates how many orders were returned
* Shows the most common return reasons
* Finds which categories are returned the most

---

### Data preparation

Before analysis, the script:

* creates new columns:

  * revenue = price × quantity
  * profit = revenue − cost
* handles missing values (for returns)

---

## Concepts I used

* pandas DataFrame
* groupby and aggregation
* filtering data
* value_counts
* lambda functions
* handling missing data
* writing modular code (functions)

---

## How to run

Install the libraries:

```bash
pip install pandas matplotlib
```

Run the script:

```bash
python script.py
```

---

## What I learned

This project helped me understand how to:

* work with real datasets
* clean and prepare data
* calculate useful metrics
* think more like a data analyst

---

## Possible improvements

* add charts to visualize the results
* export the report to a file
* build a small dashboard

---

## Author

Iyed Ferjeoui
Computer Science student — ISSAT Sousse

---
