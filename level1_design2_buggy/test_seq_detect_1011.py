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

    for cycle in range(10):
        dut.clk.value = 0
        await Timer(1, units="ns")
        dut.clk.value = 1
        await Timer(1, units="ns")

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    # reset
    dut.reset.value = 0
    await Timer(2, units="ns")  # wait a bit
    dut._log.info("\nbefore %s",dut.reset.value)
    await RisingEdge(dut.clk)  
    dut.reset.value = 1
    await Timer(2, units="ns")  # wait a bit
    await RisingEdge(dut.clk)
    dut._log.info("\nbefore %s",dut.reset.value)
    dut.inp_bit.value = 1
    await Timer(2, units="ns")  # wait a bit
    await RisingEdge(dut.clk)
    dut._log.info("\nAfter %s",dut.inp_bit.value)
    dut.inp_bit.value = 0
    await Timer(2, units="ns")  # wait a bit
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    await Timer(2, units="ns")  # wait a bit
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    assert dut.seq_seen.value == 1,f"Output is incorrect {dut.seq_seen}!=1"
