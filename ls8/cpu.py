"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0


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
            print(f"MUL: {self.register[reg_a] * self.register[reg_b]}")
            return self.register[reg_a] * self.register[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
    
    def ram_read(self, mar):
        self.ram[pc]

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
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while True:
            
            IR = self.ram[self.pc]
            #print(f"register: {self.register}")
            if IR == 130:
                self.pc += 2
                self.register[self.pc] = self.ram[self.pc]
                print(self.register[self.pc])
                
            elif IR == 71:  
                print(self.register[0])
                self.pc += 1

            elif IR == 162:
                print(f"pc: {self.pc}, register:{self.register}")
                print(f"register[self.pc-4]: {self.register[self.pc - 4]}, register[self.pc - 1]: {self.register[self.pc -1]} ")
                reg_a = self.pc - 4
                reg_b = self.pc -1
                print(f"reg_a: {reg_a}")
                print(f"reg_b: {reg_b}")
                self.alu("MUL", reg_a, reg_b)

            elif IR == 1:
                print("BREAK")
                break

            self.pc += 1
        print(f"self.pc: {self.pc}")
        print(f"self.register: {self.register}")
        print(f"self.ram: {self.ram}")
            
