# high-precision-calculations-str

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/artmenlope/high-precision-calculations-str/blob/master/LICENSE.md)
![Last Commit](https://img.shields.io/github/last-commit/artmenlope/high-precision-calculations-str)

A set of Python 3 defined functions. They can provide high decimal precision calculations using numbers in `str` format. The algorithms used are the same as those used when performing the calculations by hand. All using Python 3 built-in functions.

## Usage

If you don't have the [`high_precision_calculations.py`](https://github.com/artmenlope/high-precision-calculations-str/blob/master/high_precision_calculations.py) script placed in your working directory, the functions can be imported, for example, by using 

```python
import sys
path = "<path to the folder where the script is stored>"
sys.path.insert(0, path)
import high_precision_calculations
```

<!--
<a href="https://www.codecogs.com/eqnedit.php?latex=\varphi&space;=&space;(1&plus;\sqrt{5})&space;/&space;2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\varphi&space;=&space;(1&plus;\sqrt{5})&space;/&space;2" title="\varphi = (1+\sqrt{5}) / 2" /></a> 
-->

<!-- (old) Note: For Latex formulas in Github's Markdown see https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b -->

As a practical example, for calculating the value of the golden ratio $\varphi = (1+\sqrt{5})/2$ with an accuracy of up to 50 decimal places we would type

```python
divide_str(sum_str("1", sqrt_str("5", decimal_prec=50)), "2", decimal_prec=50)
```
or 
```python
divide_str(sum_str("1", sqrt_str("5", 50)), "2", 50)
```

which should return 

```python
'1.61803398874989484820458683436563811772030917980576'
```

To see the output of the functions in this example using 15000 decimals see the file [`phi_15000_decimals.txt`](https://github.com/artmenlope/high-precision-calculations-str/blob/master/phi_15000_decimals.txt)

---

### List of auxiliar functions:
- `num_decims(num)`
- `max_num_decims(num1, num2)`
- `num_zeros_init(num)`
- `num_zeros_end(num)`
- `del_decim_zeros(num)`
- `decim_modif_str(num1, num2)`
- `make_pairs(txt)`

<!--&nbsp;-->

### List of main functions:

| **Function name**                                | **Use**                                                   |
|--------------------------------------------------|-----------------------------------------------------------|
| `sum_str(num1, num2)`                            | Addition.                                                 |
| `subt_str(num1, num2)`                           | Subtraction.                                              |
| `multiply_str(num1, num2)`                       | Multiplication.                                           |
| `divide_str(dividend, divider, decimal_prec=16)` | Division.                                                 |
| `sqrt_str(num, decimal_prec=16)`                 | Square root.                                              |
| `power_str(num, powr)`                           | Power _(the argument "powr" must be a positive integer)_. |
