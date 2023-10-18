from app.models import Project, User
from app.repos.project.project_repository_interface import IProjectRepository


class ProjectRepositoryPostgres(IProjectRepository):

        def __init__(self):
            pass
        
        def get_project(self, project_id: int):
            return Project.objects.get(project_id=project_id)

        def update_project(self, project):
            project_to_update = Project.objects.get(project_id=project['project_id'])

            to_update = project

            if 'professors' in project:
                professors = User.objects.filter(user_id__in=project['professors'])
                project_to_update.professors.set(professors)
                to_update.pop('professors')


            if 'students' in project:
                students = User.objects.filter(user_id__in=project['students'])
                project_to_update.students.set(students)
                to_update.pop('students')

            for key, value in to_update.items():
                setattr(project_to_update, key, value)

            project_to_update.save()

            return project_to_update

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
