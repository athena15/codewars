
# coding: utf-8

# In[39]:


from collections import defaultdict

def delete_nth(lst, n):
    final_lst = []
    for elem in lst:
        if final_lst.count(elem) < n:
            final_lst.append(elem)
        else:
            continue
    print(final_lst)
        


# In[42]:


delete_nth([20,37,20,21, 20],2)


# In[38]:




