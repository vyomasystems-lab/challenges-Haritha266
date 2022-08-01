# singleportRAM Design Verification

Readme file by Gopisetty Haritha

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![](https://user-images.githubusercontent.com/83575446/182152035-cb0c54fb-fc6d-45ea-876c-f5eaf4cfc0ba.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (singleportRAM module here) which takes 8 bit hex input data and 5 bit address and a write, clock signals. Thus it forms 8*64 bit ram  and gives 8-bit hex output i.e whatever input is provided will be read back

The values are assigned to the input port using 
```
    dut.data.value = 0x1
    dut.addr.value = 00000
    dut.we.value = 1
    dut.addr.value = 00000
    dut.we.value = 0
```

The assert statement is used for comparing the singleportRAM's outut to the expected value.

The following error is seen:
```
 assert dut.q.value == 0x1,f"Output is incorrect {dut.q}!=0x1"
                     AssertionError: Output is incorrect 00000!=0x1
```

## Test Scenario **(Important)**
- Test Inputs:
    dut.data.value = 0x1
    dut.addr.value = 00000
    dut.we.value = 1
    dut.addr.value = 00000
    dut.we.value = 0
- Expected Output: dut.q.value = 0x1
- Observed Output in the DUT dut.q.value = 00000

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
     always @ (posedge clk)
    begin
      if(we)
        ram[addr] <= data;
      else
        addr_reg <= addr; 
    end
 
  assign q = addr_reg;        ====> BUG
               
```
For the design, the logic should be ``assign q = ram[addr_reg];  `` instead of ``assign q = addr_reg;  `` as in the design code.

## Failed testcase


![](https://user-images.githubusercontent.com/83575446/182150353-803f68b4-136c-4d2a-92af-d3f3e9fe52ea.png)


## Verification Strategy

I've observed the 31 inputs and found that input12 and input13 are defined with same selectline.So,I gave a test input 1 on selectline defined by input12 and observed the output.Since,input12 & input13 are defined by same select line it gave wrong output

## Is the verification complete ?
