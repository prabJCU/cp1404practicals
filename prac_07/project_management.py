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


def display_projects(projects):
    """Display a list of Project objects, sorted by priority"""
    # Separate incomplete and completed projects using Project helper
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]

    # Sort both lists by priority
    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def save_projects(filename, projects):
    """Save all projects to file"""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)

        for project in projects:
            start_date_str = project.start_date.strftime("%d/%m/%Y")
            print(f"{project.name}\t{start_date_str}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def main():
    """Main menu-driven program for managing projects."""
    print("Welcome to Pythonic Project Management")

    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

    print(menu)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # TODO: implement load from another file
            pass
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            # TODO: filter by date
            pass
        elif choice == "A":
            # TODO: add new project
            pass
        elif choice == "U":
            # TODO: update project
            pass
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").upper()

    save_choice = input(f"Would you like to save to {filename}? (y/n): ").lower()
    if save_choice.startswith("y"):
        # TODO: implement saving to default file
        pass

    print("Thank you for using Pythonic Project Management")


if __name__ == "__main__":
    main()
