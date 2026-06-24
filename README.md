# E-Commerce Data Analysis — Python (Pandas)

This is a small project I built using Python and pandas to practice working with data.

---

## Google Colab Version

I also made a Google Colab version of this project.

You can run the code in your browser without installing anything.

### How to use

1. Open the notebook in Google Colab
2. Upload your CSV file or use a GitHub link
3. Run the cells

---

## Description

The script reads an e-commerce dataset from a CSV file and prints a simple report.

It focuses on:

* revenue and profit
* customer behavior
* returns
* grouping data

The code is organized into functions.

---

## What the program does

### Revenue

* Revenue by category
* Revenue by country (completed orders only)

### Customer behavior

* Number of completed, abandoned, and cancelled orders
* Percentage of each
* Abandonment rate by country

### Returns

* Number of returned orders
* Return reasons
* Most returned categories

### Data preparation

* Creates:

  * revenue = price × quantity
  * profit = revenue − cost
* Handles missing values

---

## Concepts used

* pandas DataFrame
* groupby
* filtering
* value_counts
* lambda functions
* functions (modular code)

---

## How to run

Install:

```bash id="u7a1m2"
pip install pandas matplotlib
```

Run:

```bash id="g8p2x9"
python script.py
```

---

## What I learned

* working with datasets
* cleaning data
* basic analysis
* organizing code

---

## Possible improvements

* add charts
* export results
* build a dashboard

---

## Author

Iyed Ferjeoui
Computer Science student — ISSAT Sousse
