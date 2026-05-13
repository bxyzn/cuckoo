# cuckoo

A remote for music playback

I wanted a way to control music playback on my PC while I’m cleaning or just away from the desk, without needing to physically interact with it.

Most of the time I use an offline music library, so I decided to build a mobile-style remote that’s lightweight and easy to scale.

This project uses UDP over sockets in Python to control the machine.

This requires a Linux tool/software called PLAYERCTL to work.
More about Playerctl here

Right now I don’t have a proper client-side app, so I just send UDP packets manually.

Example using nc:

```
echo 'pp' | nc *ip* 9999   # replace *ip* with machine IP
```

Or open an interactive session:
```
nc *ip* 9999
```
Commands
pp = play/pause
pl = play
pa = pause
nt = next track
pv = previous track
vu = volume up
vd = volume down
v0 = volume 0
vm = volume max

For volume controls, the range is from 0.0 to 1.0.

You can add more commands by extending the commands dictionary, for example:

`"vm": ["playerctl", "volume", "1"]`

There’s a lot more you can build on top of this.

## Playerctl

Run:

```playerctl --help```

to see available options.

When adding new command blocks to the commands variable, remember that everything inside the square brackets ( *[]* ) must be inside quotes ( *""*) .

You could also define commands like p0 or pn, where n is a variable (0–9), so playback jumps to a percentage of the track (e.g. 1 = 10%, 2 = 20%, etc.).

You can also extend the code so that after a UI command it listens for longer inputs/links and streams media (using the open command from playerctl).

Media features like loop or shuffle can also be controlled via command blocks using Playerctl options like loop and shuffle.
