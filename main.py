""" What??? """


def main(eval_: str = '0', work: bool = False) -> str:
    """ % """

    if work:
        return eval(eval_)
    return '?'


if __name__ == '__main__':
    print(f'result: {main("2**5", True)}')