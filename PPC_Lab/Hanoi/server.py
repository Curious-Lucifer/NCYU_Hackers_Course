import random, sys, string

from secret import flag

msg = '''===== Welcome To Hanoi Game =====
There are three hanoi tower
+-----+-----+-----+
|     |     |     |
|  0  |  1  |  2  |
|     |     |     |
+-----+-----+-----+
Please solve the puzzle !
------ Exmaple ------
Here is the initial state :
+-----+-----+-----+
|  l  |     |     |
| lll |     |     |
|lllll|     |     |
+-----+-----+-----+
Here is the final state :
+-----+-----+-----+
|     |     |  r  |
|     |     | rrr |
|     |     |rrrrr|
+-----+-----+-----+
Answer : 02012102101202 (which means move the top disk on tower 0 to tower 2, move the top disk on tower 0 to tower 1, ...)
'''
char_set = string.ascii_letters + string.digits

class HanoiState:
    def __init__(self, state: list):
        assert len(state) == 3

        tower_state = [[], [], []]
        for i in reversed(range(3)):
            tower_state[state[i]].append(i)
        self.tower_state = tower_state

    def __str__(self):
        random_char = random.choice(char_set)
        msg = '+' + '-----+' * 3 + '\n'
        tower_string = ["|", "|", "|"]

        for i in range(3):
            if len(self.tower_state[i]) == 0:
                for _ in range(3):
                    tower_string[_] += ' ' * 5 + '|'
            elif len(self.tower_state[i]) == 1:
                tower_string[0] += ' ' * 5 + '|'
                tower_string[1] += ' ' * 5 + '|'
                tower_string[2] += ' ' * (2 - self.tower_state[i][0]) + random_char * (2 * self.tower_state[i][0] + 1) + ' ' * (2 - self.tower_state[i][0]) + '|'
            elif len(self.tower_state[i]) == 2:
                tower_string[0] += ' ' * 5 + '|'
                tower_string[1] += ' ' * (2 - self.tower_state[i][1]) + random_char * (2 * self.tower_state[i][1] + 1) + ' ' * (2 - self.tower_state[i][1]) + '|'
                tower_string[2] += ' ' * (2 - self.tower_state[i][0]) + random_char * (2 * self.tower_state[i][0] + 1) + ' ' * (2 - self.tower_state[i][0]) + '|'
            else:
                for _ in range(3):
                    tower_string[_] += ' ' * (2 - self.tower_state[i][2 - _]) + random_char * (2 * self.tower_state[i][2 - _] + 1) + ' ' * (2 - self.tower_state[i][2 - _]) + '|'

        msg += '\n'.join(tower_string)
        msg += '\n' + '+' + '-----+' * 3
        return msg

    def move_once(self, move_instruction):
        assert len(move_instruction) == 2
        from_tower, to_tower = int(move_instruction[:1]), int(move_instruction[1:])
        assert (0 <= from_tower <= 2) and (0 <= to_tower <= 2)
        assert (len(self.tower_state[from_tower]) > 0)
        if len(self.tower_state[to_tower]) > 0:
            assert self.tower_state[from_tower][-1] < self.tower_state[to_tower][-1]
        disk = self.tower_state[from_tower].pop(-1)
        self.tower_state[to_tower].append(disk)

    def __eq__(self, other):
        return self.tower_state == other.tower_state

def main():
    print(msg)
    for i in range(100):
        print(f'------ wave {i + 1}/100 ------')

        init_state = HanoiState(random.choices([0, 1, 2], k = 3))
        fin_state = HanoiState(random.choices([0, 1, 2], k = 3))
        while fin_state == init_state:
            fin_state = HanoiState(random.choices([0, 1, 2], k = 3))
        print('Here is the initial state :')
        print(init_state)
        print('Here is the final state :')
        print(fin_state)
        ans = input('Answer > ')
        assert (len(ans) % 2) == 0
        
        for i in range(0, len(ans), 2):
            init_state.move_once(ans[i: i + 2])
        assert init_state == fin_state
    print(f'Flag : {flag}')

try:
    main()
except:
    print('Wrong answer')
    sys.exit()