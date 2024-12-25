from operator import xor


class Program():
    def __init__(self, reg_A=0, reg_B=0, reg_C=0):
        self.a: int = reg_A
        self.b: int = reg_B
        self.c: int = reg_C        
        self.out: list[str] = []
        self.pos = 0
        self.instructions: list[str] = []
        
        
    
    def run_instruction(self, opcode:str, op:str) -> int:
        opval = None
        self.pos += 2
        
        if opcode in ['1', '3', '4']:
            opval = int(op)
        else: 
            match op:
                case '0' | '1' | '2' | '3':
                    opval = int(op)
                case '4':
                    opval = self.a
                case '5':
                    opval = self.b
                case '6':
                    opval = self.c
                case _:
                    pass

        if opval == None: raise ValueError(f'opval not set. {op} invalid.')        
        
        match opcode:
            case '0':
                # adv
                self.a = int(self.a / 2**opval)
                
            case '1':
                #bxl 
                self.b = self.b ^ opval # locial XOR
                
            case '2':
                # bst
                self.b = opval % 8 # modulo 8
                
            case '3': # jump instruction
                # jnz
                if self.a == 0: pass
                else: self.pos = opval
                
            case '4':                    
                #bxc
                self.b = self.b ^ self.c 
                
            case '5':
                #out    
                self.out.append(str(int(opval)%8))   
            case '6':
                #bdv
                self.b = int(self.a / 2**opval)
            case '7':
                #cdv
                self.c = int(self.a / 2**opval)                
            case _:
                raise ValueError        

    
    def __str__(self) -> str:
        s  = f'inst : ' + ','.join(self.instructions) + '\n'
        s += f'Reg A: {self.a:>4d}\n'
        s += f'Reg B: {self.b:>4d}\n'
        s += f'Reg C: {self.c:>4d}\n' 
        if len(self.out) > 0:
            s += 'out  :  ' + ','.join(self.out) + '\n'
        return s
    
    def read_instructions(self, inst:str):
        ins = inst.split(',')
        self.instructions = ins     
        print('setup complete:')   
        print(self)        
        
    def execute(self):
        print('executing!')
        while True:
            if self.pos + 1 >= len(self.instructions): 
                print(self)
                break
            
            opcode = self.instructions[self.pos]
            op = self.instructions[self.pos+1]
            
            # print(f'running [{opcode}] with [{op}]')
            self.run_instruction(opcode, op)
            
            
    
p1 = Program(28422061)
p1.read_instructions('2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0')
p1.execute()