class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                box_key = (r//3,c//3)

                if val in row[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in boxes.get(box_key, set()):
                    return False

                row[r].add(val)
                cols[c].add(val)
                if box_key not in boxes:
                    boxes[box_key] = set()
                    boxes[box_key].add(val)

        return True
        