class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # מיון הקטעים לפי נקודת ההתחלה
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # אם הרשימה ריקה או שאין חפיפה עם הקטע האחרון
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # מיזוג קטעים חופפים
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
