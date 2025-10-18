class CreateOrderTestData:

    status_success = 201
    available_colors = ["BLACK", "GREY"]
    
    def make_order_data(color_list = None):
        odrer_data = {
            "firstName": "Scooterov",
            "lastName": "Moped",
            "address": "www Leningrad, SPB dot RU",
            "metroStation": 4,
            "phone": "+7 800 555 01 23",
            "rentTime": 5,
            "deliveryDate": "2025-12-12",
            "comment": "In scooter we trust"
        }

        if isinstance(color_list, str):
            odrer_data["color"] = [color_list]
        elif isinstance(color_list, list):
            odrer_data["color"] = color_list
            
        return odrer_data
    