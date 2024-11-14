import random
spotlight_showcase = False

# to add project details
def ADD_PROJECT_DETAILS(projects):
    global spotlight_showcase
    if not spotlight_showcase:
        project_id = input("Enter Project ID: ")   # get the user input for the project id
        duplicate_id = False    # to check whether if there are duplicate project ids
        for project in projects:
            if project[0] == project_id:
                print("Same project ID cannot enter a value.")
                duplicate_id = True
                break
        if not duplicate_id:   # if there's no any duplicated ids then get the other details
            try:
                project_name = input("Enter Project Name: ")
                category = input("Enter the name of the category the project belong: ")
                team_members = input("Enter names of team members: ")
                brief_description = input("Give a brief description about the project: ")
                country = input("Enter country name: ")
                if any(not detail for detail in [project_id, project_name, category, brief_description, country]):     #check whether the user entered all the details
                    print("Please provide all the details....")
                    return

                project = [project_id, project_name, category, team_members, brief_description, country]
                projects.append(project)     # add details to the list which is created inside the function
                print("Project details added successfully.")
            except Exception as e:
                print("An error occur while adding project details. Please try again..", e)
    else:
        print("Cannot add project details after random spotlight showcase selection.")

# to delete project details
def DELETE_PROJECT_DETAILS(projects):
    global spotlight_showcase
    if not spotlight_showcase:
        try:
            project_id = input("Enter the Project ID of the project you want to delete: ") 
            updated_projects = []  #a list to 
            project_deleted = False
            for project in projects:
                if project[0] == project_id:
                    projects.remove(project)
                    print("Projects details deleted successfully.")
                    project_deleted = True
                else:
                    updated_projects.append(project)
            if not project_deleted:
                print("Project ID not found.")
            return projects[:] == updated_projects
        except Exception as e:
            print(f"An error occur while", e)
    else:
        print("Cannot delete project details after random spotlight showcase selection")


# update project details
def UPDATE_PROJECT_DETAILS(projects):
    global spotlight_showcase  # Assuming spotlight_showcase is the global variable

    if not spotlight_showcase:
        project_id = input("Enter Project ID to update: ")
        updated_projects = []
        project_updated = False
        try:
            # Iterate through projects and update the specified project
            for project in projects:
                if project[0] == project_id:
                    print("Current Details:")
                    print(project)
                    # Update project details
                    print("Enter 'name' if you want to change the name.")
                    print("Enter 'category' if you want to change the category.")
                    print("Enter 'members' if you want to change the names of the members.")
                    print("Enter 'description' if you want to change the description.")
                    print("Enter 'country' if you want to change the country name.")
                    print("Enter 'whole' if you want to change every details you have entered before.")
                    user = input("What to want to do?...").lower()
                    if user == 'name':
                        project[1] = input("Give a new Project Name: ")
                    elif user == 'category':
                        project[2] = input("Enter the new Category of the Project: ")
                    elif user == 'members':
                        project[3] = input("Enter new names of the Team Members:  ")
                    elif user == 'description':
                        project[4] = input("Give a description about the new Project: ")
                    elif user == 'country':
                        project[5] = input("Country of the newly created Project: ")
                    elif user == 'whole':
                        project[1] = input("Give a new Project Name: ")
                        project[2] = input("Enter the new Category of the Project: ")
                        project[3] = input("Enter new names of the Team Members:  ")
                        project[4] = input("Give a description about the new Project: ")
                        project[5] = input("Country of the newly created Project: ")
                    else:
                        print("Try again....")
                    print("Project details updated successfully.")
                    project_updated = True
                return updated_projects.append(project)

            # If project not found, print message
            if not project_updated:
                print("Project ID not found!")

        except Exception as e:
            print("An error occurred while updating project details.", e)
    else:
        ("Cannot update details after random selection.")


# view project details
def VIEW_PROJECT_DETAILS(projects):
    projects.sort(key=lambda x: x[0])
    for project in projects:
        print(project)


# save project details
def SAVE_PROJECT_DETAILS(projects):
    try:
        existing_project_id = set()   # set to keep track of existing project IDs
        project_categories = {}  # dictionary to store projects grouped by category
        for project in projects:
            category = project[2]
            if category not in project_categories:
                project_categories[category] = []
            project_categories[category].append(project)
        with open("project_details.txt", "w") as file:
            for category, category_projects in project_categories.items():
                file.write(f"Category: {category}\n")
                for project in category_projects:
                    project_id = project[0]
                    if project_id in existing_project_id:
                        print("It's already there....")
                        continue
                    file.write(','.join(project) + "\n")
                    existing_project_id.add(project_id)
        print("Project details saved successfully.")
    except Exception as e:
        print("An error occurred while saving project details:", e)

