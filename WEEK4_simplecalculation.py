#!/usr/bin/env python
# coding: utf-8

# In[13]:


try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    
    if operation == '+':
        result = a + b
        print(result)
    elif operation == '-':
        result = a - b
        print(result)
    elif operation == '*':
        result = a*b
        print(result)
    elif opeartion == '/':
        result = a/b
        print(result)
    else:
        print("invalid operation. please choose again")
            
except ZeroDivisionError:
    print("division by zero is not allowed")
except ValueError:
    print("please enter a valid number")
            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




