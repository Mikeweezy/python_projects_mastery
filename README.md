# 🐍 Python Daily Journey

> **One project a day — from `print("hello world")` to shipping real software.**
> 180+ days · 4 phases · built daily with an AI pair programmer (Cline).

Live repo: **https://github.com/Mikeweezy/python_projects_mastery**

## 🎯 The rules

1. **Show up daily** — 20 focused minutes beats 3 frantic hours on Sunday.
2. **Code before you peek** — attempt `starter.py` *before* opening `solution.py`.
3. **Commit every day** — one day = one commit = one green square.
4. **Write it down** — 2 minutes in the day's `notes.md` cements what you learned.
5. **Review every 7th day** — refactor an old project with what you now know.

## 🗺️ Repository structure

```text
python_projects_mastery/
├── 01-beginner/        # Days 1–30   → syntax, logic, files, small games
├── 02-intermediate/    # Days 31–75  → OOP, APIs, packages, GUI, databases
├── 03-advanced/        # Days 76–120 → async, web frameworks, data, Docker
├── 04-pro/             # Days 121+   → full-stack, deployment, CI/CD, ML
├── templates/          # README / starter / notes templates for each new day
├── scripts/            # helper: new_day.py scaffolds the next day's folder
├── .github/workflows/  # tiny CI that syntax-checks every Python file
├── CURRICULUM.md       # the full day-by-day roadmap
└── PROGRESS.md         # the tracker — tick a box every day 📈
```

Each day folder looks like:

```text
day-01-hello-python/
├── README.md     # the mission: goal, requirements, hints, bonus
├── starter.py    # your canvas — TODOs guide you
├── solution.py   # only after you've tried!
└── notes.md      # what you learned / what tripped you up
```

## 📈 The four phases

| Phase | Days | You learn | Flagship projects |
|---|---|---|---|
| 🟢 **01 Beginner** | 1–30 | syntax · loops · functions · files · logic | number guessing, Hangman, quiz game, budget tracker |
| 🟡 **02 Intermediate** | 31–75 | OOP · APIs · pip/venv · testing · SQLite · GUI | weather CLI, web scraper, habit tracker, Tkinter apps |
| 🟠 **03 Advanced** | 76–120 | async · FastAPI · pandas · Docker · patterns | REST API, data dashboard, automation bots |
| 🔴 **04 Pro** | 121+ | full-stack · deploy · CI/CD · packaging · ML | SaaS-style capstone, published PyPI package |

➡️ Full plan: **[CURRICULUM.md](CURRICULUM.md)** — Progress: **[PROGRESS.md](PROGRESS.md)**

## 🔁 The daily loop (~45–60 min)

1. Open today's folder and read its `README.md`.
2. Code your attempt in `starter.py` (or from scratch — your call).
3. Compare with `solution.py`; steal ideas, note differences.
4. Fill `notes.md` and tick the box in `PROGRESS.md`.
5. Commit & push:

```bash
git add .
git commit -m "Day 4: number guessing game 🎯"
git push
```

## ▶️ Running a project

Python **3.10+** recommended. Early days use only the standard library:

```bash
python "01-beginner/day-01-hello-python/starter.py"
```

Third-party libraries appear in Phase 2+ (`pip install -r requirements.txt`).

## 🤖 Working with Cline (your AI pair programmer)

Start a chat each day and say:

- *"Scaffold Day 12 from the curriculum"* → creates the folder from `templates/`
- *"I'm stuck on TODO 3 in day 12"* → we debug together
- *"Review my day-12 solution"* → code review + refactor tips
- *"Update PROGRESS.md for day 12"* → tracker + commit

## 🚀 Connected to GitHub ✅

Remote `origin` → `https://github.com/Mikeweezy/python_projects_mastery.git`

```bash
git push          # after every daily commit
```

---
**Start here → [`01-beginner/day-01-hello-python/`](01-beginner/day-01-hello-python)** 🚀
