#CODE MONKS

import random, os, math
class Day1:

	'''
	multiply the digits in a number from last index to first.
	could have made recursive.
	Quite straightforward
	'''
	def multiplyDigits(self, numbers):
		product = 1
		while numbers > 0:
			product = numbers%10 * product
			numbers /= 10
		return product


class Day2:

	'''
	problems when I tried updating same array.
	python requires you to make a new array.
	'''
	def removeEven(self, array):
		newList = []
		for i in array:
			if len(i)%2 == 0:
				pass
			else:
				newList.append(i)
		return newList


class Day3:

	'''
	had to start counting from -1 since it will happen before I enter the if 
	to check if i find the letter.
	quite clumsy code. Could improve
	'''
	def findL(self, letter, x):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		count = -1
		for i in alphabet:
			count += 1
			if i == letter:
				if count+x > len(alphabet):
					return -1
				else:
					return alphabet[x+count]

		print "enter a letter and a value of x"


class Day4:

	'''
	checking palindrome. 
	function using python slice
	'''
	def isPalindrome(self, word):
		if len(word) < 2:
			return True

		if word[0] != word[-1]:
			return False

		return self.isPalindrome(word[1:-1])


class Day5:
	
	'''
	check if a string/array of integers is increasing in order.
	python recursive with slice.
	Similar to day4
	'''

	def incrOrd(self, number):
		if len(number) < 2:
			return True

		if number[1] <= number[0]:
			return False

		return self.incrOrd(number[2:]) 


class Day6:

	def isDiv(self, b, n):
		
		'''
		easy mode
		'''
		for i in range(0, n+1):
			if i % b == 0:
				print i

class Day7:

	'''
	multiplyDigits recursive
	'''
	def multDigRec(self, n):
		if n == 0:
			return 1

		return n%10 * self.multDigRec(n/10)



class Day8:
	'''
	string reverse recursive
	using global str to save value to
	'''
	def stringRecRev(self, string):
		global returnStr
		if len(string) == 0:
			return returnStr
		returnStr += string[-1]
		return self.stringRecRev(string[:-1])
returnStr = ""


class Day9:

	'''
	greatest common divider (GCD)
	ex: GCD(10, 4) 
	gcd(10, 4)
	gcd(4, 10%4)
	gcd(2, 4%2)
	gcd(0, 2) => 2
	'''

	def GCD(self, n1, n2):
		if n2 == 0:
			return n1
		return self.GCD(n2, n1%n2)


class Day10:

	'''
	isPrime recursive
	something is prime if its only divisable by 1
	or itself
	'''
	
	def isPrime(self, n, divisor):

		if divisor == 1:
			return True

		if n % divisor == 0:
			return False

		return self.isPrime(n, divisor-1)



class Day11:

	'''
	A lychrel number is a number that does not form a 
	palindrome after adding n with reversed n
	ex:
	56 = 56 + 65 = 121 (palindrome) after 1 iteration
	'''
	def reverseNum(self, n):
		returnStr = ""
		for i in n:
			returnStr += n[-1]
			n = n[:-1]
		return returnStr
	
	'''
	57 becomes palindromic after two iterations: 57+75 = 132, 132+231 = 363.
	59 becomes a palindrome after 3 iterations: 59+95 = 154, 154+451 = 605, 605+506 = 1111
	89 takes an unusually large 24 iterations
	'''
	def lychrelNumber(self, n):
		numberOfIterations = 0
		intR = 0
		while not Day4().isPalindrome(n):
			numberOfIterations += 1
			intR = long(n) + long(self.reverseNum(n))
			n = str(intR)
			#world record for most delayed palindrome number is 261 iterations 
			#number: 1,186,060,307,891,929,990
			if numberOfIterations > 261: 
				#196 is a candidate
				#no proof that such a number exist.
				return True
		return numberOfIterations


class Day12:

	'''
	def recRemove()
	for instance of char in string:
		remove char
	run recRemove
	'''

	def recRemove(self, c, string):
		global returnStr
		
		if string == "":
			return returnStr

		if string[0] == c:
			pass
		else:
			returnStr += string[0]

		return self.recRemove(c, string[1:])


