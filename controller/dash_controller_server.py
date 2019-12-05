import socket
import dash_circuit_board as dcb


class DashControlServer:
    """ DASH GC Controller - Triggers Actions """

    def __init__(self, proc):
        self.proc = proc
        self.sock = None    # controller socket
        self.d_sock = None  # detector socket
        self.d_proc = None  # detector process
        self.dcb_obj = dcb.DashCircuitBoard()

    def configure_controller(self):
        """ Configure the controller """

        # create a UNIX Domain Socket
        # (not available on windows so using a traditional socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.proc)

    def wait_for_detector(self):
        """ Wait for the detector to connect """

        self.sock.listen(1)
        self.d_sock, self.d_proc = self.sock.accept()

    def trigger_actions(self):
        """ Trigger actions based on requests from the detector """

        while True:

            req = self.d_sock.recv(5)

            if not req:
                self.shutdown_controller()

            self.dcb_obj.perform_actions(req.decode('utf-8'))

    def shutdown_controller(self):
        """ Shutdown the controller """

        self.sock.close()
        raise SystemExit
