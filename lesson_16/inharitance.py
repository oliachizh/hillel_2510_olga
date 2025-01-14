# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
#
# class Mouth(Animal):
#     animal_type = 'Mouse'
#
#     def __init__(self, name, color, paws):
#         Animal.__init__(self, name, color)
#         self.paws =paws
#         self.live_w_family = True
#
#     @staticmethod
#     def make_sound():
#         print('pi pi')
#
#     @staticmethod
#     def walk():
#         print("walking")
#
#
# class Bird(Animal):
#     animal_type = 'Bat'
#
#     def __init__(self, name, color, wings):
#         Animal.__init__(self, name, color)
#         self.wings = wings
#         self.can_fly = True
#
#     @staticmethod
#     def make_sound():
#         print('gav')
#
#     @staticmethod
#     def fly():
#         print("fly")
#
# class Bat(Mouth, Bird):
#
#     def __init__(self, name, color):
#         Mouth.__init__(self, name, color, paws=4)
#         Bird.__init__(self, name, color, wings=2)
#
#
#     def __str__(self):
#         return f"{self.name}, {self.wings}, {self.can_fly}"
#
# bat_1 = Bat("uni", "grey")
# print(bat_1.animal_type)

class Endpoint:
    get_user = 'url/{user_id}'
    get_user_details = 'url/{user_id}/details'

class RequestExecutor:
    def __init__(self, base_url = '127.0.0.0/'):
        self.base_url = base_url
        
    def send_request(self,url, **kwargs):
        print(f'Sending request with params {kwargs}')

#Bad option
# class UserCtrl(RequestExecutor, Endpoint):
#         def get_user_data(self, user_id):
#             url = self.get_user.format(user_id=user_id)
#             self.send_request(url=url, user_id=user_id)

class UserCtrl():
    def __init__(self, base_url=None):
        if base_url:
             self.executor = RequestExecutor(base_url)
        else:
            self.executor =RequestExecutor()

    def get_user_data(self, user_id):
        url = f'{self.executor.base_url}{Endpoint.get_user.format(user_id=user_id)}'
        self.executor.send_request(url=url, user_id=user_id)


UserCtrl().get_user_data(2)