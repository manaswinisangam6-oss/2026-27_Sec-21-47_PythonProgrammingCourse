
students = [
    {
        "name": "Asha",
        "aggregate": 88,
        "subjects": [85, 90, 88],
        "attendance": 92,
        "income": 200000,
        "time": 1
    },
    {
        "name": "Ravi",
        "aggregate": 88,
        "subjects": [80, 90, 88],
        "attendance": 85,
        "income": 180000,
        "time": 2
    },
    {
        "name": "Priya",
        "aggregate": 72,
        "subjects": [70, 75, 71],
        "attendance": 90,
        "income": 150000,
        "time": 3
    },
    {
        "name": "Kiran",
        "aggregate": 82,
        "subjects": [80, 85, 81],
        "attendance": 80,
        "income": 220000,
        "time": 4
    }
]

scholarships = 2
eligible = []

for s in students:
    reasons = []

    if s["aggregate"] < 75:
        reasons.append("Aggregate below 75%")

    if min(s["subjects"]) < 60:
        reasons.append("Subject marks below 60%")

    if s["attendance"] < 75:
        reasons.append("Attendance below 75%")

    if s["income"] > 250000:
        reasons.append("Income exceeds limit")

    if reasons:
        print(s["name"], "- Ineligible:", ", ".join(reasons))
    else:
        eligible.append(s)

# Rank eligible students using tie-break rules
eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        -min(s["subjects"]),
        s["income"],
        s["time"]
    )
)

print("\nScholarship Ranking:")

for rank, s in enumerate(eligible, start=1):
    status = "Selected" if rank <= scholarships else "Waiting List"

    print(
        rank, s["name"],
        "| Aggregate:", s["aggregate"],
        "| Attendance:", s["attendance"],
        "| Income:", s["income"],
        "|", status
    )