def RANDOM_SELECTION(file_path, projects):
    global spotlight_showcase
    try:
        points_list = []
        with open(file_path, "r") as file:
            categories = set(project[2] for project in projects)
            selected_projects = {}  # to store projects for categories
            selected_project_id = set()   #to store id in set
            for category in categories:
                category_projects = [project for project in projects if project[2] == category]
                selected_project = random.choice(category_projects)    #getting the random choice
                while selected_project[0] in selected_project_id:
                    selected_project = random.choice(category_projects)
                selected_project_id.add(selected_project[0])
                selected_projects[category] = selected_project
            for category, project in selected_projects.items():
                print(f"Category: {category}")
                print(f"Selected Project: {project}")
                print(f"Recording awards for {project[1]}:")
                total_points = 0
                for judge in range(1, 5):
                    if category in selected_projects:  # Check if category is in selected_projects
                        points = int(input(f"Judge {judge}, please enter points out of 5: "))
                        while points < 0 or points > 5:
                            print("Points should be between 0 and 5...")
                            points = int(input(f"Judge {judge}, please enter points out of 5: "))
                        total_points += points
                    else:
                        print("Invalid category selected.")
                        break
                points_list.append((total_points, project))
            points_list.sort(reverse=True)

            print("\nAward winning projects:")
            for i, (total_points, project) in enumerate(points_list[:3]):   #assing to a index for the count
                place = ""
                if i == 0:
                    place = "1st"
                elif i == 1:
                    place = "2nd"
                elif i == 2:
                    place = "3rd"
                print(f"{place} place: {project[1]} - Total Points: {total_points}")
        spotlight_showcase = True
    except FileNotFoundError:
        print("File not found.")
        spotlight_showcase = False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        spotlight_showcase = False
    except Exception as e:
        print("An error occurred:", e)
        spotlight_showcase = False


# visualize award winning projects
def VISUALIZE_AWARD_WINNING_PROJECTS(projects):
    try:
        if spotlight_showcase:
            projects.sort(key=lambda x: x[0], reverse=True)   # to get reverse versiton of results
            for i in range(3):
                print("  *", end="")
                for j in range(i):
                    print("                        *", end="")
                print()
            print(projects[0][1], '                    ', projects[0][2], '                    ',  projects[0][3])
            print(projects[0][5], '                    ', projects[1][5], '                    ',  projects[2][5])
            print("1st place                  2nd place                   3rd place")
        else:
            print("Cannot visualize before random selection.")
    except Exception as e:
        print("An error occurred while visualizing award-winning projects:", e)


def main():
    projects = []
    print("WELCOM TO 'TEXT EXPO'!!!...")
    print()
    while True:
        print("_____Select your task_____")
        print("If you want to Add details to the system enter number 1.")
        print("If you want to Delete details to the system enter number 2. (After you deleted details then enter number 5 to save it the file)")
        print("If you want to Update details to the system enter number 3. (After you updated details then enter number 5 to save it the file)")
        print("If you want to View project details enter number 4.")
        print("If you want to Save project details to a text file enter number 5. (If you want, you can save details after adding all projects details)")
        print("To get Random Selected projects from each category enter number 6.")
        print("To get Visualize representation of of winning project enter number 7.")
        print("If you want to Exit the program enter number 8.")
        print()

        task = int(input("Enter your task number: "))

        if task == 1:
            ADD_PROJECT_DETAILS(projects)
        elif task == 2:
            DELETE_PROJECT_DETAILS(projects)
        elif task == 3:
            UPDATE_PROJECT_DETAILS(projects)
        elif task == 4:
            VIEW_PROJECT_DETAILS(projects)
        elif task == 5:
            SAVE_PROJECT_DETAILS(projects)
        elif task == 6:
           RANDOM_SELECTION("project_details.txt", projects)
        elif task == 7:
            VISUALIZE_AWARD_WINNING_PROJECTS(projects)
        elif task == 8:
            print("Ohh.... you're exiting... see you again!!....")
            break
        else:
            print("Please Try again..... Invalid response.")


main()
