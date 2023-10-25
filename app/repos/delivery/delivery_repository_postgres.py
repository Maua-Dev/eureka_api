from app.models import Project, User, Task, Delivery
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository


class DeliveryRepositoryPostgres(IDeliveryRepository):


    def __init__(self):
        pass

    def create_delivery(self, delivery):
        try:
            project_set = Project.objects.get(project_id=delivery['project_id'])
            user_set = User.objects.get(user_id=delivery['user_id'])
            task_set = Task.objects.get(task_id=delivery['task_id'])
        except:
            return None

        if not project_set or not user_set or not task_set:
            return None

        user = user_set.to_dict()
        project = project_set.to_dict()
        task = task_set.to_dict()

        if task['responsible'] == 'ADVISOR' and user['role'] != 'ADVISOR':
            return None
        if task['responsible'] == 'RESPONSIBLE' and user['role'] != 'RESPONSIBLE':
            return None

        students_id = [student['user_id'] for student in project['students']]
        if user['role'] == 'STUDENT' and user['user_id'] not in students_id:
            return None

        professors_id = [professor['user_id'] for professor in project['professors']]
        if user['role'] == 'PROFESSOR' and user['user_id'] not in professors_id:
            return None

        delivery = Delivery.objects.create(
            task=task_set,
            project=project_set,
            user=user_set,
            content=delivery['content']
        )
        delivery.save()

        delivery_dict = delivery.to_dict()

        return delivery_dict


    def get_delivery(self, delivery_id):
        try:
            delivery_set = Delivery.objects.get(delivery_id=delivery_id)
        except:
            return None

        if not delivery_set:
            return None

        delivery_dict = delivery_set.to_dict()

        return delivery_dict

    def get_deliveries(self, project_id):
        try:
            deliveries_set = Delivery.objects.filter(project_id=project_id)
        except:
            return None

        if not deliveries_set:
            return None

        deliveries = [delivery.to_dict() for delivery in deliveries_set]

        return deliveries

