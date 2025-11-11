"""
CP1404 Practical - Project Management
Estimated: 50 minutes
Actual:
"""

import datetime
from project import Project


def load_projects(filename):
    """Load projects from a file and return a list of Project objects"""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # skips header
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])

            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def main():
    """Test function to load and display projects."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    for project in projects:
        print(project)

if __name__ == "__main__":
    main()