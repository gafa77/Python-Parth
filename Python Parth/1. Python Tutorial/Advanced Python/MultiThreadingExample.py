import threading
import time

def print_cube(num):
	print("Cube: {}" .format(num * num * num))

def print_square(num):
	time.sleep(2)
	print("Square: {}" .format(num * num))

def numbers1to100():
	for i in range(1,11):
		print(i)


def numbers200to300():
	for i in range(20,31):
		print(i)

if __name__ =="__main__":
	t1 = threading.Thread(target=numbers1to100,daemon=True)
	t2 = threading.Thread(target=numbers200to300)

	t1.start()
	t2.start()
	print_cube(12)
	t1.setDaemon(False)
	t1.join()
	t2.join()
	# function2
	print("Done!")
