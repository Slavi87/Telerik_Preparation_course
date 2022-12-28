number_of_targets = int(input())
george_speed = int(input())
george_latency = int(input())
peter_speed = int(input())
peter_latency = int(input())
george_time = number_of_targets * george_speed + george_latency + george_latency
peter_time = number_of_targets * peter_speed + peter_latency + peter_latency
if george_time < peter_time:
    print('George')
elif george_time > peter_time:
    print('Peter')
else:
    print('Draw')


# POINTS = 100