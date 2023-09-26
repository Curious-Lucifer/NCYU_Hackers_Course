#!/bin/sh

socat TCP-LISTEN:10000,fork EXEC:"timeout 10 python3 /chal/Welcome/server.py" &
socat TCP-LISTEN:10001,fork EXEC:"timeout 10 python3 /chal/Nth/server.py" & 
socat TCP-LISTEN:10002,fork EXEC:"timeout 120 python3 /chal/Count/server.py" & 
socat TCP-LISTEN:10003,fork EXEC:"timeout 120 python3 /chal/Guess/server.py" & 
socat TCP-LISTEN:10004,fork EXEC:"timeout 120 python3 /chal/Calculator/server.py" & 
socat TCP-LISTEN:10005,fork EXEC:"timeout 120 python3 /chal/Alphabet/server.py" & 
socat TCP-LISTEN:10006,fork EXEC:"timeout 120 python3 /chal/PI/server.py" & 
socat TCP-LISTEN:10007,fork EXEC:"timeout 120 python3 /chal/Digit/server.py" & 
exec socat TCP-LISTEN:10008,fork EXEC:"timeout 120 python3 /chal/Hanoi/server.py"