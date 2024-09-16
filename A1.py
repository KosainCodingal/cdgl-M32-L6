def hanoi(n, da, db, dc, logger):
    if n == 1:
        logger.append(f"Moved disk \x1b[35m1\x1b[0m from rod \x1b[34m{da}\x1b[0m to rod \x1b[34m{db}\x1b[0m.")
        return

    hanoi(n-1, da, dc, db, logger)
    logger.append(f"Moved disk \x1b[35m{n}\x1b[0m from rod \x1b[34m{da}\x1b[0m to rod \x1b[34m{db}\x1b[0m.")
    hanoi(n-1, dc, db, da, logger)

    
n = 6
logger = ["-- Solver log --"]
hanoi(n, 'diskA', 'diskB', 'diskC', logger)
logger.append("\x1b[32mSolved!\x1b[0m")
print("\n".join(logger))