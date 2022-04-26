#!/usr/bin/python
def hexa(bin):
    decimal,hexa=0,0
    decimal=int(bin,2)
    hexa='{:#x}'.format(decimal)
    print(f"hexa number:{hexa}")
