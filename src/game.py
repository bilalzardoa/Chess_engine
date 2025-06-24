import chess
from fastapi import FastAPI

app = FastAPI()

# Init board (correct met hoofdletter B)
board = chess.Board()

@app.get("/")
def hello_world():
    return {"message":"hello world!"}

@app.post("/move")
def make_move(move: str):
    try:
        move_obj = chess.Move.from_uci(move)
        if move_obj in board.legal_moves:
            board.push(move_obj)
            return {"status": "ok", "fen": board.fen()}
        else:
            return {"status": "illegal"}
    except ValueError:
        return {"status": "invalid_format"}


