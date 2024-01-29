from app.models import Project, User
from app.repos.project.project_repository_interface import IProjectRepository


class ProjectRepositoryPostgres(IProjectRepository):

        def __init__(self):
            pass
        
        def get_project(self, project_id: int):
            try:
                return Project.objects.get(project_id=project_id).to_dict()
            except:
                return None
            
        def get_projects_by_role(self, user_id: int):
            student_projects = []
            try:
                student_projects = Project.objects.filter(students__user_id=user_id)
            except: pass
            if len(student_projects) > 0:
                return [project.to_dict() for project in student_projects]    

            professor_projects = []
            try:
                professor_projects = Project.objects.filter(professors__user_id=user_id)
            except: pass
            if len(professor_projects) > 0:
                return [project.to_dict() for project in professor_projects]
            
            return []
                


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

            return project_to_update.to_dict()

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

            return project_created.to_dict()
