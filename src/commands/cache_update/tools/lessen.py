from src.logic_logs.file.logger import logger
from src.mongodb.connection import connection



def generator_weekday():
    ranges = {
        1: 'monday_one', 2: 'tuesday_one', 3: 'wednesday_one',
        4: 'thursday_one', 5: 'friday_one', 6: 'saturday_one',
        7: 'monday_two', 8: 'tuesday_two', 9: 'wednesday_two',
        10: 'thursday_two', 11: 'friday_two', 12: 'saturday_two'
    }


    mylist = range(1, 13)
    for i in mylist:
        yield ranges[i]
    
def generator_schedule():
    ranges = {
        # 1 курс (9 групп)
        1: "schedule_1041", 2: "schedule_1042", 3: "schedule_1051",
        4: "schedule_1050", 5: "schedule_1045", 6: "schedule_1046",
        7: "schedule_1049", 8: "schedule_1047", 9: "schedule_1048",
        # 2 курс (11 групп)
        10: "schedule_1027", 11: "schedule_1039", 12: "schedule_1035",
        13: "schedule_1038", 14: "schedule_1028", 15: "schedule_1029",
        16: "schedule_1032", 17: "schedule_1030", 18: "schedule_1031",
        19: "schedule_1036", 20: "schedule_1037",
        # 3 курс (8 групп)
        21: "schedule_1016", 22: "schedule_1020", 23: "schedule_1021",
        24: "schedule_1017", 25: "schedule_1018", 26: "schedule_1025",
        27: "schedule_1019", 28: "schedule_1024",
        # 4 курс (6 групп)
        29: "schedule_1004", 30: "schedule_1008", 31: "schedule_1014",
        32: "schedule_1005", 33: "schedule_1006", 34: "schedule_1007",
    }

    my_shedule = range(1, 35)

    for i in my_shedule:
        yield ranges[i]

async def record_cache_schedule(schedule: str, day_week: str, lst: list):
    global connection
    client_db = connection
    tgbot = client_db["tgbot"]
    current_schedule = tgbot[schedule]

    await current_schedule.update_one(
        {"_id": schedule},
        {"$set": {day_week: lst}}
    )

async def record_cache_exams(schedule_id: str, exams: dict, connection=connection):
    client_db = connection
    tgbot = client_db["tgbot"]
    current_schedule = tgbot[schedule_id]

    await current_schedule.update_one(
        {"_id": schedule_id},
        {"$set": {"exams": exams}}
    )