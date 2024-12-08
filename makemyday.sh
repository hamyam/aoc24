#!/bin/bash

# Zahl zwischen 1 und 24 abfragen
read -p "Bitte gib eine Zahl zwischen 1 und 24 ein: " number

# Überprüfen, ob die Eingabe eine gültige Zahl ist
if ! [[ "$number" =~ ^[0-9]+$ ]] || [ "$number" -lt 1 ] || [ "$number" -gt 24 ]; then
    echo "Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 24 eingeben."
    exit 1
fi

# Zahl auf zwei Stellen formatieren (z.B. 6 -> 06)
formatted_number=$(printf "%02d" "$number")
day="day$formatted_number"

# Ordner erstellen
mkdir -p "$day"

# Leere Dateien erstellen
touch "$day/input.dat"
touch "$day/sample.dat"
touch "$day/code${formatted_number}.py"
touch "$day/task${formatted_number}.md"

echo "Ordner '$day' mit Dateien wurde erfolgreich erstellt."
