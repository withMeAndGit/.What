""" What??? """


def main(work: bool | None = False) -> str:
    if work:
        return 'y'
    return 'n'


if __name__ == '__main__':
    print(f'result: {main(True)}')