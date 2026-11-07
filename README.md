# Pwn Setup

This repo is my simple setup for pwn challenges. It keeps the common tools I use in one place: pwntools, tmux, and some quick scripts for exploitation.

## What is inside

- `scripts/template.py` - basic pwntools template
- `scripts/heap_template.py` - heap challenge template
- `scripts/fstring_leak_flag.py` - example format string leak script
- `scripts/fuzz.py` - quick format string fuzzing
- `tmux/.tmux.conf` - tmux config for split panes
- `gdb/` - place for GDB helpers
- `pwntools/` - place for pwntools-related files

## Setup

Install the main tools:

```bash
sudo apt update
sudo apt install -y python3 python3-pip tmux gdb
python3 -m pip install --upgrade pip
python3 -m pip install pwntools
```

For debugging, I usually use pwndbg:

```bash
git clone https://github.com/pwndbg/pwndbg ~/pwndbg
cd ~/pwndbg
./setup.sh
```

## Tmux config

Copy the tmux config:

```bash
cp tmux/.tmux.conf ~/.tmux.conf
```

Then run:

```bash
tmux
source-file ~/.tmux.conf
```

## How I use it

- Start with `scripts/template.py` for normal binary exploitation
- Use `scripts/heap_template.py` for heap challenges
- Use the format string scripts when needed
- Run the exploit locally first, then test on remote targets

## Simple workflow

1. Run the binary
2. Check protections
3. Use pwntools to interact with it
4. Use GDB/pwndbg to inspect memory
5. Write the exploit in a script
6. Test and repeat

This repo is meant to be lightweight and easy to reuse for CTF pwn work.
