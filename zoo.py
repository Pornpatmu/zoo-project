#               code เริ่มต้น
# class Zoo: 
#     def get_ticket_price(self, age):
#         if 0 < age <= 12:
#             return 50
#         elif 13 <= age < 20:
#             return 100
#         elif 21 < age <= 60:
#             return 150
#         elif age >= 60:
#             return 100
        
class Zoo:
    def get_ticket_price(self, age):
         if age < 0:
            return 'error'
         if 0 <= age <= 12:
            return 50
         elif 13 <= age <= 20:
            return 100
         elif 21 <= age <= 60:
            return 150
         elif age >= 60:
            return 100