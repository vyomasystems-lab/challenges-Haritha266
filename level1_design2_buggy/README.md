# SEQUENCE_1011_DETECTOR Design Verification

Raedme file by Gopisetty Haritha

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


![](https://user-images.githubusercontent.com/83575446/182147208-76e39ec1-2209-46fe-8e5e-25dd21eb01b8.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (SEQUENCE_1011_DETECTOR module here) which takes in 1-bit input signal and 1 bit reset signal and clock signal and gives 1-bit output

The values are assigned to the input port using 
```
    dut.reset.value = 0
    dut.inp_bit.value = 1
    dut.clk.value = 0
```

The assert statement is used for comparing the SEQUENCE_1011_DETECTOR's outut to the expected value.

The following error is seen:
```
 assert dut.seq_seen.value == 1,f"Output is incorrect {dut.seq_seen}!=1"
                     AssertionError: Output is incorrect 0! = 1
```

## Test Scenario **(Important)**
- Test Inputs: 
    dut.reset.value = 0
    dut.reset.value = 1
    dut.inp_bit.value = 0
    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 1
    dut.inp_bit.value = 0
    dut.inp_bit.value = 0
    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 1
- Expected Output: seq_seen = 1
- Observed Output in the DUT seq_seen =0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
    SEQ_1011:
      begin
        next_state = IDLE;   ====> BUG   
      end            
```
For the sequence detector design, the logic should be

`` SEQ_1011:
      begin
        if(input_bit == 1)
          next_state = SEQ_011;
        else
          next_state = IDLE;
      end  `` 
      instead of 
`` SEQ_1011:
      begin
        next_state = IDLE;   
      end     ``
      
  as in the design code.


![](https://user-images.githubusercontent.com/83575446/182147375-1ddea87c-aa70-4dfa-b1cf-ee334fbd0174.png)


## Verification Strategy

As this is a moore overlapping sequence detector, it must detect the sequence 1011 from the contiuatiuon of previous input. In the input I've provided two such sequences where 1011 can be detected twice and Latest ouput i.e. when the sequence is detected for the second time the ouput which is high should be displayed. Since, the last state is terminated to IDLE state the second sequence is not detected. which made the output to print a 0 causing the bug. So,I've corrected by changing the last state (SQ1011).
