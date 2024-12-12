#!/bin/bash

# Funktion, um die aktuelle Zahl zu bestimmen
get_number() {
    if [ -n "$1" ]; then
        echo "$1"
    else
        read -p "Bitte gib eine Zahl zwischen 1 und 24 ein (Standard: heutiger Tag): " input
        if [[ -z "$input" ]]; then
            echo "$(date +%d)" # Standard: aktueller Tag
        else
            echo "$input"
        fi
    fi
}

# Zahl bestimmen
number=$(get_number "$1")

# Überprüfen, ob die Eingabe eine gültige Zahl ist
if ! [[ "$number" =~ ^[0-9]+$ ]] || [ "$number" -lt 1 ] || [ "$number" -gt 24 ]; then
    echo "Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 24 eingeben."
    exit 1
fi

# Zahl auf zwei Stellen formatieren (z.B. 6 -> 06)
formatted_number=$(printf "%02d" "$number")
day="day$formatted_number"

# Prüfen, ob der Ordner bereits existiert
if [ -d "$day" ]; then
    echo "Der Ordner '$day' existiert bereits."
    exit 1
fi

# Ordner erstellen
mkdir -p "$day"

# Leere Dateien erstellen
touch "$day/input.dat"
touch "$day/sample.dat"
touch "$day/code${formatted_number}.py"

# venv aktivieren und aocd Befehl ausführen
if [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
    if command -v aocd &> /dev/null; then
        echo "aocd wird ausgeführt..."
        year=$(date +"%Y") # Das aktuelle Jahr bestimmen

        # Input in input.dat schreiben
        aocd $formatted_number $year > "$day/input.dat"
        aocd $formatted_number $year --example > "$day/sample.dat"
        curl -s https://adventofcode.com/2024/day/$number | pandoc -f html -t markdown -o "$day/task${formatted_number}.md"

        echo "Daten erfolgreich in '$day/input.dat', '$day/task${formatted_number}.md' und '$day/sample.dat' geschrieben."
    else
        echo "aocd ist nicht installiert oder nicht im venv verfügbar."
    fi
    deactivate
else
    echo "venv konnte nicht gefunden oder aktiviert werden."
fi

# Erfolgsmeldung mit Dateiliste
echo "Ordner '$day' mit den Dateien wurde erfolgreich erstellt:"
ls "$day"
