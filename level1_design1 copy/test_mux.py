# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    select = 5'b00011
    input3 = 5

    dut.sel.value = select
    dut.inp3.value = input3

    await Timer(2, units='ns')

    assert dut.out.value == input3 , "Mux result is incorrect: {input3} and {select} != {OUT}, expected value={EXP}".format(
            input3 =int(dut.inp3.value), select=int(dut.sel.value), OUT=int(dut.out.value), EXP=input3)
    #cocotb.log.info('##### CTB: Develop your test here ########')
