from layout import get_body
from objects import init_variables, init_connections

def run():
    init_variables()
    body = get_body()
    init_connections(body)

if __name__ == "__main__":
    run()
