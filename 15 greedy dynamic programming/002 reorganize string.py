from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:

        result = []
        letter_count = Counter(s)
        letter_count = [(-count, letter) for letter, count in letter_count.items()]
        heapq.heapify(letter_count)  
        print(letter_count)    

        while letter_count:
            first_count, first_letter = heapq.heappop(letter_count)
            if not result or first_letter != result[-1]:
                result.append(first_letter)
                first_count += 1
                if first_count != 0:
                    heapq.heappush(letter_count, (first_count, first_letter))
                
            else:
                # means, the top letter in the priority queue is the last letter in result
                # not the letter_count is empty, but we still have one letter that is same with the last letter in result, which violate the rule, and thus, we return empty string immediately
                if not letter_count:
                    return ""
                second_count, second_letter = heapq.heappop(letter_count)
                result.append(second_letter)
                second_count += 1
                if second_count != 0:
                    heapq.heappush(letter_count, (second_count, second_letter))
                heapq.heappush(letter_count, (first_count, first_letter))
            
        return "".join(result)