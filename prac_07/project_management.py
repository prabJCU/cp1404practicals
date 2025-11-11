"""
CP1404 Practical - Project Management
Estimated: 50 minutes
Actual:
"""

import datetime
from project import Project


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
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
    """Display a list of Project objects, sorted by priority."""
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
    """Save all projects to file."""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)

        for project in projects:
            start_date_str = project.start_date.strftime("%d/%m/%Y")
            print(f"{project.name}\t{start_date_str}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def add_new_project(projects):
    """Prompt the user for project details and add a new project to the list."""
    print("Let's add a new project")

    name = input("Name: ").strip()

    start_date_str = input("Start date (dd/mm/yyyy): ").strip()
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()

    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

    print(f"{new_project.name} ({new_project.start_date.strftime('%d/%m/%Y')}) added.")


def update_project(projects):
    """Allow the user to select a project and update its completion percentage or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        project_choice = int(input("Project choice: "))
        project = projects[project_choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    print(project)

    new_percentage = input("New Percentage (leave blank to skip): ")
    if new_percentage.strip() != "":
        try:
            project.completion_percentage = int(new_percentage)
        except ValueError:
            print("Invalid input. Skipping percentage update.")

    new_priority = input("New Priority (leave blank to skip): ")
    if new_priority.strip() != "":
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid input. Skipping priority update.")

    print("Project updated successfully!")


def filter_projects_by_date(projects):
    """Display projects that start after a given date, sorted by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ").strip()

    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    filtered_projects = [p for p in projects if p.start_date >= filter_date]

    filtered_projects.sort(key=lambda p: p.start_date)

    for project in filtered_projects:
        print(project)


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
            filename = input("Filename to load from: ").strip()
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print("File not found.")
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
            pass
        elif choice == "A":
            add_new_project(projects)
            pass
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").upper()

    save_choice = input(f"Would you like to save to {filename}? (y/n): ").lower()
    if save_choice.startswith("y"):
        save_projects("projects.txt", projects)
        print("Projects saved successfully to projects.txt.")

    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
