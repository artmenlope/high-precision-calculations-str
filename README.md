# high-precision-calculations-str
A set of _Python 3_ defined functions. They can provide high decimal precision calculations using numbers in _str_ format. The algorithms used are the same as those used when performing the calculations by hand. All using _Python 3_ built-in functions.

## Usage

The functions can be imported, for example, by using 

```python
import sys
path = "<path to the folder where the script is stored>"
sys.path.insert(0, path)
import high_precision_calculations
```
  
As a practical example, for calculating the value of the golden ratio <a href="https://www.codecogs.com/eqnedit.php?latex=\varphi&space;=&space;(1&plus;\sqrt{5})&space;/&space;2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\varphi&space;=&space;(1&plus;\sqrt{5})&space;/&space;2" title="\varphi = (1+\sqrt{5}) / 2" /></a>  with an accuracy of up to 50 decimal places we would type

```python
divide_str(sum_str("1", sqrt_str("5", decimal_prec=50)), "2", decimal_prec=50)
```
or 
```python
divide_str(sum_str("1", sqrt_str("5", 50)), "2", 50)
```

which should return 

```python
'1.16803398874989484820458683436563811772030917980576'
```

List of auxiliar functions:
- num_decims(num)
- max_num_decims(num1, num2)
- num_zeros_init(num)
- num_zeros_end(num)
- del_decim_zeros(num)
- decim_modif_str(num1, num2)
- make_pairs(txt)

List of main functions:
- sum_str(num1, num2)
- subt_str(num1, num2)
- multiply_str(num1, num2)
- divide_str(dividend, divider, decimal_prec=16)
- sqrt_str(num, decimal_prec=16)
- power_str(num, powr)
