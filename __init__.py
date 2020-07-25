from mycroft import MycroftSkill, intent_file_handler


class SchoolTimetable(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('timetable.school.intent')
    def handle_timetable_school(self, message):
        self.speak_dialog('timetable.school')


def create_skill():
    return SchoolTimetable()

