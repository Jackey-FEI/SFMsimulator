# coding=utf-8
from sfm_simulator import SFMSimulator

sfm_simulator = SFMSimulator("maps/mikawalab.pgm", "maps/mikawalab.yaml", zoom=2)
sfm_simulator.debug()