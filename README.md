# 📘 ConTrack

A simple Python CLI tool to manage tasks.

---

## Features

* Create titles (categories)
* Add / delete tasks
* Mark tasks as complete (1) or not (0)
* Show all or specific titles

---

## Structure

```
project/
├── data/data.json
└── main.py
```

---

## Data Format

```json
{
  "Title": [
    {"Task": 0}
  ]
}
```

---

## Commands

**Show all:**

```
python main.py show
```

**Show specific:**

```
python main.py show -t Title1
```

**Add title/items:**

```
python main.py add Title -i Task1 Task2
```

**Delete:**

```
python main.py del Title
python main.py del Title -i Task1
```

**Mark:**

```
python main.py mark -t Title -i Task1 -as 1
```

---

## TODO

* Use argparse
* Merge duplicate functions
* Add error handling
* Add `--help`
