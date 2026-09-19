class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
# Step 1: Find first and last occurrences of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        valid_intervals = []
        
        # Step 2: Expand range for each character starting from its first occurrence
        for c in first:
            l = first[c]
            r = last[c]
            valid = True
            
            i = l
            while i <= r:
                ch = s[i]
                # If a character inside starts before our initial 'l', 
                # this starting point cannot produce a minimal valid range
                if first[ch] < l:
                    valid = False
                    break
                r = max(r, last[ch])
                i += 1
                
            if valid:
                valid_intervals.append((l, r))
                
        # Step 3: Sort valid intervals by end index (Greedy choice)
        valid_intervals.sort(key=lambda x: x[1])
        
        result = []
        last_end = -1
        
        for l, r in valid_intervals:
            if l > last_end:
                result.append(s[l:r + 1])
                last_end = r
                
        return result
        