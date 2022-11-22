import matplotlib.pyplot as plt

abs_v = []
plt_time = []
r_to_star = []

def gen_first_dots(obj, time):
    plt_time.append(time)
    for j in enumerate(obj):
        abs_v.append([])
        i = int(j[0])
        abs_v[i].append((obj[i].Vx ** 2 + obj[i].Vy ** 2)**0.5)
        r_to_star.append([])
        r_to_star[i].append(((obj[i].x - obj[0].x)**2 + (obj[i].y - obj[0].y)**2)**0.5)
    

def gen_dots(obj,time):
    for j in enumerate(obj):
        i = int(j[0])
        abs_v[i].append((obj[i].Vx ** 2 + obj[i].Vy ** 2)**0.5)
        r_to_star[i].append(((obj[i].x - obj[0].x)**2 + (obj[i].y - obj[0].y)**2)**0.5)
    plt_time.append(time)


def save_plt(i):
    plt.plot(plt_time, abs_v[i])
    plt.savefig('objv'+str(i)+'.png')
    plt.delaxes()
    plt.plot(plt_time, r_to_star[i])
    plt.savefig('objr'+str(i)+'.png')
    plt.delaxes()
    plt.plot(r_to_star[i], abs_v[i])
    plt.savefig('objrv'+str(i)+'.png')
    plt.delaxes()

if __name__ == "__main__":
    print("This module is not for direct call!")