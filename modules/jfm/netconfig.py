
nic = None

__all__ = [ "netconfig", "nic" ]

def netconfig():
  global nic
  import network
  from time import sleep_ms
  nic = network.WLAN(network.STA_IF)
  nic.active(True)
  
  # Scan for networks
  nets = nic.scan()
  
  # Do we have known networks already?
  try:
    known_nets
  except NameError:
    try:
      import known_nets as kn
      known_nets = kn.known_nets
    except ImportError:
      print("No known_nets.py\n")
      known_nets = { 'public': '' }

  
  # Walk through each found network
  for n in nets:
    sleep_ms(500)
    print("Scan found network {}\n".format(n))
    
    nm = n[0]
    # Do we know the password for it?
    if nm not in known_nets:
      print("{} is not a known network, continuing\n".format(nm))
    else:
  
      # Attempt to connect to our known net
      try:
        nic.connect(nm,known_nets[nm])
	sleep_ms(500)
      except:
        print("Unable to connect to {}\n".format(nm))
      finally:
        if nic.isconnected():
          print("Connected to {}!\n".format(nm))
	break

  if nic.isconnected():
    print("Network configuration:\n{}\n".format(nic.ifconfig()))

  else:
    print("No known networks found to connect.  Making my own\n")
    nic.active(False)
    nic = network.WLAN(network.AP_IF)
    nic.active(True)
  
