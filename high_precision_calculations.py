# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:46:12 2019

@author: armelope
"""


def num_decims(num):
    
    """
    Calculates the number of decimals.
    """

    if ("." in num):
        
        numA, numB = num.split(".")   
        num_decms = len(numB)
    
    elif ("." not in num):
        
        num_decms = 0
    
    return num_decms



def max_num_decims(num1, num2):
    
    """
    Given two numbers 'num1' and 'num2', returns 
    the maximum number of decimals found in them.
    """
    
    num_max_decs = 0
    
    if ("." in num1) or ("." in num2):
                
        if ("." in num1) and ("." not in num2):
            
            num1A, num1B = num1.split(".")
            num_max_decs = len(num1B)
                      
        elif ("." in num2) and ("." not in num1):
            
            num2A, num2B = num2.split(".")
            num_max_decs = len(num2B)
        
        elif ("." in num1) and ("." in num2):
            
            num1A, num1B = num1.split(".")
            num2A, num2B = num2.split(".")
            
            num_max_decs = max(len(num1B), len(num2B))
    
    return num_max_decs



def num_zeros_init(num):

    """
    Counts the number of zeros at the beginning
    of the number 'num'.
    """
    
    iszero = True
    num_zeros = 0
    i = 0
     
    while iszero == True and (i != len(num)-1):
         
        if num[i] == "0":
            num_zeros += 1
             
        elif num[i] != "0":
            iszero = False
          
        i += 1    
                
    return num_zeros



def num_zeros_end(num):

    """
    Counts the number of zeros at the end
    of the number 'num'.
    """
    
    iszero = True
    num_zeros = 0
    i = len(num)-1
    
    while (iszero == True) and (i != 0):
         
        if num[i] == "0":
            num_zeros += 1
             
        elif num[i] != "0":
            iszero = False
          
        i -= 1    
                
    return num_zeros



def del_decim_zeros(num):

    """
    If the number 'num' has decimals, deletes 
    the excess of zeros at the end of it. 
    """
    
    if "." in num:  
        
        num_zeros = num_zeros_end(num) 

        if num_zeros != 0:          
            num = num[:-num_zeros] 
        
        if num[-1] == ".":          
            num = num[:-1]
                
        return num

    else:
        return num
    


def decim_modif_str(num1, num2):
    
    """
    Explanations:
        
        Makes the step of multiplying by 10 to
        eliminate decimals but with 'strings'.
    
        Makes the length of both numbers 'num1' and 'num2' equal 
        while eliminating their decimal point.
    
        Removes the decimal points and fills in with zeroes.
    """

    if ("." in num1) or ("." in num2):
        
        if ("." in num1) and ("." not in num2):
                    
            num1A, num1B = num1.split(".")
            
            num1 = num1.replace(".","")
            num2 += "0"*len(num1B)
            
            
        elif ("." in num2) and ("." not in num1):
            
            num2A, num2B = num2.split(".")
            
            num2 = num2.replace(".","")
            num1 += "0"*len(num2B)
            
        
        elif ("." in num1) and ("." in num2): # error here?
    
            num1A, num1B = num1.split(".")
            num2A, num2B = num2.split(".")      
            
            num1 = num1.replace(".","")
            num2 = num2.replace(".","")
            
            num_zeros = abs(len(num1B)-len(num2B))
    
            if len(num1B) < len(num2B):
                
                num1 += "0" * num_zeros
    
            elif len(num1B) > len(num2B):
                
                num2 += "0" * num_zeros
     
    return num1, num2



def make_pairs(txt):
    
    """
    Takes a string ('txt') and separates it into 
    pairs of characters returning a list with those pairs.
    """
    
    lista = []
    string = ""  
    count = 0
    
    if len(txt)%2 != 0 :
        count = 1
    
    for i in range(len(txt)):
        
        string += txt[i]
        count += 1
        
        if count == 2:
            lista.append(string)
            string = ""
            count = 0
        
    return lista      
    


def sum_str(num1, num2):
    
    """
    Adds two numbers in 'string' format. (Accepts negative numbers)
    """
    
    # Check the maximum number of decimals.
    
    max_num_decs = max_num_decims(num1, num2)
            
    # We remove the decimal point and fill in with zeros.   
            
    num1, num2 = decim_modif_str(num1, num2)
    
    # Do the summation.
    
    summ = str(int(num1) + int(num2))
    
    # Put the decimal point.
    
    if max_num_decs != 0:
        result = summ[:-max_num_decs] + "." + summ[-max_num_decs:]
    
    elif max_num_decs == 0:
        result = summ
    
    return result
    
    

def subt_str(num1, num2):
    
    """Subtracts two numbers in 'string' format. (Accepts negative numbers)"""
    
    # Check the maximum number of decimals.
    
    max_num_decs = max_num_decims(num1, num2)
    
    # We remove the decimal point and fill in with zeros.      
            
    num1, num2 = decim_modif_str(num1, num2)
    
    # Do the subtraction.
    
    subt = str(int(num1) - int(num2))
    
    # Put the decimal point.
    
    if max_num_decs != 0:
        result = subt[:-max_num_decs] + "." + subt[-max_num_decs:]
    
    elif max_num_decs == 0:
        result = subt
    
    return result    



def multiply_str(num1,num2): 
    
    """
    Multiply two numbers 'num1' and 'num2' in string 
    format using the long multiplication algorithm.
    """
    
    max_num_decs = max_num_decims(num1, num2)
    
    #total_num_decs = num_decims(num1) + num_decims(num2)
    
    num1, num2 = decim_modif_str(num1, num2)
    
    # Calculate the steps.
    
    steps = []
    for i in range(0,len(num2)): 
        
        if (int(num1) * int(num2[::-1][i]) != 0):
            steps.append( str(int(num1)*int(num2[::-1][i])) + "0"*i )
            
        else:
            steps.append( "0"*len(num1) + "0"*i )
        
    # Add the steps.
    
    sum_steps = "0"
    for i in range(0,len(num2)):
        sum_steps = sum_str(sum_steps,steps[i])
     
    if len(sum_steps) != len(steps[-1]):
        
        n_zeros = abs(len(sum_steps)-len(steps[-1]))
        sum_steps = "0"*n_zeros + sum_steps
        
    # Put the decimal point.
    
    if max_num_decs != 0:
        
        result = sum_steps[:-2*max_num_decs] + "." + sum_steps[-2*max_num_decs:]
    
    elif max_num_decs == 0:
        
        result = sum_steps    
      
    result = del_decim_zeros(result)
    
    return result
    
    

def divide_str(dividend, divider, decimal_prec=16):
    
    """
    This function uses the long division algorithm to divide two numbers.
    
    max_iter = maximum number of iterations; equivalent to the maximum number of
    decimals plus one (dec# = max_iter-1).
    
    The result is in the format "string".
    """    
    
    max_iter = decimal_prec + 1
    remainder = 1 # != 0
    i = 0
    
    # Check for decimals.
    dividend, divider = decim_modif_str(dividend, divider)
        
    dividend, divider = int(dividend), int(divider)
       
    while (remainder != 0) and (i < max_iter):
                       
        if dividend >= divider: # Dividend greater than the divider.
            
            result = dividend//divider
            
            if dividend%divider == 0: # Exact division.
                
                if i == 0:                    
                    quotient = str(result)
                    remainder = 0
                
                else:                    
                    quotient = quotient + str(result)
                    remainder = 0
            
            else: # Not exact division.
                
                remainder = dividend%divider
                
                if i == 0:                   
                    quotient = str(result) + "."
                    
                else:          
                    quotient = quotient + str(result)
                
                dividend = remainder
                
                
        elif dividend < divider: # Dividend less than the divider.
                 
            if i == 0:                
                quotient = "0."
                
            dividend = int(str(dividend)+"0")          
            result = dividend//divider
            
            if dividend%divider == 0: # Exact division.
                
                quotient = quotient + str(result)
                remainder = 0
            
            else: # Not exact division.
                
                remainder = dividend%divider
                
                quotient = quotient + str(result)               
                dividend = int(remainder)
         
        i += 1
                       
    return quotient   
    
    

def sqrt_str(num, decimal_prec = 16):
    
    """
    Calculation of the square root of a number 'num' 
    in string format. The decimal precision is set 
    by "decimal_prec". The result is given in string 
    format. The result is obtained using a digit-by-digit 
    calculation algorithm.
    """
      
    #initialization
    
    if "." in num:
        
        numA, numB = num.split(".")
        
        num_bef_rad = len(numA) # Number of digits before the decimal point in the radicand.
        
        if len(numB)%2 != 0: # If there's not an even number of decimals.
            numB = numB + "0"
            
        pairsList = make_pairs(numA + numB)

        
    elif "." not in num:
        
        num_bef_rad = len(num) # Number of digits before the decimal point in the radicand.
        
        pairsList = make_pairs(num)
    
    num_bef_res = int((num_bef_rad+1)/2) # Number of digits before the decimal point in the result.
    max_iter = num_bef_res + decimal_prec + 1  # Maximum number of iterations.
    
    root = ""
    remainder = 1 # != 0
     
    # Calculations.
    
    i = 0 # Iteration number.
    
    while (remainder != 0) and (i < max_iter):
        
        if i == 0:   
            
            # Step 1
            radicand = int(pairsList[i])
            
            # Step 2 not necessary at first.
            # Step 3
            root_term = int(radicand**0.5)
            
            # Step 4
            root += str(root_term)
            remainder = radicand - root_term**2
            
        else:
            
            # Step 1
            if i < len(pairsList):
                radicand = int(str(remainder) + pairsList[i])      
            else:
                radicand = int(str(remainder) + "00")
            
            # Step 2
            stair_aux = multiply_str(root,"2")
            
            # Step 3
            root_term = 1
            while radicand - int(stair_aux + str(root_term))*root_term >= 0 :
                root_term += 1
            root_term -= 1  
            
            # Step 4
            root += str(root_term)
            remainder =  radicand - int(stair_aux + str(root_term))*root_term  
            
        i += 1
     
    # Results and retouching.
    
    root = root[:num_bef_res] + "." + root[num_bef_res:]
    
    if root[-1] == ".":
        root = root[:-1]
        
    return root
        


def power_str(num, powr):
    
    """
    Calculate the power of a number in string format.
    Returns num**powr.
    'powr' must be a positive integer.
    """
    
    orig_num = num
    
    for i in range(powr-1):
        
        num = multiply_str(num, orig_num)

    return num

