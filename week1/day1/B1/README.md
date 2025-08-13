# Bash básico + VS Code + Git/GitHub
cat > week1/day1/B1/README.md << 'EOF'
# Day 1 — B1: Bash basics + VS Code + Git/GitHub

## What we did
- Installed & opened **VS Code** with integrated terminal.
- Used **WSL (Ubuntu)** and basic Bash commands to navigate the filesystem.
- Created our repo **bootcamp-remote** and connected it to GitHub.
- First commits & push.

## Bash quick cheatsheet
- `pwd` → show current directory
- `ls -la` → list all files (long)
- `cd <dir>` / `cd ..` → go to dir / up one level
- `mkdir <dir>` / `mkdir -p a/b/c` → create folder(s)
- `touch file.txt` → create empty file
- `cat file.txt` → print file
- `echo "text" >> file.txt` → append text
- `cp src dst` / `mv src dst` → copy / move
- `grep -n "text" -R .` → search text recursively
- `find . -name "*.py"` → search by name
- `rm -i file` / `rm -ri dir` → delete (ask confirm / recursive)

## Git basics we used
- `git status` · `git add .` · `git commit -m "msg"` · `git push`
- Set identity (WSL):  
  `git config --global user.name "Franchutech"`  
  `git config --global user.email "francellarojasc@gmail.com"`

EOF
