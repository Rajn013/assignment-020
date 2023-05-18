#!/usr/bin/env python
# coding: utf-8

# 1. Compare and contrast the float and Decimal classes' benefits and drawbacks.
# 

#  floats are faster and more memory-efficient, suitable for a wide range of values, but can have precision and rounding issues. Decimals provide precise decimal arithmetic, accurate representation of decimal numbers, but are slower and have a more limited value range. The choice between float and Decimal depends on the specific requirements of the application.

# 2. Decimal('1.200') and Decimal('1.2') are two objects to consider. In what sense are these the same object? Are these just two ways of representing the exact same value, or do they correspond to different internal states?
# 

# Decimal('1.200') and Decimal('1.2') represent the same value of 1.2 mathematically. However, internally they have different representations due to the presence or absence of trailing zeros, making them distinct Decimal objects.

# 3. What happens if the equality of Decimal('1.200') and Decimal('1.2') is checked?
# 

# In[6]:


from decimal import Decimal

decimal1 = Decimal('1.200')
decimal2 = Decimal('1.2')

print(decimal1 == decimal2)  


# 4. Why is it preferable to start a Decimal object with a string rather than a floating-point value?
# 

# In[10]:


#example
from decimal import Decimal

float_value = 0.1
decimal_float = Decimal(float_value)
decimal_string = Decimal('0.1')


# In[11]:


print(decimal_float)


# In[12]:


print(decimal_string)


# 5. In an arithmetic phrase, how simple is it to combine Decimal objects with integers?
# 

# Decimal objects with integers in arithmetic operations is simple and straightforward. The Decimal class seamlessly handles the interoperability between Decimal objects and integers, allowing you to use standard arithmetic operators without any additional complexity.

# 6. Can Decimal objects and floating-point values be combined easily?
# 

# Combining Decimal objects with floating-point values in arithmetic operations is easy and straightforward in Python. The Decimal class seamlessly supports interoperability between Decimal objects and floating-point values, allowing you to use standard arithmetic operators without any complications.

# 7. Using the Fraction class but not the Decimal class, give an example of a quantity that can be expressed with absolute precision.
# 

# In[13]:


#The Fraction class in Python allows precise representation of rational numbers without any loss of precision. Here's an example of a quantity that can be expressed with absolute precision using the Fraction class

from fractions import Fraction
fraction = Fraction(4,8)


# In[15]:


print(fraction)


# 8. Describe a quantity that can be accurately expressed by the Decimal or Fraction classes but not by a floating-point value.
# 

# In[16]:


#example

from decimal import Decimal
decimal = Decimal('2')/ Decimal('8')


# In[17]:


print(decimal)


# In[19]:


#example

from fractions import Fraction
fraction = Fraction(2,8)


# In[20]:


print(fraction)


# Q9.Consider the following two fraction objects: Fraction(1, 2) and Fraction(1, 2). (5, 10). Is the internal state of these two objects the same? Why do you think that is?
# 

# In[25]:


#yes the internal state of these two object are same:

from fractions import Fraction

fractions1 = Fraction(1,2)
fractions2 = Fraction(5,10)


# In[26]:


print(fractions1)


# In[27]:


print(fractions2)


# Q10. How do the Fraction class and the integer type (int) relate to each other? Containment or inheritance?
# 

# The Fraction class and the int type have a containment relationship. The Fraction class can work with and contain integer 

# In[ ]:




