import creversi as reversi
import numpy as np

class novoc_Board:
    def __init__(self):
        self.board = reversi.Board()
        self.board_history = [self.board_to(self.board)]
        a = []
        c = 1
        for i in range(8):
            r = []
            for j in range(8):
                r.append(c)
                c *= 2
            a.append(r)
        self.bit_A = np.array(a)
        self.set_scores()

    def set_from_sfen(self, sfen):
        color_d =  {'B': reversi.BLACK_TURN, 'W': reversi.WHITE_TURN}
        line = sfen[0:65]
        color = color_d[sfen[64]]
        self.board = reversi.Board(line, color)
        self.board_history = [self.board_to(self.board)]
        self.set_scores()
        return

    def board_to(self, board):
        line = board.to_line()
        if board.turn:
            color = reversi.BLACK_TURN
        else:
            color = reversi.WHITE_TURN
        return {'line': line, 'color': color}

    def move_to_USIX(self, move):
        #novoc => USI-X
        d = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        move_str = d[move[0]] + str(move[1] + 1)
        return move_str

    def move_to_novoc(self, move):
        #USI-X => novoc
        d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        novoc_move = (int(d[move[0]]), int(move[1]) - 1)
        return novoc_move

    def set_scores(self):
        #スコアの更新
        my = self.board.piece_num()
        opponent = self.board.piece_sum() - my
        if self.board.turn:#自分が黒番
            self.black_score = my
            self.white_score = opponent
        else:
            self.black_score = opponent
            self.white_score = my
        #discの更新
        planes = np.empty((2, 8, 8), dtype=np.float32)
        self.board.piece_planes(planes[0])
        if self.board.turn:
            black = planes[0]
            white = planes[1]
        else:
            white = planes[0]
            black = planes[1]
        self.black_disc = []
        self.white_disc = []
        for x in range(8):
            for y in range(8):
                if black[x][y] > 0:
                    self.black_disc.append((x, y))
                elif white[x][y] > 0:
                    self.white_disc.append((x, y))
        #disc_bitの更新
        self.black_disc_bit = black * self.bit_A
        self.white_disc_bit = white * self.bit_A
        self.black_disc_bit.reshape(64,)
        self.white_disc_bit.reshape(64,)
        self.black_disc_bit = sum(self.black_disc_bit)
        self.white_disc_bit = sum(self.white_disc_bit)
        return

    def put_disc(self, color, x, y):
        move_str = self.move_to_USIX((x, y))
        self.board.move(reversi.move_from_str(move_str))
        self.board_history.append(self.board_to(self.board))
        self.set_scores()
        return

    def undo(self):
        self.board_history.pop(-1)
        a = self.board_history[-1]
        self.board.set_line(a['line'], a['color'])
        self.set_scores()
        return

    def legal(self, color):
        legal_moves = list(self.board.legal_moves)
        if 64 in legal_moves:#パス
            return []
        output = []
        for i in range(len(legal_moves)):
            str_move = reversi.move_to_str(legal_moves[i])
            novoc_move = self.move_to_novoc(str_move)
            output.append(novoc_move)
        return output
