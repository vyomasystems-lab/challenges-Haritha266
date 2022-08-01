# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer,RisingEdge, FallingEdge


@cocotb.test()
async def test_singleportRAM_bug1(dut):
   
