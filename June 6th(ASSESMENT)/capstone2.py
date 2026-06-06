#python capstone project

import csv
import numpy as np
import pandas as pd
from collections import defaultdict, Counter

FILE_NAME = "players.csv"

players = []

# TASK 1, 25, 26, 27

try:
    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            try:
                row["matches"] = int(row["matches"])
                row["runs"] = int(row["runs"])
                row["fours"] = int(row["fours"])
                row["sixes"] = int(row["sixes"])

                players.append(row)

            except ValueError:
                print("Invalid numeric value found:", row)

except FileNotFoundError:
    print("players.csv file not found")
    exit()

# TASK 2

print("\n===== ALL PLAYER RECORDS =====")

for player in players:
    print(player)

# TASK 3

print("\nTotal Players:", len(players))

# TASK 4
highest_scorer = max(players, key=lambda x: x["runs"])

print("\nHighest Scorer:")
print(highest_scorer["player_name"], highest_scorer["runs"])

# TASK 5
lowest_scorer = min(players, key=lambda x: x["runs"])

print("\nLowest Scorer:")
print(lowest_scorer["player_name"], lowest_scorer["runs"])

# TASK 6
average_runs = sum(player["runs"] for player in players) / len(players)

print("\nAverage Runs:", average_runs)

# TASK 7

print("\nPlayers Scoring More Than 600 Runs")

for player in players:
    if player["runs"] > 600:
        print(player["player_name"], player["runs"])

# TASK 8
print("\nPlayers Scoring Less Than 500 Runs")

for player in players:
    if player["runs"] < 500:
        print(player["player_name"], player["runs"])

# TASK 9
team_count = Counter(player["team"] for player in players)

print("\nPlayers By Team")
print(dict(team_count))


# TASK 10

team_runs = defaultdict(int)

for player in players:
    team_runs[player["team"]] += player["runs"]

print("\nTeam Wise Runs")
print(dict(team_runs))

# TASK 11

best_team = max(team_runs, key=team_runs.get)

print("\nBest Team:", best_team)
print("Runs:", team_runs[best_team])

# TASK 12

worst_team = min(team_runs, key=team_runs.get)

print("\nLowest Team:", worst_team)
print("Runs:", team_runs[worst_team])

# TASK 13
most_fours = max(players, key=lambda x: x["fours"])

print("\nMost Fours:")
print(most_fours["player_name"], most_fours["fours"])

# TASK 14

most_sixes = max(players, key=lambda x: x["sixes"])

print("\nMost Sixes:")
print(most_sixes["player_name"], most_sixes["sixes"])


# TASK 15

total_fours = sum(player["fours"] for player in players)

print("\nTotal Fours:", total_fours)

# TASK 16

total_sixes = sum(player["sixes"] for player in players)

print("Total Sixes:", total_sixes)

# TASK 17

player_names = sorted([player["player_name"] for player in players])

print("\nPlayer Names Sorted")
print(player_names)


# TASK 18

teams = set(player["team"] for player in players)

print("\nUnique Teams")
print(teams)

# TASK 19
team_runs_dict = dict(team_runs)

print("\nTeam Runs Dictionary")
print(team_runs_dict)


# TASK 20

player_runs_dict = {}

for player in players:
    player_runs_dict[player["player_name"]] = player["runs"]

print("\nPlayer Runs Dictionary")
print(player_runs_dict)

# TASK 21

def find_top_scorer():
    return max(players, key=lambda x: x["runs"])

# TASK 22

def calculate_average_runs():
    return sum(player["runs"] for player in players) / len(players)

# TASK 23

def find_best_team():
    return max(team_runs, key=team_runs.get)


# TASK 24

def find_total_boundaries():
    return total_fours + total_sixes

print("\n===== FUNCTION OUTPUTS =====")
print("Top Scorer:", find_top_scorer()["player_name"])
print("Average Runs:", calculate_average_runs())
print("Best Team:", find_best_team())
print("Total Boundaries:", find_total_boundaries())

# TASK 28

runs_array = np.array([player["runs"] for player in players])

print("\n===== NUMPY ANALYSIS =====")

print("Total Runs:", np.sum(runs_array))
print("Average Runs:", np.mean(runs_array))
print("Maximum Runs:", np.max(runs_array))
print("Minimum Runs:", np.min(runs_array))
print("Standard Deviation:", np.std(runs_array))
print("Median:", np.median(runs_array))

# TASK 29

df = pd.read_csv(FILE_NAME)

# ==========================================
# TASK 30
# Top 5 Run Scorers
# ==========================================

print("\nTop 5 Run Scorers")
print(df.nlargest(5, "runs"))

# TASK 31

print("\nPlayers Sorted By Runs")
print(df.sort_values("runs", ascending=False))


# TASK 32
print("\nTeam Total Runs")
print(df.groupby("team")["runs"].sum())

# TASK 33

print("\nTeam Average Runs")
print(df.groupby("team")["runs"].mean())

# TASK 34
print("\nPlayers Above 600 Runs")
print(df[df["runs"] > 600])

# TASK 35

top_team = df.groupby("team")["runs"].sum().idxmax()

print("\nTop Team:", top_team)

# REPORT GENERATION

with open("cricket_report.txt", "w") as report:

    report.write("CRICKET ANALYTICS REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Total Players : {len(players)}\n")
    report.write(f"Total Runs : {sum(player['runs'] for player in players)}\n")
    report.write(f"Average Runs : {average_runs}\n\n")

    report.write(
        f"Highest Scorer : {highest_scorer['player_name']} ({highest_scorer['runs']})\n"
    )

    report.write(
        f"Lowest Scorer : {lowest_scorer['player_name']} ({lowest_scorer['runs']})\n\n"
    )

    report.write("Team Wise Runs\n")
    report.write(str(dict(team_runs)))
    report.write("\n\n")

    report.write("Top 5 Players\n")
    report.write(str(df.nlargest(5, "runs")))
    report.write("\n\n")

    report.write(
        f"Most Fours : {most_fours['player_name']} ({most_fours['fours']})\n"
    )

    report.write(
        f"Most Sixes : {most_sixes['player_name']} ({most_sixes['sixes']})\n"
    )

print("\ncricket_report.txt Generated Successfully")

# TASK 36

top_players = df[df["runs"] > 600]

top_players.to_csv("top_players.csv", index=False)

print("top_players.csv Generated")

# TASK 37
team_summary = df.groupby("team").agg(
    Total_Runs=("runs", "sum"),
    Average_Runs=("runs", "mean"),
    Player_Count=("player_id", "count")
)

team_summary.to_csv("team_summary.csv")

print("team_summary.csv Generated")

# TASK 38


while True:

    print("\n===== CRICKET ANALYTICS MENU =====")
    print("1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        print("\nHighest Scorer:", highest_scorer["player_name"])
        print("Average Runs:", average_runs)

    elif choice == "2":

        print("\nTeam Wise Runs")
        print(dict(team_runs))

    elif choice == "3":

        print("\nTotal Fours:", total_fours)
        print("Total Sixes:", total_sixes)

    elif choice == "4":

        print("\nReports Generated:")
        print("1. cricket_report.txt")
        print("2. top_players.csv")
        print("3. team_summary.csv")

    elif choice == "5":

        print("Thank You")
        break

    else:

        print("Invalid Choice")
