cat > week1/day1/B1/terminal_basics.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

echo "== Bash Practice =="
echo "1) Print working dir"; pwd
echo "2) Create playground"; mkdir -p ./playground/assets; ls -la
echo "3) Create files"; touch playground/notas.txt playground/tareas.md playground/data.csv
echo "4) Append text"; echo "Hello from Day1" >> playground/notas.txt
echo "5) Show file"; cat playground/notas.txt
echo "6) Copy & move"; cp playground/tareas.md playground/assets/; mv playground/data.csv playground/assets/
echo "7) Find files"; find playground -name "*.md"
echo "8) Grep text"; grep -n "Hello" -R playground || true
echo "9) Safe delete (confirm)"; rm -i playground/notas.txt || true
echo "Done!"
EOF
chmod +x week1/day1/B1/terminal_basics.sh