class Day13:

	'''
	dudeneyNum
		1 =  1 x  1 x  1   ;   1 = 1
	  	512 =  8 x  8 x  8   ;   8 = 5 + 1 + 2
	 	4913 = 17 x 17 x 17   ;  17 = 4 + 9 + 1 + 3
	 	5832 = 18 x 18 x 18   ;  18 = 5 + 8 + 3 + 2
		17576 = 26 x 26 x 26   ;  26 = 1 + 7 + 5 + 7 + 6
		19683 = 27 x 27 x 27   ;  27 = 1 + 9 + 6 + 8 + 3
	'''

	def cube(self, x):
		return int(round(x ** (1. / 3))) 

	def sumNum(self, num):
		if num == 0:
			return 0
		return num%10 + self.sumNum(num/10)
	
	def dudeneyNum(self, num):
		cube = self.cube(num)
		sumN = self.sumNum(num)
		if cube == sumN:
			return True
		return False


class Day14:

	'''
	python switch statement
	using .get
	'''

	def wishes(self, holiday):
		return {'christmas' : "Merry Christmas", 'pask': 'Glad Pask'}.get(holiday, 'not in the list')

	'''
	can also use dictionaries
	eg. wishes2 -> print Day14.wishes2()['pask']
	or inside the function:
	def funct(num):
		return {1 : 'x', 2 : 'f'}[num]
	worse performance?
	'''

	def wishes2(self):
		return {'christmas' : 'Merry Christmas', "pask" : 'Glad Pask'}



class Day15:

	'''
	convering to list from tuple, 
	doesnt work the other way around because
	tuples are immutable
	'''
	def converToList(self, tup):
		lista = []
		for i in tup:
			lista.append(i)

		return lista


class Day16:

	'''
	powersum(3, 3) = 0^3 + 1^3 + 2^3 + 3^3
	'''

	def powerSum(self, num, p):
		powSum = 0
		for i in range(0, num+1):
			powSum += pow(i, p)

		return powSum


class Day17:

	'''
	mix two integer arrays randomly
	'''

	def mix(self, a, b):
		retArr = [] 
		while len(a) > 0 or len(b) > 0:
			r = random.random()

			if len(a) == 0:
				retArr.append(b[0])
				b = b[1:]
			elif len(b) == 0:
				retArr.append(a[0])
				a = a[1:]
			elif r < 0.5:
				retArr.append(a[0])
				a = a[1:]
			else:
				retArr.append(b[0])
				b = b[1:]
		
		return retArr



class Day18:

	def __init__(self, num):
		self.num = num

	def gt(self, other):
		if self.num > other.num:
			return True
		return False
	
	#less than 
	def __lt__(self, other):
		if self.num < other.num:
			return True
		return False


class Day18B:

	'''
	list comperhension
	'''
	#a set has all unique values
	def setComp(self, arr):
		return {n for n in arr}

	#a set containing tuples
	def dictComp(self, dic):
		return {(name, age) for name, age in dic.iteritems()}
		
	#square all numbers in an array with list comperhensions
	def numberSquares(self, arr):
		return [(num, num*num) for num in arr]

	#combine firstname and lastname with list comps
	def arrayCombine(self, A, B):
		return { A[index]+" "+B[index] for index in range(0, len(A)) if len(B) == len(A) }


class Day19:


	'''
	multiply odd digits in a number
	'''
	def multOdd(self, n):
		product = 1

		while n > 0:
			if (n%10) % 2 != 0:
				product *= n%10
			n = n/10

		return product



class Day20:

	def asterix(self, s):
		badWords = ['fuck', 'idiot']
		retSt = ''
		words = s.split(' ')
		for i in range(0, len(words)):
			if words[i] in badWords:
				retSt += '*'*len(words[i])
				retSt += ' '
			else:
				retSt += words[i]
				retSt += ' '

		return retSt



