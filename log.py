import logging
logging.basicConfig(filename="log.txt", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S", format="%(asctime)s %(levelname)s [%(name)s@%(filename)s::%(lineno)d] %(message)s %(args)s")
    
#import _10_module
def main() -> None:
    logging.info("Logger info")
    logging.error("Query error", {"sql": "SELECT *", "err": "Syntax error"})



if __name__ == "__main__":
    main()