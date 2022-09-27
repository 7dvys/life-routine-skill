from mycroft import MycroftSkill, intent_file_handler


class LifeRoutine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('routine.life.intent')
    def handle_routine_life(self, message):
        self.speak_dialog('routine.life')


def create_skill():
    return LifeRoutine()

