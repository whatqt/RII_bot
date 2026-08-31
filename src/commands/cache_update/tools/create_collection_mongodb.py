from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError



connection = MongoClient("localhost", 27017)
tgbot = connection["tgbot"]
schedules = [
    # 1 курс
    "schedule_1041",
    "schedule_1042",
    "schedule_1051",
    "schedule_1050",
    "schedule_1045",
    "schedule_1046",
    "schedule_1049",
    "schedule_1047",
    "schedule_1048",
    # 2 курс
    "schedule_1027",
    "schedule_1039",
    "schedule_1035",
    "schedule_1038",
    "schedule_1028",
    "schedule_1029",
    "schedule_1032",
    "schedule_1030",
    "schedule_1031",
    "schedule_1036",
    "schedule_1037",
    # 3 курс
    "schedule_1016",
    "schedule_1020",
    "schedule_1021",
    "schedule_1017",
    "schedule_1018",
    "schedule_1025",
    "schedule_1019",
    "schedule_1024",
    # 4 курс
    "schedule_1004",
    "schedule_1008",
    "schedule_1014",
    "schedule_1005",
    "schedule_1006",
    "schedule_1007",
]

dict_schedule = {
    "monday_one": [],
    "tuesday_one": [],
    "wednesday_one": [],
    "thursday_one": [],
    "friday_one": [],
    "saturday_one": [],
    "monday_two": [],
    "tuesday_two": [],
    "wednesday_two": [],
    "thursday_two": [],
    "friday_two": [],
    "saturday_two": [],
    "exams": {}
}

for schedule in schedules:
    # tgbot.create_collection(
    #     schedule
    # )
    try:
        current_schedule = tgbot[schedule]
        dict_schedule["_id"] = schedule
        current_schedule.insert_one(dict_schedule)
        print(f"{schedule} был создан")
    except DuplicateKeyError: 
        print(f"{schedule} уже был создан")
        continue