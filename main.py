import sys


def get_twos_complement_number(number: str) -> str:
	new_number = "".join([f"{(int(i) + 1) % 2}" for i in number])
	return bin(int(f'0b{new_number}', 2) + int("0b1", 2))[2:]


def main():
	print("Enter two negative binary numbers and their sum will be returned.")
	number1 = input("Enter the first negative binary number: ")
	number2 = input("Enter the second negative binary number: ")
	numbersList = []
	for i in (number1, number2):
		if not i.startswith('-'):
			sys.exit("The numbers should be negative!")
		else:
			for j in i[1:]:
				if j not in ['0', '1']:
					sys.exit("One of the numbers inputted is not a binary number!")
			i = i[1:].zfill(4)
			numbersList.append(i)
	twos_complement_list = [get_twos_complement_number(i) for i in numbersList]
	final_answer = bin(int(f'0b{twos_complement_list[0]}', 2) + int(f'0b{twos_complement_list[1]}', 2))[2:]
	twos_complement_of_the_final_answer = get_twos_complement_number(final_answer)
	print("The total is: -" + twos_complement_of_the_final_answer)


if __name__ == '__main__':
	main()
