from pwn import *
from tqdm import trange

r = remote('172.104.90.38', 10008)

class HanoiState:
    def __init__(self, towers_state: list[list]):
        self.towers_state = towers_state

    def __str__(self):
        return str(self.towers_state)

    def move(self, from_tower, to_tower):
        disk = self.towers_state[from_tower].pop(-1)
        self.towers_state[to_tower].append(disk)

def get_towers_state():
    r.recvline()
    resp = r.recvlines(3)
    r.recvline()

    towers_state = [[], [], []]
    for layer in resp:
        towers = layer.split(b'|')[1: -1]
        for i in range(3):
            if towers[i].count(b' ') != 5:
                towers_state[i].append((5 - towers[i].count(b' ')) // 2)
    
    for i in range(3):
        towers_state[i].reverse()
    return HanoiState(towers_state)

def get_move(state: HanoiState, disk, target_tower):
    for i in range(3):
        if disk in state.towers_state[i]:
            if i == target_tower:
                return state, []
            current_tower = i
            continue
        if i == target_tower:
            continue
        blank_tower = i

    move = []
    for i in reversed(range(disk)):
        state, partial_move = get_move(state, i, blank_tower)
        move += partial_move

    state.move(current_tower, target_tower)
    move += [current_tower, target_tower]
    return state, move

def get_ans(init_state: HanoiState, fin_state: HanoiState):
    state = HanoiState(init_state.towers_state)
    move = []
    for disk in reversed(range(3)):
        for i in range(3):
            if disk in fin_state.towers_state[i]:
                target_tower = i

        state, partial_move = get_move(state, disk, target_tower)
        move += partial_move

    return move

r.recvlines(23)

for i in trange(100):
    r.recvlines(2)
    init_state = get_towers_state()
    r.recvline()
    fin_state = get_towers_state()
    r.sendlineafter(b'> ', ''.join(str(n) for n in get_ans(init_state, fin_state)).encode())

r.interactive()