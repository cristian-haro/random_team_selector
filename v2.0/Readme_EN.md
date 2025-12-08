# Random Team Selector

## Overview

This project is a tool for randomly selecting football teams from an Excel file. The system filters teams marked as eligible and selects one at random as the winner.

**Available in two versions:**
- **Python Version**: Executable script using Python
- **Executable Version**: Ready-to-use .exe application (no dependencies required)

## Project Structure

### Python Version
```
random_team_selector/
│
├── equipos.xlsx         # Excel file with team database
├── app.py               # Main script (Python)
├── requirements.txt     # Project dependencies
└── README.md           # This documentation
```

### Executable Version
```
random_team_selector/
│
├── app.exe              # Main executable application (Windows)
├── equipos.xlsx         # Excel file with team database
└── README.md           # This documentation
```

## Excel File Structure (`equipos.xlsx`)

The Excel file contains the following columns:

| Column | Description | Example |
|---------|-------------|---------|
| **Pais** | Team country | Spain, England, Italy |
| **Liga** | Competing league | Premier League, La Liga, Serie A |
| **Equipo** | Team name | Real Madrid, Arsenal, Juventus |
| **Elegible** | Eligibility mark | `x` (yes) or empty (no) |

### Data Example

```excel
| Pais      | Liga        | Equipo        | Elegible |
|-----------|-------------|---------------|----------|
| Spain     | La Liga     | Barcelona     | x        |
| England   | Premier L.  | Arsenal       |          |
| Italy     | Serie A     | Juventus      | x        |
```

**Valid eligibility marks:**
- `x` or `X` → Team eligible for selection
- `si` or `sí` (case-insensitive) → Also valid
- **Any other value or empty** → Team **not eligible**

---

# 🚀 EXECUTABLE VERSION (.exe)

### Features
- **No Python installation required**
- **No additional dependencies needed**
- **Double-click execution**
- **Compatible with Windows 10/11**
- **Everything works locally, no internet required**

### Quick Installation

1. **Download** the exe folder

![Step 1.](https://raw.githubusercontent.com/cristian-haro/random_team_selector/refs/heads/main/img/Readme_1.png "Step 1")

![Step 2](https://raw.githubusercontent.com/cristian-haro/random_team_selector/refs/heads/main/img/Readme_2.png "Step 2")

2. **Configure your Excel**:
   - Open `equipos.xlsx`
   - Mark eligible teams with `x`
   - Save changes

3. **Run** by double-clicking `app.exe`

### ⚠️ Security Note (Windows)

It's normal for Windows Defender to show a warning. This happens with compiled Python applications. To run it:

1. Click "More info"
2. Select "Run anyway"
3. The application is 100% safe and contains no malware

### Using the Executable

1. **Prepare your Excel** with eligible teams marked with `x`
2. **Run** `app.exe`
3. **See the result** immediately:

```
==============================
🎲 DRAW RESULT 🎲
==============================
🏆 TEAM:  Atlético
🌍 LEAGUE:    La Liga
==============================

Press Enter to exit...
```

4. **Press Enter** to close the window

---

# PYTHON VERSION

## Main Script: `app.py`

### Features

1. **Data reading**: Reads the Excel file `equipos.xlsx`
2. **Validation**: Verifies file and required columns exist
3. **Data cleaning**: Normalizes the "Elegible" column to avoid errors
4. **Filtering**: Selects only teams marked as eligible
5. **Random selection**: Chooses a winning team at random from eligible ones
6. **Presentation**: Displays results clearly and attractively

## Installation and Configuration

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or copy files** to a local folder
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install pandas openpyxl
   ```

### Dependencies (`requirements.txt`)

- **pandas** (>=1.3.0): For tabular data manipulation
- **openpyxl** (>=3.0.0): For Excel file reading/writing

## Usage

### Basic Execution

1. Ensure `equipos.xlsx` is in the same folder as the script
2. Mark teams you want to participate with `x`
3. Run the script:
   ```bash
   python app.py
   ```
4. The result will display in the console

### Expected Output

```
==============================
🎲 DRAW RESULT 🎲
==============================
🏆 TEAM:  Atlético
🌍 LEAGUE:    La Liga
==============================
```

---

# Troubleshooting

## Common Issues

| Problem | Solution |
|----------|----------|
| **"Windows protected your PC"** | Click "More info" → "Run anyway" |
| **"equipos.xlsx not found"** | Ensure Excel is in the same folder |
| **"No eligible teams"** | Mark at least one team with `x` in Excel |
| **Error opening Excel** | Close Excel before running the program |
| **Always same result** | Verify you have multiple teams marked with `x` |

## For Python Version

If `app.py` doesn't work:
1. Verify Python is installed: `python --version`
2. Install dependencies: `pip install pandas openpyxl`
3. Ensure you're in the correct folder

---

# Customization

## Modifying Team List

1. Open `equipos.xlsx`
2. Edit, add, or remove teams
3. Mark with `x` those you want to be eligible
4. Save changes

## Using for Other Purposes

The tool is flexible and can be used for:
- Gift draws
- Random participant selection
- Team assignments in games
- Any list requiring random selection

Just maintain the column structure:
- **Pais/Liga**: Categories (can be anything)
- **Equipo**: Items to draw
- **Elegible**: Which items are available

---

# Support and Contributions

## Reporting Issues
1. Verify you followed the steps correctly
2. Ensure files are in the same folder
3. If problem persists, contact me

## Improvement Suggestions
Contributions are welcome.

---

**Version**: 1.1.0  
**Last updated**: December 2025  
**Compatibility**: Windows 10/11, Python 3.7+