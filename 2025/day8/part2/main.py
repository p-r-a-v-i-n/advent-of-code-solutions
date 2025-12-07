from collections import defaultdict
def count_timelines():
    with open("./2025/day8/input.txt") as f:
        content = f.read().strip().splitlines()
        grid = [list(line) for line in content]
        rows = len(grid)
        cols = len(grid[0])
        start_col = None
        for c, ch in enumerate(grid[0]):
            if ch == 'S':
                start_col = c
                break
        if start_col is None:
            raise ValueError("No 'S' found in top row")

        counts = defaultdict(int)
        counts[start_col] = 1

        for r in range(1, rows):
            row = grid[r]
            next_counts = defaultdict(int)
            for c, cnt in list(counts.items()):
                if cnt == 0:
                    continue
                if 0 <= c < cols and row[c] == '^':
                    if c - 1 >= 0:
                        next_counts[c - 1] += cnt
                    if c + 1 < cols:
                        next_counts[c + 1] += cnt
                else:
                    if 0 <= c < cols and row[c] == '.':
                        next_counts[c] += cnt
            counts = next_counts
            if not counts:
                break

        return sum(counts.values())
print(count_timelines())
