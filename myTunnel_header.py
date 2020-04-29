
from scapy.all import *
import sys, os

TYPE_MYTUNNEL = 0x1212
TYPE_IPV4 = 0x0800

class MyTunnel(Packet):
    name = "MyTunnel"
    fields_desc = [
        ShortField("pid", 0),
        ShortField("dst_id", 0),
        ShortField("flag_1", 0),
        ShortField("flag_2", 0),
        ShortField("flag_3", 0),
        IntField("flag_4",0)
        
    ]
    def mysummary(self):
        return self.sprintf("pid=%pid%, dst_id=%dst_id%, flag_1=%flag_1%, flag_2=%flag_2%, flag_3=%flag_3%,flag_4=%flag_4%")


bind_layers(Ether, MyTunnel, type=TYPE_MYTUNNEL)
bind_layers(MyTunnel, IP, pid=TYPE_IPV4)

