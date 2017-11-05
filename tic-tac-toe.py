board = {
'top-L':'','top-M':'','top-R':'',
'mid-L':'','mid-M':'','mid-R':'',
'low-L':'','low-M':'','low-R':'',
}

def toPrint(board):
	print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
	print('-+-+-')
	print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
	print('-+-+-')
	print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])

def thegame():
	print('Welcome to tic-tac-toe game : ')
	print(' turn for O')
	turn = 'O'
	for i in range(9):	
		print('turn for '+turn)
		print('enter the position')
		pos = input()
		board[pos] = turn
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
			print('turn for X')
		toPrint(board)

thegame()

