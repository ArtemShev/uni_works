import random
with open('key.txt', encoding="utf-8") as file:
    alphabet = file.readline().rstrip()
    key = file.readline().rstrip()

def crypt(alph_in, alph_out, text):
    crypt = str.maketrans(alph_in, alph_out)
    new_text = text.translate(crypt)
    return new_text

# генерация рандомного ключа
def generate_random_key(alph):
    global key
    print ('old one:',key)
    new_key =''
    words = alph.split()
    for i, word in enumerate(map(list, words)):
        random.shuffle(word)
        new_key = ''.join(word)
    with open('key.txt', 'r') as f:
        old_key = f.read().splitlines()
        old_key[1] = new_key
    with open('key.txt', 'w') as f:
        for keys in old_key:
            f.write(str(keys)+'\n')
    key = new_key
    return new_key
