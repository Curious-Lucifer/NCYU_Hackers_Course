#!/bin/sh

exec socat TCP-LISTEN:10009,fork EXEC:"timeout 120 python3 /chal/Identify/server.py"