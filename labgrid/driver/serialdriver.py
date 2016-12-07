import attr
from ..protocol import ConsoleProtocol
from ..resource import SerialPort
import pexpect

@attr.s
class SerialDriver(ConsoleProtocol):
    target = attr.ib()

    def __attrs_post_init__(self):
        self.port = self.target.get_resource(SerialPort)
        if not self.port:
            raise NotImplementedError
        self.target.drivers.append(self)
        self.port.timeout=1.0

    def run(self, cmd: str):
        """
        Runs the supplied cmd and returns the result

        Arguments:
        cmd -- cmd to be run
        """
        self.port.write("{}\n".format(cmd).encode("utf-8"))
        return self.port.read()