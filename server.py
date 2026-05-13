import socket, subprocess

ip="0.0.0.0"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))

commands = {
    "pp": ["playerctl", "play-pause"],
    "pl": ["playerctl", "play"],
    "pa": ["playerctl", "pause"],
    "nt": ["playerctl", "next"],
    "pv": ["playerctl", "previous"],
    "vu": ["playerctl", "volume", "0.1+"],
    "vd": ["playerctl", "volume", "0.1-"],
    "v0": ["playerctl", "volume", "0"],
    "vm": ["playerctl", "volume", "1"],
}

def execute(cmd):
    if cmd in commands:
        subprocess.run(commands[cmd])
        return "ok"
    else: return "invalid command"

while True:
    data, addr = server.recvfrom(2)
    cmd = data.decode().strip()
    response = execute(cmd)
    server.sendto(response.encode(), addr)