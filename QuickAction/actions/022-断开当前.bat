cd E:\python\pkuipgw\
color f0
mode con lines=10 cols=37
python pkuipgw.py -c pkuipgwrc disconnect
@echo off
ping 127.0.0.1 -n 10 > nul