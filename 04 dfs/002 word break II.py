class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def dfs(s, cur_index, space_index):
            if cur_index == len(s):
                return []

            all_possible_sentences = []

            # 在通常的backtrack中，我们会用到for () loop，在每个iteration的结尾，进行restore state
            # 这种for loop，本身就是sequence，执行第一个，执行第二个，执行第三个。
            # 而且，每种case之间，并不是exclusive的

            # case 1,  add space in right side of current letter
            last_space_index = space_index[-1] if len(space_index) != 0 else -1
            last_letter = s[last_space_index + 1 : cur_index + 1]
            space_index.append(cur_index)
            if last_letter in wordDict:
                possible_sentences_case_1 = dfs(s, cur_index + 1, space_index)
                if cur_index == len(s) - 1:
                    all_possible_sentences += [ last_letter + " " + sentence  for sentence in possible_sentences_case_1] if possible_sentences_case_1 else [last_letter]
                else:
                    all_possible_sentences += [ last_letter + " " + sentence  for sentence in possible_sentences_case_1] if possible_sentences_case_1 else []
            
            # csae 2, NO space in right side of current letter
            space_index.pop()
            possible_sentences_case_2 = dfs(s, cur_index + 1, space_index)

            all_possible_sentences += possible_sentences_case_2

            return all_possible_sentences

        return dfs(s, 0, [])