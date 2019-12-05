import configurations.youtube as yt
import configurations.netflix as nf
import configurations.amazon_prime as ap

class DashCircuitBoard:
    ''' Configure gestures to '''

    def __init__(self):
        self.config_name = 'init'
        self.config_class = None
        self.config_obj = None
        self.context_pool = ['init']
        self.init_config = { "1": "youtube",
            "2": "netflix",
            "3": "amazon_prime"
        }
        self.class_map = { "youtube": yt.YouTube,
            "netflix": nf.Netflix,
            "amazon_prime": ap.AmazonPrimeVideo
        }

    def load_configuration(self, config_name):
        ''' Load a new configuration '''

        self.config_name = config_name
        self.config_class = self.class_map[config_name]
        self.config_obj = self.config_class()
        if self.context_pool[-1] != config_name:
            self.context_pool.append(config_name)

    def remove_configuration(self):
        ''' Remove the current configuration '''

        # remove current service class
        tmp = self.config_class
        self.config_class = None
        del tmp

        # remove current service object
        tmp = self.config_obj
        self.config_obj = None
        del tmp

        # remove the service from context pool
        self.context_pool.pop()

    def perform_actions(self, gesture_code):
        ''' Perform action '''

        if self.config_name == 'init':
            self.load_configuration(self.init_config[gesture_code])
            self.config_obj.execute_command_for_gesture("1")
        else:
            resp = self.config_obj.execute_command_for_gesture(gesture_code)
            if resp == 0:
                self.remove_configuration()
                if len(self.context_pool) > 1:
                    self.load_configuration(self.context_pool[-1])
                else:
                    self.config_name = 'init'
            elif resp == -1:
                print(f'Something bad happened with {self.config_name}')
            elif resp == 1:
                print(f"Good control over {self.config_name}")
            else:
                print("Uh Oh!!! This shouldn't happen")
