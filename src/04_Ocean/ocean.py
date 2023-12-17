import sys
from typing import List


class Ocean:
    state: List[List[int]]

    def __init__(self, init_state: List[List[int]]):
        self.state = init_state

    def __str__(self) -> str:
        return "\n".join(["".join(str(el) for el in row) for row in self.state])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.state!r})"

    def gen_next_quantum(self) -> "Ocean":
        next_state = []
        for i in range(len(self.state)):
            next_state.append([])
            for j in range(len(self.state[i])):
                next_state[i].append(self.gen_next_cell(self,i,j)) 
        return Ocean(init_state=next_state)

    def gen_next_cell(self,i,j) -> int:
        cell = self.state[i][j]
        if cell == 1:
            return 1
        neighbors = self.get_neighbors(self.state,i,j)
        fishes = neighbors.count(2) 
        shrimps = neighbors.count(3)
        if cell == 2:
            if fishes > 3 or fishes < 2:
                return 0
            else:
                return 2
        if cell == 3:
            if shrimps > 3 or shrimps < 2:
                return 0
            else:
                return 3
        if cell == 0:
            if fishes == 2 or fishes == 3:
                return 2
            if shrimps == 2 or shrimps == 3:
                return 3
        return cell

        
    def get_neighbors(state,i,j) -> List[int]:
        result = []
        for ofset_i in range(-1,2):
            for ofset_j in range(-1,2):
                if ofset_i != 0 and ofset_j != 0:
                    cell_i = i + ofset_i
                    cell_j = j + ofset_j
                    if cell_i >=0 and cell_i <= len(state)-1 and cell_j >= 0 and cell_j <= len(state[i])-1:
                        result.append(state[i][j])
        return result
                



if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = (int(i) for i in sys.stdin.readline().split())
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
