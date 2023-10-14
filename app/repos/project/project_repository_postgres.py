from app.models import Project, User
from app.repos.project.project_repository_interface import IProjectRepository


class ProjectRepositoryPostgres(IProjectRepository):

        def get_project(self, project_id: int):
            return Project.objects.get(project_id=project_id)

        def update_project(self, project):
            project_updated = Project.objects.filter(project_id=project['project_id'])
            project_updated.update(**project)
            return project_updated

        def __init__(self):
            pass

        def create_project(self, project):
            professors = User.objects.filter(user_id__in=project['professors'])

            project_created = Project.objects.create(
                title=project['title'],
                qualification=project['qualification'],
                code=project['code'],
                shift=project['shift'],
                stand_number=project['stand_number'],
                is_entrepreneurship=project['is_entrepreneurship']
            )

            project_created.professors.set(professors)

            if 'students' in project:
                students = User.objects.filter(user_id__in=project['students'])
                project_created.students.set(students)
                project_created.save()

            return project_created
