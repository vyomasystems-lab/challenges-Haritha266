# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    select = 12
    input12 = 1

    dut.sel.value = select
    dut.inp12.value = input12

    await Timer(2, units='ns')

    assert dut.out.value == input12 , "Mux result is incorrect: {input12} and {select} != {OUT}, expected value={EXP}".format(
            input12 =int(dut.inp12.value), select=int(dut.sel.value), OUT=int(dut.out.value), EXP=input12)
