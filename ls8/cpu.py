"""CPU functionality."""
from colorama import init, Fore
init(autoreset=True)
import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0 # program counter
        self.stack_pointer = 244 # stack for temporary info


    def load(self, program):
        """Load a program into memory."""
        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        for instruction in program:
            print(f"instruction from program: {instruction}")
            self.ram[address] = instruction
            address += 1


        #Sprint(self.ram)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            print(f"MULTIPLY RESULT: {self.register[reg_a] * self.register[reg_b]} !")
            return self.register[reg_a] * self.register[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
    
    def ram_read(self, mar):
        self.ram[mar]

    def ram_write(self, mar, mdr ):
        self.ram[mar] = mdr
        
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.register[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while True:
            if self.pc > 30:
                break
            print(Fore.GREEN + f"--------\nREADING: {self.ram[self.pc]} AT RAM[PC == {self.pc}], STACK_POINTER: {self.stack_pointer}")
            IR = self.ram[self.pc]
            a = self.ram[self.pc + 1]
            b = self.ram[self.pc + 2]
            #print(f"register: {self.register}")
            
            # LDI 
            if IR == 130: 
                print(f"--------\nLDI R{a} = {b}")           
                self.register[a] = b
                self.pc += 2
            # PRINT
            elif IR == 71:  
                print(Fore.YELLOW + f"--------\nPRINTING: R{a} == {self.register[a]} pc: {self.pc} ")
                self.pc += 1
            # MULTIPLY
            elif IR == 162:
                print(Fore.LIGHTCYAN_EX + f"--------\nMULTIPLYING pc: {self.pc}, register:{self.register}")
                print(f"register[self.pc-4]: {self.register[self.pc - 4]}, register[self.pc - 1]: {self.register[self.pc -1]} ")
                
                print(f"reg a: {a}")
                print(f"reg b: {b}")
                self.alu("MUL", a, b)
            # PUSH
            elif IR == 69:
                
                self.stack_pointer -= 1
                self.ram[self.stack_pointer] = self.register[a]
                print(f"--------\nPUSH R{a} to RAM[{self.stack_pointer}]")
                print(f"RAM[{self.stack_pointer}] == {self.ram[self.stack_pointer]}")
                self.pc += 1
            # POP
            elif IR == 70:                
                self.register[a] = self.ram[self.stack_pointer] 
                print(f"--------\nPOP RAM[{self.stack_pointer}] to R{a}")
                print(f"R{a} == {self.register[a]}")
                self.stack_pointer += 1
                self.pc += 1
            # INTHANDLER
            elif IR == 132:
                self.pc += 2
                print(f"INTHANDLER")

            # CALL
            elif IR == 80:     
                print(f"CALL")
                #self.pc = self.register[0]
                
            # HALT
            elif IR == 1:
                print(Fore.LIGHTRED_EX+ "HALT")
                break

                

            self.pc += 1
        print(f"self.pc: {self.pc}")
        print(f"self.register: {self.register}")
        print(f"self.ram: {self.ram}")
            
