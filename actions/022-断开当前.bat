set /p dir=<actions/ipgw/var/dir.txt
set /p disk=<actions/ipgw/var/disk.txt
%disk%
cd %dir%
color f0
mode con lines=8 cols=37
python pkuipgw.py -c pkuipgwrc disconnect
@echo off
ping 127.0.0.1 -n 10 > nul