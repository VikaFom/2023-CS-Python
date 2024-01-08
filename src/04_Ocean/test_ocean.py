from ocean import Ocean

def read_state_from_file(path):
    file = open(path)
    n_rows, n_clms = (int(i) for i in file.readline().split())
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in file.readline().split()]
        init_state.append(line)
    return init_state


def test_ocean_init():
    init_state = read_state_from_file('src/04_Ocean/testinput.txt')
    ocean = Ocean(init_state=init_state)
    assert init_state == ocean.state


def test_ocean_repr():
    ocean = Ocean(read_state_from_file('src/04_Ocean/testinput.txt'))
    assert eval(repr(ocean))


def test_ocean_step():
    ocean1 = Ocean(read_state_from_file('src/04_Ocean/testinput.txt'))
    ocean2 = Ocean(read_state_from_file('src/04_Ocean/step1result.txt'))
    ocean3 = ocean1.gen_next_quantum()
    assert ocean3 == ocean2
