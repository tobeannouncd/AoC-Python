from io import StringIO
from crt import CRT

class MyCRT(CRT):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ans = 0
    
    def _cycle(self, *args, **kwargs) -> None:
        if (self.cycle - 20) % 40 == 0:
            self.ans += self.cycle*self.x
        super()._cycle(*args, **kwargs)

def solve(data: str) -> None:
    c = MyCRT()
    signal = StringIO(data)
    c.run(signal)
    print(c.ans)
    print(c.screen)



if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
