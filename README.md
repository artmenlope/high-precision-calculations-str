# high-precision-calculations-str
A set of _Python 3_ defined functions. They can provide high decimal precision calculations using numbers in _str_ format. The algorithms used are the same as those used when performing the calculations by hand. All using _Python 3_ built-in functions.

## Usage examples

The functions can be imported, for example, by using 

```python
import sys
path = "<path to the folder where the script is stored>"
sys.path.insert(0, path)
import high_precision_calculations
```
  
As a practical example, to calculate the value of the golden ratio <a href="https://www.codecogs.com/eqnedit.php?latex=\varphi&space;=&space;(1&plus;\sqrt{5})&space;/&space;2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\varphi&space;=&space;(1&plus;\sqrt{5})&space;/&space;2" title="\varphi = (1+\sqrt{5}) / 2" /></a> with an accuracy of up to 50 decimal places we would type

```python
multiply_str("0.5", sum_str("1", sqrt_str("5", decimal_prec=50)))
```
which should return 

```python
'1.6180339887498948482045868343656381177203091798057625'
```
