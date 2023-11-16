from lattice import Point, from_str


def solve(data: str) -> None:
    tree_heights = {pt:int(val) for pt, val in from_str(data)}
    
    n_visible = 0
    best_score = 0
    for pt, height in tree_heights.items():
        score = 1
        visible = False
        for d in Point(0, 0).adjacent():
            n = 0
            cur = pt + d
            while cur in tree_heights:
                n += 1
                if tree_heights[cur] >= height:
                    break
                cur += d
            score *= n
            if cur not in tree_heights:
                visible = True
        n_visible += visible
        best_score = max(best_score, score)
    print(n_visible)
    print(best_score)



if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
