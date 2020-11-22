import pandas as pd
month_cols = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# most of below sensors are from check_outliers.ipynb
def modify_suspicious_meter(sub):

    #257 - missing
    sub.loc[sub.meter_id == "0x81fa8eddb2b09393d3719984ca5520cb50f45efd", month_cols] = 0
    #291
    sub.loc[sub.meter_id == "0x2ce3d582a1316db5bcfe405cbd6070268944778e", month_cols] = 0
    #301 - missing
    sub.loc[sub.meter_id == "0xfcf81d3a033ed6490da5353ad84b6848f2bddb6d", month_cols] = 0
    #377
    sub.loc[sub.meter_id == "0x306e6baa9367d3c43fa6ecc2d0054b207d6ef471", month_cols] = 50 # December value
    #515 - missing
    sub.loc[sub.meter_id == "0x423fa805ddb0cba9bdb4460f9a78540287eefd0e", month_cols] = 0
    #775 - missing [***]
    sub.loc[sub.meter_id == "0xd23ef71e350e2d1c196c4e8c86b0366f24625f27", month_cols] = 0
    #963
    sub.loc[sub.meter_id == "0x11f730d29bba6ceccf25bebb76ba0e36486bb069", month_cols] = 5 # December value
    #993 - missing
    sub.loc[sub.meter_id == "0xf226527dbcb9b2afdbdb5d63e7c27d8bef036941", month_cols] = 0
    #1025 - missing
    sub.loc[sub.meter_id == "0x669a5529a8c912ae5df50d05b9b1f12a623304c1", month_cols] = 0
    #1091 - missing
    sub.loc[sub.meter_id == "0xe41c230484378b2312fbf1fc99d289e0b51a3c52", month_cols] = 0
    #1150 - missing
    sub.loc[sub.meter_id == "0xa0a3003a10a350195ebe503e0899ebeaccee78ae", month_cols] = 0
    #1156
    sub.loc[sub.meter_id == "0x61dd4b16c11dcd1d7e410f0ad7babf37dc1928dd", month_cols] = 50 # December value
    #1245
    sub.loc[sub.meter_id == "0xd9583a22cacb4a8e859bc9f33b54612c86fe7ce2", month_cols] = 0
    #1342 - missing?
    sub.loc[sub.meter_id == "0x95fc7e54336e87feed25423b86d9ea92e47432dc", month_cols] = 0
    #1360 - missing
    sub.loc[sub.meter_id == "0x800c9648a84c44cf1a1b0a0ada6283495a69fe8b", month_cols] = 0
    #1435
    sub.loc[sub.meter_id == "0x0a7d02ab9cf4a3dd1a21f6940b5f8ad91fcbd13a", month_cols] = 10 # December value
    #1545 - missing
    sub.loc[sub.meter_id == "0x59799e9835ff86e7926d43592c9fa93415a8b754", month_cols] = 0
    #1600 - low
    sub.loc[sub.meter_id == "0x391e6c2169c27de797ccbdf2d623365da28a6d3d", month_cols] = 2 # November and December mean value
    #1632 - missing
    sub.loc[sub.meter_id == "0x8056a9c7dfd5b10fda8336580fc7e00b6c80e7c4", month_cols] = 0
    #1887 - missing [***]
    sub.loc[sub.meter_id == "0x5c74fe4757ca70cf3c8e2ea491db1ae420649299", month_cols] = 10# December value
    #1971
    sub.loc[sub.meter_id == "0x67ca58db2caa5c31a3223609b3d5122dbcbbcdd6", month_cols] = 10 # December value
    #2005
    sub.loc[sub.meter_id == "0x5a9840bf9d91dff79ac0648b528cddad67868147", month_cols] = 50 # November and December mean value
    #2035 - low
    sub.loc[sub.meter_id == "0xdc06d14af4048e4b4b38b8119c77dcce785c1aa5", month_cols] = 50 # mean value
    #2042
    sub.loc[sub.meter_id == "0x0bb3e76a57e589d8e2a930aa868c225f5347fc71", month_cols] = 4 # November and December mean value
    #2080 - missing [***]
    sub.loc[sub.meter_id == "0xe2154c841409bba5b83d208c83c33938d1a02474", month_cols] = 0
    #2151 - missing [***]
    sub.loc[sub.meter_id == "0xe5c7a9422ea390997565ae6f037383ff79cf9daa", month_cols] = 10 # November and December mean value
    #2424 - low
    sub.loc[sub.meter_id == "0x240e5e22734a44a174b7dabcf1ea00d70d9ec168", month_cols] = 2 # November and December mean value
    #2475
    sub.loc[sub.meter_id == "0x346c07a72bf83bb591ef699f4abc02fd89d7105b", month_cols] = 20 # December value
    #2711
    sub.loc[sub.meter_id == "0xdd6f5700bd227b17f00c19564563094661450620", month_cols] = 0
    #2907
    sub.loc[sub.meter_id == "0x843fed762825bfdc1f8f07349d425fd5c7b4cd1e", month_cols] = 10 # December value
    #2955
    sub.loc[sub.meter_id == "0x463d557082956a82ac9cc68ef5ccf15a0a7ebda8", month_cols] = 250 # mean value
    #3224
    sub.loc[sub.meter_id == "0x61c5f4683169ab47eac0bbd439919f2d8ec68dd8", month_cols] = 10 # December value

    return sub


