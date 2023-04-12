phrase=("Ram is a boy he stuided in Herald College Kathmandu, he is very popular among students on College")
phrase=phrase.lower()
result={}
word_list=phrase.split()
for word in phrase:
    if word not in result:
        result[word]=1
    else:
        result[word]+=1
print(result)
