import re
import os


def preprocessing(filename):
    file = open(filename)
    content = file.read()
    word = re.compile(r'[^a-zA-Z]')
    content = word.sub('', content)
    content = content.lower()
    return content


def generate_n_gram(content, n):
    n_gram = []
    for i in range(len(content) - n + 1):
        n_gram.append(content[i:i + n])
    return n_gram


def rolling_hashing(n_gram, Base, n):
    hashlist = []
    hash = 0
    initial = n_gram[0]

    for i in range(n):
        hash += ord(initial[i]) * (Base ** (n - 1 - i))
    hashlist.append(hash)

    for i in range(1, len(n_gram)):
        pre = n_gram[i - 1]
        present = n_gram[i]
        hash = (hash - ord(pre[0]) * (Base ** (n - 1))) * Base + ord(present[n - 1])
        hashlist.append(hash)
    return hashlist


def winnowing(hashlist, t, n):
    window = t - n + 1
    minValue = minPos = 0
    fingerprint = {}
    for i in range(len(hashlist) - window + 1):
        temp = hashlist[i:i + window]
        minValue = temp[0]
        minPos = 0
        for j in range(window):
            if temp[j] <= minValue:
                minValue = temp[j]
                minPos = j
        if (i + minPos) not in fingerprint.keys():
            fingerprint[i + minPos] = minValue
    return fingerprint


def comparison(fingerprint_1, fingerprint_2):
    count = 0
    size = min(len(fingerprint_1), len(fingerprint_2))
    for i in fingerprint_1.values():
        for j in fingerprint_2.values():
            if (i == j):
                count += 1
                break
    return count / size


if __name__ == '__main__':
    print('分片大小为5')
    print('检测阈值为9')
    dirpath = os.getcwd()
    print(dirpath)  # 输出当前路径
    path_1 = dirpath + "\\test_1.txt"
    path_2 = dirpath + "\\test_2.txt"
    fingerprint_1 = winnowing(rolling_hashing(generate_n_gram(preprocessing(path_1), 5), 17, 5), 9, 5)
    fingerprint_2 = winnowing(rolling_hashing(generate_n_gram(preprocessing(path_2), 5), 17, 5), 9, 5)
    print("相似度：")
    print(comparison(fingerprint_1, fingerprint_2))
