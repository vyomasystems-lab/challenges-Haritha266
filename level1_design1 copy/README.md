# MUX Design Verification

Raedme file by Gopisetty Haritha

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![](https://user-images.githubusercontent.com/83575446/182013260-17b68455-53dd-4f6a-9373-bd353c5e6efe.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 
```
    dut.sel.value = 12
    dut.inp12.value = 1
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.out.value == input12 , "Mux result is incorrect: {input12} and {select} != {OUT}, expected value={EXP}".format(input12 =int(dut.inp12.value), select=int(dut.sel.value), OUT=int(dut.out.value), EXP=input12)
                     AssertionError: Mux result is incorrect: 1 and 12 != 0, expected value=1
```

![](https://user-images.githubusercontent.com/83575446/182013296-91377a05-cca7-449c-bef3-9068ae10383e.png)

## Test Scenario **(Important)**
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

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

![](https://user-images.githubusercontent.com/83575446/182013309-dbcde8f2-ed9a-4603-9992-51170460a01a.png)


## Verification Strategy

## Is the verification complete ?
