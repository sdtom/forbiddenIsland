from mpf.core.mode import Mode


class Turret(Mode):

    def mode_init(self):
        print("My custom mode code is being initialized")

    def mode_start(self, **kwargs):
        # The mode_start method needs **kwargs because some events that
        # start modes pass additional parameters

        print("My custom mode code is starting")

        self.add_mode_event_handler('stepper_center_turret_ready', self.ejectTheBall)


    def my_callback(self):
        print("My delayed call was just called!")

    def ejectTheBall(self, **kwargs):
        del kwargs
        print("Ejecting..")
        self.machine.ball_devices.bd_trough.eject()
        self.add_mode_event_handler('stepper_center_turret_ready', self.ejectTheBall)
        
    def mode_stop(self, **kwargs):
        # The mode_stop method needs **kwargs because some events that
        # stop modes pass additional parameters

        print("My custom mode code is stopping")