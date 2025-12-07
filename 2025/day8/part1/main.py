def count_splits():
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
    
        beams = set([start_col])
        splits = 0
        visited = set()

        for r in range(1, rows):
            row = grid[r]
            next_beams = set()
            for c in beams:
                if c is None:
                    continue
                if 0 <= c < cols and row[c] == '^':
                    if (r, c) not in visited:
                        splits += 1
                        visited.add((r, c))
                        if c-1 >= 0:
                            next_beams.add(c-1)
                        if c+1 < cols:
                            next_beams.add(c+1)
                    else:
                        pass
                else:
                    if 0 <= c < cols and row[c] == '.':
                        next_beams.add(c)
            beams = next_beams
            if not beams:
                break
        return splits

print(count_splits())
        