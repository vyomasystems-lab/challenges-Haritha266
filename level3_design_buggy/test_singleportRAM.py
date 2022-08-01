# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer,RisingEdge, FallingEdge

async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(5):
        dut.clk.value = 1
        await Timer(1, units="ns")
        dut.clk.value = 0
        await Timer(1, units="ns")

@cocotb.test()
async def test_singleportRAM_bug1(dut):
    dut.clk.value = 1
    await Timer(2, units="ns")  # wait a bit
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    dut.q.value = 0
    # reset
    dut.data.value = 0x1
    dut.addr.value = 00000
    dut.we.value = 1
    await Timer(2, units="ns")  # wait a bit
    await RisingEdge(dut.clk)
    dut.addr.value = 00000
    dut.we.value = 0  
    await Timer(2, units="ns")  # wait a bit
    await RisingEdge(dut.clk)
    
    assert dut.q.value == 0x1,f"Output is incorrect {dut.q}!=0x1"
