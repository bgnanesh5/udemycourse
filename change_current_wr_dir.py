import os
'''
req_path=input("Enter path to change working dir: ")
print("The current working dir is: ",os.getcwd())
try:
	os.chdir(req_path)
	print("Now your new working dir is: ",os.getcwd())
except FileNotFoundError:
	print("Given path is not a valid path. So cannot change working directory")
except NotADirectoryError:
	print("Given path is not a valid path. So cannot change working directory")
except PermissionError:
	print("Sorry you donot have access for the given path. So cannot change working directory")
except Exception as e:
	print(e)
'''
def main():
	req_path=input("Enter path to change working dir: ")
	print("The current working dir is: ",os.getcwd())
	try:
		os.chdir(req_path)
		print("Now your new working dir is: ",os.getcwd())
	except FileNotFoundError:
			print("Given path is not a valid path. So cannot change working directory")
	except NotADirectoryError:
			print("Given path is not a valid path. So cannot change working directory")
	except PermissionError:
			print("Sorry you donot have access for the given path. So cannot change working directory")
	except Exception as e:
			print(e)
	return None

if __name__=="__main__":
	main()