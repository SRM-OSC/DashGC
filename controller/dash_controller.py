import dash_controller_server as dash_cs


def main():
    ''' Test the DASH Controller '''

    dash_control = dash_cs.DashControlServer(('127.0.0.1', 5555))
    dash_control.configure_controller()
    dash_control.wait_for_detector()
    dash_control.trigger_actions()
    dash_control.shutdown_controller()


if __name__ == '__main__':
    main()
