import numpy as np


def solve(data: str) -> None:
    alg, img = data.strip().split("\n\n")
    
    def window(arr: np.ndarray, fill: str) -> np.ndarray:
        rows, cols = arr.shape
        p = np.pad(arr, 2, constant_values=fill)
        return np.lib.stride_tricks.sliding_window_view(
            p, (3,3)
        ).reshape(rows+2, cols+2, 9)
    
    def _enhance(arr: np.ndarray) -> str:
        i = 0
        for x in arr:
            i = (i << 1) + int(x == '#')
        return alg[i]
    
    def enhance(arr: np.ndarray, fill: str) -> np.ndarray:
        return np.apply_along_axis(_enhance, -1, window(arr, fill))
    
    img = np.array([list(x) for x in img.splitlines()])
    fill = '.'
    for n in 2, 48:
        for _ in range(n):
            img = enhance(img, fill)
            if fill == '.' and alg[0] == '#':
                fill = '#'
            elif fill == '#' and alg[-1] == '.':
                fill = '.'
        print(np.count_nonzero(img == '#'))
    



if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
