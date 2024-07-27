class Solution:
    from collections import Counter
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # build the user-web_list map
        user_2_weblist = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website), key = lambda x: x[1]):
            user_2_weblist[user].append(web)

        # build the pattern count map
        pattern_2_count = Counter()
        for user, web_list in user_2_weblist.items():
            pattern_combinations = Counter(set(combinations(web_list, 3)))
            pattern_2_count.update(pattern_combinations)
        
        # sort
        return max(sorted(pattern_2_count), key = pattern_2_count.get)
        # return sorted(pattern_2_count.items(), key = lambda x: (-x[1], x[0]))[0][0]
