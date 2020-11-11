prefix='de';
words=['dog', 'deal', 'deer','deal', 'deer']
l=len(prefix);
for i in words:
    if prefix in i[:l]:
        print(i);