from app.repos.project.project_repository_interface import IProjectRepository


class ProjectRepositoryMock(IProjectRepository):

        def __init__(self):
            self.projects = [
                {
                    "project_id": 1,
                    'title': "Teste",
                    'qualification': "Engenharia da Computação",
                    'code': "ECOM000",
                    'shift': "DIRUNO",
                    'stand_number': "1",
                    'is_entrepreneurship': False,
                    'professors': [1, 2, 3],
                    'students': [4, 5],
                }
            ]

        def get_project(self, project_id: int):
            for project in self.projects:
                if project['project_id'] == project_id:
                    return project
            return None

        def create_project(self, project):
            project['is_entrepreneurship'] = project.get("is_entrepreneurship", False)
            project['students'] = project.get("students", [])
            project["project_id"] = len(self.projects) + 1
            
            self.projects.append(project)
            return project

        def update_project(self, project):
            for i in range(len(self.projects)):
                if self.projects[i]['project_id'] == project['project_id']:
                    for key in project:
                        self.projects[i][key] = project[key]

                    return project
            return None
