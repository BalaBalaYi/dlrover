"""给定一个起始字符串和一个终止字符串，以及一个单词表，求是否可以将起始字符串每次改
一个字符，直到改成终止字符串，且所有中间的修改过程表示的字符串都可以在单词表里找到。
若存在，输出需要修改次数最少的所有更改方式。

输入：
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出：
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

输入：
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]

输出：[]

解释：endWord "cog" 不在字典中，所以无法完成转换。
"""
from collections import defaultdict, deque


def findLadders(begin_word, end_word, word_list):
    word_set = set(word_list)
    letters = "abcdefghijklmnopqrstuvwxyz"

    if end_word not in word_set:
        return []

    # 删除begin word，避免重复访问
    if begin_word in word_set:
        word_set.remove(begin_word)

    # 构件图：记录每个单词的前驱单词
    pre_words = defaultdict(list)

    # 记录每个单词到beginWord的最短距离
    distance = {beginWord: 0}

    # BFS
    found = False
    step = 0
    queue = deque([begin_word])

    while queue:
        step += 1
        size = len(queue)

        # 记录当前层的单词
        current_level_words = set()

        for _ in range(size):
            current_word = queue.popleft()
            print(f"process word: {current_word}")

            # 生成当前单词的所有可能变换
            for i in range(len(current_word)):
                for c in letters:
                    if c == current_word[i]:
                        # 相同字母，没有必要替换
                        continue

                    # 替换成新单词
                    new_word = current_word[:i] + c + current_word[i+1:]

                    # 如果新单词匹配
                    if new_word == end_word:
                        found = True
                        pre_words[new_word].append(current_word)
                    else:
                        # 如果不匹配
                        if new_word in word_set:
                            # 在词表中
                            if new_word not in distance:
                                # 如果新单词是第一次访问，或者在同一层访问
                                distance[new_word] = step
                                pre_words[new_word].append(current_word)
                                current_level_words.add(new_word)
                            elif distance[new_word] == step:
                                # 如果已经在同一层访问过，说明有多条最短路径
                                pre_words[new_word].append(current_word)

            # 将当前层的单词加入队列
            for word in current_level_words:
                queue.append(word)
            print(f"current words in queue: {queue}")

            # 移除已经生成的单词，避免重复访问
            word_set -= current_level_words
    if not found:
        return []

    print(f"pre words: {pre_words}")

    # DFS回溯最短路径
    result = []

    def dfs(path, word):
        if word == begin_word:
            result.append([begin_word] + path[::-1])
            return

        for pre_word in pre_words[word]:
            path.append(word)
            dfs(path, pre_word)

    dfs([], end_word)
    return result


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(f"result: {findLadders(beginWord, endWord, wordList)}")
    # 输出: [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]
