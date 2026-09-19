class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue
                
                # Un-indent these lines 1 level back:
                box_index = (r // 3) * 3 + (c // 3)
                if digit in rows[r] or digit in cols[c] or digit in boxes[box_index]:
                    return False
                    
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box_index].add(digit)

        return True