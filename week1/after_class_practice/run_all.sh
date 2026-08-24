#!/usr/bin/env bash

set -u

BASE_DIR=$(cd "$(dirname "$0")" && pwd)
RUN_ROOT="$BASE_DIR/runs"
LOG_ROOT="$BASE_DIR/logs"
mkdir -p "$RUN_ROOT" "$LOG_ROOT"

# Exercise 1: verify the current shell.
{
  echo '$ echo "$SHELL"'
  echo "$SHELL"
  echo '$ bash --version | head -n 1'
  bash --version | head -n 1
} > "$LOG_ROOT/ex01.log" 2>&1

# Exercise 2: inspect long-format permissions.
{
  echo '$ ls -l /'
  ls -l /
  echo '$ ls -ld / /tmp /usr/bin/bash'
  ls -ld / /tmp /usr/bin/bash
} > "$LOG_ROOT/ex02.log" 2>&1

# Exercise 3: test glob patterns.
EX03="$RUN_ROOT/ex03"
mkdir -p "$EX03"
cd "$EX03"
touch a.txt b.txt c.txt file1.txt file2.txt fileA.txt file10.txt note.md
{
  echo '$ ls *.txt'
  ls *.txt
  echo '$ ls file?.txt'
  ls file?.txt
  echo '$ ls {a,b,c}.txt'
  ls {a,b,c}.txt
} > "$LOG_ROOT/ex03.log" 2>&1

# Exercise 4: compare three quoting forms.
{
  echo '$ printf with single quotes'
  printf '%s\n' 'price=$5 ! \n'
  echo '$ printf with double quotes and escapes'
  printf "price=\$5 ! \\n\n"
  echo '$ printf with ANSI-C quotes'
  printf $'price=$5 !\nsecond line\n'
} > "$LOG_ROOT/ex04.log" 2>&1

# Exercise 5: redirect stdout and stderr separately and together.
EX05="$RUN_ROOT/ex05"
mkdir -p "$EX05"
cd "$EX05"
{
  echo '$ ls /nonexistent /tmp > stdout.txt 2> stderr.txt'
  ls /nonexistent /tmp > stdout.txt 2> stderr.txt
  echo '$ head -n 8 stdout.txt'
  head -n 8 stdout.txt
  echo '$ cat stderr.txt'
  cat stderr.txt
  echo '$ ls /nonexistent /tmp > both.txt 2>&1'
  ls /nonexistent /tmp > both.txt 2>&1
  echo '$ head -n 10 both.txt'
  head -n 10 both.txt
} > "$LOG_ROOT/ex05.log" 2>&1

# Exercise 6: use exit status and conditional execution.
EX06="$RUN_ROOT/ex06"
mkdir -p "$EX06"
cd "$EX06"
target="mydir_25020007193_$$"
{
  echo '$ false; echo $?'
  false
  echo "$?"
  echo '$ true && echo success'
  true && echo success
  echo '$ false || echo fallback'
  false || echo fallback
  echo '$ test -d "$target" || mkdir "$target"'
  test -d "$target" || mkdir "$target"
  echo '$ ls -ld "$target"'
  ls -ld "$target"
} > "$LOG_ROOT/ex06.log" 2>&1

# Exercise 7: show that cd is a shell builtin and compare a subshell.
EX07="$RUN_ROOT/ex07"
mkdir -p "$EX07/subdir"
cd "$EX07"
{
  echo '$ type cd'
  type cd
  echo '$ pwd'
  pwd
  echo '$ (cd subdir; pwd)'
  (cd subdir; pwd)
  echo '$ pwd'
  pwd
} > "$LOG_ROOT/ex07.log" 2>&1

# Exercise 8: check whether a filename argument exists.
EX08="$RUN_ROOT/ex08"
mkdir -p "$EX08"
cd "$EX08"
printf 'sample\n' > existing.txt
cat > check.sh <<'EOF'
#!/usr/bin/env bash
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <file>" >&2
  exit 2
fi
if [ -f "$1" ]; then
  echo "File exists: $1"
else
  echo "File not found: $1"
  exit 1
fi
EOF
{
  echo '$ bash check.sh existing.txt'
  bash check.sh existing.txt
  echo '$ bash check.sh missing.txt'
  bash check.sh missing.txt
  status=$?
  echo '$ echo $?'
  echo "$status"
} > "$LOG_ROOT/ex08.log" 2>&1

# Exercise 10: demonstrate set -x tracing.
EX10="$RUN_ROOT/ex10"
mkdir -p "$EX10"
cd "$EX10"
rm -f sample.txt
cat > trace.sh <<'EOF'
#!/usr/bin/env bash
set -x
name="trace-demo"
echo "hello $name"
test -f sample.txt || touch sample.txt
wc -c sample.txt
EOF
{
  echo '$ bash trace.sh'
  bash trace.sh
} > "$LOG_ROOT/ex10.log" 2>&1

# Exercise 11: create a dated backup with command substitution.
EX11="$RUN_ROOT/ex11"
mkdir -p "$EX11"
cd "$EX11"
{
  echo "$ printf 'week-1 notes\\n' > notes.txt"
  printf 'week-1 notes\n' > notes.txt
  echo '$ cp notes.txt "notes_$(date +%Y-%m-%d).txt"'
  cp notes.txt "notes_$(date +%Y-%m-%d).txt"
  echo '$ ls -l notes*.txt'
  ls -l notes*.txt
  echo '$ cmp -s notes.txt "notes_$(date +%Y-%m-%d).txt" && echo identical'
  cmp -s notes.txt "notes_$(date +%Y-%m-%d).txt" && echo identical
} > "$LOG_ROOT/ex11.log" 2>&1

printf 'Generated %s exercise logs in %s\n' "$(find "$LOG_ROOT" -type f -name 'ex*.log' | wc -l)" "$LOG_ROOT"
