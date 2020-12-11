
board = {
	'1h': 'bking',
	'6c': 'wqueen',
	'2g': 'bbishop',
	'5h': 'bqueen',
	'3e': 'wking',
	'4e': 'wpawn',
	'2e': 'bpawn',
	'1e': 'bpawn',
	'9z': 'bpawn',
	'1a': 'xcovid'
}

def is_valid_chess_board(board):
	valid_chessboard = True
	pieces_pos, pieces_names = list(board.keys()), list(board.values())

	# Define valid items:
	valid_numbers 	= '12345678'
	valid_letters 	= 'abcdefgh'
	valid_colors 	= 'wb'
	valid_names 	= ['pawn', 'knight', 'bishop', 'rook', 'king','queen']

	pieces = {}
	
	# Count pieces:
	for piece in board.values():
		pieces.setdefault(piece, 0)
		pieces[piece] += 1

	w_pieces = [w_piece for w_piece in pieces_names if w_piece[:1] == 'w']
	w_pawns = [w_pawn for w_pawn in w_pieces if w_pawn[1:] == 'pawn']

	b_pieces = [b_piece for b_piece in pieces_names if b_piece[:1] == 'b']
	b_pawns = [b_pawn for b_pawn in b_pieces if b_pawn[1:] == 'pawn']

	# Define invalid positions and pieces:
	invalid_pos = [pos for pos in pieces_pos if pos[0] not in valid_numbers or pos[1] not in valid_letters]
	invalid_pieces = [piece for piece in pieces_names if piece[:1] not in valid_colors or piece[1:] not in valid_names]


	# Provide checks for pieces:
	if pieces.get('bking') != 1 or pieces.get('wking') != 1:
		valid_chessboard = False

	if (len(w_pieces) > 16 or len(b_pieces) > 16 or 
		len(w_pawns) > 8 or len(b_pawns) > 8):
		valid_chessboard = False

	if invalid_pos:
		valid_chessboard = False

	if invalid_pieces:
		valid_chessboard = False

	return valid_chessboard
