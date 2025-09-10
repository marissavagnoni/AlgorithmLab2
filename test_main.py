from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(16, 2, 2) == 80
	assert simple_work_calc(5, 3, 2) == 20


def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(8, 2, 2,lambda n: 1) == 15
	assert work_calc(2, 3, 2, lambda n: n*n) == 7
	assert work_calc(20, 3, 2, lambda n: n) == 230



def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	a = 4
	b = 2
	#Case 1: c < log_b a
	c1 = 1 #log_2(4) = 2 > 1
	work_fn1 = lambda n: work_calc(n, a, b, lambda n: n**c1)
	#Case 2: c > log_b a
	c2 = 3 #log_2(4) = 2 < 3
	work_fn2 = lambda n: work_calc(n, a, b, lambda n: n**c2)

	res = compare_work(work_fn1, work_fn2)

	print(res)


def test_compare_span():
	a = 4
	b = 2
	c1 = 1 #f(n) = n
	c2 = 3 #f(n) = n^3
	span_fn1 = lambda n: span_calc(n, a, b, lambda n: n**c1)
	span_fn2 = lambda n: span_calc(n, a, b, lambda n: n**c2)

	results = []
	for n in [10, 20, 50, 100, 1000, 5000, 10000]:
		results.append((n, span_fn1(n), span_fn2(n)))