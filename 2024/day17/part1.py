class ChronospatialComputer:
    def __init__(self, data: list[str]) -> None:
        self.register_a = int(data[0][data[0].rfind(':') + 1 :])
        self.register_b = int(data[1][data[1].rfind(':') + 1 :])
        self.register_c = int(data[2][data[2].rfind(':') + 1 :])

        self.program = [int(d) for d in data[4][data[4].rfind(':') + 1 :].split(',')]

        self.output: list[int] = []

        self.instruction_pointer: int = 0

    def _print_state(self) -> None:
        print(f'Register A: {self.register_a}')
        print(f'Register B: {self.register_b}')
        print(f'Register C: {self.register_c}')
        print()
        print(f'Program: {','.join([str(p) for p in self.program])}')
        print()
        print(f'Output:  {','.join([str(o) for o in self.output])}')
        print()

    def _combo_operand(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.register_a
            case 5:
                return self.register_b
            case 6:
                return self.register_c
        print('invalid program')
        exit(-1)

    def run(self) -> None:
        print('BEGIN\n')
        self._print_state()

        instruction_pointer: int = 0

        while instruction_pointer < len(self.program):
            opcode = self.program[instruction_pointer]
            operand = self.program[instruction_pointer + 1]

            match opcode:
                case 0:  # adv
                    self.register_a //= 2 ** self._combo_operand(operand)
                case 1:  # bxl
                    self.register_b ^= operand
                case 2:  # bst
                    self.register_b = self._combo_operand(operand) % 8
                case 3:  # jnz
                    if self.register_a != 0:
                        instruction_pointer = operand
                        continue
                case 4:  # bxc
                    self.register_b ^= self.register_c
                case 5:  # out
                    self.output.append(self._combo_operand(operand) % 8)
                case 6:  # bdv
                    self.register_b //= self.register_a / (2 ** self._combo_operand(operand))
                case 7:  # cdv
                    self.register_c = self.register_a // (2 ** self._combo_operand(operand))

            instruction_pointer += 2

        print('END\n')
        self._print_state()


with open('input2.txt') as file:
    data = [line.replace('\n', '') for line in file.readlines()]

computer = ChronospatialComputer(data)
computer.run()
