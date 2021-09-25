class Invoker():
    def invoke(self, commands):
        # if len(commands) > 1:
        #     for command in commands:
        #         command.execute()
        commands.execute()