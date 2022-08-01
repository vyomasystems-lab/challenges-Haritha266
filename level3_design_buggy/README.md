# singleportRAM Design Verification

Raedme file by Gopisetty Haritha

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![](https://user-images.githubusercontent.com/83575446/182152035-cb0c54fb-fc6d-45ea-876c-f5eaf4cfc0ba.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (singleportRAM module here) which takes in 31 inputs each 2-bit  and 5 bit select line and gives 2-bit output

The values are assigned to the input port using 
```
    dut.sel.value = 12
    dut.inp12.value = 1
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
 assert dut.q.value == 0x1,f"Output is incorrect {dut.q}!=0x1"
                     AssertionError: Output is incorrect 00000000!=0x1
```

## Test Scenario **(Important)**
- Test Inputs: select=12 input12=1
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
     5'b01011: out = inp11;
      5'b01101: out = inp12;        ====> BUG
      5'b01101: out = inp13;           
```
For the mux design, the logic should be ``5'b01100: out = inp12;  `` instead of ``5'b01101: out = inp12;  `` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://user-images.githubusercontent.com/83575446/182150353-803f68b4-136c-4d2a-92af-d3f3e9fe52ea.png)


## Verification Strategy

I've observed the 31 inputs and found that input12 and input13 are defined with same selectline.So,I gave a test input 1 on selectline defined by input12 and observed the output.Since,input12 & input13 are defined by same select line it gave wrong output

## Is the verification complete ?
