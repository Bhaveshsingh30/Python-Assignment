#!/usr/bin/env python
# coding: utf-8

# ## 1. In the below elements which of them are values or an expression? 
# eg:- values can be
# integer or string and expressions will be mathematical operators.
# *
# &#39;hello&#39;
# -87.8
# -
# /
# +
# 6
Answer 
*                                      -> mathematical operator
&#39;hello&#39;                        -> integer or string
-87.8                                  -> value(float)
-                                      -> mathematical operator
/                                      -> mathematical operator
+                                      -> mathematical operator
6                                      -> integer
# ## 2. What is the difference between string and variable?
A string is a data type that represents a sequence of characters, such as "hello world". A variable is a named reference to a value, which can be of any data type, including a string. So, you can assign a string value to a variable. 
For example:
string = "hello world"
# ## 3. Describe three different data types.
1.Integer: represents a whole number, such as 1, 2, or -10.
2.Float: represents a real number with decimal points, such as 1.0, -0.5, or 3.14.
String: represents a sequence of characters, such as "Hello" or "Goodbye".
# ## 4. What is an expression made up of? What do all expressions do?
An expression in Python is made up of values, operators, and/or variables that are combined to produce a result.

All expressions evaluate to a single value, which can be of any data type (e.g. integer, float, string, etc.). The value can be assigned to a variable or used directly in a statement or function.

For example, the expression 2 + 3 is an arithmetic expression that evaluates to 5. 
The expression "Hello" + " " + "World" is a string expression that evaluates to "Hello World".
# ## 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
An expression is a combination of values, operators, and/or variables that can be evaluated to a single value.

A statement, on the other hand, is a complete instruction in a program that performs some action, such as assignment, control flow, or function calls. An assignment statement like spam = 10 is an example of a statement. The expression 10 is being evaluated and its value is being assigned to the variable spam.

In general, all statements are executed one by one in a sequential order, whereas expressions are evaluated to produce a value that can be used in various parts of a program.
# ## 6. After running the following code, what does the variable bacon contain?                   
#         

# In[1]:


bacon = 22    
bacon + 1

After running the code, the variable bacon will contain the value 23.
# ## 7.What should the values of the following two terms be?

# In[2]:


'spam' + 'spamspam'


# In[3]:


'spam' * 3


# The value for both term is same  i.e. - 'spamspamspam'

# ## 8. Why is eggs a valid variable name while 100 is invalid?
In Python, variable names must start with a letter or an underscore and can only contain letters, numbers, and underscores.
So, eggs is a valid variable name because it starts with a letter, whereas 100 is invalid because it starts with a number.
# ## 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
# ## 10.Why does this expression cause an error? How can you fix it?

# In[4]:


'I have eaten ' + 99 + ' burritos.'


# In[5]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




