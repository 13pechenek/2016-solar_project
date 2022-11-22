import matplotlib.pyplot as plt

abs_v = []
plt_time = []

def gen_first_dots(obj, time):
    plt_time.append(time)
    for j in enumerate(obj):
        abs_v.append([])
        i = int(j[0])
        abs_v[i].append((obj[i].Vx ** 2 + obj[i].Vy ** 2)**0.5)
    

def gen_dots(obj,time):
    for j in enumerate(obj):
        i = int(j[0])
        abs_v[i].append((obj[i].Vx ** 2 + obj[i].Vy ** 2)**0.5)
    plt_time.append(time)


def save_plt(i):
    plt.plot(plt_time, abs_v[i])
    plt.savefig('obj'+str(i)+'.png')
    plt.delaxes()