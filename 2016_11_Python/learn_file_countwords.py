def divide_word(line):
    def not_none(words):
        for word in words:
            if word != '':
                return True
            else:
                return False
    words = list(filter(not_none, line.split(' ')))
    countwords = {}
    for word in words:
        if word in countwords:
            countwords[word] += 1
        else:
            countwords[word] = 1
    return countwords
def replace_str(line):
    for chars in "~!@#$%^&*()_+-=<>?:{}'/\[]|.,;`":
        line = line.replace(chars, '')
    return line.strip()
def main():
    file_name = input('Please Input The File Name: ')
    file = open(file_name, 'r', encoding='utf-8')
    wordlist = {}
    for line in file:
        words = divide_word(replace_str(line))
        for key_1 in words:
            for key_2 in wordlist:
                if key_1 == key_2:
                    words[key_1] += 1
                    wordlist[key_2] +=1
        wordlist.update(words)
    print(wordlist)
    file.close()
    input()
if __name__ == '__main__':
    main()