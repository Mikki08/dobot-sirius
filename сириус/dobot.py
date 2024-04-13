from bottle import route, run, template
from serial.tools import list_ports
import pydobot

available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[0].device
port2 = available_ports[1].device

device = pydobot.Dobot(port=port, verbose=False)
device1 = pydobot.Dobot(port=port2, verbose=False)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

device.speed(1000, 1000)
device.home()

device1.speed(1000, 1000)
device1.home()


@route('/angle/<J1>/<J2>/<J3>')
def index(J1,J2,J3):
    device.angle(j1=float(J1),j2=float(J2),j3=float(J3),r=0, wait=False)
    device1.angle(j1=float(J1),j2=float(J2),j3=float(J3),r=0, wait=True)
    return template('<b>angle {{J1}},{{J2}},{{J3}}</b>!', J1=J1,J2=J2,J3=J3)

#device.speed(1000, 1000)
#x, y, z = 0, 0, 0
#device.move_to(x, y, z, r, wait=True)# we wait until this movement is done before continuing

#@route('/move_to/<X>/<Y>/<Z>')
#def index(X,Y,Z):
    #device.move_to(x + float(X), y + float(Y), z + float(Z), r, wait=False)
    #device1.move_to(x + float(X), y + float(Y), z + float(Z), r, wait=True)
    #return template('<b>move_to {{X}},{{Y}},{{Z}}</b>!', X=X,Y=Y,Z=Z)

@route('/move_to/<X>/<Y>/<Z>')
def index(X,Y,Z):
    device.move_to(x = float(X), y = float(Y), z = float(Z), r=0, wait=False)
    device1.move_to(x = float(X), y = float(Y), z = float(Z), r=0, wait=True)
    return template('<b>move_to {{X}},{{Y}},{{Z}}</b>!', X=X,Y=Y,Z=Z)


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

#run(host='10.82.163.226', port=8080)
run(host='10.10.201.127', port=8080)

device.close()