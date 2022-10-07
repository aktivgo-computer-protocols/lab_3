from icmplib import *

# https://github.com/ValentinBELYN/icmplib/blob/main/docs/3-sockets.md
# https://pypi.org/project/icmplib/

if __name__ == '__main__':
    sock = ICMPv4Socket()

    try:
        for i in (0, 10):
            request = ICMPRequest(
                destination='localhost',
                id=PID,
                sequence=i,
            )

            sock.send(request)
            reply = sock.receive(request)
            print(str(reply.bytes_received) + ' bytes from ' + reply.source +
                  ': icmp_seq=' + str(reply.sequence) + ' ttl=' + str(2) + ' time=' + str(reply.time) + ' ms')
            reply.raise_for_status()

    except TimeoutExceeded as err:
        # The timeout has been reached
        print(err)

    except DestinationUnreachable as err:
        # The reply indicates that the destination host is unreachable
        print(err)

    except TimeExceeded as err:
        # The reply indicates that the time to live exceeded in transit
        print(err)

    except ICMPLibError as err:
        # All other errors
        print(err)
