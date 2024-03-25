import collections 
from enum import Enum 
from pprint import pprint
import functools

class dir(Enum):
    r = 1
    w = 2
    rw = 3 

class data_type(Enum):
    bool = 1
    uint16 = 2
    float = 3

class io_type(Enum):
    d_input = 1
    d_output = 2
    a_input = 3
    a_output = 4
    pwm_out = 5
    ls_switch = 6

def reducer(acc, val) :
    acc[val.io_type].append(val.name)
    return acc 

def analog_map(io_tuple) :
    return tuple({'offset': x.offset, 'date_type': x.data_type, 'dir': x.dir, 'name': x.name, 'scale': x.param1 } for x in io_tuple)

def digital_map(io_tuple) :
    return tuple(map(lambda x: {'offset': x.offset, 'date_type': x.data_type, 'dir': x.dir, 'name': x.name }, io_tuple))

def create_ana_result_tuple() :
    ana_results = collections.namedtuple("analog result", ['value', 'raw'])

    return tuple([
      ana_results(3.3, 0xffff), 
      ana_results(0, 0x0000),
      ana_results(1.25, 0x7000)
    ])

def create_io_tuple() :
    io = collections.namedtuple('io', ['offset', 'data_type', 'dir', 'io_type', 'param1', 'param2', 'name'])

    return tuple([
        io(0, data_type.bool, dir.r, io_type.d_input, 0, 0, "DigInput1"),
        io(1, data_type.bool, dir.r, io_type.d_input, 0, 0, "DigInput2"),
        io(2, data_type.bool, dir.r, io_type.d_input, 0, 0, "DigInput3"),
        io(3, data_type.bool, dir.r, io_type.d_input, 0, 0, "DigInput4"),
        io(4, data_type.bool, dir.r, io_type.d_input, 0, 0, "DigInput5"),
        io(5, data_type.bool, dir.r, io_type.d_input, 0, 0, "DigInput6"),
        io(16, data_type.uint16, dir.r, io_type.a_input, 3.3, 4096, "Analog 1"),
        io(17, data_type.uint16, dir.r, io_type.a_input, 3.3, 4096, "Analog 2"),
        io(44, data_type.uint16, dir.r, io_type.a_output, 3.3, 4096, "Analog 2"),
    ])


io_tuple = create_io_tuple()

ana_iterator = filter(lambda x: (x.io_type == io_type.a_input), io_tuple)
dig_iterator = filter(lambda x: (x.io_type == io_type.d_input), io_tuple)


io_by_type = functools.reduce(reducer, io_tuple,
                                {io_type.d_input: [], io_type.a_input: [], io_type.d_output: [], io_type.a_output: []})

pprint(io_by_type)

#pprint(tuple(ana_iterator))

# pprint(digital_map(dig_iterator))
pprint(analog_map(ana_iterator))