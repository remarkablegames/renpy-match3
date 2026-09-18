init -1 python:

    def match_score(cell_count, level):
        return (SCORE_BASE + (cell_count - 3) * SCORE_PER_TILE) * level


    class Match3Board:

        def __init__(self, rows, cols, kinds):
            self.rows = rows
            self.cols = cols
            self.kinds = kinds
            self.grid = None
            self.regenerate()

        def regenerate(self):
            while True:
                self.grid = []
                for r in range(self.rows):
                    row = []
                    for c in range(self.cols):
                        banned = set()
                        if c >= 2 and row[-1] == row[-2]:
                            banned.add(row[-1])
                        if r >= 2 and self.grid[-1][c] == self.grid[-2][c]:
                            banned.add(self.grid[-1][c])
                        choices = [kind for kind in self.kinds if kind not in banned]
                        row.append(renpy.random.choice(choices))
                    self.grid.append(row)
                if self.possible_moves():
                    break

        def get(self, r, c):
            return self.grid[r][c]

        def neighbors(self, r, c):
            result = []
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    result.append((nr, nc))
            return result

        def swap(self, r1, c1, r2, c2):
            self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]

        def find_matches(self):
            matches = set()
            for r in range(self.rows):
                c = 0
                while c < self.cols:
                    kind = self.grid[r][c]
                    run = 1
                    while c + run < self.cols and self.grid[r][c + run] == kind:
                        run += 1
                    if run >= 3:
                        for cc in range(c, c + run):
                            matches.add((r, cc))
                    c += run
            for c in range(self.cols):
                r = 0
                while r < self.rows:
                    kind = self.grid[r][c]
                    run = 1
                    while r + run < self.rows and self.grid[r + run][c] == kind:
                        run += 1
                    if run >= 3:
                        for rr in range(r, r + run):
                            matches.add((rr, c))
                    r += run
            return matches

        def remove(self, cells):
            for r, c in cells:
                self.grid[r][c] = None

        def drop(self):
            for c in range(self.cols):
                column = [self.grid[r][c] for r in range(self.rows)]
                column = [kind for kind in column if kind is not None]
                while len(column) < self.rows:
                    column.insert(0, renpy.random.choice(self.kinds))
                for r in range(self.rows):
                    self.grid[r][c] = column[r]

        def possible_moves(self):
            for r in range(self.rows):
                for c in range(self.cols):
                    if c + 1 < self.cols:
                        self.swap(r, c, r, c + 1)
                        if self.find_matches():
                            self.swap(r, c, r, c + 1)
                            return True
                        self.swap(r, c, r, c + 1)
                    if r + 1 < self.rows:
                        self.swap(r, c, r + 1, c)
                        if self.find_matches():
                            self.swap(r, c, r + 1, c)
                            return True
                        self.swap(r, c, r + 1, c)
            return False
