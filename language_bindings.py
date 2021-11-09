#!/usr/bin/env python
# coding: utf-8

# In[1]:


import concurrent.futures
import time


# In[2]:


def read_file(file):
    sentences = []
    with open(file) as f:
        lines = f.readlines()
        
    for sentence in lines:
        temp = sentence.strip()
        if temp != '':
            sentences.append(temp)
    return sentences


# In[3]:


def count_words_serial(sentences):
    word_count = {}
    for sentence in sentences:
        for word in sentence.split(" "):
            if(word in word_count):
                word_count[word]+=1
            else:
                word_count[word] = 1
    return word_count


# In[4]:


def word_count_parallel(sentences):
    num_threads = 4
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        total_len = len(sentences)
        add_len = total_len//num_threads;
        curr_len = 0
        for i in range(num_threads):
            if(i==num_threads-1):
                divide_sentences = sentences[curr_len:]
            else:
                divide_sentences = sentences[curr_len:curr_len+add_len]
            futures.append(executor.submit(count_words_serial, divide_sentences))
            curr_len += add_len

        int_maps = []
        for future in concurrent.futures.as_completed(futures):
            int_maps.append(future.result())
    return int_maps


# In[5]:


def combine_results(int_maps):
    result_map = {}
    for temp_map in int_maps:
        for key,value in temp_map.items():
            result_map[key]=result_map.get(key, 0) + value
    return result_map


# In[6]:


start_time = time.time()
sentences = read_file('input2.txt')
int_maps = word_count_parallel(sentences)
result_map = combine_results(int_maps)
end_time = time.time()
diff_time = end_time-start_time


# In[8]:


diff_time

