from time import sleep
loading = 'LOADING...'
for i in range(10):
    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.5)
