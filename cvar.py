# MIT License

# Copyright (c) 2018 nrajasin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


global instance
instance=1
global localdat
localdat={}


global tcp_frame_length
tcp_frame_length=0
global tcp_ip_length
tcp_ip_length=0
global tcp_length
tcp_length=0

global udp_frame_length
udp_frame_length=0
global udp_ip_length
udp_ip_length=0
global udp_length
udp_length=0

global arp_frame_length
arp_frame_length=0

global src_length
src_length=0

global dst_length
dst_length=0


global ssl
ssl=0
global http
http=0
global ftp
ftp=0
global ssh
ssh=0
global dns
dns=0
global smtp
smtp=0
global dhcp
dhcp=0

global tcp
tcp=0
global udp
udp=0
global arp
arp=0

global IDs
IDs=[]


global ports
ports=[]

global tot_pack
tot_pack=0