import concurrent.futures

def count_words(sentences):
    word_count = {}
    for sentence in sentences:
        for word in sentence.split(" "):
            if(word in word_count):
                word_count[word]+=1
            else:
                word_count[word] = 1
    return word_count

sentences = []

with open('input.txt') as f:
    lines = f.readlines()

for sentence in lines:
    temp = sentence.strip()
    if temp != '':
        sentences.append(temp)    

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
        futures.append(executor.submit(count_words, divide_sentences))
        curr_len += add_len

    int_maps = []
    for future in concurrent.futures.as_completed(futures):
        int_maps.append(future.result())

def combine_results(int_maps):
    result_map = {}
    for temp_map in int_maps:
        for key,value in temp_map.items():
            result_map[key]=result_map.get(key, 0) + value