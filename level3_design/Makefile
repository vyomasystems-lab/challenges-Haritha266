# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

#export PYTHONPATH := $(PWD):$(PYTHONPATH)  # reference model

VERILOG_SOURCES = $(PWD)/singleportRAM.v              # provide your design path

TOPLEVEL :=  singleportRAM         # design file
MODULE   :=   test_singleportRAM  # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
