# Downloads source code of lichess.org game, translates position into pgn, inputs pgn into localized computer, returns
# analysis

import urllib.request
import chess
import chess.uci
import chess.pgn


def evaluation_function(game_url):

    # Downloads sourcecode into raw.txt

    urllib.request.urlretrieve(game_url, "raw.txt")

    # Pulls out rough PGN string from raw.txt and puts in pgn_output.txt

    with open('raw.txt', 'r') as infile, open('pgn_output.txt', 'w') as outfile:
        copy = False
        for line in infile:
            if line.__contains__('[Termination &quot;Unterminated&quot;]'):
                copy = True
            elif line.__contains__(' </div>'):
                copy = False
            elif copy:
                outfile.write(line)

    # Takes PGN from pgn_output.txt runs engine evaluation

    with open('pgn_output.txt', 'r') as f:
        game = chess.pgn.read_game(f)

    # Configures python_chess settings

    game = game.end()
    board = game.board()
    handler = chess.uci.InfoHandler()
    engine = chess.uci.popen_engine('C:\\Users\\Control\\Desktop\\stockfish-8-win\\Windows\\stockfish_8_x64.exe')
    engine.info_handlers.append(handler)

    engine.position(board)

    evaltime = 1500
    evaluation = engine.go(movetime=evaltime)

    return board.san(evaluation[0]), board.variation_san(handler.info["pv"][1])
